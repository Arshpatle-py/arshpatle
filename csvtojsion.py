import csv
import json

# Convert attendance CSV to JSON
def attendance_to_json(input_file, output_file):

    with open(input_file, "r", newline="") as file:
        reader = csv.reader(file)

        # First row contains column names
        headers = next(reader)

        attendance = []

        # Convert each row into a dictionary
        for row in reader:
            record = dict(zip(headers, row))
            attendance.append(record)

    # Write attendance data into JSON
    with open(output_file, "w") as file:
        json.dump(attendance, file, indent=4)

    return attendance


# Main program
if __name__ == "__main__":

    # Create sample attendance CSV
    with open("attendance.csv", "w", newline="") as file:
        file.write(
            "Roll No,Name,Date,Status\n"
            "1,Aditi,21-09-2026,Present\n"
            "2,Rahul,21-09-2026,Absent\n"
            "3,Sneha,21-09-2026,Present\n"
            "4,Arjun,21-09-2026,Present\n"
        )

    # Convert CSV to JSON
    data = attendance_to_json("attendance.csv", "attendance.json")

    print("Attendance CSV converted to JSON successfully!")
    print("\nAttendance Data:")

    # Display JSON data
    print(json.dumps(data, indent=4))
