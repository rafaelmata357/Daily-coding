class Calculator:
    ''' Class to create different aritmentic functions
    '''
    
    def __init__(self):
        #self.num1 = num1
        #self.num2 = num2
        return None

    def add(self,x,y):
        return x+y

    def fib(self, n):
        ''' Fucntion to calculate the n-element in the Fibonacci series

            Params: n integer, n-element

            Returns: fib_series , list
        '''

        initial_state = [1, 1]

        for i in range(n):
            print("This should be a Fibonacci Series....")

    




if __name__ == '__main__': 


    # Create a Calculator object with two numbers




     calc = Calculator()

     # Call the add method on the Calculator object to get the sum of the two numbers
     sum = calc.add(10,2)

     print("The sum is:", sum)
     calc.fib(5)
