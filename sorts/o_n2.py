import numpy as np 


def insertion_sort(array):
  """
  Given an array, think of the array as 2 different arrays, the sorted portion
  and the unsorted portion. Iterate the unsorted array and place it in the 
  correct location in the sorted array.   

  The algorithem is considered to be O(n^2):
  loop 1: iterates all the elements in the array one time makeing it O(n)
  loop 2: iterates within the loop above and only iterates the sorted array O(i)
  
  number of iterations = 0 + 1 + 2 + 3 ... (n-2) + (n-1) + n
  cost of each write: O(4) = (if condition) + (3 writes per swap)

  run time is the sum of all numbers from 0 to n times the cost per write

  1 + 2 + 3 + 4 = 10 
  4 + 3 + 2 + 1 = 10 

  (5 + 5 + 5 + 5)/2 = 10 
  (4 (5))/2 = 10 

  n(n + 1)/2 = (n ^ 2 + n)/2

  highest cost term is n ^ 2, in large arrays n^2 dominates so the runtime is 
  O(n^2)


  the actual runtime with constants assuming a search cost of 1 and a write cost 
  of 1 is  (1 + 3) * (n ^ 2 + n)/2 = 2n^2 + 2n 

  making this better than bubble but worse than selection sort.  

  """
  print(array)
  for i in range(len(array)): # O(n)
    # i is the number you need to place:
    for j in range(0, i): # O(i)
      # j indexes the sorted array
      if array[i] < array[j]: # O(1)
        array[i], array[j] = array[j], array[i] # O(1)
      
      # [6 | 3, 9, 7]
      # [3, 6 | 9, 7]
      # [3, 6, 9 | 7]
  print(array)
  return array 

def selection_sort(array):
  """
  Given an array, think of the array as 2 different arrays, the sorted portion
  and the unsorted portion. Iterate the unsorted array to find the minimum and 
  swap it with the largest value in the sorted array, placing the minimum in 
  in the correct place in the sorted array at all times.   

  The algorithem is considered to be O(n^2):
  loop 1: iterates all the elements in the array one time makeing it O(n)
  loop 2: iterates within the loop above and only iterates the sorted array O(n - i)
  
  number of iterations = n + (n - 1) + (n - 2) + ... + 1 + 0
  cost of each write: O(2) = (if condition) + (1 writes per swap)

  n(n + 1)/2 = (n ^ 2 + n)/2

  highest cost term is n ^ 2, in large arrays n^2 dominates so the runtime is 
  O(n^2)


  the actual runtime with constants assuming a search cost of 1 and a write cost 
  of 1 is  3 + (1 + 1) * (n ^ 2 + n)/2 = n^2 + n + 3

  making this the best n^2 sort.  
  """
  print(array)
  for i in range(len(array)):
    # i is the number you need to place:
    minim = i
    for j in range(i + 1, len(array)):
      # j indexes the sorted array
      if array[minim] > array[j]:
        minim = j

    array[i], array[minim] = array[minim], array[i]      
      # [6 | 3, 9, 7]
      # [3, 6 | 9, 7]
      # [3, 6, 9 | 7]
  print(array)
  return array 

def bubble_sort(array):
  """
  iterate the array n times swapping numbers next to each other until the 
  largest numbers get bubbled to the top. 


  loop one O(n)
  loop two O(n - 1)

  run time: n * (n - 1) = n^2 - n
  cost of write: 1(compare) + 3(writes) = 4

  runtime = 4 * n ^ 2 - 4n

  making this the worst sort.
  """
  print(array)
  for i in range(len(array)):
    for j in range(len(array) - 1):
      # j indexes the sorted array
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
  print(array)
  return array 

if __name__ == "__main__":
  # print(selection_sort(np.random.randint(0, 10, size = [10])))
  # selection_sort([9, 7, 4, 3, 0, 3, 3, 4, 1, 2])
  # selection_sort(np.random.randint(0, 10, size = [10]))
  bubble_sort(np.random.randint(0, 10, size = [10]))