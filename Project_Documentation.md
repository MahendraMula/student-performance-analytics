# Formal Project Documentation: Student Performance Analytics System

**Assignment:** Python Project Assignment for Python with AI Students  
**Organization:** EWB Courses  
**Official Project Title:** Student Performance Analytics System  
**Submission Deadline:** 15 October 2026  

---

## 1. Project Title & Student Details

- **Project Title:** Student Performance Analytics System
- **Course Name:** Python with AI
- **Organization / Provider:** EWB Courses
- **Student Name:** Mahendra Mula `[Student Name]`
- **Email:** maheshbanu58@gmail.com `[Student Email]`
- **Submission Date:** October 2026

---

## 2. Objective

Educational institutions require rapid, reliable, and unbiased methods to evaluate cohort-wide student performance. Traditional manual spreadsheet evaluations are prone to formula errors, do not scale across multiple disciplines, and lack automated tie-handling or cohort diagnostics.

The objective of this project is to develop an automated command-line analytics application that:
1. Ingests student examination and attendance records from CSV files.
2. Performs vector-accelerated mathematical transformations (totals, averages, standard deviations) using **NumPy**.
3. Organizes, filters, and summarizes tabular records using **Pandas**.
4. Applies rigorous academic rules for letter grading and pass/fail determination.
5. Generates cohort-level insights: highest and lowest marks, class averages, subject-level performance comparison, and honor roll identification.
6. Presents data clearly for educators and evaluators without requiring inspection of source code.

---

## 3. Technologies Used

- **Python (Version 3.10+)**: Core programming language utilizing core constructs (variables, loops, conditionals, functions).
- **NumPy (Version 2.x)**: High-performance array operations for numerical summation, averages, standard deviation, and median.
- **Pandas (Version 2.x)**: Tabular data handling, CSV parsing, data alignment, boolean masking, and formatted display.
- **Matplotlib (Version 3.x)**: Generation of summary charts and visual reports.
- **Unittest (Standard Library)**: Automated test suite for numerical verification and edge-case handling.
- **Git & GitHub**: Version control and submission artifact hosting.

---

## 4. Dataset Description

The dataset [`students.csv`](students.csv) contains **20 realistic student records** across multiple engineering disciplines:

| Column Name | Data Type | Description | Sample Value |
|:---|:---|:---|:---|
| `Student_ID` | String | Unique identifier for each student | S101 |
| `Name` | String | Full student name | Aarav Sharma |
| `Department` | String | Department/Major | Computer Science |
| `Math_Marks` | Integer | Marks obtained in Mathematics (0–100) | 88 |
| `Physics_Marks` | Integer | Marks obtained in Physics (0–100) | 92 |
| `Python_Marks` | Integer | Marks obtained in Python Programming (0–100) | 95 |
| `Attendance` | Integer | Percentage of classes attended (0–100) | 94 |

**Data Integrity Features:**
- No missing or null values in demonstration records.
- Realistic score variance (ranges from 30 to 99) to validate all grade levels (`A` through `F`).
- Contains boundary scenarios: students failing due to average score vs. students failing due to an individual subject mark below 35.
- 100% synthetic demonstration data; does not contain real personal data.

---

## 5. Implementation Details

The implementation follows a modular architecture separating reusable logic ([`functions.py`](functions.py)) from the user execution driver ([`main.py`](main.py)):

### A. Data Ingestion & Validation
- Implemented in `load_dataset()`.
- Validates the existence of the CSV file on disk.
- Asserts that all mandatory columns are present before proceeding.
- Returns a structured Pandas DataFrame.

### B. Student-Level Calculations (NumPy Vectorization)
- Implemented in `calculate_student_metrics()`.
- Extracts marks columns into a 2D NumPy array matrix: `marks_matrix = df[subject_cols].to_numpy(dtype=float)`.
- Calculates row-wise sums: `np.sum(marks_matrix, axis=1)` to generate `Total_Marks`.
- Calculates row-wise means: `np.round(np.mean(marks_matrix, axis=1), 2)` to generate `Average_Marks`.

