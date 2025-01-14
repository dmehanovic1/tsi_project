import numpy as np
import h5py
from scipy.io import wavfile
import time

from tsi_project.source.plotter import *

def check_input(input_data):
    '''
    Internal function that checks validity of input data in module functions.

    Parameters:
    :param input_data (list): input sequence

    Returns:
    :return: 1 if input is valid, raises error if input is invalid
    '''
    # Check if the input is a list or np.ndarray
    if not isinstance(input_data, (list, np.ndarray)):
        raise ValueError("Input must be a list or np.ndarray.")

    # Check if all elements in the list are numeric (int or float)
    if not all(isinstance(i, (int, float, complex, np.int16, np.int32, np.int64, np.int8)) for i in input_data):
        raise ValueError("All elements of the list or np.ndarray must be numeric values (int or float or complex).")

    # Input cannot be empty
    if (len(input_data)<=0):
        raise ValueError("Input cannot be empty sequence")

    # Valid input
    return 1

def import_audio(a_from, a_to, a_path):
    '''
    Imports time domain sequence from a specified .wav audio file from A [sec] to B[sec].

    Parameters:
    a_from (float): defines import starting moment in seconds
    a_to (float): defines import ending  moment in seconds

    Returns:
    list (array_like): time domain sequence

    Example:
    >>> import_audio(1,2,"filename.wav")
    #imports audio data from file "filename.wav" from second 1 to second 2
    '''
    try:
        samp_rate, x = wavfile.read(a_path)
        from_sec = a_from
        to_sec = a_to
        x = x[(int)(from_sec*samp_rate):(int)(to_sec*samp_rate)]
        return x
    except:
        raise ValueError("Problem encountered while loading the audio file...")

def import_audio_n_samples(a_from, n, a_path):
    '''
    Imports N time domain sequence samples from a specified .wav audio file from A [sec].

    Parameters:
    :param a_from (float): defines import starting moment in seconds
    :param n (int): defines number of samples

    Returns:
    :return list: time domain sequence

    Example:
    >>> import_audio_n_samples(1,64,"filename.wav")
    #imports 64 audio data samples from file "filename.wav" from second 1.
    '''
    try:
        samp_rate, x = wavfile.read(a_path)
        from_sec = a_from
        x = x[(int)(from_sec*samp_rate):(n+(int)(from_sec*samp_rate))]
        return x
    except:
        raise ValueError("Problem encountered while loading the audio file...")

def save_hdf5(xreal, ximag, Xreal, Ximag, magnitude, phase, freqs, t):
    '''
    Saves the data in hdf5 format. Inputs represent data to be saved.

    Parameters:
    :param xreal: real samples in time domain
    :param ximag: imaginary samples in time domain
    :param Xreal: real samples in frequency domain
    :param Ximag: imaginary samples in frequency domain
    :param magnitude: magnitude samples in frequency domain
    :param phase: phase samples in frequency domain
    :param freqs: frequeny samples
    :param t: time samples

    Returns:
    :return: None
    '''
    tx = str(time.time())
    tx = tx.replace(".", "-")

    with h5py.File(tx + '.h5', 'w') as f:
        f.create_dataset('timestamp', data = tx)
        f.create_dataset('xreal', data = xreal)
        f.create_dataset('ximag', data = ximag)
        f.create_dataset('Xreal', data = Xreal)
        f.create_dataset('Ximag', data = Ximag)
        f.create_dataset('magnitude', data = magnitude)
        f.create_dataset('phase', data = phase)
        f.create_dataset('freqs', data = freqs)
        f.create_dataset('t', data = t)
    print("Data saved to " + tx + ".h5")

def read_hdf5(filename):
    '''
    Reads and plots data from a specified hdf5 file.

    Parameters:
    :param filename (string): name of the hdf5 file

    Returns:
    :return: None
    '''
    xreal = []
    ximag = []
    Xreal = []
    Ximag = []
    magnitude = []
    phase = []
    freqs = []
    t = []
    with h5py.File(filename, 'r') as file:
        xreal = file['xreal']
        xreal = xreal[:]
        ximag = file['ximag']
        ximag = ximag[:]
        Xreal = file['Xreal']
        Xreal = Xreal[:]
        Ximag = file['Ximag']
        Ximag = Ximag[:]
        magnitude = file['magnitude']
        magnitude = magnitude[:]
        phase = file['phase']
        phase = phase[:]
        freqs = file['freqs']
        freqs = freqs[:]
        t = file['t']
        t = t[:]
    plot_hdf5(xreal, ximag, Xreal, Ximag, magnitude, phase, freqs, t)




#   v1.0.0  @author Amila Čengić
#           @date   09.12.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Denin Mehanović
#           @date   23.12.2024.
#           @change Dodane funkcije za import signala
