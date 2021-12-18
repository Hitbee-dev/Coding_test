def quick_sort(arr, start, end):
    if start >= end: # 배열의 개수가 1개 이하일 때 종료
        return

    pivot = start # pivot은 배열의 첫번째 원소로 정함
    i = start+1 # 작은값은 arr[1]부터 시작
    j = end # 큰값은 arr[-1]부터 시작

    while i <= j: # 비교할 배열이 크로스가 되거나, 딱 맞을 때 까지 반복
        while i <= end and arr[i] < arr[pivot]:
            i += 1 # 앞의 값이 마지막으로 비교할 때가 아니고, 앞의 값이 pivot 값보다 작을 때 오른쪽으로 한칸 이동
        while j > start and arr[j] > arr[pivot]:
            j -= 1 # 뒤의 값이 마지막으로 비교할 때가 아니고, 뒤의 값이 pivot 값보다 작을 때 왼쪽으로 한칸 이동
        if i > j:
            temp = arr[j]
            arr[j] = arr[pivot]
            arr[pivot] = temp
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    quick_sort(arr, start, j-1)
    quick_sort(arr, j+1, end)
    return arr

data = [48, 1, 10, 5, 8, 13, 17, 20, 7, 6, 4, 3, 2, 9, 11, 12]
print(quick_sort(data, 0, len(data)-1))
