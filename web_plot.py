import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery

def main():
    st.title("Basic Graph Plotting App")

    mass_input = st.number_input("Enter desired stellar mass: ")
    mass = mass_input
    #mass = float(mass_input)
    metallicity_input = st.number_input("Enter desired stellar metallicity (positive): ")
    #metallicity = float(metallicity_input)
    metallicity = metallicity_input

    track = mistery.get_track(M=mass, FeH=metallicity)

    st.write("Select graph axes.")

    graph_x_axis = st.sidebar.selectbox(
        "Select x-axis",
        (track.dtype.names)
    )

    graph_y_axis = st.sidebar.selectbox(
        "Select y-axis",
        (track.dtype.names)
    )

    x_data = track[graph_x_axis]
    y_data = track[graph_y_axis]

    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(x_data, y_data)
    st.pyplot(fig)

    #return graph_x_axis, graph_y_axis

if __name__ == "__main__":
    main()