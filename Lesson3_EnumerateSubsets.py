def print_all_subsets(input_str):
    all_subsets = get_all_subsets(input_str)
    if all_subsets:
        print(f'Subsets of {input_str} are({len(all_subsets)})')

        for subset in all_subsets:
            print(subset)

def print_subset_size(input_str):
    all_subsets = get_all_subsets(input_str)
    if all_subsets:
        print(f"{input_str} has {len(all_subsets)} subsets")

def get_all_subsets(input_str):
    if not input_valid(input_str):
        print("Invalid input string, max length supported is 32")
        return

    num_subsets = len(input_str) ** 2
    results = []

    for ii in range(num_subsets):
        subset_str = generate_one_subset_from_bit_pattern(ii, input_str)
        results.append(subset_str)

    return results

def generate_one_subset_from_bit_pattern(value, str_parameter):
    number_of_bits_in_int = 32
    num_bits_to_check = min(number_of_bits_in_int, len(str_parameter))
    subset_str = ""

    for i in range (num_bits_to_check):
        # Check if the ith bit of value is 1:
        # We do this by left shifting 0x1 (which is bit pattern 01) by i places.
        # this puts the 1 in the 0x1 at the ith position.
        # And when we do a bit and with value, it tells if the ith bit in value is 1 or 0
        bit_pattern_with_ith_but_as_1 = 0x1 << i # Left shift 01 by i positions
        ith_bit_value = value & bit_pattern_with_ith_but_as_1

        if ith_bit_value != 0:
            subset_str = subset_str + str_parameter[i] # take ith char of str

    return subset_str

def input_valid(input_str):
    return input_str and len(input_str) <= 32

print_all_subsets("abc")
print_subset_size("abc")
print_subset_size("abcde")
print_subset_size("adcdefghij")
print_all_subsets(None)
print_subset_size("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")