import numpy as np

def check_input(input_data):
    # Check if the input is a list or np.ndarray
    if not isinstance(input_data, (list, np.ndarray)):
        raise ValueError("Input must be a list or np.ndarray.")

    # Check if all elements in the list are numeric (int or float)
    if not all(isinstance(i, (int, float, complex)) for i in input_data):
        raise ValueError("All elements of the list or np.ndarray must be numeric values (int or float or complex).")

    # Input cannot be empty
    if (len(input_data)<=0):
        raise ValueError("Input cannot be empty sequence")

    # Valid input
    return 1

#   v1.0.0  @author Amila Čengić
#           @date   09.12.2024.
#           @change Inicijalna verzija
