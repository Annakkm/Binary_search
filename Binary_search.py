

def binary_search(list_n, item):
    low = 0
    high = len(list_n) - 1

    while low <= high:
        mid = (low + high) // 2
        guess_m = list_n[mid]
        if guess_m == item:
            return mid
        if guess_m < item:
            low = mid + 1
        if guess_m > item:
             high = mid - 1
    return None

item = 5
numbers_guess = [1, 2, 3, 5, 6, 7, 10,]

print(binary_search(numbers_guess, item))
