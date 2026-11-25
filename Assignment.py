# Program: Count lines, extract first two lines
# and write them into a new file

# 1. Count the total number of lines
def count_lines(input_path):
    with open(input_path, "r") as f:
        return sum(1 for line in f)


# 2. Extract the first two lines
def extract_first_two_lines(input_path):
    with open(input_path, "r") as f:
        lines = []
        for i in range(2):
            line = f.readline()
            if not line:
                break
            lines.append(line)
    return lines


# 3. Write extracted lines into a new file
def write_to_file(output_path, lines):
    with open(output_path, "w") as f:
        f.writelines(lines)


# Main Program
input_file = "input.txt"
output_file = "output.txt"

total = count_lines(input_file)
print("Total number of lines:", total)

first_two = extract_first_two_lines(input_file)
print("First two lines:", first_two)

write_to_file(output_file, first_two)

print("Data successfully written to output.txt")
