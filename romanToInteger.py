def roman_to_int(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    prev_value = 0
    for numeral in s:
        current_value = roman_values[numeral]
        # current_value = 1

        # If a smaller numeral appears before a larger one, subtract the smaller value
        if current_value > prev_value:
            result += current_value - 2 * prev_value
        
        else:
            result += current_value
        
        prev_value = current_value
    
    return result

# Example usage:
roman_numeral = "XXVII"
result_integer = roman_to_int(roman_numeral)
print(result_integer)
