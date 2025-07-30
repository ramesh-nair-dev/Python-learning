import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Sample1.txt")
samplefile = open(file_path, "w")
for i in range(1,6):
    samplefile.write("This is line number " + str(i) + "\n")
samplefile.close()

# This code opens a file named "Sample1.txt" in write mode (`"w"`), which means it will create the file if it doesn't exist or overwrite it if it does.
# It then writes five lines to the file, each containing a string that indicates the line number.
# After writing, it closes the file to ensure that all data is saved properly and resources are released.

samplefile = open(file_path, "w")
samplefile.write("This is overwriting the file with this line.\n")
samplefile.close()

# This code opens the same file "Sample1.txt" again in write mode, which will overwrite the existing content.
# It writes a single line to the file, effectively replacing any previous content.
# After writing, it closes the file to ensure that the new content is saved and resources are released.
