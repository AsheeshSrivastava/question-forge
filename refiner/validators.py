"""
Quality Validator - Ensure 4.8/5 threshold is met
"""

from typing import Dict, List, Tuple
from .parser import Question
from .analyzer import QuestionAnalyzer


class QualityValidator:
    """Validate question quality against flagship standards"""

    def __init__(self, config_path: str = "config.yaml", threshold: float = 4.8):
        self.analyzer = QuestionAnalyzer(config_path)
        self.threshold = threshold

    def validate(self, question: Question) -> Tuple[bool, Dict[str, any]]:
        """
        Validate a single question
        Returns: (passes, validation_report)
        """

        scores = self.analyzer.analyze(question)
        passes = scores["overall"] >= self.threshold

        report = {
            "passes": passes,
            "overall_score": scores["overall"],
            "threshold": self.threshold,
            "scores": scores,
            "issues": [],
            "suggestions": []
        }

        if not passes:
            # Identify what's holding the score down
            for criterion, score in scores.items():
                if criterion == "overall":
                    continue

                if score < 4.5:
                    report["issues"].append({
                        "criterion": criterion,
                        "score": score,
                        "gap": round(4.5 - score, 2)
                    })

            # Get suggestions
            report["suggestions"] = self.analyzer.get_improvement_suggestions(question, scores)

        return passes, report

    def validate_batch(self, questions: List[Question]) -> Dict[str, any]:
        """
        Validate multiple questions
        Returns summary report
        """

        results = {
            "total": len(questions),
            "passed": 0,
            "failed": 0,
            "average_score": 0.0,
            "threshold": self.threshold,
            "distribution": {
                "excellent": 0,  # ≥4.8
                "very_good": 0,  # 4.5-4.7
                "good": 0,       # 4.0-4.4
                "adequate": 0,   # 3.5-3.9
                "needs_work": 0, # 3.0-3.4
                "poor": 0        # <3.0
            },
            "failed_questions": []
        }

        total_score = 0

        for q in questions:
            passes, report = self.validate(q)

            if passes:
                results["passed"] += 1
            else:
                results["failed"] += 1
                results["failed_questions"].append({
                    "id": q.id,
                    "question": q.question[:50] + "..." if len(q.question) > 50 else q.question,
                    "score": report["overall_score"],
                    "top_issue": report["issues"][0] if report["issues"] else None
                })

            score = report["overall_score"]
            total_score += score

            # Distribution
            if score >= 4.8:
                results["distribution"]["excellent"] += 1
            elif score >= 4.5:
                results["distribution"]["very_good"] += 1
            elif score >= 4.0:
                results["distribution"]["good"] += 1
            elif score >= 3.5:
                results["distribution"]["adequate"] += 1
            elif score >= 3.0:
                results["distribution"]["needs_work"] += 1
            else:
                results["distribution"]["poor"] += 1

        results["average_score"] = round(total_score / len(questions), 2)

        return results

    def get_refinement_priority(self, questions: List[Question]) -> List[Tuple[Question, float, List[str]]]:
        """
        Get questions prioritized by refinement need
        Returns: List of (question, score, top_issues)
        """

        priorities = []

        for q in questions:
            scores = self.analyzer.analyze(q)
            if scores["overall"] < self.threshold:
                issues = self.analyzer.identify_issues(q, scores)
                top_issues = [desc for cat, desc, pri in issues[:3]]
                priorities.append((q, scores["overall"], top_issues))

        # Sort by score (lowest first = highest priority)
        priorities.sort(key=lambda x: x[1])

        return priorities
