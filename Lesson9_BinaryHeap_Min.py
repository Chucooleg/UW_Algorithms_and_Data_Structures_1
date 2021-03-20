
class BinaryHeapMin:
    def __init__(self, numbers):
        self.num_elements = len(numbers) - 1 # since we don't use element at index 0, we do Length -1
        self.heap = []
        self.heap.extend(numbers)
        self.heap.extend([None] * self.num_elements)

        self.build_heap()

    def build_heap(self):
        # Remember, there is nothing to be done at the leaf level
        # We will start at leaflevel - 1
        # So, we start from the parent of the last element
        currentIndex = self.get_parent_index(self.num_elements)
        while currentIndex > 0:
            self.heapify_down(currentIndex)
            currentIndex -= 1
            self.output(f"After processing index {currentIndex + 1}: ")

    def get_parent_index(self, index):
        return index // 2

    def get_left_child_index(self, index):
        return index << 1 # same as index * 2

    def get_right_child_index(self, index):
        return (index << 1) + 1 # same as index * 2 + 1

    def has_left_child(self, index):
        return self.get_left_child_index(index) <= self.num_elements

    def has_right_child(self, index):
        return self.get_right_child_index(index) <= self.num_elements

    def number_of_elements(self):
        return self.num_elements

    def heapify_down(self, starting_index = 1): # start with root if no other index is specified
        current_index = starting_index
        smaller_child_index = self.get_smaller_child_index(current_index)

        while smaller_child_index > 0 and self.heap[smaller_child_index] < self.heap[current_index]:
            self.swap_values(current_index, smaller_child_index) # Since child is smaller, swap it with its parent
            current_index = smaller_child_index
            smaller_child_index = self.get_smaller_child_index(current_index)

    def get_min(self):
        return self.heap[1] # first or root element. 0th index is not used in this implementation.

    def add(self, value):
        # To keep this code simple, I will just return if no space left in my array
        if self.num_elements >= len(self.heap):
            print("Ran out of space.")
            return

        # 1. Append the value, ie, add to end
        self.num_elements += 1
        self.heap[self.num_elements] = value

        # 2. HeapifyUp
        self.heapify_up()

    def heapify_up(self):
        # Start with the parent of the last element we just added.
        current_index = self.num_elements
        parent_index = self.get_parent_index(current_index)

        while parent_index > 0 and self.heap[parent_index] > self.heap[current_index]:
            self.swap_values(current_index, parent_index) # Since child is smaller, swap it with its parent

            current_index = parent_index
            parent_index = self.get_parent_index(current_index)

    def delete_min(self):
        # 1. Replace root with last element.
        self.heap[1] = self.heap[self.num_elements]
        self.num_elements -= 1 # post decrement num_elements

        # 2. HeapifyDown
        self.heapify_down()

    def get_smaller_child_index(self, index):
        smaller_child_index = 0

        if index > 0 and self.has_right_child(index):
            # Take the smaller of left or right
            # NOTE: I didn't check if has_left_child(index) is true... Is that ok?
            if self.heap[self.get_right_child_index(index)] < self.heap[self.get_left_child_index(index)]:
                smaller_child_index = self.get_right_child_index(index)
            else:
                smaller_child_index = self.get_left_child_index(index)
        elif index > 0 and self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

        return smaller_child_index

    def swap_values(self, index_a, index_b):
        val_at_b = self.heap[index_b]
        self.heap[index_b] = self.heap[index_a]
        self.heap[index_a] = val_at_b

    @staticmethod
    def generate_some_values_1():
        values = [0, 77, 35, 52, 30, 15, 7] # we won't use index 0
        return values

    def output(self, msg):
        connector = ", "
        # We've got to do a little extra work here because we pre-populated the list with Nones to set it to an appropriate size
        strings = [str(content) for content in self.heap if content]
        # This is a list comprehension, a concise way transform objects from one list into another
        # It's the equivalent of writing:
        # for content in self.heap:
        #   if content:
        #       strings.append(content)
        print(f"{msg} {str(connector.join(strings))}")

    @staticmethod
    def do_heap_add(min_heap):
        print("")
        print("Doing Adds now:")
        print("Adding 100")

        min_heap.add(100)
        min_heap.output("After add 100: ")

        min_heap.add(1)
        min_heap.output("After add 1: ")

    @staticmethod
    def do_min_operations(min_heap):
        print("")
        print("Doing get_min and delete_min operations now:")

        print("get_min returned: " + str(min_heap.get_min()))

        num_deletes = min_heap.number_of_elements() - 1
        for ii in range(num_deletes):
            min_heap.delete_min()
            print("After delete_min, get_min returned: " + str(min_heap.get_min()))

some_values = BinaryHeapMin.generate_some_values_1()

print("Starting values: " + ", ".join([str(value) for value in some_values]))

min_heap_1 = BinaryHeapMin(some_values)
BinaryHeapMin.do_heap_add(min_heap_1)
BinaryHeapMin.do_min_operations(min_heap_1)

# Run this code in ur own time and step thru it.
# Add another method, say, generate_some_values_2() that will return different values for u to
# play around with the min heap

# Write code for the max heap. You can use this code as a starting point, or start from scratch
# and come back to this code if u want to refer to something.