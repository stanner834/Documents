def unique_in_order(sequence):
    if not sequence:
        return []  # Return an empty list for an empty input sequence

    result = [sequence[0]]  # Start with the first element

    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            result.append(sequence[i])  # Add non-repeating elements to the result list

    return result

# Test the function
result = unique_in_order('AAAABBBCCDAABBB')
print(result)  # Output should be ['A', 'B', 'C', 'D', 'A', 'B']
