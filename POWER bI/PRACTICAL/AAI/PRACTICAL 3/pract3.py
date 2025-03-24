# Example to Demonstrate the Union, Intersection, Complement, and Difference Between Two Fuzzy Sets 
 
# Initialize fuzzy sets 
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6} 
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5} 
 
# Print the given fuzzy sets 
print('The First Fuzzy Set is :', A) 
print('The Second Fuzzy Set is :', B) 
 
# 1. Union of Two Fuzzy Sets (Maximum of values) 
Y_union = {} 
for A_key, B_key in zip(A, B): 
    A_value = A[A_key] 
    B_value = B[B_key] 
     
    # Union takes the maximum of values 
    if A_value > B_value: 
        Y_union[A_key] = A_value 
    else: 
        Y_union[B_key] = B_value 
 
print('Fuzzy Set Union is :', Y_union) 
 
 
# 2. Intersection of Two Fuzzy Sets (Minimum of values) 
Y_intersection = {} 
for A_key, B_key in zip(A, B): 
    A_value = A[A_key] 
    B_value = B[B_key] 
     
    # Intersection takes the minimum of values 
    if A_value < B_value: 
        Y_intersection[A_key] = A_value 
    else: 
        Y_intersection[B_key] = B_value 
 
print('Fuzzy Set Intersection is :', Y_intersection) 
 
 
# 3. Complement of Fuzzy Set A (1 - value of each element) 
Y_complement = {} 
for A_key in A: 
    Y_complement[A_key] = 1 - A[A_key] 
 
print('Fuzzy Set Complement of A is :', Y_complement) 
 
 
# 4. Difference Between Two Fuzzy Sets (A - B) 
Y_difference = {} 
for A_key, B_key in zip(A, B): 
    A_value = A[A_key] 
    B_value = B[B_key] 
    B_value = 1 - B_value  # Complement of B for difference operation 
     
    # Difference takes the minimum between A_value and complement of B_value 
    if A_value < B_value: 
        Y_difference[A_key] = A_value 
    else: 
        Y_difference[B_key] = B_value 
 
print('Fuzzy Set Difference (A - B) is :', Y_difference)
