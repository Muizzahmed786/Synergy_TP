import json

def read_csv_manual(file_path: str) -> list[dict]:
    data = []
    with open(file_path, 'r') as file:
        header_line = file.readline()
        if not header_line:
            return data
        headers = header_line.strip().split(',')

        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            values = cleaned_line.split(',')

            rows = {}
            for i in range(len(headers)):
                key = headers[i]
                value = values[i]
                rows[key] = value

            data.append(rows)

    return data

def convert_types(rows: list[dict]) -> list[dict]:
    for row in rows:
        if 'score' in row:
            try:
                row['score'] = int(row['score'])
            except ValueError:
                row['score'] = 0

        if 'submitted' in row:
            status = str(row['submitted']).strip().lower()
            if status == 'yes' or status == 'true':
                row['submitted'] = 'yes'
            else:
                row['submitted'] = 'no'
                
    return rows

def calculate_summary(rows: list[dict]) -> dict:
    total_students = len(rows)
    submitted_students = 0
    missing_students = 0
    total_score = 0

    highest_score = 0
    highest_scorer_name = ''
    lowest_score = 100
    lowest_scorer_name = ''

    not_submitted = []
    below_5 = []

    domain_scores = {}
    domain_counts = {}

    for row in rows:
        if 'submitted' in row and row['submitted'] == 'yes':
            submitted_students += 1
            total_score += row['score']
            if row['score'] > highest_score:
                highest_score = row['score']
                highest_scorer_name = row['name']
            if row['score'] < lowest_score:
                lowest_score = row['score']
                lowest_scorer_name = row['name']
            if 'domain' in row:
                domain = row['domain']
                if domain not in domain_scores:
                    domain_scores[domain] = 0
                    domain_counts[domain] = 0
                domain_scores[domain] += row['score']
                domain_counts[domain] += 1
        else:
            missing_students += 1
            not_submitted.append(row['name'])
        
        if row['score'] < 5:
            below_5.append(row['name'])
    
    if submitted_students > 0:
        average_score = total_score / submitted_students
    else: 
        average_score = 0
    
    domain_avg = {}
    for domain in domain_scores:
        if domain_counts[domain] > 0:
            domain_avg[domain] = domain_scores[domain] / domain_counts[domain]
        else:
            domain_avg[domain] = 0
    
    summary = {
        "Total students" : total_students,
        "Submitted students" : submitted_students,
        "Missing students" : missing_students,
        "Average score" : average_score,
        "Highest score" : highest_score,
        "Highest scorer" : highest_scorer_name,
        "Lowest score" : lowest_score,
        "Lowest scorer name" : lowest_scorer_name,
        "Not submitted" : not_submitted,
        "Scores below 5" : below_5
    }

    return summary

def write_json(data: dict, output_path: str) -> None:
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)
