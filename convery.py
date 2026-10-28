with open("input.txt", "r") as file:
    data = file.read()

print("Original Text:", data)

with open("output.txt", "w") as file:
    file.write(data.upper())
    
print("Text converted to uppercase successfully.")
