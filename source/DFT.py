'''
Implementation of the Discrete Fourier Transform (DFT)
'''

import cmath

def m_dft(x):
    '''
    Calculates the Discrete Fourier Transform (DFT) of a signal x.
    :param x: A list or array of signal values in the time domain
    :return: A list of complex values in the frequency domain.

    Example of function usage:
        signal = [1, 0, -1, 0]  # Define the input signal
        result = m_dft(signal)  # Call the function to compute the DFT
    '''
    
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
