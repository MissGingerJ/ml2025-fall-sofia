# Han Jiang, 11/04/2025
import numpy as np

class KNN_Regr:
    def __init__(self):
        
        # Initialize an empty list to store numbers.

        self.x = []
        self.y = []

    def insert_data(self, x, y):
        
        # Add the user provided number into the list.
        self.x.append(x)
        self.y.append(y)

    def predict(self, k, x_new):
        
        N = len(self.x)
        x_array = np.array(self.x)
        y_array = np.array(self.y)
        
        if k<=0 or k > N:
            raise ValueError("k must be a positive integer not exceeding the number of points.")
        
        dists = np.abs(x_array - x_new)
        sorted_idx = np.argsort(dists)

        return np.mean(y_array[sorted_idx[:k]])

        

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

    # Q2: Then the program asks the user for input k (positive integer) and reads it.
    while True:
        try:
            k = int(input("Please enter a positive integer k which is smaller than N: "))
            if k > 0 and k <= N:
                break
            else:
                print("Please enter a positive integer which is smaller than N.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Q3: Then the program asks the user to provide N (x, y) points (one by one) 
    # and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
    model = KNN_Regr()

    print(f"Please enter N pairs of numbers: ")
    for i in range(N):
        while True:
            try:
                x = float(input(f"Please enter the x of {i+1}th pair of numbers : "))
                y = float(input(f"Please enter the y of {i+1}th pair of numbers : "))
                model.insert_data(x, y)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Q4: In the end, the program asks the user for input X and outputs: 
    # the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
    while True:
        try:
            X_new = float(input("Please enter a number as the X of the new point: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    try:
        y_hat = model.predict(k, X_new)
        print("The predicted y_hat is", y_hat)
    except ValueError as e:
        # k invalid relative to N
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
        


        
