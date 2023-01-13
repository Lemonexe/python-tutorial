from matplotlib import pyplot as plt
import numpy as np

# DRAW PLOTS WITH PYPLOT
# normal R -> R plot
x = np.linspace(0, 2*np.pi, num=1000)
sinx = np.sin(x)

plt.plot(x, sinx)
plt.show() # necessary when executing from command line


# draw on secondary axis
y2 = 120 + 60*np.cos(x*2.6)
f = 180/np.pi # conversion factor

fig, ax = plt.subplots() # figure object, axes object
ax.plot(x*f, sinx, 'k-') # draw on primary axis (black line)
ax2 = ax.twinx() # make a twin axis object sharing the same X axis
ax2.plot(x*f, y2, 'r--') # draw on secondary axis (green dashed)
# decorations...
ax.set_xlim(0, 360) # x range
ax.set_ylim(-1, 1) # y range
ax2.set_ylim(0, 200) # y2 range
ax.set_xlabel('angle [°C]')
ax.set_ylabel('x', color='k')
ax2.set_ylabel('T [°C]', color='r')
plt.title('weird reactor')
plt.show()



# DRAW R^2 -> R
s = np.linspace(-10, 10, num=50)
x, y = np.meshgrid(s, s)
z = x**2 + 2*y**2 + 30*x
plt.imshow(z)
plt.colorbar()
plt.show()
# with additional tools I could draw 3D chart..


# DRAW AN IMAGE
import imageio # I/O between numpy matrices and images
img = imageio.imread('base/had.png')
plt.imshow(img)
plt.show()

img.shape # (128, 128, 4) is height, width, color channels

# I can also process sounds into matrices using import scipy.io.wavfile
# and then do Fourier transform or something using numpy.fft.fftfreq
