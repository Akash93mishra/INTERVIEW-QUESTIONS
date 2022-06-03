
def insertion_sort(array):

     for i in range(1, len(array)):
         j = i
         while j > 0 and array[j-1] > array[j]:
             array[j-1], array[j] = array[j], array[j-1]
             j -= 1

array = [12, 11, 13, 5, 6]
insertion_sort(array)
print(array)




