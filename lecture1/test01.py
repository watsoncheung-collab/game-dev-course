# Prompt for user information
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
student_class = input("Enter your class: ")
phone_number = input("Enter your phone number: ")

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Information</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }}
        h1 {{
            color: #333;
        }}
        p {{
            font-size: 16px;
            color: #555;
        }}
    </style>
</head>
<body>
    <h1>Student Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Student ID:</strong> {student_id}</p>
    <p><strong>Class:</strong> {student_class}</p>
    <p><strong>Phone Number:</strong> {phone_number}</p>
</body>
</html>
"""

# Write to an HTML file
with open("student_info.html", "w") as file:
    file.write(html_content)

print("HTML file 'student_info.html' has been created.")
