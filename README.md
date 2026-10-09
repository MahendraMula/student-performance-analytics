# Student Performance Analytics System

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-2.x-013243.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458.svg)
![Build Status](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)

**Assignment:** Python Project Assignment for Python with AI Students  
**Organization:** EWB Courses  
**Official Project Title:** Student Performance Analytics System  
**Submission Deadline:** 15 October 2026  

---

## 1. Project Overview

The **Student Performance Analytics System** is a modular Python data analysis project developed for the EWB Courses Python with AI curriculum. The system automates the ingestion, numerical processing, academic grading, and cohort-level performance analysis of student academic records using **NumPy** and **Pandas**.

It takes raw student marks across multiple disciplines, performs vectorized mathematical calculations, evaluates rule-based academic outcomes, and generates human-readable statistical summaries.

---

## 2. Objective & Problem Solved

### The Problem
Manual evaluation of student marks across departments is labor-intensive, error-prone, and slow. Educators frequently struggle to quickly identify underperforming students requiring intervention, detect subject-level teaching bottlenecks, and recognize top academic achievers.

### The Objective
To build an automated, transparent, and reproducible command-line analytics pipeline that:
- Reads student records from standardized CSV datasets.
- Computes individual totals and averages using fast numerical operations.
- Automatically determines academic grades and pass/fail statuses using explicit conditional rules.
- Computes cohort-wide benchmarks (class average, median, standard deviation, extrema).
- Conducts subject-wise diagnostic evaluations to find high and low-scoring domains.
- Handles edge cases such as academic ties and missing files gracefully.

---

## 3. Technologies Used

- **Python (3.10+)**: Primary language demonstrating variables, data types, loops, conditionals, and functions.
- **NumPy**: Vectorized array operations, matrix sum/mean calculations, standard deviation, and median.
- **Pandas**: Tabular DataFrame loading, schema validation, data slicing, aggregation, and tabular formatting.
- **Matplotlib**: Generation of analytical summary charts and visual reports.
- **Unittest**: Automated testing suite verifying analytical calculations.

---

## 4. Key Features

1. **Robust Data Ingestion**: Validates file existence and required schema before processing.
2. **Vectorized Numerical Computations**: Employs NumPy array math (`np.sum`, `np.mean`) for fast metric calculation.
3. **Explicit Rule-Based Grading**: Evaluates multi-tier letter grades (`A` to `F`) without ambiguity.
4. **Holistic Pass/Fail Assessment**: Enforces both cohort average minimums and subject-level clearing criteria.
5. **Cohort-Wide Benchmarking**: Computes class average, median, standard deviation, and boundary values.
6. **Subject-Wise Analytics**: Measures average scores per subject and programmatically identifies the strongest subject.
7. **Tie-Aware Honor Roll**: Identifies top performers without arbitrarily discarding students with identical top marks.
8. **At-Risk Student Flagging**: Isolates failed students for targeted academic counseling.

---

## 5. Dataset Description

The project includes `students.csv`, a clean and realistic demonstration dataset containing **20 student records** across multiple engineering departments:

| Column Name | Data Type | Description | Valid Range |
|:---|:---|:---|:---|
| `Student_ID` | String | Unique student alphanumeric identifier | S101 – S120 |
| `Name` | String | Full name of the student | Real-world sample names |
| `Department` | String | Academic department (CS, IT, DS, ME) | Text |
| `Math_Marks` | Integer | Mathematics exam score | 0 – 100 |
| `Physics_Marks` | Integer | Physics exam score | 0 – 100 |
| `Python_Marks` | Integer | Python programming score | 0 – 100 |
| `Attendance` | Integer | Lecture attendance percentage | 0 – 100% |

*Note: The dataset represents synthetic demonstration data and contains no real student personal data.*

---

## 6. Project Structure

```
student-performance-analytics/
├── main.py                     # Main execution pipeline and console reporting
├── functions.py                # Reusable analytics, grading, and NumPy/Pandas functions
├── students.csv                # Demonstration student dataset (20 records)
├── test_analytics.py           # Comprehensive automated unit test suite
├── requirements.txt            # Project dependencies (numpy, pandas, matplotlib)
├── .gitignore                  # Git ignore rules for Python artifacts and caches
├── README.md                   # Comprehensive project documentation
├── Project_Documentation.md   # Formal assessment documentation (10 PDF sections)
└── screenshots/                # Verified visual execution outputs
    ├── terminal_output.png
    └── analytics_summary_chart.png
```

---

## 7. Grading & Pass/Fail Rules

### Grading Scheme
Grades are derived directly from a student's unrounded average marks across all subjects:

