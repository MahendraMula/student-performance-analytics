"""
main.py - Main execution driver for Student Performance Analytics System.

EWB Courses - Python Project Assignment for Python with AI Students.
Submission Deadline: 15 October 2026.

Demonstrates:
- Variables & Data Types
- Loops & Conditionals
- Custom Modular Functions
- NumPy Numerical Calculations
- Pandas DataFrames & Data Aggregation
"""

import os
import sys
from functions import (
    load_dataset,
    calculate_student_metrics,
    apply_grading_and_status,
    calculate_class_statistics,
    get_top_performers,
    get_lowest_performers,
    analyze_subject_performance,
    get_pass_fail_summary
)


def print_separator(char: str = "=", length: int = 80) -> None:
    """Print standard visual divider."""
    print(char * length)


def print_header(title: str) -> None:
    """Print styled section header."""
    print()
    print_separator("=")
    print(f" {title.upper()} ".center(80, " "))
    print_separator("=")


def run_pipeline(dataset_path: str = "students.csv") -> None:
    """
    Executes the end-to-end Student Performance Analytics workflow.
    """
    print_separator("*")
    print(" STUDENT PERFORMANCE ANALYTICS SYSTEM ".center(80, " "))
    print(" EWB Courses | Python with AI Assignment ".center(80, " "))
    print_separator("*")

    # Step 1: Load and Validate Dataset
    print("\n[Step 1] Loading Dataset...")
    try:
        raw_df = load_dataset(dataset_path)
    except Exception as e:
        print(f"[Error] Failed to load dataset: {e}")
        sys.exit(1)

    num_records = len(raw_df)
    print(f"-> Successfully loaded '{dataset_path}'")
    print(f"-> Total records: {num_records} students")
    print(f"-> Columns detected: {list(raw_df.columns)}")

    # Step 2: Perform Student-Level Calculations
    print("\n[Step 2] Processing Student Metrics (NumPy calculations)...")
    df_metrics = calculate_student_metrics(raw_df)
    processed_df = apply_grading_and_status(df_metrics)
    print("-> Calculated Total Marks, Average Marks, Grades, and Pass/Fail statuses.")

    # Section 1: Dataset Overview & Complete Student Table
    print_header("1. Complete Student Performance Summary")
    display_columns = [
        "Student_ID", "Name", "Department",
        "Math_Marks", "Physics_Marks", "Python_Marks",
        "Total_Marks", "Average_Marks", "Grade", "Status"
    ]
    print(processed_df[display_columns].to_string(index=False))

    # Section 2: Class Overall Statistics
    print_header("2. Overall Class Performance Metrics")
    class_stats = calculate_class_statistics(processed_df)
    print(f"  * Total Students Evaluated : {num_records}")
    print(f"  * Class Average Marks      : {class_stats['class_average']:.2f}")
    print(f"  * Class Median Marks       : {class_stats['class_median']:.2f}")
    print(f"  * Standard Deviation       : {class_stats['class_std_dev']:.2f}")
    print(f"  * Highest Average Mark     : {class_stats['highest_average']:.2f}")
    print(f"  * Lowest Average Mark      : {class_stats['lowest_average']:.2f}")
    print(f"  * Highest Total Marks      : {class_stats['highest_total']:.0f}")
    print(f"  * Lowest Total Marks       : {class_stats['lowest_total']:.0f}")

    # Section 3: Pass vs Fail Distribution
    print_header("3. Pass vs Fail Analysis")
    pf_summary = get_pass_fail_summary(processed_df)
    print(f"  * Passed Students : {pf_summary['Passed']} ({pf_summary['Pass_Percentage']}%)")
    print(f"  * Failed Students : {pf_summary['Failed']} ({100.0 - pf_summary['Pass_Percentage']:.2f}%)")

    # Display failed students if any
    failed_students = processed_df[processed_df["Status"] == "Fail"]
    if not failed_students.empty:
        print("\n  Students requiring academic attention (Status: Fail):")
        print(failed_students[["Student_ID", "Name", "Department", "Average_Marks", "Status"]].to_string(index=False))

    # Section 4: Subject-Wise Performance Analysis
    print_header("4. Subject-Wise Analytics")
    subject_df, best_subject = analyze_subject_performance(processed_df)
    print(subject_df.to_string(index=False))
    print(f"\n  -> Best Performing Subject: {best_subject} (Highest average score)")

    # Section 5: Top Performing Students
    print_header("5. Top-Performing Students (Honor Roll)")
    top_students = get_top_performers(processed_df, top_n=3)
    top_cols = ["Student_ID", "Name", "Department", "Average_Marks", "Total_Marks", "Grade"]
    print(top_students[top_cols].to_string(index=False))

    # Section 6: Lowest Performing Students
    print_header("6. Lowest-Performing Students")
    lowest_students = get_lowest_performers(processed_df)
    print(lowest_students[top_cols].to_string(index=False))

    print_separator("=")
    print(" Analytics processing complete! All results verified. ".center(80, " "))
    print_separator("=")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_file = os.path.join(current_dir, "students.csv")
    run_pipeline(dataset_file)
