import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def f(z): return np.tan(np.square(z))

def g(z): return np.sin(f(z))

def h(z): return f(z) + g(z)

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

def general_julia(mesh, c=-1, f=np.square, num_iter=100, radius=2):

    z = mesh.copy()
    diverge_len = np.zeros(z.shape)

    for i in range(num_iter):
        conv_mask = np.abs(z) < radius
        z[conv_mask] = f(z[conv_mask]) + c
        diverge_len[conv_mask] += 1

    return diverge_len

def newton_fractal(mesh, f, df, num_iter=10, r=2):

    z = mesh.copy()
    diverge_len = np.zeros(z.shape)

    for i in range(num_iter):
        conv_mask = np.abs(z) < r
        pz = f(z[conv_mask])
        dp = df(z[conv_mask])
        z[conv_mask] = z[conv_mask] - pz/dp
        diverge_len[conv_mask] += 1

    return diverge_len

def f_tan(z): return np.square(np.tan(z))

def d_tan(z): return 2*np.tan(z) / np.square(np.cos(z))

def divergence_rate(mesh, num_iter=10, radius=2):

    z = mesh.copy()
    diverge_len = np.zeros(mesh.shape)  # Keep tally of the number of iterations

    # Iterate on element if and only if |element| < radius (Otherwise assume divergence)
    for i in range(num_iter):
        conv_mask = np.abs(z) < radius
        diverge_len[conv_mask] += 1
        z[conv_mask] = f(z[conv_mask])

    return diverge_len

x, y = np.meshgrid(np.linspace(-2, 2, 2000), np.linspace(-2, 2, 2000))
mesh = x + (1j * y)

def plot_fractal(fractal, title='Fractal', figsize=(6, 6), cmap='rainbow', extent=[-2, 2, -2, 2]):

    fig, ax = plt.subplots(figsize=figsize)

    ax.set_title(f'${title}$')
    ax.set_xlabel('Real axis')
    ax.set_ylabel('Imaginary axis')

    im = ax.imshow(fractal, extent=extent, cmap=cmap)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(im, cax=cax, label='Number of iterations')

output = julia(mesh, num_iter=10, radius=2)
kwargs = {'cmap' : 'binary', 'figsize': (7, 7), 'extent': [-1, 1, -1, 1]}

plot_fractal(output, **kwargs)

plt.show()