# Han Jiang, 11/16/2025
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNN_Regr:
    def __init__(self):
        
        # Initialize empty NumPy arrays (explicitly use NumPy for data initialization)

        self.x = np.empty(0, dtype=float)
        self.y = np.empty(0, dtype=float)

    def insert_data(self, x, y):

        # Add the user provided number

        self.x = np.append(self.x, float(x))
        self.y = np.append(self.y, float(y))

    def label_variance(self, ddof=0):

        # Compute label variance

        if self.y.size == 0:

            return float('nan')
        
        return float(np.var(self.y, ddof=ddof))

    def predict(self, k, x_new):
    
        N = self.x.size

        if k <= 0 or k > N:
            raise ValueError("k must be a positive integer not exceeding the number of points.")

        X_train = self.x.reshape(-1, 1)  # shape (N, 1) for scikit-learn
        y_train = self.y

        model = KNeighborsRegressor(n_neighbors=k, p=2)
        model.fit(X_train, y_train)
        y_pred = model.predict(np.array([[float(x_new)]], dtype=float))[0]
        return float(y_pred)
    
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


    # Q5: Additionally, provide the variance of labels in the training dataset.
    var_y = model.label_variance()
    print(f"Training label variance: {var_y:.6f}")

if __name__ == "__main__":
    main()    

