from manual_parser import read_csv_manual, convert_types, calculate_summary, write_json
from pandas_parser import read_csv_pandas, calculate_summary_pandas
import sys

output_path = "task_3/output/manual_summary.json"
pandas_output_path = "task_3/output/pandas_summary.json"

file_path = sys.argv[1]

data = read_csv_manual(file_path)
processed_data = convert_types(data)
summary = calculate_summary(processed_data)

df = read_csv_pandas(file_path)
pandas_summary = calculate_summary_pandas(df)

write_json(pandas_summary, pandas_output_path)
write_json(summary, output_path)
