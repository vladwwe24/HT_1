#6. Write a script to check whether a specified value is contained in a group of values.
#        Test Data :
#        3 -> [1, 5, 8, 3] : True
#        -1 -> (1, 5, 8, 3) : False

a = int(input())
b = int(input())
lst = [1, 5, 8, 3]
tpl = (1, 5, 8, 3)
print(a in lst)
print(b in tpl)
