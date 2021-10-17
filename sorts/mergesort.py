import numpy as np 


def mergesort_recursive(array, i, j, level):
  """
  you split the array into 2 halfs repeatedly until you hit the base case, an 
  array or one number. An array of one number is a sorted array. Therefore 
  every time a child returns to parent it must return a sorted array. So you can 
  compare in sorted order to get a sorted array. 

  this is a recursion, so getting run time is dependedent on a recursion tree. 

                 n 
             n/2    n/2 
          n/4 n/4 n/4 n/4 

                ...
      1 1 1 1 1 1 1 1 1 1 1 1...
  

  in total each level in the recursion will iterate through the array n times
  how many levels are in the tree? 

  each array gets split in half one time at each level. 


                     n 
             n/2^1       n/2^1 
          n/2^2 n/2^2 n/2^2 n/2^2 

                ...
      (n/n = n/2^l) 1 1 1 1 1 1 1 1 1 1 1...
  
  n = 2 ^ l 
  l = log2(n)
  
  log2(n) levels = lagorithem run time is n * log2(n)

  space compleity 

  at the maxium depth of the recursion tree there is log2(n) levels 

  n + n/2 + n/4 + n/8 
  
  n * (2 ^ (-i) from i = 0 to i = log2(n))

  n * (geometric series, r = 1/2 = sum(a * r ^ i) = a(1 - r^n)/(1 - r)) 

  (1 - (1/2) ^ log2(n))/(1 - 1/2)

  2 * (1 - 1/n) = 2 - 2/n

  n * (2 - 2/n) = 2n - 2

  so in total space is O(n)
  """
  mid = (i + j)//2

  if mid == i:
    # exit condition
    return 
  
  mergesort_recursive(array, i, mid, level + 1)
  mergesort_recursive(array, mid, j, level + 1)

  arr1, pointer1 = array[i:mid].copy(), 0
  arr2, pointer2 = array[mid:j].copy(), 0

  for t in range(i, j):
    if pointer1 >= len(arr1) or pointer2 >= len(arr2):
      break
    if arr1[pointer1] < arr2[pointer2]:
      array[t] = arr1[pointer1]
      pointer1 += 1
    else:
      array[t] = arr2[pointer2]
      pointer2 += 1
  
  for i in range(pointer1, len(arr1)):
    array[t] = arr1[i]
    t += 1
  for i in range(pointer2, len(arr2)):
    array[t] = arr2[i]
    t += 1
  return array


if __name__ == "__main__":
  # print(selection_sort(np.random.randint(0, 10, size = [10])))
  # selection_sort([9, 7, 4, 3, 0, 3, 3, 4, 1, 2])
  # selection_sort(np.random.randint(0, 10, size = [10]))
  print(mergesort_recursive(np.random.randint(0, 31, size = [31]), 0, 31, 0))