immutable_var= 1,2,'d','c'
print(immutable_var)
#immutable_var[0]=4
print(type(immutable_var))
mutable_list=([1,2,3,4],5)
print(mutable_list)
mutable_list[0][3]=9
print(mutable_list)