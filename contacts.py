import pandas as pd

# List of phone numbers
phone_numbers = [
    "+237678603120", "0786201863", "0702760646", "0746131450", "0700122006", 
    "0782700798", "0768566433", "0718673418", "0710323464", "0776722209", 
    "0786630476", "0796919100", "0104454967", "0742449114", "0702506631", 
    "07066414402", "07066414402", "+237670830282", "0714562549", "0793622489", 
    "0784421233", "0708941869", "0727486255", "0110540550", "0741793102", "0745815616"
]

# Generate names as PY001, PY002, ...
names = [f"PY{str(i+1).zfill(3)}" for i in range(len(phone_numbers))]

# Create a DataFrame
df = pd.DataFrame({"Name": names, "Phone Number": phone_numbers})

# Save to CSV
csv_filename = "/mnt/data/contact_list.csv"
df.to_csv(csv_filename, index=False)

# Return the file path
csv_filename
