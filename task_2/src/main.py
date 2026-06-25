from analyzer import read_submissions, get_submitted_students, calculate_average_score, get_domain_wise_average, get_missing_submissions, write_summary


students = read_submissions("task_2/data/submissions.csv")
submitted_students = get_submitted_students(students)
avg_score = calculate_average_score(submitted_students)
domain_avg = get_domain_wise_average(submitted_students)
missing_students = get_missing_submissions(students)

# summary reposrt
total_students = len(students)
total_submitted_students = len(submitted_students)
total_missing_students = len(missing_students)

summary = {
    "Total students" : total_students,
    "Total submissions" : total_missing_students,
    "Average score" : avg_score,
    "Total missing students" : total_missing_students
}

write_summary(summary, "task_2/output/submissions.json")

# print(students)
# print(f"Number of submitted students: {len(submitted_students)}")
# print(f"average score = {avg_score}")
# print(domain_avg)
