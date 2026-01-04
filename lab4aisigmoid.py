import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")

st.write("""
The Sigmoid function is defined as:
f(x) = 1 / (1 + e^(-x))
""")

# Input range
x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

# Plot
plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.title("Sigmoid Activation Function")
plt.grid(True)

st.pyplot(plt)
