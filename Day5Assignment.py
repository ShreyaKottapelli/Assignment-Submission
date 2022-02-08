# DAY 5 ASSIGNMENT OF PYTHON
# USE FILTER FUNCTION TO FILTER OUT THE ELEMENTS FROM A LIST THAT ARE DIVISIBLE BY 3 AND 5
my_list = list(range(1, 100))
res1 = list(filter(lambda x: (x % 3 == 0) and (x % 5 == 0), my_list))
print(res1, "These numbers are divisible by 3 & 5 \n")
res2 = list(filter(lambda x: (x % 3 == 0), my_list))
print(res2, "These numbers are divisible by 3 \n")
res3 = list(filter(lambda x: (x % 5 == 0), my_list))
print(res3, "These numbers are divisible by 5 \n")
