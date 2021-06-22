my_list= [500, 1, 2, 3, 50, 120, 150, 1100]
for n in my_list:
    if n>100:
        print(n)
    else: None

###################################################2)
my_result=[]
for n in my_list:
    if n>100:
        my_result.append(n)
        print(list(my_result))

