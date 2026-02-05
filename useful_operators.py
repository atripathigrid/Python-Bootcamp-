#RANGE FUNCTION in python 
mylist = [1,2,3,4]
for num in range(10):
    print(num)

mylist = [1,2,3,4]
for num in range(4,10):
    print(num)
    
mylist = [1,2,3,4]
for num in range(0,10,2):
    print(num)

range(0,10,2)

list(range(0,10,2))

index_count = 0

for letter in 'abcdefgh':
    print('At index {} the letter {}' .format(index_count,letter))
    index_count += 1
    