### C. Rule-Based Grading & Pass/Fail Evaluation
- Implemented in `assign_grade()` and `evaluate_pass_fail()`.
- Grades are evaluated through conditional statements:
  - `A`: Average $\ge 90.0$
  - `B`: $80.0 \le \text{Average} < 90.0$
  - `C`: $70.0 \le \text{Average} < 80.0$
  - `D`: $60.0 \le \text{Average} < 70.0$
  - `E`: $50.0 \le \text{Average} < 60.0$
  - `F`: $\text{Average} < 50.0$
- Pass/Fail rule:
  - A student **passes** if and only if: $\text{Average} \ge 40.0$ **AND** $\min(\text{Subject Marks}) \ge 35.0$.
  - Evaluated using explicit `for` loop iterations across subject scores.

### D. Cohort & Subject Analytics
- Implemented in `calculate_class_statistics()` and `analyze_subject_performance()`.
- Computes cohort metrics using NumPy: `np.mean()`, `np.median()`, `np.std()`, `np.max()`, and `np.min()`.
- Aggregates subject averages to determine the highest performing academic domain.
- Identifies Top Performers (`get_top_performers`) while preserving ties by matching threshold marks.

---

## 6. Key Features

1. **Clean Separation of Concerns**: Logic is organized cleanly between reusable backend functions and presentation code.
2. **True Numerical Optimization**: Uses native NumPy array buffers rather than slow Python standard loops for bulk calculations.
3. **Comprehensive Edge-Case Handling**: Handled scenarios include ties in top ranks, subject-specific failure criteria, and missing input files.
4. **Automated Unit Testing**: Includes 9 unit tests checking boundary conditions, missing files, and numerical accuracy.
5. **Human-Readable Output Formatting**: Console reports use aligned headers, tabular format, and visual dividers.

---

## 7. Output & Visual Results

### Terminal Output
The script prints structured sections:
1. Overall Student Performance Table
2. Overall Class Performance Metrics
3. Pass vs. Fail Breakdown
4. Subject-Wise Analytics
5. Top Performers (Honor Roll)
6. Lowest Performers

A high-resolution screenshot of the console execution is stored at:
[`screenshots/terminal_output.png`](screenshots/terminal_output.png)

### Analytics Visualizations
A multi-panel performance chart illustrating Subject-Wise Average Performance and Grade Distribution is stored at:
[`screenshots/analytics_summary_chart.png`](screenshots/analytics_summary_chart.png)

---

## 8. Final Outcome

The completed application successfully:
- Processes multi-subject student cohorts instantly.
- Accurately classifies performance across 6 grade categories.
- Correctly identifies that out of 20 students, **17 passed (85.0%)** and **3 failed (15.0%)**.
- Discovers that **Python** had the highest class average (74.75 marks).
- Highlights top achievers: S104 Ananya Iyer (97.33% average, Grade A), S114 Priya Pillai (95.67% average, Grade A), and S118 Tanvi Bhat (92.67% average, Grade A).

---

## 9. Challenges & Learning

### Technical Challenges Encountered
1. **Column Collision in Dynamic Filtering**: In an early iteration, `get_subject_columns` extracted all columns ending with `_Marks`. When `Total_Marks` was computed, subsequent calls incorrectly included totals in the subject average calculation. This was diagnosed and resolved by explicitly excluding computed aggregate columns.
2. **Handling Academic Ties**: Using simple `.head(3)` or `.iloc[:3]` arbitrarily excludes students who scored identical top marks. A threshold-based filtering approach was implemented so that all students matching the top score cutoff are recognized.
3. **Multi-Condition Pass Evaluation**: Distinguishing students who achieved an overall average above 40% but failed a single subject (such as Aditya Joshi scoring 34 in Math) required compound evaluation rather than naive thresholding on average marks.

### Key Concepts Learned
- Practical vectorization techniques using NumPy.
- DataFrame transformations, boolean indexing, and iteration in Pandas.
- Writing modular Python code with type annotations and docstrings.
- Constructing unit tests using Python's `unittest` framework.
- Managing code and project documentation according to educational and industry standards.

---

## 10. GitHub Repository

- **Repository Name:** `student-performance-analytics`
- **Owner:** `MahendraMula`
- **Repository URL:** `https://github.com/MahendraMula/student-performance-analytics`
- **Submission Status:** Ready for push to GitHub and URL submission via the EWB Courses Google Form.
