#  "ab" ->  "ab" and  "ba"
#  "abc" ->  "abc" "bac" "cab" "cba" "bca" "acb"   6 total.
#  "abcd" --> Will have 4! permutations : 24
#  for a string of length N, u will have N! permutations.
#
#  "abc"  Find me all permutations of "ab" , and then I will add 'c' to all of them in all the insertion points
#          result set has "ba" and "ab" --> Adding 'c' to every string in the result set -->> "cba", "bca", "bac"
#                                                                                             "cab", "acb", "abc"
#  "ab"    Find me all permutations of "a", and then I will add 'b' to all of them in all the insertion points
#          result set has "a" --> Adding 'b' to every string in the result set -->>  "ba" and "ab"
#  "a"     the permutations of this is just the stirng "a"  <-- recursion base case.


def add_char_to_string_at_position(str_to_add_ch_in, insert_pos, ch):
    new_string = []
    new_string.extend(str_to_add_ch_in)
    new_string.insert(insert_pos, ch)
    return new_string


def add_permutations(local_results, ch, results):
    for ii in range(len(local_results)):
        str_to_add_ch_in = local_results[ii]

        length = len(str_to_add_ch_in) + 1
        for str_index in range(length):
            new_str = add_char_to_string_at_position(str_to_add_ch_in, str_index, ch)
            results.append(new_str)

# abc -> ab -> a [recursion stops
# add_permutations (ba), (ab)
# add_permutations (cba, bca, bac), (cab, acb, abc)


def permute(input_str, results):
    if len(input_str) == 1:
        results.append(input_str)
        return

    local_results = []
    permute(input_str[:-1], local_results)
    add_permutations(local_results, input_str[-1], results)


input_str = ["a", "b", "c", "d", "e", "f", "g"]
results = []
permute(input_str, results)

print(f'Num permutations of {input_str} {len(results)}')