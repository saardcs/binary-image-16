import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Binary Decoder Activity", layout="wide")
st.title("🧠 Binary Decoder Activity")

st.markdown("""
You're given 8 rows to fill in. For each row, enter **two numbers between 0–15**.  
Each number will be converted to 4-bit binary and combined to form a full 8-bit row.  
Your inputs will reveal a hidden image!
""")

st.sidebar.header("Your Binary Inputs")
binary_inputs = []

for i in range(8):
    col1, col2 = st.sidebar.columns(2)
    with col1:
        val1 = st.number_input(f"Row {i+1} - Part 1", min_value=0, max_value=15, step=1, key=f"row_{i}_1")
    with col2:
        val2 = st.number_input(f"Row {i+1} - Part 2", min_value=0, max_value=15, step=1, key=f"row_{i}_2")
    
    # Convert both numbers to 4-bit binary and combine
    binary_row = format(val1, '04b') + format(val2, '04b')
    binary_inputs.append(binary_row)

if st.sidebar.button("Show Image"):
    binary_grid = []
    for bin_input in binary_inputs:
        binary_grid.append([int(bit) for bit in bin_input])

    # Create a 2D NumPy array from the binary grid
    image_array = np.array(binary_grid)

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(image_array, cmap='Greys', vmin=0, vmax=1)
    ax.set_xticks([])
    ax.set_yticks([])
    st.pyplot(fig)
