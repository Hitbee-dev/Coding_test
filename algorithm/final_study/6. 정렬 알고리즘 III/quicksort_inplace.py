def quick_sort(arr, start, end):
    if start >= end: # 재귀 탈출 조건
        return

    pivot = start # pivot은 배열의 첫번째 원소로 정함
    left = start+1 # 작은값은 arr[1]부터 시작
    right = end # 큰값은 arr[-1]부터 시작

    while left <= right:  # 작은값과 큰값을 비교하며 작은값을 찾음
        while left <= end and arr[left] < arr[pivot]:
            left += 1  # 앞의 값이 마지막으로 비교할 때가 아니고, 앞의 값이 pivot 값보다 작을 때 오른쪽으로 한칸 이동
        while right > start and arr[right] > arr[pivot]:
            right -= 1  # 뒤의 값이 마지막으로 비교할 때가 아니고, 뒤의 값이 pivot 값보다 작을 때 왼쪽으로 한칸 이동
        if left > right:  # 비교할 배열이 크로스가 되면
            temp = arr[right]  # 배열의 마지막 원소를 temp에 저장
            arr[right] = arr[pivot]  # 배열의 마지막 원소를 pivot으로 저장
            arr[pivot] = temp # pivot으로 저장된 원소를 temp로 저장
        else:
            temp = arr[left]  # 배열의 앞 원소를 temp에 저장
            arr[left] = arr[right]  # 배열의 앞 원소를 배열의 마지막 원소로 저장
            arr[right] = temp  # 배열의 마지막 원소를 temp로 저장

    quick_sort(arr, start, right-1)  # 작은값을 정렬
    quick_sort(arr, right+1, end)  # 큰값을 정렬
    return arr # 정렬된 배열을 반환

data = [48, 1, 10, 5, 8, 13, 17, 20, 7, 6, 4, 3, 2, 9, 11, 12]
print(quick_sort(data, 0, len(data)-1)) 
