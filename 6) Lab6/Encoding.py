def encode(binary):
    """Converts a binary string or list of binary digits to a decimal integer."""
    if isinstance(binary, str):
        binary = binary.strip()  # Remove any leading/trailing whitespace
        decimal = int(binary, 2)  # Convert binary string to decimal integer
    elif isinstance(binary, list):
        binary_str = ''.join(str(bit) for bit in binary)  # Convert list to string
        decimal = int(binary_str, 2)  # Convert binary string to decimal integer
    else:
        raise ValueError("Input must be a binary string or list of binary digits.")

    return decimal

