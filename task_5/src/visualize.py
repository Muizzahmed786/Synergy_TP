import pandas as pd
import matplotlib.pyplot as plt

def load_cleaned_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def plot_domain_average_score(df: pd.DataFrame, output_path: str) -> None:
    domain_avg = df.groupby('domain')['score'].mean()
    plt.figure(figsize=(8, 5))
    plt.bar(domain_avg.index, domain_avg.values, color='skyblue', edgecolor='black', width=0.5)
    plt.title('Average Score by Domain', fontsize=14, fontweight='bold')
    plt.xlabel('Domain', fontsize=12)
    plt.ylabel('Average Score', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{output_path}/domain_average_score.png")
    plt.close()

def plot_attendance_vs_score(df: pd.DataFrame, output_path: str) -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(df['attendance_percent'], df['score'], color='darkorange', edgecolor='black', s=100, alpha=0.8)
    plt.title('Attendance Percentage vs. Score', fontsize=14, fontweight='bold')
    plt.xlabel('Attendance Percent (%)', fontsize=12)
    plt.ylabel('Score', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f"{output_path}/attendance_vs_score.png")
    plt.close()

def plot_submission_status_count(df: pd.DataFrame, output_path: str) -> None:
    status_counts = df['submitted'].value_counts()
    labels = [str(idx).capitalize() for idx in status_counts.index]
    plt.figure(figsize=(6, 5))
    
    plt.bar(labels, status_counts.values, color=['mediumseagreen', 'tomato'], edgecolor='black', width=0.4)
    plt.title('Submission Status Count', fontsize=14, fontweight='bold')
    plt.xlabel('Submitted Status', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.yticks(range(0, int(status_counts.max()) + 2))
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig(f"{output_path}/submission_status_count.png")
    plt.close()