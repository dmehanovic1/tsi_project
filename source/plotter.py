'''
Modul za vizualizaciju
'''
import numpy as np
import matplotlib.pyplot as plt

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