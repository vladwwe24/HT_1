#11. Write a script to remove duplicates from Dictionary.

dic1 = {1:10, 2:20, 3:30, 4:40, 5:30, 6:40, 7:50, 8:60, 9:50, 10:60}
a = {}
for key, value in dic1.items():
    if value not in a.values():
        a[key] = value
print(a)
