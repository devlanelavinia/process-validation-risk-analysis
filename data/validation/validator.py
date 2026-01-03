import csv

def validate_row(row):
    issues = []

    if not row['employee_id']:
        issues.append('Missing employee_id')

    if not row['access_level']:
        issues.append('Missing access_level')

    if row['access_level'] == 'admin' and not row['last_review_date']:
        issues.append('Admin without review date')

    return issues


with open('data/sample_input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        problems = validate_row(row)
        if problems:
            print(f"Row {row['employee_id']}: {problems}")
