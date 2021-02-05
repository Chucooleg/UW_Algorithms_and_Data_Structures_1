#Assumes number >= 0 and base > 0; Does no validation of input
def convert(number, base_value):
    if number < 0 or base_value < 0 or base_value > 16:
        return ""
    num_bits = 32
    bit_string_list = ["0"] * num_bits

    index = 0
    while number > 0:
        lsb = number % base_value #lsb will have values from 0 to (baseValue - 1)

        bit_string_list[num_bits - index - 1] = str(get_char(lsb))
        # In both C# and Python strings are immutable. C# offers StringBuilder for dynamically building up strings.
        # We're basically replicating the bit of functionality we need from it here,
        # by storing the individual strings in a list then joining all those strings together for our return value.

        number //= base_value #number = number // baseValue;
        # Be careful to note the difference between // (integer division) and / (float division)
        
        index += 1 # number = number + 1

    return ''.join(bit_string_list)
    # We're using a string literal ('') & string.join to combine our list of strings into one with '' as the separator.

def get_char(number):
    if number <= 9:
        return chr(ord('0') + int(number))
    else:
        return chr(ord('A') + int(number - 10))

# Assumes number >= 0. Does no validation of input
def convert_to_binary(number):
    num_bits = 32
    bit_string_list = ["0"] * num_bits
    for i in range(num_bits - 1):
        lsb = (number >> i) & 0x1
        if lsb is 0:
            bit_string_list[num_bits - i - 1] = "0"
        else:
            bit_string_list[num_bits - i - 1] = "1"

        # Could also be bit_string_list[num_bits - i - 1] = "0" if lsb is 0 else "1"
    return ''.join(bit_string_list)


print("Binary conversions")
print(convert_to_binary(0))
print(convert_to_binary(1))
print(convert_to_binary(10))
print(convert_to_binary(15))
print(convert(15, 2))
print("Base3 conversions")
print(convert(15, 3))
print(convert(26, 3))
print("Base16 conversions")
print(convert(1, 16))
print(convert(15, 16))
print(convert(16, 16))
print(convert(32, 16))
print(convert(64, 16))
print(convert(255, 16))
print(convert(256, 16))
print(convert(1024, 16))
