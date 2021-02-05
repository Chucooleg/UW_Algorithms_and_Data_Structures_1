from timeit import default_timer as timer

class Fibonacci:

    def __init__(self):
        self.fib_store = {}
        # Dictionary is used to store the computed fibonacci values.
        # N is the key, and Fib(N) is the value.
        # For example:
        # mFibStore[0] will have 0
        # mFibStore[1] will have 1
        # mFibStore[2] will have 1
        # mFibStore[3] will have 2
        # mFibStore[4] will have 3
        # mFibStore[5] will have 5
        # mFibStore[6] will have 8  and so on



    @staticmethod
    def do_fibonacci_recursive_with_memoization(n, num_repeated_computes):
        ############################################################################################
        # We will call GetFibRecursiveMemoization on a new object every time in the for loop below.
        # This means that the memoization done in the first iteration will NOT provide any help (optimization)
        # to subsequent iterations because we are creating a new Fibonacci object every time in the loop
        start = timer()
        for itr in range(num_repeated_computes):
            fib1 = Fibonacci().get_fib_recursive_memoization(n)
        end = timer()
        print(f"FibRecursiveWithMem({n}). {num_repeated_computes} repeated computes. Diff objects. Time: {end - start} seconds")
        ##############################################################################################
        # We will call GetFibRecursiveMemoization on the SAME object every time in the for loop below.
        # Thats why we create one object outside the for loop only.
        # This means that the memoization done in the first iteration WILL provide  help (optimization)
        # to subsequent iterations because we would be storing all the computed fibonacci values first time in the loop,
        # and these will just get used for all subsequent loop iterations.
        start = timer()
        f1 = Fibonacci() # Create the object once outside the loop
        for itr in range(num_repeated_computes):
            fib1 = f1.get_fib_recursive_memoization(n)
        end = timer()
        print(f"FibRecursiveWithMem({n}). {num_repeated_computes} repeated computes. Same object. Time: {end - start} seconds")

    @staticmethod
    def do_fibonacci_iterative(n, num_repeated_computes):
        f1 = Fibonacci()
        start = timer()

        for itr in range(num_repeated_computes):
            fib1 = f1.get_fib_iterative(n)
        end = timer()
        print(f"GetFibIterative({n}). {num_repeated_computes} repeated computes. Time: {end - start} seconds")

    @staticmethod
    def get_fib_recursive(n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            return Fibonacci.get_fib_recursive(n - 1) + Fibonacci.get_fib_recursive(n - 2)

    def get_fib_recursive_memoization(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            if n not in self.fib_store:
                self.fib_store[n] = self.get_fib_recursive_memoization(n - 1) + self.get_fib_recursive_memoization(n - 2)
            return self.fib_store[n]

    def get_fib_iterative(self, n):
        fib_n_1 = 0 # initialized to Fib(0), which is 0. Will eventually contain Fib(N-1) value
        fib_n_2 = 1 # initialized to Fib(1), which is 1. Will eventually contain Fib(N-2) value
        fib_n = 0   # Will eventually contain Fib(N) value

        while n > 0:
            fib_n = fib_n_1 + fib_n_2

            # get ready for next iteration of the loop (if there is one)
            fib_n_2 = fib_n_1
            fib_n_1 = fib_n

            n -= 1

        return fib_n

#So, we have, in order of increasing speed, the following

#    Recursive fibonacci with no memoization
#    Recursive fibonacci with memoization
#    Iterative fibonacci
#    Recursive fibonacci with memoization repeatedly on the same object

n = 90
num_repeated_computes = 500000

Fib = Fibonacci()
Fib.do_fibonacci_recursive_with_memoization(n, num_repeated_computes)
Fib.do_fibonacci_iterative(n, num_repeated_computes)