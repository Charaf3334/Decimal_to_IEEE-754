import sys

def int_to_binary(integer):
    
    if integer == 0:
        return '0'
    result = ''
    integer = abs(int(integer))

    while integer > 0:
        if integer % 2 == 0:
            result += '0'
        else:
            result += '1'
        integer //= 2

    return result[::-1]


def fraction_part_to_binary(decimal):
    
    fraction = abs(decimal) - int(abs(decimal))
    result = ''
    max_bits = 23
    i = 0
    
    while fraction > 0 and i < max_bits:
        fraction *= 2
        bit = int(fraction)
        fraction -= bit
        result += str(bit)
        i += 1
    
    return result

def IEEE_754(decimal):
    
    if decimal == 0:
        return '0' * 32

    sign_bit = '0' if decimal >= 0 else '1'
     
    decimal = abs(decimal)
    int_part = int(decimal)
    int_binary = int_to_binary(int_part)
    frac_binary = fraction_part_to_binary(decimal)

    if int_part != 0:
        first_one_index = int_binary.find('1')
        exponent = len(int_binary) - first_one_index - 1
        mantissa = int_binary[first_one_index + 1:] + frac_binary
    else:
        first_one_index = frac_binary.find('1')
        exponent = -(first_one_index + 1)
        mantissa = frac_binary[first_one_index + 1:]

    exp_bits = int_to_binary(127 + exponent).zfill(8)
    mantissa = mantissa.ljust(23, '0')[:23]

    return sign_bit + exp_bits + mantissa

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        print(f'Error: {n} is not a valid decimal number!')
        return False

def main():
    
    if len(sys.argv) < 2:
        print('Error: must enter at least one decimal number!')
        return

    for arg in sys.argv[1:]:
        if is_number(arg):
            decimal = float(arg)
            ieee_format = IEEE_754(decimal)
            print(f'{decimal} -> {ieee_format}')


if __name__ == '__main__':
    main()