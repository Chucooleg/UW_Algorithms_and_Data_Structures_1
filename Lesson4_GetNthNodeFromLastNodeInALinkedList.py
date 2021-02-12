import collections

# Not catching exceptions etc. in this example, to keep it simple.
def print_nth_from_last(N, list):
    if not list:
        return
    # 1 2 3 4 5
    # Let's say N = 2
    # current <- 1
    # n_behind_current <- 1
    # loop and will make current point to node with value 3
    # n_behind_current <-- 1 and so, n_behind_current is 2 behind current.
    # Now I will move both current and n_behind_current forward until current gets to the end of the list
    current = 0
    n_behind_current = 0
    # Because Python doesn't have a build in LinkedList type, we are going to use a deque (double-ended queue)
    # and maintain our own count as we move through it.

    num = N
    while num > 0 and current < len(list):
        num -= 1
        current += 1
    if num > 0:
        print(f"Ran out of list for {N}th element")
    else:
        while current < len(list):
            current += 1
            n_behind_current += 1

        print (f'{N}th element from end of list is {list[n_behind_current]}')

def output(list):
    if not list:
        return

    for element in list:
        print(element)

def create_list(size):
    list = collections.deque()

    for ii in range(0, size - 1):
        list.append(ii)

    return list

l1 = create_list(100)
output(l1)
print_nth_from_last(1, l1)
print_nth_from_last(99, l1)
print_nth_from_last(100, l1)
print_nth_from_last(101, l1)