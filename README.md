# record-vertifier
record-verifier/
├── README.md
├── pyproject.toml
├── .gitignore
├── .env.example
│
├── data/
│   ├── raw/
│   │   └── entries.csv
│   ├── processed/
│   └── reports/
│
├── src/
│   └── record_verifier/
│       ├── __init__.py
│       ├── config/
│       │   ├── settings.py
│       │   └── sources.py
│       ├── ingestion/
│       │   └── load_entries.py
│       ├── search/
│       │   └── mock_search.py
│       ├── analysis/
│       │   ├── credibility.py
│       │   ├── verdict.py
│       │   └── risk.py
│       ├── reporting/
│       │   └── export.py
│       └── cli/
│           └── main.py
│
├── tests/
│   └── test_verdict.py
│
└── scripts/
    └── run_pipeline.py
