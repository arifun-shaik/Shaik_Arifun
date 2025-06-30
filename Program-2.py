def generate_series_count(a):
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    print("Output:", result)

# Example usage
generate_series_count(4)  # Output: [1, 3, 5, 7]
