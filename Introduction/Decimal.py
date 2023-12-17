def to_decimal(binary_str):
    binary_str = binary_str.lstrip("0")
    decimal_value = 0
    for digit in binary_str:
        decimal_value = decimal_value * 2 + int(digit)
    return decimal_value


# Example usage:
binary_string = "101010"
decimal_number = to_decimal(binary_string)
print(f"The decimal representation of {binary_string} is {decimal_number}.")