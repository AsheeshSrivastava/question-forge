#!/usr/bin/env python3
"""
QuestionForge - Database Export Helper
Quick export from your Python question database

"Small fixes, big clarity" - Quest & Crossfire
"""

import sys
from pathlib import Path

# Add QuestionForge to path
sys.path.insert(0, str(Path(__file__).parent))

from convert_to_jsonl import QuestionConverter


# ============================================================
# CONFIGURATION - EDIT THIS SECTION
# ============================================================

# Database connection (choose your database type)

# Option 1: SQLite
DATABASE_TYPE = 'sqlite'
DATABASE_PATH = 'questions.db'  # Change to your database path

# Option 2: MySQL (uncomment if using MySQL)
# DATABASE_TYPE = 'mysql'
# MYSQL_CONFIG = {
#     'host': 'localhost',
#     'user': 'your_username',
#     'password': 'your_password',
#     'database': 'question_bank'
# }

# Option 3: PostgreSQL (uncomment if using PostgreSQL)
# DATABASE_TYPE = 'postgresql'
# POSTGRES_CONFIG = {
#     'host': 'localhost',
#     'user': 'your_username',
#     'password': 'your_password',
#     'database': 'question_bank'
# }

# SQL Query - EDIT THIS to match your table structure
SQL_QUERY = """
    SELECT
        id,
        topic,
        question_text as question,
        question_type as style,
        difficulty_level as difficulty,
        bloom_level,
        keywords,
        subtopics,
        prerequisites
    FROM questions
    WHERE subject = 'Python'
    AND active = 1
    ORDER BY id
"""

# Output file
OUTPUT_FILE = 'python_questions.jsonl'

# ============================================================
# END CONFIGURATION
# ============================================================


def export_from_sqlite(db_path, query):
    """Export from SQLite database"""
    import sqlite3

    print(f"📦 Connecting to SQLite: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print(f"🔍 Executing query...")
    cursor.execute(query)

    # Convert to dicts
    columns = [desc[0] for desc in cursor.description]
    questions = []

    for row in cursor.fetchall():
        q = dict(zip(columns, row))
        questions.append(q)

    conn.close()
    print(f"✅ Loaded {len(questions)} questions from SQLite")

    return questions


def export_from_mysql(config, query):
    """Export from MySQL database"""
    try:
        import mysql.connector
    except ImportError:
        print("❌ Error: mysql-connector-python not installed")
        print("   Install: pip install mysql-connector-python")
        sys.exit(1)

    print(f"📦 Connecting to MySQL: {config['host']}/{config['database']}")
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)

    print(f"🔍 Executing query...")
    cursor.execute(query)

    questions = cursor.fetchall()

    conn.close()
    print(f"✅ Loaded {len(questions)} questions from MySQL")

    return questions


def export_from_postgresql(config, query):
    """Export from PostgreSQL database"""
    try:
        import psycopg2
        from psycopg2.extras import RealDictCursor
    except ImportError:
        print("❌ Error: psycopg2 not installed")
        print("   Install: pip install psycopg2-binary")
        sys.exit(1)

    print(f"📦 Connecting to PostgreSQL: {config['host']}/{config['database']}")
    conn = psycopg2.connect(**config)
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    print(f"🔍 Executing query...")
    cursor.execute(query)

    questions = [dict(row) for row in cursor.fetchall()]

    conn.close()
    print(f"✅ Loaded {len(questions)} questions from PostgreSQL")

    return questions


def export_from_pandas_db(query, db_path=None, db_type='sqlite'):
    """Export using pandas (works with any database)"""
    try:
        import pandas as pd
    except ImportError:
        print("❌ Error: pandas not installed")
        print("   Install: pip install pandas")
        sys.exit(1)

    print(f"📦 Connecting to database with pandas...")

    if db_type == 'sqlite':
        import sqlite3
        conn = sqlite3.connect(db_path)
    else:
        print("❌ For non-SQLite, use specific export function")
        sys.exit(1)

    print(f"🔍 Executing query...")
    df = pd.read_sql(query, conn)
    conn.close()

    questions = df.to_dict('records')
    print(f"✅ Loaded {len(questions)} questions via pandas")

    return questions


def main():
    """Main export function"""

    print("\n" + "="*60)
    print("🔥 QuestionForge - Database Export")
    print("="*60 + "\n")

    # Load questions from database
    try:
        if DATABASE_TYPE == 'sqlite':
            questions = export_from_sqlite(DATABASE_PATH, SQL_QUERY)

        elif DATABASE_TYPE == 'mysql':
            questions = export_from_mysql(MYSQL_CONFIG, SQL_QUERY)

        elif DATABASE_TYPE == 'postgresql':
            questions = export_from_postgresql(POSTGRES_CONFIG, SQL_QUERY)

        else:
            print(f"❌ Unknown database type: {DATABASE_TYPE}")
            sys.exit(1)

    except Exception as e:
        print(f"\n❌ Database error: {str(e)}")
        print("\n💡 Tips:")
        print("   - Check DATABASE_PATH or config")
        print("   - Verify SQL_QUERY matches your table structure")
        print("   - Ensure database file/server is accessible")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    if not questions:
        print("\n⚠️  No questions found!")
        print("   Check your SQL_QUERY and filters")
        sys.exit(1)

    # Convert to JSONL
    print(f"\n🔄 Converting to QuestionForge format...")
    converter = QuestionConverter()

    try:
        normalized = converter.from_dict_list(questions)
        converter.to_jsonl(normalized, OUTPUT_FILE)
        converter.print_summary()

        print(f"\n✅ Export complete!")
        print(f"\n📁 Output: {OUTPUT_FILE}")
        print(f"\n🚀 Next steps:")
        print(f"   1. Verify: head -n 1 {OUTPUT_FILE}")
        print(f"   2. Analyze: py main.py analyze {OUTPUT_FILE}")
        print(f"   3. Upload to Hugging Face Space")

    except Exception as e:
        print(f"\n❌ Conversion error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