- **Grade A**: $\text{Average} \ge 90.0$
- **Grade B**: $80.0 \le \text{Average} < 90.0$
- **Grade C**: $70.0 \le \text{Average} < 80.0$
- **Grade D**: $60.0 \le \text{Average} < 70.0$
- **Grade E**: $50.0 \le \text{Average} < 60.0$
- **Grade F**: $\text{Average} < 50.0$

### Pass/Fail Evaluation Criteria
To maintain academic rigor, passing requires meeting two conditions simultaneously:
1. **Overall Average**: The student's overall average must be at least **40.0%**.
2. **Subject Minimum**: The student must score at least **35.0 marks** in every individual subject.

*If a student has an overall average $\ge 40\%$ but scores $< 35$ in any single subject, their status is evaluated as **Fail**.*

---

## 8. Setup & Installation

### Prerequisites
- Python 3.10 or higher installed.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MahendraMula/student-performance-analytics.git
   cd student-performance-analytics
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 9. Running the Project

Run the main analytics pipeline from the project root:

```bash
python main.py
```

---

## 10. Sample Output

```
********************************************************************************
                      STUDENT PERFORMANCE ANALYTICS SYSTEM                      
                    EWB Courses | Python with AI Assignment                     
********************************************************************************

[Step 1] Loading Dataset...
-> Successfully loaded 'students.csv'
-> Total records: 20 students
-> Columns detected: ['Student_ID', 'Name', 'Department', 'Math_Marks', 'Physics_Marks', 'Python_Marks', 'Attendance']

[Step 2] Processing Student Metrics (NumPy calculations)...
-> Calculated Total Marks, Average Marks, Grades, and Pass/Fail statuses.

================================================================================
                    1. COMPLETE STUDENT PERFORMANCE SUMMARY                     
================================================================================
Student_ID            Name             Department  Math_Marks  Physics_Marks  Python_Marks  Total_Marks  Average_Marks Grade Status
      S101    Aarav Sharma       Computer Science          88             92            95        275.0          91.67     A   Pass
      S102      Diya Patel       Computer Science          76             81            84        241.0          80.33     B   Pass
      S103     Rohan Verma Information Technology          42             38            55        135.0          45.00     F   Pass
      S104     Ananya Iyer           Data Science          95             98            99        292.0          97.33     A   Pass
...

================================================================================
                      2. OVERALL CLASS PERFORMANCE METRICS                      
================================================================================
  * Total Students Evaluated : 20
  * Class Average Marks      : 71.28
  * Class Median Marks       : 76.00
  * Standard Deviation       : 20.51
  * Highest Average Mark     : 97.33
  * Lowest Average Mark      : 34.00
  * Highest Total Marks      : 292
  * Lowest Total Marks       : 102

================================================================================
                            3. PASS VS FAIL ANALYSIS                            
================================================================================
  * Passed Students : 17 (85.0%)
  * Failed Students : 3 (15.00%)

================================================================================
                           4. SUBJECT-WISE ANALYTICS                            
================================================================================
Subject  Average_Marks  Highest_Marks  Lowest_Marks  Std_Dev
   Math          68.65             96            30    21.28
Physics          70.45             98            32    21.25
 Python          74.75             99            40    19.29

  -> Best Performing Subject: Python (Highest average score)

================================================================================
                    5. TOP-PERFORMING STUDENTS (HONOR ROLL)                     
================================================================================
Student_ID         Name   Department  Average_Marks  Total_Marks Grade
      S104  Ananya Iyer Data Science          97.33        292.0     A
      S114 Priya Pillai Data Science          95.67        287.0     A
      S118   Tanvi Bhat Data Science          92.67        278.0     A
```

---

## 11. Testing & Verification

Run the automated test suite with:

```bash
python -m unittest test_analytics.py
```

**Verification Results:**
- 9 test cases executed.
- 100% pass rate covering data loading, NumPy math, boundary grading, tie-handling, and pass/fail logic.

---

## 12. Screenshots

Visual execution captures are maintained inside the [`screenshots/`](screenshots/) directory:

- **Terminal Output Screenshot**: `screenshots/terminal_output.png`
- **Analytics Performance Chart**: `screenshots/analytics_summary_chart.png`

---

## 13. Limitations & Assumptions

1. **Fixed Evaluation Scale**: Subject marks are assumed to be out of a maximum of 100.
2. **Even Weighting**: All subjects carry equal weight when computing total marks and average marks.
3. **Synthetic Demonstration Data**: The dataset represents realistic synthetic academic records curated for educational demonstration.

---

## 14. GitHub Repository

- **Repository URL**: `https://github.com/MahendraMula/student-performance-analytics` *(To be pushed upon remote repository creation)*
