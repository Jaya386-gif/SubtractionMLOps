
import os
import pandas as pd
from evidently import Report
from evidently.presets import DataSummaryPreset

# Sample subtraction data
data = {
    "num1": [20, 30, 50, 40, 60, 80, 90, 100, 45, 70,
             25, 55, 65, 75, 85, 95, 35, 48, 62, 88],

    "num2": [10, 10, 20, 15, 30, 40, 50, 60, 15, 20,
             5, 25, 35, 30, 45, 55, 15, 18, 22, 38],

    "result": [10, 20, 30, 25, 30, 40, 40, 40, 30, 50,
               20, 30, 30, 45, 40, 40, 20, 30, 40, 50]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Create Evidently report
report = Report([
    DataSummaryPreset()
])

# Generate report
snapshot = report.run(df, None)

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Save HTML report
snapshot.save_html("reports/evidently_report.html")

print("Evidently AI report generated successfully!")
