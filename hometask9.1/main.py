with open("month.txt", "r") as file:
    content = file.readlines()
    content.reverse()
with open("month_reversed.txt", "a") as f:
    content[0] += "\n"
    content[-1] = content[-1].replace("\n", "")
    for i in content:
        f.write(str(i))
