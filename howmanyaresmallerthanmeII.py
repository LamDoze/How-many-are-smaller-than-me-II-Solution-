def smaller(arr):
    if not arr:
        return []
    
    rank = {val: idx + 1 for idx, val in enumerate(sorted(set(arr)))}
    compressed_arr = [rank[val] for val in arr]
    
    # Binary Indexed Tree (Fenwick Tree)
    def update(bit, index, value):
        while index < len(bit):
            bit[index] += value
            index += index & -index
    
    def query(bit, index):
        sum = 0
        while index > 0:
            sum += bit[index]
            index -= index & -index
        return sum
    
    # Initialize BIT
    n = len(arr)
    bit = [0] * (n + 1)
    result = []
    
    for i in reversed(range(n)):
        count_smaller = query(bit, compressed_arr[i] - 1)
        result.append(count_smaller)
        update(bit, compressed_arr[i], 1)

    return result[::-1]

# Test cases
print(smaller([5, 4, 3, 2, 1]))  # [4, 3, 2, 1, 0]
print(smaller([1, 2, 0]))        # [1, 1, 0]