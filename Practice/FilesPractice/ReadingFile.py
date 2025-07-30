import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Sample.txt")
samplefile = open(file_path, "r")
for line in samplefile.readlines():
    print(line)
# print(samplefile.readlines())
samplefile.close()

# This code opens a file named "Sample.txt" located in the same directory as the script.
# It reads the file line by line and prints each line to the console.
# After reading the file, it closes the file to free up system resources.
# The `os` module is used to construct the file path, ensuring that the code works regardless of the operating system.
# The `readlines()` method reads all lines from the file and returns them as a list, which is then iterated over in the for loop.
# This is a basic example of file handling in Python, demonstrating how to read from a text file and process its contents.
# Note: Ensure that "Sample.txt" exists in the same directory as this script for it to run successfully.
# If you want to read the entire file at once, you can use:
# content = samplefile.read()
# print(content)
# This will read the entire file into a single string instead of line by line.