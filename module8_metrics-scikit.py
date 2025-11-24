# Han Jiang, 11/23/2025
import numpy as np
from sklearn.metrics import precision_score, recall_score

class Precision_Recall:
    def __init__(self, N):

        # Preallocate arrays with known size for efficiency

        self.N = N
        self.x = np.zeros(N, dtype=np.int8)  # ground truth
        self.y = np.zeros(N, dtype=np.int8)  # prediction
        self.index = 0  # current insertion index

    def insert_data(self, x, y):

        # Insert the user provided number at the next available position

        if self.index >= self.N:

            raise IndexError("All data points have already been inserted.")
        
        if x not in [0, 1]:
            raise ValueError("x and y should be 0 or 1.") 
        if y not in [0, 1]:
            raise ValueError("x and y should be 0 or 1.") 
        
        self.x[self.index] = int(x)
        self.y[self.index] = int(y)
        self.index += 1

    def precision(self, zero_division=0):

        if self.index == 0:
            return float('nan')
        return float(precision_score(self.x, self.y, zero_division=zero_division))

    def recall(self, zero_division=0):

        if self.index == 0:
            return float('nan')
        return float(recall_score(self.x, self.y, zero_division=zero_division))


def read_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt).strip())
            if n > 0:
                return n
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_binary_pair(i):
    while True:
        try:
            s = input(f"Enter the {i+1}th pair as 'x y' (each 0 or 1): ").strip()
            parts = s.replace(",", " ").split()
            if len(parts) != 2:
                print("Please enter exactly two numbers (0 or 1), e.g., '1 0'.")
                continue
            x_val = int(float(parts[0]))
            y_val = int(float(parts[1]))
            if x_val not in (0, 1) or y_val not in (0, 1):
                print("Both x and y must be 0 or 1.")
                continue
            return x_val, y_val
        except ValueError:
            print("Invalid input. Please enter 0 or 1 for both x and y.")


def main():
    # Q1: Ask for N

    while True:
        try:
            N = int(input("Please enter a positive integer N: ").strip())
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize model with preallocated arrays
    PR = Precision_Recall(N)

    # Q2: Then the program asks the user to provide N (x, y) points (one by one) and 
    # reads all of them: first: x value, then: y value for every point one by one.

    print(f"Please enter N pairs of numbers, x and y should be 0 or 1: ")
    for i in range(N):
        while True:
            try:
                x = float(input(f"Please enter the x of {i+1}th pair of numbers : "))
                y = float(input(f"Please enter the y of {i+1}th pair of numbers : "))
                PR.insert_data(x, y)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")    

    # print(PR.x, PR.y)
    # Q3: Compute Precision and Recall
    if np.sum(PR.x) == 0:

        prec = PR.precision(zero_division=1)
        rec = PR.recall(zero_division=1)

        print("\nResults:")
        print(f"Precision: {prec:.4f}")
        print(f"Recall:    {rec:.4f}")
    
    else:

        prec = PR.precision()
        rec = PR.recall()

        print("\nResults:")
        print(f"Precision: {prec:.4f}")
        print(f"Recall:    {rec:.4f}")

if __name__ == "__main__":
    main()
