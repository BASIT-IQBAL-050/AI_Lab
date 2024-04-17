def encode(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value

# Example usage
binary_representation = "010"
decimal_value = encode(binary_representation)
print(f"The decimal representation of binary '{binary_representation}' is: {decimal_value}")
