def solve(n, arr) :
    # write your code here
    frequency = {}
    for num in arr:
      frequency[num] = frequency.get(num, 0) + 1
    
    frequency_values = list(frequency.values())
    frequency_keys = list(frequency.keys())
    
    max_frequency = max(frequency_values)
    max_frequency_index = frequency_values.index(max_frequency)
    
    print(frequency_keys[max_frequency_index])