def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Add remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = []

    print("Enter the elements of the array:")
    for _ in range(n):
        arr.append(int(input()))

    sorted_arr = merge_sort(arr)

    print("Sorted array:", sorted_arr)
