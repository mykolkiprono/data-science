from random import randint 
N = 10
array = [range(N)]
for i in range (N):
    array.append(randint(1,99))
    
    
for j in range(N):
    print(array[j])

print(list(array))