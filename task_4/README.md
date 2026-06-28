## Task objective
Data cleaning on a messy dataset

## Folder structure.
```
└── 📁task_4
    └── 📁data
        ├── messy_students.csv
    └── 📁output
        ├── cleaned_students.csv
        ├── cleaning_report.md
        ├── summary_after.json
        ├── summary_before.json
    └── 📁src
        └── 📁__pycache__
            ├── clean_data.cpython-313.pyc
            ├── validate_data.cpython-313.pyc
        ├── clean_data.py
        ├── main.py
        └── validate_data.py
```
## Required packages.
pandas, sys, json

## Setup instructions.
Make sure the required packages are installed.

## Exact run command.
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv

## Expected output files.
1. summary_before.json <br/>
2. summary_after.json <br/>
3. cleaned_student.csv <br />
4. cleaning_report.md <br />

## Report file path
`task_4/output/cleaning_report.md`

## Short explanation of the implemented logic.
- The dataset was loaded to a dataframe.
- The duplicate rows were removed.
- `domain` column was standardized
- fields like `attendance_percent`, `weight`, `height`, `study_hours` were made consistent
- for numeric attributes, missing fields were replaced by the mean value
- values which were out of bound in `attendace_percent` were capped between `[0, 100]`.
