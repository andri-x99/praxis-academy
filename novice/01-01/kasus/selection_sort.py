def selection_sort(nums):
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    ''' i sebagai salah satu angka di dalam range
    diibaratkan i adalah angka terendah
    j sebagai salah satu angka di dalam range yang bernilai sesudah angka i

    jika j kurang dari dari angka paling rendah yaitu i
    maka yang dijadikan patokan angka terendah adalah menjadi j
    algoritma pertukaran i,j menjadi j,i'''


# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

#kek di bubble sorting ya, definisikan range, ambil fungsi, dan keluarkan dengan print