'''
Visualisation module
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def m_3dplot(X):
    '''
    Creates 3D graph representing the results of DFT/FFT. It shows magnitude and phase as functions of frequency.
    :param X: Frequency domain samples of signal which is result of performing DFT/FFT.
    :return: None

    Example of usage: m_3dplot([1+1j,2,1,2])
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
    Kreira grafik signala u vremenskom domenu, magnitude signala u frekventnom domenu, te faze signala u
    frekventnom domenu.
    :param t: uzorci vremena
    :param x: uzorci signala u vremenskom domenu
    :param X: uzorci signala u frekventnom domenu
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
    axes[1].set_xlabel("Frekvecija [Hz]")
    axes[1].set_ylabel("Magnituda [-]")

    axes[2].stem(freqs, phase, 'green', markerfmt = ".", basefmt = "-g")
    axes[2].set_title("Faza u frekventnom domenu")
    axes[2].set_xlabel("Frekvecija [Hz]")
    axes[2].set_ylabel("Faza [rad]")

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