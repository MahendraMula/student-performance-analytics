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
- **Student Name:** Mula Venkata Surya Mahendra
- **Email:** maheshbanu58@gmail.com
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
- Implemented in `assign_grade()`, `evaluate_pass_fail()`, and `apply_grading_and_status()`.
- Grades are evaluated under this project's defined grading policy using conditional statements on `Average_Marks`:
  - `A`: $90.0 \le \text{Average} \le 100.0\%$
  - `B`: $80.0 \le \text{Average} < 90.0\%$
  - `C`: $70.0 \le \text{Average} < 80.0\%$
  - `D`: $60.0 \le \text{Average} < 70.0\%$
  - `E`: $40.0 \le \text{Average} < 60.0\%$
  - `F`: $\text{Average} < 40.0\%$ (Failing average)
- Pass/Fail rule:
  - A student **passes** if and only if: $\text{Average} \ge 40.0$ **AND** $\min(\text{Subject Marks}) \ge 35.0$.
  - Otherwise, the student fails. Evaluated using explicit `for` loop iterations across subject scores.
- Policy Alignment:
  - Grade F is strictly aligned with failing average performance ($\text{Average} < 40.0\%$). Consequently, any student assigned Grade F automatically receives Status **Fail** (e.g., S113 at 34.00% and S119 at 39.33%), eliminating contradictions where a student receives Grade F but passes.
  - Students with an average between $40.0\%$ and $59.99\%$ receive **Grade E**. If all their individual subject marks are $\ge 35$, they receive Status **Pass** (e.g., S103 at 45.00%, S110 at 49.00%, and S115 at 58.33%).
  - If a student achieves an overall average $\ge 40.0\%$ but scores $< 35$ in any subject (e.g., student S108 scoring 34 in Math with a 40.67% average), they receive **Grade E** and Status **Fail**.

### D. Cohort, Subject & Visual Analytics
- Implemented in `calculate_class_statistics()`, `analyze_subject_performance()`, `get_top_performers()`, `get_lowest_performers()`, `get_pass_fail_summary()`, and `generate_analytics_chart()`.
- Computes cohort metrics using NumPy: `np.mean()`, `np.median()`, `np.std()`, `np.max()`, and `np.min()`.
- Aggregates subject averages (`Math: 68.65`, `Physics: 70.45`, `Python: 74.75`) to determine the highest-performing academic domain (`Python`).
- Identifies Top Performers (`get_top_performers`) and Lowest Performers (`get_lowest_performers`) while preserving ties by matching threshold marks.
- Renders a two-panel Matplotlib analytical summary chart (`generate_analytics_chart`) depicting Subject-Wise Average Performance and Grade Distribution (`A` through `F`).

---

## 6. Key Features

1. **Clean Separation of Concerns**: Logic is organized cleanly between reusable backend functions ([`functions.py`](functions.py)) and presentation driver code ([`main.py`](main.py)).
2. **Vectorized Numerical Computations**: Uses NumPy array operations (`np.sum`, `np.mean`, `np.median`, `np.std`) for accurate student and cohort calculations.
3. **Comprehensive Edge-Case Handling**: Handled scenarios include ties in top and lowest ranks, subject-specific failure criteria, aligned grading boundaries, and missing input files.
4. **Automated Unit Testing**: Includes **12 automated unit tests** in [`test_analytics.py`](test_analytics.py) checking all grade boundaries (`40`, `50`, `60`, `70`, `80`, `90`), pass/fail edge cases, real dataset verification, missing files, numerical accuracy, and chart generation.
5. **Single Consolidated Terminal Report**: Console output is presented in one unified `Complete Student Performance Summary` section combining the full 20-student table and compact cohort statistics.

---

## 7. Output & Visual Results

### Terminal Output
Executing `python main.py` outputs a single consolidated terminal section titled **Complete Student Performance Summary** containing:
1. Complete student tabular records (`Student_ID`, `Name`, `Department`, `Math_Marks`, `Physics_Marks`, `Python_Marks`, `Total_Marks`, `Average_Marks`, `Grade`, `Status`, `Attendance`).
2. Integrated cohort performance summary (`20 Students | Passed: 17 (85.0%) | Failed: 3`, `Class Average: 71.28% (Median: 76.00%, Std Dev: 20.51)`, `Highest Score: 97.33% (Total: 292) | Lowest Score: 34.00% (Total: 102)`, `Subject Averages: Math: 68.65, Physics: 70.45, Python: 74.75 (Best Subject: Python)`, `Top Performer(s)`, and `Lowest Performer`).

A verified screenshot of the terminal output is stored at:
[`screenshots/terminal_output.png`](screenshots/terminal_output.png)

### Analytics Visualizations
A two-panel Matplotlib summary chart generated by `generate_analytics_chart()` is stored at:
[`screenshots/analytics_summary_chart.png`](screenshots/analytics_summary_chart.png)
- **Left Panel (`Subject-Wise Average Performance`)**: Bar chart displaying exact subject averages — Math (`68.65`), Physics (`70.45`), and Python (`74.75`).
- **Right Panel (`Grade Distribution (A to F)`)**: Bar chart displaying cohort grade counts under the aligned policy — `A: 6`, `B: 4`, `C: 1`, `D: 3`, `E: 4`, and `F: 2`.

---

## 8. Final Outcome

The completed application successfully:
- Processes multi-subject student cohorts from [`students.csv`](students.csv) (20 student records).
- Classifies student performance across 6 aligned grade categories (`A: 6`, `B: 4`, `C: 1`, `D: 3`, `E: 4`, `F: 2`).
- Identifies that out of 20 students, **17 passed (85.0%)** and **3 failed (15.0%)** (S108 with Grade E due to Math = 34 < 35; S113 and S119 with Grade F due to Average < 40%).
- Determines that **Python** achieved the highest subject average (`74.75`, compared to Physics `70.45` and Math `68.65`).
- Highlights top achievers: S104 Ananya Iyer (`97.33%` average, Total `292`, Grade `A`), S114 Priya Pillai (`95.67%` average, Grade `A`), and S118 Tanvi Bhat (`92.67%` average, Grade `A`), as well as lowest performer S113 Ishaan Deshmukh (`34.0%` average, Total `102`, Grade `F`).

---

## 9. Challenges & Learning

### Technical Challenges Encountered
1. **Column Collision in Dynamic Filtering**: In an early iteration, `get_subject_columns` extracted all columns ending with `_Marks`. When `Total_Marks` was computed, subsequent calls incorrectly included totals in the subject average calculation. This was diagnosed and resolved by explicitly excluding computed aggregate columns.
2. **Handling Academic Ties**: Using simple `.head(3)` or `.iloc[:3]` arbitrarily excludes students who scored identical top marks. A threshold-based filtering approach was implemented so that all students matching the top score cutoff are recognized.
3. **Multi-Condition Pass Evaluation**: Distinguishing students who achieved an overall average above 40% but failed a single subject (such as Aditya Joshi scoring 34 in Math) required compound evaluation rather than naive thresholding on average marks.
4. **Policy Alignment between Grades and Pass Status**: In the initial scheme, Grade F was defined as `< 50%` while pass required an average of `40%`, causing students in the 40–49% range (S103, S110) to receive Grade F while passing. The grading scale was updated to allocate Grade E for 40–59.99% and Grade F strictly for `< 40%`, ensuring Grade F unambiguously indicates failing performance and eliminating contradictory outcomes.

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
