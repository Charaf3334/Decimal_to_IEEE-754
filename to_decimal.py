import sys

def is_valid(bin):
    if (len(bin) != 32):
        print('Error: not a valid 32bit binary floating point number')
        return False
    if (not(set(bin) <= {'0', '1'})):
        print('Error: not a valid 32 bit binary floating point number')
        return False
    return True

def integer_converter(bin):
    result = 0
    if len(bin) < 8:
        bin = bin.zfill(8)
    bin = bin[::-1]
    for i in range(0, len(bin)):
        if bin[i] == '1':
            result += (2 ** i)
    return result

def fractional_converter(bin):
    result = 0
    for i in range(1, len(bin)):
        if bin[i - 1] == '1':
            result += (2 ** (i * -1))
    return round(result, 2)

def get_decimal_from_binary(bin):
    sign = 1 if bin[0] == '0' else -1
    exponent = integer_converter(bin[1:9])
    shifted = exponent - 127
    temp = '1' + bin[9:]
    integer_part = temp[0:shifted + 1]
    fractional_part = temp[shifted + 1:]
    return sign * (integer_converter(integer_part) + fractional_converter(fractional_part))
    

def main():
    
    if (len(sys.argv) < 2):
        print('Error: must enter at least one 32bit binary floating point number!')
        return
    
    for arg in sys.argv[1:]:
        if is_valid(arg):
            result = get_decimal_from_binary(arg)
            print(f'{arg} -> {result}')
    

if __name__ == '__main__':
    main()