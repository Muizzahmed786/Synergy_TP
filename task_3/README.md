## Task objective
To implement csv parser without using any external libraries

## Folder structure.
```
└── 📁task_3
    └── 📁data
        ├── submissions.csv
    └── 📁output
        ├── manual_summary.json
        ├── pandas_summary.json
    └── 📁src
        └── 📁__pycache__
            ├── manual_parser.cpython-313.pyc
            ├── pandas_parser.cpython-313.pyc
        ├── main.py
        ├── manual_parser.py
        ├── pandas_parser.py
    └── README.md
```
## Required packages.
pandas, sys

## Setup instructions.
Since no external packages were used, directly clone the repository and <br/> execute the run command.

## Exact run command.
python task_3/src/main.py task_3/data/submissions.csv

## Expected output files.
1. manual_summary.json <br/>
2. pandas_summary.json

## Short explanation of the implemented logic.
the rows of the data file is read. for each row the values are stored by spliting with `,` being the limiter. Then the type conversion is applied on the `score` and `submission` column. <br />
