# Print characteries 

#for u in input().split():print(end=int(u[:-1])*u[-1])

#print(''.join([int(i[:-1])*i[-1] for i in input().split()]))

# Study case
p = [int(i[:-1])*i[-1] for i in input().split()]

print(type(p)) # list 
print(p) # = > input: 1# 2% ; output = ['#', '%%']

j = "".join(p) # Convert to String
print(type(j)) # str
print(j)
