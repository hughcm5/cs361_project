def merge_sort(Arr,start,end):
    if(start<end):
        mid = (start+end)//2 #Computes floor of middle value
        merge_sort(Arr,start,mid)
        merge_sort(Arr,mid+1,end)
        merge(Arr,start, mid, end)

def merge(Arr, start, mid, end):
  #temporary arrays to copy the elements of subarray
  leftArray_size = (mid-start)+1
  rightArray_size = (end-mid)

  leftArray = [0]*leftArray_size
  rightArray = [0]*rightArray_size

  for i in range(0, leftArray_size):
    leftArray[i] = Arr[start+i]

  for i in range(0, rightArray_size):
    rightArray[i] = Arr[mid+1+i]

  i=0
  j=0
  k=start

  while (i < leftArray_size and j < rightArray_size):
    if (leftArray[i] < rightArray[j]):
      # filling the original array with the smaller element
      Arr[k] = leftArray[i]
      i = i+1
    else:
      # filling the original array with the smaller element
      Arr[k] = rightArray[j]
      j = j+1
    k = k+1

  # copying remaining elements if any
  while (i<leftArray_size):
    Arr[k] = leftArray[i]
    k = k+1
    i = i+1

  while (j<rightArray_size):
    Arr[k] = rightArray[j]
    k = k+1
    j = j+1


def kthElement(arr1, arr2, k):
    nu_arr = arr1 + arr2

    length = len(nu_arr)

    merge_sort(nu_arr, 0, length - 1)

    if 0 < k <= len(nu_arr):
        return nu_arr[k - 1]
    

Arr1 = [1,2,3,5,6]
Arr2= [3,4,5,6,7]

k= 5


print(kthElement(Arr1, Arr2, k))
