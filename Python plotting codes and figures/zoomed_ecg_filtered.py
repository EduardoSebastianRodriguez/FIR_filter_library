import numpy as np
import matplotlib.pyplot as mpl

input=np.loadtxt('ecg_filtered.dat')
print(input)

mpl.plot(input[80300:81300])
mpl.title('Zoomed filtered ECG ')
mpl.xlabel('time(ms)')
mpl.ylabel('amplitude (mV)')
mpl.savefig('zoomed_ecg_filtered.pdf')
