import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Sample.txt")
samplefile = open(file_path, "a")
for i in range(1,6):
    samplefile.write("\n This is a new line added to the file line no :" + str(i))
samplefile.close()



