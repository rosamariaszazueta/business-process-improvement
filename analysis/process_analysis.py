import pandas as pd

# Load the vendor request data
df = pd.read_csv("data/vendor_requests.csv")

# Calculate total processing time for each request
df["Total_Days"] = (
    df["Manager_Days"]
    + df["Compliance_Days"]
    + df["Finance_Days"]
    + df["Approval_Days"]
    + df["Vendor_Setup_Days"]
)

# Display the average processing time
average_time = df["Total_Days"].mean()

print("Average vendor approval time:", round(average_time, 2), "days")

# Display the average time by process stage
stage_averages = df[
    [
        "Manager_Days",
        "Compliance_Days",
        "Finance_Days",
        "Approval_Days",
        "Vendor_Setup_Days",
    ]
].mean()

print("\nAverage processing time by stage:")
print(stage_averages)

# Compare incomplete and complete requests
incomplete_comparison = df.groupby("Incomplete_Request")["Total_Days"].mean()

print("\nAverage processing time by request completeness:")
print(incomplete_comparison)
