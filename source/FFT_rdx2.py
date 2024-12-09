'''
Implementation of Fast Fourier Transform (FFT) (radix 2)
'''
import cmath
import numpy as np
from tsi_project.source.common import *

def _is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

def m_fft_rdx2(x):
    '''
    Calculates the Fast Fourier Transform (FFT radix 2) of a signal x.

    Parameters:
    x (list): A list or array of signal values in the time domain

    Returns:
    list: A list of complex values in the frequency domain.

    Example of function usage:
    m_fft_rdx2([1,0,-1,1])
    '''

    check_input(x)

    N = len(x)

    if (not(_is_power_of_2(N))):
        raise ValueError("Error: Sequence length is not a power of 2.")

    if N <= 1:
        return x

    # Split the array into even and odd indices
    even = m_fft_rdx2(x[::2])  # Even index elements
    odd = m_fft_rdx2(x[1::2])  # Odd index elements

    # Initialize twiddle
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]

    # Combine the results
    result = [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

    return result



#   v1.0.0  @author Denin Mehanović
#           @date   03.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Amila Čengić
#           @date   09.12.2024.
#           @change Implementiran FFT_rdx2
