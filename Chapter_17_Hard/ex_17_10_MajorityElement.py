def majority_element(arr):
    current_majority = 0
    candidate = None
    for i in range(len(arr)):
        if not candidate:
            candidate = arr[i]
            print(f"New candidate : {candidate}")
        if arr[i] == candidate:
            current_majority += 1
        else:
            current_majority -= 1
        if current_majority == 0:
            print(f"Majority hits 0, reset candidate : {candidate}")
            candidate = None
    for i in range(len(arr)):
        if arr[i] == candidate:
            current_majority += 1
    return candidate if current_majority > len(arr) / 2 else None


print(majority_element([3,1,7,1,3,7,3,7,1,7,7]))