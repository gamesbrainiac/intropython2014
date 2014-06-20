# encoding=utf-8
# Created by quazinafiulislam

import numpy as np
import scipy.fftpack as fft

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def func(t, freqs):
    return sum(np.sin(2.0 * np.pi * f * t) for f in freqs)


N = 4096  # Number of data points
freqs = (1.0, 2.0, 5.0)  # Initial frequencies

# Time domain data
t = np.linspace(0, 10, N)
y_t = func(t, freqs)

# Frequency domain data
dt = t[1] - t[0]
f = fft.fftfreq(N, dt)
y_f = abs(fft.fft(y_t))

# Params for slider positions
left, bottom, width, height = 0.1, 0.02, 0.8, 0.03
shift = height + 0.02

# Plotting the data initially.
fig, (tax, fax) = plt.subplots(nrows=2)

for ax in (tax, fax):
    ax.grid(True)

plt.subplots_adjust(left=left, bottom=0.25)

tp, = tax.plot(t, y_t)
fp, = fax.plot(f, y_f, 'r-')

tax.set_xlabel('Time')
tax.set_ylabel('y(t)')

fax.set_xlabel('Frequency')
fax.set_ylabel('Y(f)')

fax.set_xlim(0, 10)
fax.set_ylim(y_f.min(), y_f.max())

# matplotlib axes objects to hold the sliders
slider_axes = [plt.axes([left, bottom + i * shift, width, height]) for i in range(len(freqs))]

# matplotlib sliders to change the frequency in real time.
sliders = [Slider(ax, s, valmin=0.1, valmax=10.0, valinit=f)
           for ax, f, s in zip(slider_axes, freqs, ['3', '2', '1'])]


def update(val):
    # Function to be ran whenever the sliders are changed.
    freqs = [slider.val for slider in sliders]

    y_t = func(t, freqs)
    y_f = abs(fft.fft(y_t))

    tp.set_ydata(y_t)
    fp.set_ydata(y_f)

    fax.set_ylim(y_f.min(), y_f.max())

    fig.canvas.draw_idle()

# Set each slider to run update when changed.
for slider in sliders:
    slider.on_changed(update)

plt.show()