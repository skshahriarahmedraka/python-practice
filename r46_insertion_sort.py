
# Python program for implementation of Selection 
# Sort 
'''
import sys 
A = [64, 25, 12, 22, 11] 
A=li
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  
'''

li=[9,3,6,1,7,3,2,7,8,4]
for i in range(len(li)):
    m=i
    for j in range(i+1,len(li)):
        if(li[m]<li[j]):
            m=j
    li[i],li[m]=li[m],li[i]

print("sorted list: ")
for i in li:
    print(f"{i}")