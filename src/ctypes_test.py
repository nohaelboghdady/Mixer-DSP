from ctypes import c_double, c_int
import numpy as np
import time
import matplotlib.pyplot as plt
from numpy.ctypeslib import ndpointer
import ctypes
import os

# loading the library
c_lib = ctypes.CDLL("./test.dll")

ft = c_lib.dft
fft=c_lib.fft

ft.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ctypes.c_int]

fft.argtypes =[ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),ctypes.c_int]

signal_length = []
execution_time_dft = []
execution_time_fft = []
error = []
count = 0
while count < 1000:
    count += 10
    #filling input array
    signal_length.append(count)
    main_input = np.arange(count)
    samples = len(main_input)
    
    #preparing arguments
    zero =np.zeros(samples)
    dft_input = np.column_stack((main_input, zero))
    fft_input = np.column_stack((main_input, zero))
    
    #dft
    start1 = time.time()
    ft(dft_input, samples)
    end1 = time.time()
    execution_time_dft.append(end1-start1)
    
    #fft
    start2 = time.time()
    fft(fft_input, samples) 
    end2 = time.time()
    execution_time_fft.append(end2-start2)
    
    #calc error
    mean_error= np.square(np.subtract(dft_input, fft_input)).mean()
    error.append(mean_error)

#plotting Complexities
plt.subplot(211)
plt.plot(signal_length, execution_time_dft)
plt.ylabel('execution_time')
plt.plot(signal_length,execution_time_fft)


#plotting errors
plt.subplot(212)
plt.plot(signal_length,error)
plt.xlabel('signal_length')
plt.ylabel('Error')

plt.show()


