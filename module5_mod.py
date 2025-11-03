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