'''
Pokretač svih testova
'''
import pytest

def run_tests():
    pytest.main(["pt_DFT.py", "-v", "--color=yes"])
    pytest.main(["pt_FFT.py", "-v", "--color=yes"])

run_tests()

#   v1.0.0  @author Denin Mehanović
#           @date   03.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Denin Mehanović
#           @date   17.11.2024.
#           @change Dodano pokretanje testova definiranih u pt_DFT.py

#   v1.0.2  @author Amila Čengić
#           @date   09.12.2024
#           @change Dodano pokretanje testova definiranih u pt_FFT.py i formatiran ispis izlaza pytest-a
