#9. Write a script to replace last value of tuples in a list.
#        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

lst_1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
lst_1 = [i for i in lst if i != ()]
print(lst)
