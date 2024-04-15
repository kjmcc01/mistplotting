import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks
from plot_default import plot_default_tracks

def main():
    st.title("mistery stellar evolution plotting app")

    mass_input = st.text_input("Enter desired stellar mass (separate by spaces): ")
    mass = mass_input.split(" ")
    try:
        mass = [float(i) for i in mass]
    except:
        mass = mass

    metallicity_input = st.number_input("Enter desired stellar metallicity (positive): ")
    metallicity = metallicity_input

    times_input = st.number_input("Enter desired age of isochrones (in Gyr): ")
    
    tracks = get_mistery_tracks(mass, metallicity)
    isochrones = get_mistery_isochrones(times_input, metallicity)

    plot_default_tracks(tracks, isochrones)

    st.sidebar.title("Select graph axes.")

    graph_x_axis = st.sidebar.selectbox(
        "Select x-axis",
        (tracks[0].dtype.names)
    )

    graph_y_axis = st.sidebar.selectbox(
        "Select y-axis",
        (tracks[0].dtype.names)
    )

    st.sidebar.write(
        "log_Teff: effective temperature (logarithmic)  \n"
        "log_L: luminosity (logarithmic)"
        " ")

    fig, ax = plt.subplots(figsize=(5,5))
    for i in range(0, len(tracks)):
        x_data = tracks[i][graph_x_axis]
        y_data = tracks[i][graph_y_axis]
        ax.plot(x_data, y_data)
    st.pyplot(fig)

    #return graph_x_axis, graph_y_axis

if __name__ == "__main__":
    main()