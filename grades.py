total = 0
count = 0

with open("grades.csv", "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            continue

        parts = line.strip().split(";")

        name = parts[0]
        grade = int(parts[1])

        total += grade
        count += 1

        if grade == 5:
            print(name)

if count > 0:
    print("Average score:", total / count)
else:
    print("No ratings")