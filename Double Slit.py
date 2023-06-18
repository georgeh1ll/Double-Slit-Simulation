import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def calculate_intensity(s_width, w_length, s_distance, d_slits, x_vals):
    return (((np.sin((np.pi * s_width * x_vals) / (w_length * s_distance))) / ((np.pi * s_width * x_vals) / (w_length * s_distance))) ** 2) * ((np.cos((np.pi * d_slits * x_vals) / (w_length * s_distance))) ** 2)

x_vals = np.arange(-0.005, 0.005, 0.00001)
slit_width = 100 * (10 ** -6)
wavelength = 500 * (10 ** -9)
screen_distance = 50 * (10 ** -2)
distance_between_slits = 1 * 10 ** -3

y_vals = calculate_intensity(slit_width, wavelength, screen_distance, distance_between_slits, x_vals)
plot, = plt.plot(x_vals, y_vals,color='red')
plt.xlabel("Distance from center")
plt.ylabel("Intensity")
plt.title("Double Slit Intensity Simulation")

wavelength_slider_ax = plt.axes([0.25, 0, 0.15, 0.05])
slit_width_slider_ax = plt.axes([0.75, 0, 0.15, 0.05])
screen_distance_slider_ax = plt.axes([0.75, 0.03, 0.15, 0.05])
distance_between_slits_slider_ax = plt.axes([0.25, 0.03, 0.15, 0.05])

wavelength_slider = Slider(wavelength_slider_ax, 'Wavelength (nm)', 100, 1000, valinit=wavelength * 10 ** 9)
slit_width_slider = Slider(slit_width_slider_ax, "Slit Width (micrometers)", 10, 1000, valinit=slit_width * 10 ** 6)
screen_distance_slider = Slider(screen_distance_slider_ax, "Distance to Screen (cm)", 10, 100, valinit=screen_distance * 10 ** 2)
distance_between_slits_slider = Slider(distance_between_slits_slider_ax, "Distance b/w slits (mm)", 0.1, 10, valinit=distance_between_slits * 10 ** 3)

def update(val):
    wavelength = wavelength_slider.val * (10 ** -9)
    slit_width = slit_width_slider.val * (10 ** -6)
    screen_distance = screen_distance_slider.val * (10 ** -2)
    distance_between_slits = distance_between_slits_slider.val * (10 ** -3)
    y_vals = calculate_intensity(slit_width, wavelength, screen_distance, distance_between_slits, x_vals)
    plot.set_ydata(y_vals)

wavelength_slider.on_changed(update)
slit_width_slider.on_changed(update)
screen_distance_slider.on_changed(update)
distance_between_slits_slider.on_changed(update)

plt.show()
