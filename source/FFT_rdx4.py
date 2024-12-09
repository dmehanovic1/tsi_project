'''
Implementation of Fast Fourier Transform (FFT) (radix 4)
'''
import cmath
import numpy as np
from tsi_project.source.common import *

def _is_power_of_4(n):
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

def m_fft_rdx4(x):
    '''
    Calculates the Fast Fourier Transform (FFT radix 4) of a signal x.

    Parameters:
    x (list): A list or array of signal values in the time domain

    Returns:
    list: A list of complex values in the frequency domain.

    Example of function usage:
    m_fft_rdx4([1,0,-1,1])
    '''

    check_input(x)

    N = len(x)

    if (not(_is_power_of_4(N))):
        raise ValueError("Error: Sequence length is not a power of 4.")

    if N <= 1:
        return x

    # Split the input into four parts
    x0 = m_fft_rdx4(x[::4])  # Elements at indices 0, 4, 8, ...
    x1 = m_fft_rdx4(x[1::4])  # Elements at indices 1, 5, 9, ...
    x2 = m_fft_rdx4(x[2::4])  # Elements at indices 2, 6, 10, ...
    x3 = m_fft_rdx4(x[3::4])  # Elements at indices 3, 7, 11, ...

    # Twiddle factors for N=4
    W = [np.exp(-2j * np.pi * k / N) for k in range(N // 4)]

    # Initialize the output array
    result = [0] * N

    # Combine the results from the four parts
    for k in range(N // 4):
        w0 = W[k] * x1[k]
        w1 = W[2 * k] * x2[k]
        w2 = W[3 * k] * x3[k]

        # Compute the FFT values for each section
        result[k] = x0[k] + w0 + w1 + w2
        result[k + N // 4] = x0[k] - w0 + w1 - w2
        result[k + N // 2] = x0[k] + w0 - w1 - w2
        result[k + 3 * N // 4] = x0[k] - w0 - w1 + w2

    return result


#   v1.0.0  @author Denin Mehanović
#           @date   03.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Amina Omerčević
#           @date   09.12.2024.
#           @change Implementiran FFT_rdx4
