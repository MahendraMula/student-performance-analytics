"""
functions.py - Reusable Data Analytics Functions for Student Performance Analytics System.

This module provides data loading, student-level calculations, class-level analytics,
grading logic, pass/fail evaluation, and presentation utilities using NumPy and Pandas.
"""

from typing import Dict, List, Tuple
import os
import numpy as np
import pandas as pd


def load_dataset(file_path: str = "students.csv") -> pd.DataFrame:
    """
    Load student dataset from a CSV file into a Pandas DataFrame.
    Validates file existence, schema, and basic integrity.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: Dataset file not found at '{file_path}'. Please check path.")

    df = pd.read_csv(file_path)

    required_columns = [
        "Student_ID", "Name", "Department",
        "Math_Marks", "Physics_Marks", "Python_Marks", "Attendance"
    ]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Error: Dataset is missing required columns: {missing}")

    if df.empty:
        raise ValueError("Error: Dataset file is empty.")

    return df


def get_subject_columns(df: pd.DataFrame) -> List[str]:
    """
    Extract columns representing subject marks (excluding computed totals or averages).
    """
    exclude = {"Total_Marks", "Average_Marks"}
    return [col for col in df.columns if col.endswith("_Marks") and col not in exclude]


def calculate_student_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Total Marks and Average Marks for each student using NumPy.
    """
    processed_df = df.copy()
    subject_cols = get_subject_columns(processed_df)

    # Extract numerical marks matrix into NumPy array
    marks_matrix = processed_df[subject_cols].to_numpy(dtype=float)

    # NumPy calculations across columns (axis=1: per student)
    processed_df["Total_Marks"] = np.sum(marks_matrix, axis=1)
    processed_df["Average_Marks"] = np.round(np.mean(marks_matrix, axis=1), 2)

    return processed_df


def assign_grade(average_mark: float) -> str:
    """
    Assign letter grade based on student average marks:
    - A : average >= 90
    - B : 80 <= average < 90
    - C : 70 <= average < 80
    - D : 60 <= average < 70
    - E : 50 <= average < 60
    - F : average < 50
    """
    if average_mark >= 90.0:
        return "A"
    elif average_mark >= 80.0:
        return "B"
    elif average_mark >= 70.0:
        return "C"
    elif average_mark >= 60.0:
        return "D"
    elif average_mark >= 50.0:
        return "E"
    else:
        return "F"


def evaluate_pass_fail(row: pd.Series, subject_cols: List[str]) -> str:
    """
    Determine Pass/Fail status for a student:
    Condition: Average marks >= 40 AND each individual subject mark >= 35.
    Demonstrates conditional statements.
    """
    if row["Average_Marks"] < 40.0:
        return "Fail"

    for col in subject_cols:
        if row[col] < 35.0:
            return "Fail"

    return "Pass"


def apply_grading_and_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply grade assignment and pass/fail evaluation across the DataFrame.
    Demonstrates loops and conditional checks.
    """
    processed_df = df.copy()
    subject_cols = get_subject_columns(processed_df)

    grades: List[str] = []
    statuses: List[str] = []

    # Iterate over student records using loop
    for idx, row in processed_df.iterrows():
        grade = assign_grade(row["Average_Marks"])
        status = evaluate_pass_fail(row, subject_cols)
        grades.append(grade)
        statuses.append(status)

    processed_df["Grade"] = grades
    processed_df["Status"] = statuses

    return processed_df


def calculate_class_statistics(df: pd.DataFrame) -> Dict[str, float]:
    """
    Compute overall class-level summary statistics using NumPy.
    """
    averages = df["Average_Marks"].to_numpy()
    totals = df["Total_Marks"].to_numpy()

    return {
        "class_average": float(np.round(np.mean(averages), 2)),
        "class_median": float(np.round(np.median(averages), 2)),
        "class_std_dev": float(np.round(np.std(averages), 2)),
        "highest_average": float(np.max(averages)),
        "lowest_average": float(np.min(averages)),
        "highest_total": float(np.max(totals)),
        "lowest_total": float(np.min(totals)),
    }


def get_top_performers(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """
    Retrieve top N performing students based on Average Marks and Total Marks.
    Properly handles ties by including all students matching the threshold score.
    """
    # Sort descending by Average_Marks and Total_Marks
    sorted_df = df.sort_values(by=["Average_Marks", "Total_Marks"], ascending=[False, False])
    if len(sorted_df) <= top_n:
        return sorted_df

    # Threshold mark of the top_n-th student to handle ties fairly
    cutoff_mark = sorted_df.iloc[top_n - 1]["Average_Marks"]
    return sorted_df[sorted_df["Average_Marks"] >= cutoff_mark]


def get_lowest_performers(df: pd.DataFrame, bottom_n: int = 2) -> pd.DataFrame:
    """
    Retrieve lowest performing student(s) based on Average Marks.
    Properly handles ties by matching the minimum score.
    """
    min_avg = df["Average_Marks"].min()
    return df[df["Average_Marks"] == min_avg]


def analyze_subject_performance(df: pd.DataFrame) -> Tuple[pd.DataFrame, str]:
    """
    Calculate subject-wise average marks, minimum, and maximum using NumPy/Pandas.
    Identifies the best-performing subject based on average marks.
    """
    subject_cols = get_subject_columns(df)
    stats_list = []

    for subject in subject_cols:
        marks = df[subject].to_numpy()
        subj_name = subject.replace("_Marks", "")
        stats_list.append({
            "Subject": subj_name,
            "Average_Marks": round(float(np.mean(marks)), 2),
            "Highest_Marks": int(np.max(marks)),
            "Lowest_Marks": int(np.min(marks)),
            "Std_Dev": round(float(np.std(marks)), 2),
        })

    subject_df = pd.DataFrame(stats_list)
    best_subject_idx = subject_df["Average_Marks"].idxmax()
    best_subject = subject_df.loc[best_subject_idx, "Subject"]

    return subject_df, best_subject


def get_pass_fail_summary(df: pd.DataFrame) -> Dict[str, int]:
    """
    Count passed and failed students and compute passing percentage.
    """
    total_students = len(df)
    passed_count = int((df["Status"] == "Pass").sum())
    failed_count = int((df["Status"] == "Fail").sum())
    pass_percentage = round((passed_count / total_students) * 100, 2) if total_students > 0 else 0.0

    return {
        "Total": total_students,
        "Passed": passed_count,
        "Failed": failed_count,
        "Pass_Percentage": pass_percentage
    }
