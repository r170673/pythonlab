import scipy.io
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile
w=np.arange(-np.pi,np.pi,0.001*np.pi)
F=100
Fs=500
#x=[1,2,3,4,5]
Fs,x=scipy.io.wavfile.read("no-1.wav")
print(Fs)
#x=x[:,0]
print(x.shape)
l=len(x)
X=[]
for i in range(0,len(w)):
	s=0
	for n in range(0,l):
		s=s+x[n]*np.exp(-1*1j*w[i]*n)
	X.append(s)

plt.title("DTFT Magnitude Spectra")
plt.stem(w,np.abs(X))

plt.show()	
