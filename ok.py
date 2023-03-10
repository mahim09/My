def two_digit_sum(num):
    """
    Returns the sum of the digits of a two-digit number.
    """
    if num < 10 or num > 99:
        raise ValueError("Input must be a two-digit number")
    return sum(int(digit) for digit in str(num))
