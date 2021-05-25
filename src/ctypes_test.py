from ctypes import c_double, c_int, CDLL
import numpy as np
import time
import matplotlib.pyplot as plt
from numpy.ctypeslib import ndpointer
import ctypes

# loading the library
c_lib = CDLL("/Users/moham/Desktop/Mixer-DSP/src/test2.dll")

ft = c_lib.dft
fft=c_lib.fft

ft.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ctypes.c_int]

fft.argtypes =[ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),ctypes.c_int]

signal_length=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
execution_time_dft = []
execution_time_fft = []
error = []
for i in signal_length:
    #filling input array
    main_input = np.arange(i)
    samples = len(main_input)
    
    #preparing arguments
    zero =np.zeros(samples)
    dft_input = np.column_stack((main_input, zero))
    dft_output= np.column_stack((main_input, zero))
    fft_input = np.column_stack((main_input, zero))
    
    #dft
    start1 = time.time()
    ft(dft_input, dft_output, samples)
    end1 = time.time()
    execution_time_dft.append(end1-start1)
    
    #fft
    start2 = time.time()
    fft(fft_input, samples) 
    end2 = time.time()
    execution_time_fft.append(end2-start2)
    
    #calc error
    # mean_error= np.subtract(dft_output, fft_input)
    mean_error= np.square(np.subtract(dft_output, fft_input)).mean()
    
    error.append(mean_error)


#plotting Complexities



plt.subplot(221)
plt.ylabel('execution_time')
plt.xlabel('signal_length')
plt.plot(signal_length, execution_time_dft)
plt.plot(signal_length,execution_time_fft)
plt.subplot(222)
plt.xlabel('signal_length')
plt.ylabel('execution_time')
plt.title("DFT")
plt.plot(signal_length, execution_time_dft)
plt.subplot(223)
plt.xlabel('signal_length')
plt.ylabel('execution_time')
plt.title("FFT")
plt.ylim(0,0.2)
plt.plot(signal_length,execution_time_fft)


#plotting errors
plt.subplot(224)
plt.plot(signal_length,error)
plt.xlabel('signal_length')
plt.ylabel('Error')
plt.title("Error")
plt.show()


