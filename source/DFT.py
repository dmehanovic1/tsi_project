'''
Implementation of the Discrete Fourier Transform (DFT)
'''

import cmath
from tsi_project.source.common import *

def m_dft(x):
    '''
    Calculates the Discrete Fourier Transform (DFT) of a signal x.

    Parameters:
    x (list): A list or array of signal values in the time domain

    Returns:
    list: A list of complex values in the frequency domain.

    Example of function usage:
    m_dft([1,0,-1,1])
    '''

    check_input(x)

    N = len(x)

    X = []

    for k in range(N):
        #Calculate the sum of the k-th frequency component
        sum = 0
        for n in range (N):
            sum += x[n] * cmath.exp(-2j*cmath.pi*k*n/N)
        X.append(sum)

    return X

#   v1.0.0  @author Denin Mehanović
#           @date   03.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Denin Mehanović
#           @date   17.11.2024.
#           @change Implementirana funkcija m_dft

#   v1.0.2  @author Denin Mehanović
#           @date   18.11.2024.
#           @change Uklonjen nepotrebni import

#   v1.0.3  @author Amila Čengić
#           @date   20.11.2024.
#           @change Prevedeni opisi na engleski jezik i dodan primjer pozivanja

#   v1.0.4  @author Amila Čengić
#           @date   09.12.2024.
#           @change Dorađen docstrings
