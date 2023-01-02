from matplotlib import pyplot
import numpy as np

# DRAW PLOTS WITH PYPLOT
x = np.linspace(0, 2*np.pi, num=1000)
sinx = np.sin(x)

pyplot.plot(x, sinx)
pyplot.show() # necessary when executing from command line

s = np.linspace(-10, 10, num=50)
x, y = np.meshgrid(s, s)
z = x**2 + 2*y**2 + 30*x
pyplot.imshow(z)
pyplot.colorbar()
pyplot.show()

# with additional tools I could draw 3D chart..

import imageio # I/O between numpy matrices and images
img = imageio.imread('base/had.png')
pyplot.imshow(img)
pyplot.show()

img.shape # (128, 128, 4) is height, width, color channels

# I can also process sounds into matrices using import scipy.io.wavfile
# and then do Fourier transform or something using numpy.fft.fftfreq
