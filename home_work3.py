value=750
new_value = value / 2 if value < 100 else value *-1
print(new_value)

#####################################################2)
value=70
new_value = 1 if value < 100 else 0
print(new_value)

#####################################################3)
value=800
new_value = True if value < 100 else False
print(new_value)

#####################################################4)
my_str='qwI7KJHJYFsdjhs'
my_str_new=my_str.upper()
print(my_str_new)

#####################################################5)
my_str_new=my_str.lower()
print(my_str_new)

#####################################################6)
my_str_new=my_str*2 if len(my_str) <5 else my_str

print(my_str_new)

#####################################################7)
my_str_new=my_str+my_str[::-1] if len(my_str) <5 else my_str

print(my_str_new)



