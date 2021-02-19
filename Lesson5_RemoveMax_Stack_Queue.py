import collections
#        stack
#       * 1      <--- Top of stack
#       * 2
#       * 3
#       * 4
#       *
#       * Put elements in a queue (and keep track of max element)
#       *
#       * Queue:
#       * 1      <--- Front of queue
#       * 2
#       * 3
#       * 4
#       *
#       * Pop elements from queue and push onto the stack (except for max element(s) )
#       *
#       * stack
#       *
#       * 3        <--- Top of stack
#       * 2
#       * 1
#       *
#       * Transfer from stack to queue
#       *
#       * queue
#       * 3        <--- Front of queue
#       * 2
#       * 1
#       *
#       * Final step: transfer from queue to stack
#       *
#       * stack:   <--- Top of stack
#       * 1
#       * 2
#       * 3


def validate_input(stack):
 return stack and len(stack) > 0


def output(stack):
    print("topOfStack: ")
    for element in stack:
        print(str(element) + " ")
    print(":bottomOfStack")


def remove_max(stack):
    if not validate_input(stack):
        #throw exception
        return -1 # we would throw an exception and wouldn't have to return -1
                  # Returning -1 is not great, because that could actually be a max element in the stack

    # First, find out the max value in the stack
    queue1 = collections.deque() #allocate a queue (using a deque as just a regular queue).
    max_element = -11111 # TBD fix

    while len(stack) > 0:
        element = stack.pop()
        max_element = max(max_element, element)
        queue1.append(element)

    # Now we know the value of the maximum element in the stack.
    # Push elements from queue to the stack (which is now empty), with the exception of elements = max_element

    while len(queue1) > 0:
        element = queue1.popleft()
        if element != max_element:
            stack.append(element)

    # Now stack has all emements exception those whose value is max_element
    # However, the order of elements in the stack is wrong.
    # Transfer from stack to queue.

    while len(stack) > 0:
        queue1.append(stack.pop())

    # And back to the stack --- final step

    while len(queue1) > 0:
        stack.append(queue1.popleft())

    return max_element


def do_removing_thingies(stack):
    if not validate_input(stack):
        print("Empty stack")
        return
    print("==================================================")
    print("Stack before RemoveMax call:")
    output(stack)

    max_element = remove_max(stack)
    print(f"max_element removed was {max_element}")
    print("Resultant stack:")
    output(stack)


def create_stack():
    stack = collections.deque()
    # 7, 77, 88, 2, 97, 5, 117, 107, 61, 107, 52
    stack.append(7)
    stack.append(77)
    stack.append(88)
    stack.append(2)
    stack.append(97)
    stack.append(5)
    stack.append(117)
    stack.append(107)
    stack.append(61)
    stack.append(107)
    stack.append(52)

    return stack


stack1 = create_stack()
for ii in range(len(stack1) - 1, 0, -1):
    do_removing_thingies(stack1)