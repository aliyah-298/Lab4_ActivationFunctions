import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

st.write("""
The Hyperbolic Tangent (Tanh) function is defined as:
f(x) = tanh(x)
""")

# Input range
x = np.linspace(-10, 10, 100)
y = np.tanh(x)

# Plot
plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.title("Tanh Activation Function")
plt.grid(True)

st.pyplot(plt)
