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
        # Grade A: 90 - 100%
        self.assertEqual(assign_grade(100.0), "A")
        self.assertEqual(assign_grade(95.0), "A")
        self.assertEqual(assign_grade(90.0), "A")
        self.assertEqual(assign_grade(89.99), "B")
        self.assertEqual(assign_grade(89.9), "B")

        # Grade B: 80 - 89.99%
        self.assertEqual(assign_grade(80.0), "B")
        self.assertEqual(assign_grade(79.99), "C")
        self.assertEqual(assign_grade(79.9), "C")

        # Grade C: 70 - 79.99%
        self.assertEqual(assign_grade(70.0), "C")
        self.assertEqual(assign_grade(69.99), "D")
        self.assertEqual(assign_grade(69.9), "D")

        # Grade D: 60 - 69.99%
        self.assertEqual(assign_grade(60.0), "D")
        self.assertEqual(assign_grade(59.99), "E")
        self.assertEqual(assign_grade(59.9), "E")

        # Grade E: 40 - 59.99% (includes exact boundaries 40% and 50%)
        self.assertEqual(assign_grade(50.0), "E")
        self.assertEqual(assign_grade(49.0), "E")
        self.assertEqual(assign_grade(45.0), "E")
        self.assertEqual(assign_grade(40.0), "E")

        # Grade F: Below 40%
        self.assertEqual(assign_grade(39.99), "F")
        self.assertEqual(assign_grade(39.9), "F")
        self.assertEqual(assign_grade(34.0), "F")
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

    def test_aligned_policy_student_scenarios(self):
        """
        Verify explicit acceptance criteria:
        1. 45% average and all subject marks >= 35 receives Grade E and Status Pass.
        2. 49% average and all subject marks >= 35 receives Grade E and Status Pass.
        3. Average below 40% receives Grade F and Status Fail.
        4. Average >= 40% but any subject mark < 35 receives Status Fail.
        5. No student with Grade F can ever receive Status Pass.
        """
        test_df = pd.DataFrame([
            # 1. 45% average, all subjects >= 35 (e.g. 45, 45, 45) -> Grade E, Pass
            {"Student_ID": "X1", "Name": "Case45Pass", "Department": "CS", "Math_Marks": 45, "Physics_Marks": 45, "Python_Marks": 45, "Attendance": 80},
            # 2. 49% average, all subjects >= 35 (e.g. 48, 49, 50) -> Grade E, Pass
            {"Student_ID": "X2", "Name": "Case49Pass", "Department": "CS", "Math_Marks": 48, "Physics_Marks": 49, "Python_Marks": 50, "Attendance": 80},
            # 3. Average below 40% (e.g. 38, 39, 39 -> 38.67%) -> Grade F, Fail
            {"Student_ID": "X3", "Name": "CaseBelow40", "Department": "IT", "Math_Marks": 38, "Physics_Marks": 39, "Python_Marks": 39, "Attendance": 70},
            # 4. Average >= 40% (50.0%) but one subject mark < 35 (Math=32) -> Grade E, Fail
            {"Student_ID": "X4", "Name": "CaseSubjectFail", "Department": "DS", "Math_Marks": 32, "Physics_Marks": 58, "Python_Marks": 60, "Attendance": 75},
            # 5. Exactly 40% average with all subjects >= 35 (e.g. 35, 40, 45) -> Grade E, Pass
            {"Student_ID": "X5", "Name": "CaseExact40Pass", "Department": "ME", "Math_Marks": 35, "Physics_Marks": 40, "Python_Marks": 45, "Attendance": 75},
            # 6. Exactly 40% average but one subject below 35 (34, 43, 43) -> Grade E, Fail
            {"Student_ID": "X6", "Name": "CaseExact40SubjFail", "Department": "ME", "Math_Marks": 34, "Physics_Marks": 43, "Python_Marks": 43, "Attendance": 75},
        ])
        metrics_df = calculate_student_metrics(test_df)
        scored_df = apply_grading_and_status(metrics_df)

        x1 = scored_df.loc[scored_df["Student_ID"] == "X1"].iloc[0]
        self.assertEqual(x1["Average_Marks"], 45.0)
        self.assertEqual(x1["Grade"], "E")
        self.assertEqual(x1["Status"], "Pass")

        x2 = scored_df.loc[scored_df["Student_ID"] == "X2"].iloc[0]
        self.assertEqual(x2["Average_Marks"], 49.0)
        self.assertEqual(x2["Grade"], "E")
        self.assertEqual(x2["Status"], "Pass")

        x3 = scored_df.loc[scored_df["Student_ID"] == "X3"].iloc[0]
        self.assertLess(x3["Average_Marks"], 40.0)
        self.assertEqual(x3["Grade"], "F")
        self.assertEqual(x3["Status"], "Fail")

        x4 = scored_df.loc[scored_df["Student_ID"] == "X4"].iloc[0]
        self.assertGreaterEqual(x4["Average_Marks"], 40.0)
        self.assertEqual(x4["Grade"], "E")
        self.assertEqual(x4["Status"], "Fail")

        x5 = scored_df.loc[scored_df["Student_ID"] == "X5"].iloc[0]
        self.assertEqual(x5["Average_Marks"], 40.0)
        self.assertEqual(x5["Grade"], "E")
        self.assertEqual(x5["Status"], "Pass")

        x6 = scored_df.loc[scored_df["Student_ID"] == "X6"].iloc[0]
        self.assertEqual(x6["Average_Marks"], 40.0)
        self.assertEqual(x6["Grade"], "E")
        self.assertEqual(x6["Status"], "Fail")

        # Critical invariant: No Grade F student may have Status Pass
        grade_f_students = scored_df[scored_df["Grade"] == "F"]
        self.assertTrue((grade_f_students["Status"] == "Fail").all())

    def test_actual_dataset_grade_and_status_alignment(self):
        """
        Verify the actual students.csv records under the aligned policy.
        Ensures S103 and S110 are Grade E and Pass, and no Grade F student has Pass.
        """
        raw_df = load_dataset("students.csv")
        metrics_df = calculate_student_metrics(raw_df)
        scored_df = apply_grading_and_status(metrics_df)

        # S103 (Rohan Verma): 42, 38, 55 -> Avg 45.00 -> Grade E, Pass
        s103 = scored_df.loc[scored_df["Student_ID"] == "S103"].iloc[0]
        self.assertEqual(s103["Average_Marks"], 45.0)
        self.assertEqual(s103["Grade"], "E")
        self.assertEqual(s103["Status"], "Pass")

        # S110 (Rahul Mehta): 45, 50, 52 -> Avg 49.00 -> Grade E, Pass
        s110 = scored_df.loc[scored_df["Student_ID"] == "S110"].iloc[0]
        self.assertEqual(s110["Average_Marks"], 49.0)
        self.assertEqual(s110["Grade"], "E")
        self.assertEqual(s110["Status"], "Pass")

        # S108 (Aditya Joshi): Math 34 (< 35), Avg 40.67 -> Grade E, Fail
        s108 = scored_df.loc[scored_df["Student_ID"] == "S108"].iloc[0]
        self.assertEqual(s108["Grade"], "E")
        self.assertEqual(s108["Status"], "Fail")

        # Invariant on the real dataset: Zero students with Grade F and Status Pass
        grade_f_pass = scored_df[(scored_df["Grade"] == "F") & (scored_df["Status"] == "Pass")]
        self.assertEqual(len(grade_f_pass), 0)

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
