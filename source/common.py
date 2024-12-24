import numpy as np
from scipy.io import wavfile

def check_input(input_data):
    # Check if the input is a list or np.ndarray
    if not isinstance(input_data, (list, np.ndarray)):
        raise ValueError("Input must be a list or np.ndarray.")

    # Check if all elements in the list are numeric (int or float)
    if not all(isinstance(i, (int, float, complex, np.int16)) for i in input_data):
        raise ValueError("All elements of the list or np.ndarray must be numeric values (int or float or complex).")

    # Input cannot be empty
    if (len(input_data)<=0):
        raise ValueError("Input cannot be empty sequence")

    # Valid input
    return 1

def import_audio(a_from, a_to, a_path):
    try:
        samp_rate, x = wavfile.read(a_path)
        from_sec = a_from
        to_sec = a_to
        x = x[(int)(from_sec*samp_rate):(int)(to_sec*samp_rate)]
        return x
    except:
        raise ValueError("Problem encountered while loading the audio file...")

def import_audio_n_samples(a_from, n, a_path):
    try:
        samp_rate, x = wavfile.read(a_path)
        from_sec = a_from
        x = x[(int)(from_sec*samp_rate):(n+(int)(from_sec*samp_rate))]
        return x
    except:
        raise ValueError("Problem encountered while loading the audio file...")

#   v1.0.0  @author Amila Čengić
#           @date   09.12.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Denin Mehanović
#           @date   23.12.2024.
#           @change Dodane funkcije za import signala
