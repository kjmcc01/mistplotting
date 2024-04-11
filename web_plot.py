import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks
from plot_default import plot_default_tracks

def main():
    st.title("mistery stellar evolution plotting app")

    mass_input = st.number_input("Enter desired stellar mass: ")
    mass = mass_input
    metallicity_input = st.number_input("Enter desired stellar metallicity (positive): ")
    metallicity = metallicity_input

    times_input = st.number_input("Enter desired age of isochrones (in Gyr): ")

    plot_default_tracks(mass, times_input, metallicity)

    tracks = get_mistery_tracks(mass, metallicity)
    isochrones = get_mistery_isochrones(times_input, metallicity)

    st.sidebar.write("Select graph axes.")

    graph_x_axis = st.sidebar.selectbox(
        "Select x-axis",
        (tracks.dtype.names)
    )

    graph_y_axis = st.sidebar.selectbox(
        "Select y-axis",
        (tracks.dtype.names)
    )

    x_data = tracks[graph_x_axis]
    y_data = tracks[graph_y_axis]

    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(x_data, y_data)
    st.pyplot(fig)

    #return graph_x_axis, graph_y_axis

if __name__ == "__main__":
    main()