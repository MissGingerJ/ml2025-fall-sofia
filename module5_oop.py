# Han Jiang, 11/02/2025

class Data_Processor:
    def __init__(self):
        
        # Initialize an empty list to store numbers.

        self.numbers = []

    def insert_number(self, number):
        
        # Add the user provided number into the list.

        self.numbers.append(number)

    def search_number(self, X):
        
        """
        Search for number X in the list.
        Returns the index (1-based) if found, otherwise -1.
        """

        if X in self.numbers:
            return self.numbers.index(X) + 1  
        else:
            return -1
        

def main():
    # Q1: The program asks the user for input N (positive integer) and reads it
    while True:
        try:
            N = int(input("Please enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Q2: Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
    processor = Data_Processor()

    for i in range(N):
        while True:
            try:
                num = int(input(f"Please enter {i+1}th number: "))
                processor.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Q3: In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
    # or the index (from 1 to N) of this X if the user inputed it before.
    while True:
        try:
            X = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    index = processor.search_number(X)
    print(index)


if __name__ == "__main__":
    main()
        


        
