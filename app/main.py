def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line_number"),
        "column": error.get("column_number"),
        "message": error.get("text"),
        "name": error.get("code"),
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors":
            [
                {
                    "line": error.get("line_number"),
                    "column": error.get("column_number"),
                    "message": error.get("text"),
                    "name": error.get("code"),
                    "source": "flake8",
                }
                for error in errors
            ],
        "path": file_path,
        "status": "failed",
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report["./test_source_code_2.py"],
            "path": "./test_source_code_2.py",
            "status": "passed",
        },
        {
            "errors":
            [
                {
                    "line": value.get("line_number"),
                    "column": value.get("column_number"),
                    "message": value.get("text"),
                    "name": value.get("code"),
                    "source": "flake8",
                }
                for value in linter_report["./source_code_2.py"]
            ],
            "path": "./source_code_2.py",
            "status": "failed",
        },
        {
            "errors":
                [
                    {
                        "line": value.get("line_number"),
                        "column": value.get("column_number"),
                        "message": value.get("text"),
                        "name": value.get("code"),
                        "source": "flake8",
                    }
                    for value in linter_report["./source_code_1.py"]
                ],
            "path": "./source_code_1.py",
            "status": "failed",
        },
        {
            "errors":
                [
                    {
                        "line": value.get("line_number"),
                        "column": value.get("column_number"),
                        "message": value.get("text"),
                        "name": value.get("code"),
                        "source": "flake8",
                    }
                    for value in linter_report["./test_source_code_1.py"]
                ],
            "path": "./test_source_code_1.py",
            "status": "failed",
        },

    ]
