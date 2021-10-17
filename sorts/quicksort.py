import numpy as np 


def quicksort(array, i, j):
  """
  you split the array into 2 halfs repeatedly until you hit the base case, an 
  array of one number. pick a number move it to the last index. swap all numbers
  such that number to the right are larger than selected, on left are smaller than 
  selected.  

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

  a copy of the array is not made, so only one copy of the array is needed 
  so you need log(n) function calls to complete a quick sort. so only log(n)
  additonal memory i needed. 
  """
  if j == i:
    # exit condition
    return 

  mid = j - 1
  p1 = i 
  p2 = mid - 1
  while (p1 <= p2):# and p2 >= i and p1 <= mid - 1):
    if array[p1] >= array[mid]:
      array[p1], array[p2] = array[p2], array[p1]
      p2 -= 1
    else:
      p1 += 1
  
  array[p1], array[mid] = array[mid], array[p1]
  mid = p1
  quicksort(array, i, mid)
  quicksort(array, mid + 1, j)
  return array


if __name__ == "__main__":
  # print(selection_sort(np.random.randint(0, 10, size = [10])))
  # selection_sort([9, 7, 4, 3, 0, 3, 3, 4, 1, 2])
  # selection_sort(np.random.randint(0, 10, size = [10]))

  # [6, 9, 2, 0, 9, 2, 6, 0, 9, 4]
  # [6 9 2 0 9 2 6 0 9 |4|]
  # [9 9 2 0 9 2 6 0 |6 4|]
  # [0 9 2 0 9 2 6 |9 6 4|]
  num = 100
  array = np.random.randint(0, num, size = [num])
  print(array)
  print(all(quicksort(array, 0, num) == sorted(array)))