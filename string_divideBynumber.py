def number_to_words(number) :
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if number < 10 :
        return ones[number]
    elif number < 20 :
        return teens[number - 10]
    elif number < 100 :
        tens_digit = number // 10
        ones_digit = number % 10
        return tens[tens_digit] + '-' + ones[ones_digit] if ones_digit != 0 else tens[tens_digit]
    elif number < 1000 :
        hundreds_digit = number // 100
        remainder = number % 100
        if remainder == 0 :
            return ones[hundreds_digit] + ' hundred'
        else :
            return ones[hundreds_digit] + ' hundred ' + number_to_words ( remainder )
    elif number < 1000000 :
        thousands = number_to_words ( number // 1000 )
        remainder = number % 1000
        if remainder == 0 :
            return thousands + ' thousand'
        else :
            return thousands + ' thousand ' + number_to_words ( remainder )


# Example usage
print ( number_to_words ( 123 ) )  # Output: "one hundred twenty-three"
print ( number_to_words ( 9999 ) )  # Output: "nine thousand nine hundred ninety-nine"
print ( number_to_words ( 212345 ) )  # Output: "two hundred twelve thousand three hundred forty-five"
