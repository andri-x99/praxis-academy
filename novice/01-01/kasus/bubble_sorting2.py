def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True

    '''Jadi itu si swapped dibikin true pas diawal biar bisa masuk loop
    Nah terus pas masuk loop while swapped, si swapped dibikin false karena kalau sewaktu-waktu sudah urut jadi bisa keluar dan loop while swapped dan fungsi bubble sort bisa berakhir
    Nah ngecek sudah urut atau belum itu ada di dalam for
    Loop si for ini dia ngulang sampe range(len(nums)-1) habis
    Btw range itu pas disini aku cukup lihat contohnya aja. Ngeliat definisi kadang jlimet. Misal range(4) nanti dia jadi 0,1,2,3. 4 angka dimulai dari 0.
    Nah kenapa angka dalam range itu yang di pake len(nums)-1 alias panjang arraynya si nums dikurang 1
    Nah nanti di for itu di cek sepasang2.
    Ngeceknya pake if yang di dalam for
    Nah kalo masuk si if nanti di tuker dan nilai si swapped dibalikin ke true
    Biar bisa di cek lagi berpasangan dari awal
    Gitu terus sampe urut

    https://www.youtube.com/watch?v=nmhjrI-aW5o&feature=youtu.be'''

# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

# random list berisi angka ga jelas
# ngambil fungsi bubble sort terus dimasukin ke random list
# nampilin kondisi random list sekarang 