'''
Implementacija diskretne Fourier-ove transformacije
'''

import cmath

def m_dft(x):
    '''
    Računa diskretnu Furier-ovu transformaciju (DFT) signala x.
    :param x: Niz tipa list ili array vrijednosti signala u vremenskom domenu
    :return: Lista kompleksnih vrijednosti u frekventnom domenu.
    '''
    N = len(x)
    X = []

    for k in range(N):
        #Izračunaj sumu k-te komponente frekvencije
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