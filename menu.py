import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from tsi_project.source.DFT import *
from tsi_project.source.FFT_rdx2 import *
from tsi_project.source.FFT_rdx4 import *
from tsi_project.source.plotter import *
from tsi_project.source.common import *
from scipy.io import wavfile

menu = lambda: None

# Placeholder functions for different algorithms
def fft2(sequence):
    print("Running FFT2...")
    try:
        X = m_fft_rdx2(sequence)
        t = list(range(0, len(sequence)))
        xreal, ximag, Xreal, Ximag, magnitude, phase, freqs = m_plot_v2(t, sequence, X)
        save_hdf5(xreal, ximag, Xreal, Ximag, magnitude, phase, freqs, t)
        return X
    except Exception as e:
        print(f"An error occurred: {e}")
        menu()

def fft4(sequence):
    print("Running FFT4...")
    try:
        X = m_fft_rdx4(sequence)
        t = list(range(0, len(sequence)))
        xreal, ximag, Xreal, Ximag, magnitude, phase, freqs = m_plot_v2(t, sequence, X)
        save_hdf5(xreal, ximag, Xreal, Ximag, magnitude, phase, freqs, t)
        return X
    except Exception as e:
        print(f"An error occurred: {e}")
        menu()

def dft(sequence):
    print("Running DFT...")
    try:
        X = m_dft(sequence)
        t = list(range(0, len(sequence)))
        xreal, ximag, Xreal, Ximag, magnitude, phase, freqs = m_plot_v2(t, sequence, X)
        save_hdf5(xreal, ximag, Xreal, Ximag, magnitude, phase, freqs, t)
        return X
    except Exception as e:
        print(f"An error occurred: {e}")
        menu()

def transform_cmd(cmd1, cmd2, cmd3):
    if cmd1 == 'fft2':
        return fft2(cmd2)
    elif cmd1 == 'fft4':
        return fft4(cmd2)
    elif cmd1 == 'dft':
        return dft(cmd2)
    else:
        print("Unknown command!")
        return None

# Function to handle 'man' command input
def handle_man_input():
    try:
        print("Please enter the sequence in time domain (e.g., [1, 2, 3, 4]):")
        sequence_input = input()
        sequence = eval(sequence_input)  # This allows input as a Python list
        return np.array(sequence)
    except Exception as e:
        print("An error occured, try again... Details below:")

# Function to handle file-based sequence loading
def handle_file_input():
    return None #Has to return sequence that need to be checked manually for errors after return

# Function to process the sequence based on CMDS3
def handle_cmds3():
    sequence = []

    print("Please enter the file path:")
    path = input().strip()

    print("Do you want to specify a range or number of samples?")
    print("1. Range (from A to B)")
    print("2. Samples (from A and N samples)")
    choice = input("Enter choice (1/2): ").strip()

    if choice == '1':
        print("Enter the start time A:")
        A = float(input())
        print("Enter the end time B:")
        B = float(input())
        try:
            sequence = import_audio(A, B, path)
            return sequence
        except Exception as e:
            print("An error occured.")
    elif choice == '2':
        print("Enter the start time A:")
        A = int(input())
        print("Enter the number of samples N:")
        N = int(input())
        try:
            sequence = import_audio_n_samples(A, N, path)
            return sequence
        except Exception as e:
            print("An error occured.")
    else:
        print("Invalid choice!")
        return sequence

# Menu loop for the user to interact with the system
def menu():
    '''
    Function that runs user interface.
    '''
    while True:
        print("\nMenu:")
        print("1. Transform CMD1 CMD2")
        print("2. Load data from hdf5 file")
        print("3. Exit")
        choice = input("Enter choice (1 or 2 or 3): ").strip()

        if choice == '1':
            print("Enter CMD1 (fft2, fft4, dft):")
            cmd1 = input().strip()
            print("Enter CMD2 (man or file):")
            cmd2 = input().strip()

            if cmd2 == 'man':
                sequence = handle_man_input()
            elif cmd2 == 'file':
                sequence = handle_cmds3()
            else:
                print("Invalid CMD2!")
                continue

            # Execute transformation on the sequence
            print(f"Performing {cmd1} on sequence: {sequence}")
            result = transform_cmd(cmd1, sequence, None)
            print("Result:", result)
        elif choice == '2':
            try:
                filename = input("Enter file name: (e.g., filename1.h5) ").strip()
                read_hdf5(filename)
                print("Loaded.")
            except Exception as e:
                print("Problem loading a file...")
                print("Try again")
        elif choice == '3':
            print("Exiting...")
            print("Application closed.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
