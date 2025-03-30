my_list = []

my_list.append(10)  # Append one element at a time
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f'The initial appended elements: {my_list}')

my_list.insert(2,15) 
print(f'my_list after inserting 15 to index 2: {my_list}')

another_list=[50,60,70]
my_list.extend(another_list)
print(f'The extended element {my_list}')
    
my_list.pop()
print(f'my_list after the removal of the last element {my_list}')

my_list.sort()
print(f'Sorted list in ascending order {my_list}')

print(f'The index of 30 is: {my_list.index(30)}')

    

