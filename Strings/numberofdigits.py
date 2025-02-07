string="Hello World 2025"
count=0

for i in range(len(string)): 
    if string[i].isdigit():
        count += 1
print(count)