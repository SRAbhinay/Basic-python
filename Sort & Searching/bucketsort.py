def bucket_sort(arr):
   
    max_val ,min_val = max(arr), min(arr)
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    sorted_arr = []
    
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)
    return sorted_arr
