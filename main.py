import streamlit as st
from Fractal import *

def uncheckBox(key):
    st.session_state[key] = False

def callPlot():
    if julia_selected:
        output = julia(mesh, c=julia_c, num_iter=julia_iterations, radius=julia_radius)  # FIX: pass c
        kwargs = {'title': julia_title}
    else:
        output = mandelbrot(mesh, num_iter=mandelbrot_iterations, radius=mandelbrot_radius)  # FIX: pass settings
        kwargs = {'title': mandelbrot_title}

    fig = plot_fractal(output, **kwargs)
    st.pyplot(fig)

st.header("Simple Fractal Visualizer", text_alignment='center')

l1, m1, m2, r1 = st.columns(4)

with m1:
    julia_selected = st.checkbox("Julia's Set", key='julia_check', on_change=uncheckBox, args=['mandelbrot_check'], value=True)  # FIX: renamed variable

with m2:
    mandelbrot_selected = st.checkbox("Mandelbrot's Set", key='mandelbrot_check', on_change=uncheckBox, args=['julia_check'])  # FIX: renamed variable

if julia_selected:
    st.subheader("Julia's Set", text_alignment='center')
    julia_title = st.text_input("Title", value="Julia's Set")
    julia_c = st.number_input("Value of 'c'", value=-1.0)
    julia_iterations = st.number_input("Number of iterations", min_value=1, value=10, step=1)  # FIX: positive integer
    julia_radius = st.number_input("Radius", min_value=0.1, value=2.0)  # FIX: positive radius

if mandelbrot_selected:
    st.subheader("Mandelbrot's Set", text_alignment='center')
    mandelbrot_title = st.text_input("Title", value="Mandelbrot's Set")
    mandelbrot_iterations = st.number_input("Number of iterations", min_value=1, value=10, step=1)  # FIX: positive integer
    mandelbrot_radius = st.number_input("Radius", min_value=0.1, value=2.0)  # FIX: positive radius

with st.container(horizontal_alignment='center'):
    if st.button("Generate Fractal"):
        callPlot()
