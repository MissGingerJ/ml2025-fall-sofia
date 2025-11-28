# Han Jiang, 11/28/2025

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

class GetData:
    def __init__(self, N):
        """
        Preallocate arrays with known size for efficiency.
        x: real-valued feature, shape (N, 1)
        y: non-negative integer class labels, shape (N,)
        """
        self.N = N
        self.x = np.zeros((N, 1), dtype=float)
        self.y = np.zeros(N, dtype=int)
        self.index = 0  # current insertion index

    def insert_data(self, x, y):
        """
        Insert (x, y) pair.
        x: real number (feature)
        y: non-negative integer (class label)
        """
        if self.index >= self.N:
            raise IndexError("All data points have already been inserted.")
        
        # x can be any real number
        # y must be a non-negative integer
        if not isinstance(y, (int, np.integer)):
            raise ValueError("y must be an integer.")
        if y < 0:
            raise ValueError("y must be a non-negative integer.")
        
        self.x[self.index, 0] = float(x)
        self.y[self.index] = int(y)
        self.index += 1


def read_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt).strip())
            if n > 0:
                return n
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_xy_pairs(dataset_name, dataset_obj):
    """
    Read (x, y) pairs from the user and insert into dataset_obj (GetData).
    """
    N = dataset_obj.N
    print(f"\nPlease enter {N} (x, y) pairs for {dataset_name}:")
    print("x is a real number, y is a non-negative integer.")
    for i in range(N):
        while True:
            try:
                x_str = input(f"Please enter x for the {i+1}th pair: ").strip()
                y_str = input(f"Please enter y for the {i+1}th pair: ").strip()

                x_val = float(x_str)
                y_val = int(y_str)

                if y_val < 0:
                    print("y must be a non-negative integer. Please try again.")
                    continue

                dataset_obj.insert_data(x_val, y_val)
                break
            except ValueError:
                print("Invalid input. x should be real, y should be a non-negative integer. Please try again.")
            except Exception as e:
                print(f"Error: {e}. Please try again.")


def main():
    # 1. Read training set size N
    N = read_positive_int("Enter N (number of training pairs): ")

    # 2. Read N training (x, y) pairs
    train_data = GetData(N)
    read_xy_pairs("TrainS", train_data)

    # 3. Read test set size M
    M = read_positive_int("\nEnter M (number of test pairs): ")

    # 4. Read M test (x, y) pairs
    test_data = GetData(M)
    read_xy_pairs("TestS", test_data)

    X_train = train_data.x
    y_train = train_data.y
    X_test = test_data.x
    y_test = test_data.y

    # 5. Set up kNN classifier and GridSearchCV for hyperparameter search

    # ===== safer CV choice for classification =====
    unique_classes, counts = np.unique(y_train, return_counts=True)
    min_class_count = counts.min()

    best_model = None
    best_k = 1  # default

    # Use up to 5-fold cross-validation, but not more than number of samples
    if len(y_train) > 1 and min_class_count > 1:
        cv_folds = min(5, min_class_count)

        # smallest training set size across CV folds:
        # min_train_size = N - ceil(N / cv)
        N_train = len(y_train)
        min_train_size = N_train - int(np.ceil(N_train / cv_folds))

        # define k range respecting:
        # 1 <= k <= 10 and k <= min_train_size
        max_k = min(10, int(min_train_size))
        if max_k < 1:
            max_k = 1
        k_values = list(range(1, max_k + 1))

        knn = KNeighborsClassifier()
        param_grid = {"n_neighbors": k_values}

        grid_search = GridSearchCV(
            estimator=knn,
            param_grid=param_grid,
            scoring="accuracy",
            cv=cv_folds
        )
        grid_search.fit(X_train, y_train)

        best_k = grid_search.best_params_["n_neighbors"]
        best_model = grid_search.best_estimator_
    else:
        # Edge case: only one training sample, just use k=1
        best_k = 1
        best_model = KNeighborsClassifier(n_neighbors=1)
        best_model.fit(X_train, y_train)

    # 6. Evaluate best model on the test set
    y_pred = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    # 7. Output results
    print("\nResults:")
    print(f"Best k (number of neighbors): {best_k}")
    print(f"Test accuracy: {test_accuracy:.4f}")
if __name__ == "__main__":
    main()