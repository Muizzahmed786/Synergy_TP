import csv
import json
from typing import List, Dict

def read_submissions(file_path: str) -> List[Dict]:
    submissions = []
    try:
        with open(file_path, "r") as file:
            read = csv.DictReader(file)
            for r in read:
                try:
                    r["score"] = int(r["score"])
                    submissions.append(r)
                except TypeError:
                    print(f"Invalid score for {r['name']}")
                    continue
    except FileNotFoundError:
        print(f"file {file_path} not found :( please check your file path")
        return []
    return submissions

def get_submitted_students(data: List[Dict]) -> List[Dict]:
    submitted_students = []
    for student in data:
        if student["submitted"].lower() == "yes":
            submitted_students.append(student)

    return submitted_students

def calculate_average_score(submitted_students: List[Dict]) -> float:
    if len(submitted_students) == 0: return 0
    total_score = 0
    for student in submitted_students:
        total_score += student["score"]
    avg = total_score / len(submitted_students)

    return avg

def get_domain_wise_average(submitted_students: List[Dict]) -> Dict[str, float]:
    domain_scores = {}
    domain_avg = {}

    # first we segragate the scores domain wise
    for s in submitted_students:
        domain = s["domain"]
        score = s["score"]
        if domain not in domain_scores:
            domain_scores[domain] = []
        domain_scores[domain].append(score)

    # then for each group total score is calculated and average is calculated and appended
    for d in domain_scores:
        total = 0
        for score in domain_scores[d]:
            total += score
        avg = total / len(domain_scores[d])
        domain_avg[d] = avg

    return domain_avg

def get_missing_submissions(data: List[Dict]) -> List[str]:
    missing_submissions = []
    for student in data:
        if student["submitted"] == "no":
            missing_submissions.append(student["name"])
    return missing_submissions



