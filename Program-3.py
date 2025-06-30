def generate_series_up_to_x(a):
    count = a if a % 2 == 1 else a - 1
    result = []
    num = 1
    for _ in range(count):
        result.append(num)
        num += 2
    print("Output:", result)

# Example usage
generate_series_up_to_x(6)  # Output: [1, 3, 5, 7, 9]
