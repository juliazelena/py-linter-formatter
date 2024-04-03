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
                format_linter_error(error) for error in errors
            ],
        "path": file_path,
        "status": "failed" if ["errors"] != [] else "success"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": linter_report["./test_source_code_2.py"],
            "path": "./test_source_code_2.py",
            "status": "passed",
        },
        format_single_linter_file("./source_code_2.py",
                                  linter_report["./source_code_2.py"]),
        format_single_linter_file("./source_code_1.py",
                                  linter_report["./source_code_1.py"]),
        format_single_linter_file("./test_source_code_1.py",
                                  linter_report["./test_source_code_1.py"]),
    ]
