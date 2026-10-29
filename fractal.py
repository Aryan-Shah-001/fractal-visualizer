import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def julia(mesh, c=-1, num_iter=10, radius=2):
    z = mesh.copy()
    diverge_len = np.zeros(z.shape)

    for i in range(num_iter):
        conv_mask = np.abs(z) < radius
        z[conv_mask] = np.square(z[conv_mask]) + c
        diverge_len[conv_mask] += 1

    return diverge_len

def mandelbrot(mesh, num_iter=10, radius=2):
    c = mesh.copy()
    z = np.zeros(mesh.shape, dtype=np.complex128)
    diverge_len = np.zeros(z.shape)

    for i in range(num_iter):
        conv_mask = np.abs(z) < radius
        z[conv_mask] = np.square(z[conv_mask]) + c[conv_mask]
        diverge_len[conv_mask] += 1

    return diverge_len

def plot_fractal(fractal, title='Fractal', figsize=(6, 6), cmap='rainbow', extent=[-2, 2, -2, 2]):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title)  # FIX: ordinary title, no math formatting
    ax.set_xlabel('Real axis')
    ax.set_ylabel('Imaginary axis')
    im = ax.imshow(fractal, extent=extent, cmap=cmap)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    fig.colorbar(im, cax=cax, label='Number of iterations')
    return fig  # FIX: return figure for Streamlit instead of plt.show()

x, y = np.meshgrid(np.linspace(-2, 2, 400), np.linspace(-2, 2, 400))
mesh = x + (1j * y)
