'''
Testovi FFT modula
'''
import pytest
import cmath
import numpy as np
import inspect
from tsi_project.source.FFT_rdx2 import *
from tsi_project.source.FFT_rdx4 import *
from tsi_project.source.common import *

def test_1a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1,1,1,1]
    result = m_fft_rdx2(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_1b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1,1,1,1]
    result = m_fft_rdx4(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_2a():
    test_name = inspect.currentframe().f_code.co_name
    x = [0,0,0,0]
    result = m_fft_rdx2(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_2b():
    test_name = inspect.currentframe().f_code.co_name
    x = [0,0,0,0]
    result = m_fft_rdx4(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_3a():
    test_name = inspect.currentframe().f_code.co_name
    x = []
    try:
        result = m_fft_rdx2(x)
    except ValueError as e:
        assert ValueError("Input cannot be empty sequence")

def test_3b():
    test_name = inspect.currentframe().f_code.co_name
    x = []
    try:
        result = m_fft_rdx4(x)
    except ValueError as e:
        assert ValueError("Input cannot be empty sequence")

def test_4a():
    test_name = inspect.currentframe().f_code.co_name
    x = 6
    try:
        result = m_fft_rdx2(x)
    except ValueError as e:
        assert ValueError("Input must be a list or np.ndarray.")

def test_4b():
    test_name = inspect.currentframe().f_code.co_name
    x = 6
    try:
        result = m_fft_rdx4(x)
    except ValueError as e:
        assert ValueError("Input must be a list or np.ndarray.")

def test_5a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1, "kla", 2, 4]
    try:
        result = m_fft_rdx2(x)
    except ValueError as e:
        assert ValueError("All elements of the list or np.ndarray must be numeric values (int or float or complex).")

def test_5b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1, "kla", 2, 4]
    try:
        result = m_fft_rdx4(x)
    except ValueError as e:
        assert ValueError("All elements of the list or np.ndarray must be numeric values (int or float or complex).")

def test_6a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1, "kla", 2, 4]
    try:
        result = m_fft_rdx2(x)
    except ValueError as e:
        if e == ValueError("Error: Sequence length is not a power of 2."):
            assert ValueError("Error: Sequence length is not a power of 2.")

def test_6b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1, "kla", 2, 4, 5]
    try:
        result = m_fft_rdx4(x)
    except ValueError as e:
        if e == ValueError("Error: Sequence length is not a power of 4."):
            assert ValueError("Error: Sequence length is not a power of 4.")

def test_7a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1,2,3,4]
    result = m_fft_rdx2(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_7b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1,2,3,4]
    result = m_fft_rdx4(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_8a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j]
    result = m_fft_rdx2(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_8b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j]
    result = m_fft_rdx4(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_9a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1,2,3]
    try:
        result = m_fft_rdx2(x)
    except ValueError as e:
        if e == ValueError("Error: Sequence length is not a power of 2."):
            assert ValueError("Error: Sequence length is not a power of 2.")

def test_9b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1,2,3]
    try:
        result = m_fft_rdx4(x)
    except ValueError as e:
        if e == ValueError("Error: Sequence length is not a power of 4."):
            assert ValueError("Error: Sequence length is not a power of 4.")

def test_10a():
    test_name = inspect.currentframe().f_code.co_name
    x = [1]
    result = m_fft_rdx2(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_10b():
    test_name = inspect.currentframe().f_code.co_name
    x = [1]
    result = m_fft_rdx4(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_audio1():
    test_name = inspect.currentframe().f_code.co_name
    seq = import_audio(1,1.1,"C:/Workspace/TKM/TKM1/TSI/Projekt/venv/tsi_project/media/StarWars60.wav")
    for r, e in zip(seq, seq):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_audio2():
    test_name = inspect.currentframe().f_code.co_name
    try:
        seq = import_audio(1, 1.1, "./media/Stars60.wav")
    except Exception as e:
        if e == ValueError("Problem encountered while loading the audio file..."):
            assert ValueError("Problem encountered while loading the audio file...")

#   v1.0.0  @author Amina Omerčević
#           @date   09.12.2024.
#           @change Inicijalna verzija
