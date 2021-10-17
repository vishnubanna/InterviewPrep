import numpy as np 

def downheap(array, i, j):

  def left_child(index):
    return 2 * index + 1

  def right_child(index):
    return 2 * index + 2
  
  index = 0
  while (index + i < j):
    rc_ind = right_child(index)
    lc_ind = left_child(index)
    next_ind = -1

    if rc_ind >= j:
      next_ind = lc_ind
    
    if lc_ind >= j:
      next_ind = rc_ind

    if next_ind >= j:
      break
    elif next_ind < 0:
      if array[rc_ind + i] > array[lc_ind + i]:
        next_ind = rc_ind
      else:
        next_ind = lc_ind

    if array[index + i] < array[next_ind + i]:
      array[index + i], array[next_ind + i] = array[next_ind + i], array[index + i]
    index = next_ind
  return 

def reheap(array, i, j):
  j -= 1
  def parent_index(index, i):
    return ((index - 1)//2 - i)

  index = j - i
  while (index >= 0):
    parent = parent_index(index, i)
    
    if parent < 0:
      break
    
    if array[index + i] >= array[parent + i]:
      array[index + i], array[parent + i] = array[parent + i], array[index + i]
    index = parent
  return 

def heapify(array):
  for t in range(1, len(array)):
    reheap(array, 0, t + 1)
  return array

def heapsort(array):
  array = heapify(array) # max heap

  max_ind = len(array) - 1
  while max_ind > 0:
    array[0], array[max_ind] = array[max_ind], array[0]
    max_ind -= 1
    downheap(array, 0, max_ind + 1)
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
  print(heapsort(array))
  print(all(heapsort(array) == sorted(array)))