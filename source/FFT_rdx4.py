'''
Implementation of Fast Fourier Transform (FFT) (radix 4)
'''
import cmath
import numpy as np
from tsi_project.source.common import *

def _is_power_of_4(n):
    '''
    Internal function that checks if the input number is the power of 4.
    '''
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

def fft_base_case(x):
    '''
    Internal function that returns base case for FFT radix 4.
    '''
    N = len(x)
    if N == 1:
        return x
    if N == 2:
        return np.array([x[0] + x[1], x[0] - x[1]])
    if N == 3:
        return np.array([x[0] + x[1] + x[2],
                         x[0] + x[1] * np.exp(-2j * np.pi / 3) + x[2] * np.exp(-4j * np.pi / 3),
                         x[0] + x[1] * np.exp(-4j * np.pi / 3) + x[2] * np.exp(-2j * np.pi / 3)])

    if N == 4:
        # Simple DFT for size 4
        return np.array([x[0] + x[1] + x[2] + x[3],
                         x[0] + x[1] * np.exp(-2j * np.pi / 4) + x[2] * np.exp(-4j * np.pi / 4) + x[3] * np.exp(
                             -6j * np.pi / 4),
                         x[0] + x[1] * np.exp(-4j * np.pi / 4) + x[2] * np.exp(-8j * np.pi / 4) + x[3] * np.exp(
                             -12j * np.pi / 4),
                         x[0] + x[1] * np.exp(-6j * np.pi / 4) + x[2] * np.exp(-12j * np.pi / 4) + x[3] * np.exp(
                             -18j * np.pi / 4)])

def m_fft_rdx4(x):
    '''
    Calculates the Fast Fourier Transform (FFT radix 4) of a signal x.

    Parameters:
    x (list): A list or array of signal values in the time domain

    Returns:
    list: A list of complex values in the frequency domain.

    Example:
    >>> m_fft_rdx4([1,0,-1,1])
    '''

    check_input(x)

    N = len(x)

    if (not(_is_power_of_4(N))):
        raise ValueError("Error: Sequence length is not a power of 4.")

    if N <= 4:
        return fft_base_case(x)

    # Split the input into 4 parts
    x0 = x[0::4]  # Every 4th element starting from index 0
    x1 = x[1::4]  # Every 4th element starting from index 1
    x2 = x[2::4]  # Every 4th element starting from index 2
    x3 = x[3::4]  # Every 4th element starting from index 3

    # Recursively compute the FFT for each part
    fft_x0 = m_fft_rdx4(x0)
    fft_x1 = m_fft_rdx4(x1)
    fft_x2 = m_fft_rdx4(x2)
    fft_x3 = m_fft_rdx4(x3)

    # Combine the results
    W4 = np.exp(-2j * np.pi / N * np.arange(N // 4))
    result = np.zeros(N, dtype=complex)

    for k in range(N // 4):
        W0 = np.exp(-2j * np.pi * k / N)
        W1 = np.exp(-2j * np.pi * 2 * k / N)
        W2 = np.exp(-2j * np.pi * 3 * k / N)
        W3 = np.exp(-2j * np.pi * 4 * k / N)

        result[k] = fft_x0[k] + W0 * fft_x1[k] + W1 * fft_x2[k] + W2 * fft_x3[k]
        result[k + N // 4] = fft_x0[k] + W1 * fft_x1[k] + W2 * fft_x2[k] + W3 * fft_x3[k]
        result[k + N // 2] = fft_x0[k] + W2 * fft_x1[k] + W3 * fft_x2[k] + W0 * fft_x3[k]
        result[k + 3 * N // 4] = fft_x0[k] + W3 * fft_x1[k] + W0 * fft_x2[k] + W1 * fft_x3[k]

    return result


#   v1.0.0  @author Denin Mehanović
#           @date   03.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Amina Omerčević
#           @date   09.12.2024.
#           @change Implementiran FFT_rdx4

#   v1.0.2  @author Denin Mehanović
#           @date   23.12.2024.
#           @change Proširen base case