import json
import os

REPORT_FILE = "backend/reports.json"


def load_reports():
    if not os.path.exists(REPORT_FILE):
        return []

    with open(REPORT_FILE, "r") as file:
        return json.load(file)


def save_reports(reports):
    with open(REPORT_FILE, "w") as file:
        json.dump(reports, file, indent=4)


def submit_report(content, reason):

    reports = load_reports()

    new_report = {
        "content": content,
        "reason": reason
    }

    reports.append(new_report)

    save_reports(reports)

    return "Report submitted successfully"


def get_all_reports():
    return load_reports()