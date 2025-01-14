'''
Visualisation module
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def m_3dplot(X):
    '''
    Creates 3D graph representing the results of DFT/FFT. It shows magnitude and phase as functions of frequency.

    Parameters:
    :param X: Frequency domain samples of signal which is result of performing DFT/FFT.

    Returns:
    :return: None

    Example:
    >>> m_3dplot([1+1j,2,1,2])
    '''
    N = len(X)
    freqs = np.fft.fftfreq(N)
    magnitude = np.abs(X)
    phase = np.angle(X)

    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')

    scatter = ax.scatter(freqs, magnitude, phase, c=magnitude, cmap='viridis', s=50)
    fig.colorbar(scatter, ax=ax, label='Magnitude')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Magnitude')
    ax.set_zlabel('Phase (radians)')
    plt.title('3D representation of DFT')
    plt.show()

def m_plot3(t, x, X):
    '''
    Creates graphs of signal in time domain, magnitude and phase in frequency domain.

    Parameters:
    :param t: time samples
    :param x: signal samples in time domain
    :param X: singal samples in frequency domain

    Returns:
    :return: None
    '''
    magnitude = np.abs(X)
    phase = np.angle(X)
    freqs = np.fft.fftfreq(len(t), d=(t[1]-t[0]))

    fig, axes = plt.subplots(3, 1, figsize=(10,8))
    axes[0].plot(t, x, color = 'blue')
    axes[0].set_title("Signal u vremenskom domenu")
    axes[0].set_xlabel("Vrijeme [s]")
    axes[0].set_ylabel("Amplituda [-]")

    axes[1].stem(freqs, magnitude, 'red', markerfmt = ".", basefmt = "-r")
    axes[1].set_title("Magnituda u frekventnom domenu")
    axes[1].set_xlabel("Frekvencija [Hz]")
    axes[1].set_ylabel("Magnituda [-]")

    axes[2].stem(freqs, phase, 'green', markerfmt = ".", basefmt = "-g")
    axes[2].set_title("Faza u frekventnom domenu")
    axes[2].set_xlabel("Frekvencija [Hz]")
    axes[2].set_ylabel("Faza [rad]")

    plt.tight_layout()
    plt.show()

def m_plot_v2(t, x, X):
    '''
    Creates graphs of signal in time and frequency domain (real and imaginary parts), magnitude and phase in frequency domain.

    Parameters:
    :param t: time samples
    :param x: signal samples in time domain
    :param X: singal samples in frequency domain

    Returns:
    :return: xreal, ximag, Xreal, Ximag, magnitude, phase, freqs
    '''
    magnitude = np.abs(X)
    phase = np.angle(X)
    freqs = np.fft.fftfreq(len(t), d=(t[1]-t[0]))

    xreal = [z.real for z in x]
    ximag = [z.imag for z in x]
    Xreal = [z.real for z in X]
    Ximag = [z.imag for z in X]

    fig, axes = plt.subplots(2, 3, figsize=(15,10))

    axes[0, 0].stem(t, xreal)
    axes[0, 0].set_title("Signal u vremenskom domenu (realni dio)")
    axes[0, 0].set_xlabel("Broj uzorka")
    axes[0, 0].set_ylabel("Amplituda [-]")

    axes[1, 0].stem(t, ximag)
    axes[1, 0].set_title("Signal u vremenskom domenu (kompleksni dio)")
    axes[1, 0].set_xlabel("Broj uzorka")
    axes[1, 0].set_ylabel("Amplituda [-]")

    axes[0, 1].stem(freqs, Xreal)
    axes[0, 1].set_title("Signal u frekventnom domenu (realni dio)")
    axes[0, 1].set_xlabel("Frekvencija [Hz]")
    axes[0, 1].set_ylabel("Amplituda [-]")

    axes[1, 1].stem(freqs, Ximag)
    axes[1, 1].set_title("Signal u frekventnom domenu (kompleksni dio)")
    axes[1, 1].set_xlabel("Frekvencija [Hz]")
    axes[1, 1].set_ylabel("Amplituda [-]")

    axes[0, 2].stem(freqs, magnitude, 'red', markerfmt = ".", basefmt = "-r")
    axes[0, 2].set_title("Magnituda u frekventnom domenu")
    axes[0, 2].set_xlabel("Frekvencija [Hz]")
    axes[0, 2].set_ylabel("Magnituda [-]")

    axes[1, 2].stem(freqs, phase, 'green', markerfmt = ".", basefmt = "-g")
    axes[1, 2].set_title("Faza u frekventnom domenu")
    axes[1, 2].set_xlabel("Frekvencija [Hz]")
    axes[1, 2].set_ylabel("Faza [rad]")

    plt.tight_layout()
    plt.show()
    return xreal, ximag, Xreal, Ximag, magnitude, phase, freqs

def plot_hdf5(xreal, ximag, Xreal, Ximag, magnitude, phase, freqs, t):
    '''
    Creates graphs of signal in time and frequency domain (real and imaginary parts), magnitude and phase in frequency domain.

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
    fig, axes = plt.subplots(2, 3, figsize=(15,10))

    axes[0, 0].stem(t, xreal)
    axes[0, 0].set_title("Signal u vremenskom domenu (realni dio)")
    axes[0, 0].set_xlabel("Broj uzorka")
    axes[0, 0].set_ylabel("Amplituda [-]")

    axes[1, 0].stem(t, ximag)
    axes[1, 0].set_title("Signal u vremenskom domenu (kompleksni dio)")
    axes[1, 0].set_xlabel("Broj uzorka")
    axes[1, 0].set_ylabel("Amplituda [-]")

    axes[0, 1].stem(freqs, Xreal)
    axes[0, 1].set_title("Signal u frekventnom domenu (realni dio)")
    axes[0, 1].set_xlabel("Frekvencija [Hz]")
    axes[0, 1].set_ylabel("Amplituda [-]")

    axes[1, 1].stem(freqs, Ximag)
    axes[1, 1].set_title("Signal u frekventnom domenu (kompleksni dio)")
    axes[1, 1].set_xlabel("Frekvencija [Hz]")
    axes[1, 1].set_ylabel("Amplituda [-]")

    axes[0, 2].stem(freqs, magnitude, 'red', markerfmt = ".", basefmt = "-r")
    axes[0, 2].set_title("Magnituda u frekventnom domenu")
    axes[0, 2].set_xlabel("Frekvencija [Hz]")
    axes[0, 2].set_ylabel("Magnituda [-]")

    axes[1, 2].stem(freqs, phase, 'green', markerfmt = ".", basefmt = "-g")
    axes[1, 2].set_title("Faza u frekventnom domenu")
    axes[1, 2].set_xlabel("Frekvencija [Hz]")
    axes[1, 2].set_ylabel("Faza [rad]")

    plt.tight_layout()
    plt.show()

#   v1.0.0  @author Denin Mehanović
#           @date   18.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Denin Mehanović
#           @date   19.11.2024.
#           @change Dodan docstrings na nivou modula

#   v1.0.2  @author Denin Mehanović
#           @date   24.12.2024.
#           @change 3d plot funkcija