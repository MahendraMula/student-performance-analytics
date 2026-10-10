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
================================================================================
                      Complete Student Performance Summary                      
================================================================================
Student_ID            Name             Department  Math_Marks  Physics_Marks  Python_Marks  Total_Marks  Average_Marks Grade Status  Attendance
      S101    Aarav Sharma       Computer Science          88             92            95        275.0          91.67     A   Pass          94
      S102      Diya Patel       Computer Science          76             81            84        241.0          80.33     B   Pass          88
      S103     Rohan Verma Information Technology          42             38            55        135.0          45.00     F   Pass          72
      S104     Ananya Iyer           Data Science          95             98            99        292.0          97.33     A   Pass          98
      S105    Vikram Singh             Mechanical          65             70            68        203.0          67.67     D   Pass          80
      S106      Neha Gupta       Computer Science          58             62            60        180.0          60.00     D   Pass          85
      S107      Kavya Nair           Data Science          91             89            94        274.0          91.33     A   Pass          92
      S108    Aditya Joshi Information Technology          34             40            48        122.0          40.67     F   Fail          65
      S109     Pooja Reddy       Computer Science          82             78            85        245.0          81.67     B   Pass          90
      S110     Rahul Mehta             Mechanical          45             50            52        147.0          49.00     F   Pass          70
      S111  Sneha Kulkarni           Data Science          89             94            91        274.0          91.33     A   Pass          95
      S112       Varun Rao Information Technology          72             68            75        215.0          71.67     C   Pass          82
      S113 Ishaan Deshmukh       Computer Science          30             32            40        102.0          34.00     F   Fail          60
      S114    Priya Pillai           Data Science          96             93            98        287.0          95.67     A   Pass          96
      S115      Manish Das             Mechanical          55             58            62        175.0          58.33     E   Pass          78
      S116 Riya Chatterjee       Computer Science          79             84            88        251.0          83.67     B   Pass          89
      S117  Siddharth Jain Information Technology          63             67            71        201.0          67.00     D   Pass          84
      S118      Tanvi Bhat           Data Science          90             92            96        278.0          92.67     A   Pass          93
      S119    Karan Chopra             Mechanical          38             36            44        118.0          39.33     F   Fail          68
      S120     Meera Menon       Computer Science          85             87            90        262.0          87.33     B   Pass          91

--------------------------------------------------------------------------------
Class Overview : 20 Students | Passed: 17 (85.0%) | Failed: 3
Class Average  : 71.28% (Median: 76.00%, Std Dev: 20.51)
Highest Score  : 97.33% (Total: 292) | Lowest Score: 34.00% (Total: 102)
Subject Averages: Math: 68.65, Physics: 70.45, Python: 74.75 (Best Subject: Python)
Top Performer(s): Ananya Iyer (97.33%), Priya Pillai (95.67%), Tanvi Bhat (92.67%)
Lowest Performer: Ishaan Deshmukh (34.0%)
================================================================================
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
