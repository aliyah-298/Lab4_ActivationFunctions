import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

st.write("""
The Rectified Linear Unit (ReLU) is defined as:
f(x) = max(0, x)
""")

# Input range
x = np.linspace(-10, 10, 100)
y = np.maximum(0, x)

# Plot
plt.figure()
plt.plot(x, y)
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.title("ReLU Activation Function")
plt.grid(True)

st.pyplot(plt)
