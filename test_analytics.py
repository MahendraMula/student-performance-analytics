"""
test_analytics.py - Automated Unit Tests for Student Performance Analytics System.

Verifies:
1. Data loading and validation.
2. NumPy calculations (Totals and Averages).
3. Grading scheme boundaries.
4. Pass/Fail conditions (Average >= 40 and each subject >= 35).
5. Class statistics (mean, min, max, std).
6. Subject-wise analytics.
7. Top/Lowest performer selection with tie handling.
"""

import unittest
import numpy as np
import pandas as pd
from functions import (
    load_dataset,
    calculate_student_metrics,
    assign_grade,
    evaluate_pass_fail,
    apply_grading_and_status,
    calculate_class_statistics,
    get_top_performers,
    get_lowest_performers,
    analyze_subject_performance,
    get_pass_fail_summary
)


class TestStudentPerformanceAnalytics(unittest.TestCase):

    def setUp(self):
        # Create a controlled synthetic DataFrame for deterministic tests
        self.sample_data = pd.DataFrame([
            {"Student_ID": "T1", "Name": "Alice", "Department": "CS", "Math_Marks": 95, "Physics_Marks": 90, "Python_Marks": 95, "Attendance": 95},
            {"Student_ID": "T2", "Name": "Bob", "Department": "IT", "Math_Marks": 80, "Physics_Marks": 85, "Python_Marks": 80, "Attendance": 88},
            {"Student_ID": "T3", "Name": "Charlie", "Department": "DS", "Math_Marks": 70, "Physics_Marks": 75, "Python_Marks": 72, "Attendance": 80},
            {"Student_ID": "T4", "Name": "Diana", "Department": "ME", "Math_Marks": 60, "Physics_Marks": 65, "Python_Marks": 62, "Attendance": 78},
            {"Student_ID": "T5", "Name": "Evan", "Department": "CS", "Math_Marks": 50, "Physics_Marks": 55, "Python_Marks": 52, "Attendance": 75},
            {"Student_ID": "T6", "Name": "Fay", "Department": "IT", "Math_Marks": 30, "Physics_Marks": 40, "Python_Marks": 45, "Attendance": 60}, # Subject fail
            {"Student_ID": "T7", "Name": "George", "Department": "DS", "Math_Marks": 36, "Physics_Marks": 38, "Python_Marks": 39, "Attendance": 70}, # Avg < 40
            {"Student_ID": "T8", "Name": "Hannah", "Department": "CS", "Math_Marks": 95, "Physics_Marks": 90, "Python_Marks": 95, "Attendance": 95}, # Tie with Alice
        ])

    def test_load_dataset(self):
        df = load_dataset("students.csv")
        self.assertGreaterEqual(len(df), 20)
        self.assertIn("Student_ID", df.columns)
        self.assertIn("Python_Marks", df.columns)

    def test_load_dataset_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_dataset("non_existent_file.csv")

    def test_student_metrics_calculations(self):
        metrics_df = calculate_student_metrics(self.sample_data)
        # Alice: 95 + 90 + 95 = 280, avg = 280 / 3 = 93.33
        alice = metrics_df.loc[metrics_df["Student_ID"] == "T1"].iloc[0]
        self.assertEqual(alice["Total_Marks"], 280.0)
        self.assertEqual(alice["Average_Marks"], 93.33)

    def test_grade_boundaries(self):
        self.assertEqual(assign_grade(95.0), "A")
        self.assertEqual(assign_grade(90.0), "A")
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(80.0), "B")
        self.assertEqual(assign_grade(79.9), "C")
        self.assertEqual(assign_grade(70.0), "C")
        self.assertEqual(assign_grade(69.9), "D")
        self.assertEqual(assign_grade(60.0), "D")
        self.assertEqual(assign_grade(59.9), "E")
        self.assertEqual(assign_grade(50.0), "E")
        self.assertEqual(assign_grade(49.9), "F")
        self.assertEqual(assign_grade(0.0), "F")

    def test_pass_fail_rules(self):
        metrics_df = calculate_student_metrics(self.sample_data)
        scored_df = apply_grading_and_status(metrics_df)
        
        # T1 (Alice) has avg > 40 and all subjects >= 35 -> Pass
        t1 = scored_df.loc[scored_df["Student_ID"] == "T1"].iloc[0]
        self.assertEqual(t1["Status"], "Pass")

        # T6 (Fay) has Math = 30 (< 35) -> Fail despite avg = 38.33
        t6 = scored_df.loc[scored_df["Student_ID"] == "T6"].iloc[0]
        self.assertEqual(t6["Status"], "Fail")

        # T7 (George) has avg = (36+38+39)/3 = 37.67 (< 40) -> Fail
        t7 = scored_df.loc[scored_df["Student_ID"] == "T7"].iloc[0]
        self.assertEqual(t7["Status"], "Fail")

    def test_class_statistics(self):
        metrics_df = calculate_student_metrics(self.sample_data)
        stats = calculate_class_statistics(metrics_df)
        self.assertIn("class_average", stats)
        self.assertIn("highest_total", stats)
        self.assertEqual(stats["highest_total"], 280.0)

    def test_subject_analysis(self):
        subj_df, best_subj = analyze_subject_performance(self.sample_data)
        self.assertEqual(len(subj_df), 3) # Math, Physics, Python
        self.assertIn(best_subj, ["Math", "Physics", "Python"])

    def test_top_performers_and_ties(self):
        metrics_df = calculate_student_metrics(self.sample_data)
        top_df = get_top_performers(metrics_df, top_n=1)
        # Alice (T1) and Hannah (T8) both have 93.33 average, both should be present
        ids = list(top_df["Student_ID"])
        self.assertIn("T1", ids)
        self.assertIn("T8", ids)

    def test_pass_fail_summary_counts(self):
        metrics_df = calculate_student_metrics(self.sample_data)
        scored_df = apply_grading_and_status(metrics_df)
        summary = get_pass_fail_summary(scored_df)
        self.assertEqual(summary["Total"], 8)
        self.assertEqual(summary["Passed"] + summary["Failed"], 8)
        self.assertEqual(summary["Failed"], 2) # T6 and T7
        self.assertEqual(summary["Passed"], 6)


if __name__ == "__main__":
    unittest.main()
