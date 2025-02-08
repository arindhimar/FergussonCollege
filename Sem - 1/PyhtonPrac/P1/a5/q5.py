import os

file_path = "input.txt"
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("Arin")  

with open(file_path, "r") as f1:
    content = f1.read()

reversed_content = content[::-1]

with open("reversed.txt", "w") as f2:
    f2.write(reversed_content)

print(f"The content of '{file_path}' has been reversed and saved to 'reversed.txt'.")