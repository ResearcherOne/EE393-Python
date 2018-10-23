# Umut Cakan S006742 Computer Science - Quiz 1

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = []
list4 = []

# Iteration for answer a.
for i in range(len(list1)):
    for j in range(len(list2)):
        # Add one solution for answer of the a.
        list3.append(str(list1[i]) + list2[j])
        # Add one part of the solution for answer of b. 1a, 1b, 1c...
        list4.append(str(list1[i]) + list2[j])
        # Add second part of the solution for answer of b. a1, b1, c1...
        list4.append(list2[j] + str(list1[i]))
        
        
print("The answer of a is:", list3)        
print("The answer of b is:", list4)
