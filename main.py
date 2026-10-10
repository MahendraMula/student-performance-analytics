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


def run_pipeline(dataset_path: str = "students.csv") -> None:
    """
    Executes the end-to-end Student Performance Analytics workflow
    and displays a single unified performance summary.
    """
    try:
        raw_df = load_dataset(dataset_path)
    except Exception as e:
        print(f"[Error] Failed to load dataset: {e}")
        sys.exit(1)

    # Preserve all student-level calculations internally
    df_metrics = calculate_student_metrics(raw_df)
    processed_df = apply_grading_and_status(df_metrics)

    # Preserve all class-level, subject, and top-performer analytics internally
    class_stats = calculate_class_statistics(processed_df)
    pf_summary = get_pass_fail_summary(processed_df)
    subject_df, best_subject = analyze_subject_performance(processed_df)
    top_students = get_top_performers(processed_df, top_n=3)
    lowest_students = get_lowest_performers(processed_df)

    # Exactly one main output section
    print_separator("=")
    print(" Complete Student Performance Summary ".center(80, " "))
    print_separator("=")

    # Complete student records table with Attendance included
    display_columns = [
        "Student_ID", "Name", "Department",
        "Math_Marks", "Physics_Marks", "Python_Marks",
        "Total_Marks", "Average_Marks", "Grade", "Status", "Attendance"
    ]
    print(processed_df[display_columns].to_string(index=False))

    # Compact summary within the same section without additional headings
    top_names = ", ".join(f"{row['Name']} ({row['Average_Marks']}%)" for _, row in top_students.iterrows())
    lowest_names = ", ".join(f"{row['Name']} ({row['Average_Marks']}%)" for _, row in lowest_students.iterrows())
    subj_avg_str = ", ".join(f"{row['Subject']}: {row['Average_Marks']}" for _, row in subject_df.iterrows())

    print()
    print_separator("-")
    print(f"Class Overview : {len(processed_df)} Students | Passed: {pf_summary['Passed']} ({pf_summary['Pass_Percentage']}%) | Failed: {pf_summary['Failed']}")
    print(f"Class Average  : {class_stats['class_average']:.2f}% (Median: {class_stats['class_median']:.2f}%, Std Dev: {class_stats['class_std_dev']:.2f})")
    print(f"Highest Score  : {class_stats['highest_average']:.2f}% (Total: {class_stats['highest_total']:.0f}) | Lowest Score: {class_stats['lowest_average']:.2f}% (Total: {class_stats['lowest_total']:.0f})")
    print(f"Subject Averages: {subj_avg_str} (Best Subject: {best_subject})")
    print(f"Top Performer(s): {top_names}")
    print(f"Lowest Performer: {lowest_names}")
    print_separator("=")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_file = os.path.join(current_dir, "students.csv")
    run_pipeline(dataset_file)
