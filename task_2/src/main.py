from analyzer import read_submissions, get_submitted_students, calculate_average_score, get_domain_wise_average, get_missing_submissions


students = read_submissions("task_2/data/submissios.csv")
submitted_students = get_submitted_students(students)
avg_score = calculate_average_score(submitted_students)
domain_avg = get_domain_wise_average(submitted_students)
missing_students = get_missing_submissions(students)

print(students)
print(f"Number of submitted students: {len(submitted_students)}")
print(f"average score = {avg_score}")
print(domain_avg)
