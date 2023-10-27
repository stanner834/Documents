def find_outlier(integers):
    even_count = 0
    odd_count = 0
    even_outlier = None
    odd_outlier = None

    for num in integers:
        if num % 2 == 0:  # Even number
            even_count += 1
            even_outlier = num
        else:  # Odd number
            odd_count += 1
            odd_outlier = num

    if even_count == 1:  # There's only one even number, so it's the outlier
        return even_outlier
    elif odd_count == 1:  # There's only one odd number, so it's the outlier
        return odd_outlier
    else:
        return None  # No outlier found

# Test the function
integers = [2, 4, 6, 8, 10, 7]
outlier = find_outlier(integers)
if outlier is not None:
    print(f"The outlier is {outlier}")
else:
    print("No outlier found")

