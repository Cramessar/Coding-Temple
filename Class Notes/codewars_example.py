def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    else: 
        arr.remove(max(arr))
        arr.remove(min(arr))
        r = sum(arr)
        return r