import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks
from plot_default import plot_default_tracks
from plot_mistery_tracks import plot_new_tracks 

def main():
    st.title("mistery stellar evolution plotting app")

    mass_input = st.text_input("Enter desired stellar mass (in solar masses, separate by spaces): ")
    mass = mass_input.split(" ")
    try:
        mass = [float(i) for i in mass]
    except:
        mass = mass

    metallicity_input = st.number_input("Enter desired stellar metallicity: ")
    metallicity = metallicity_input

    ages_input = st.text_input("Enter desired age of isochrones (in Gyr, separate by spaces): ")
    ages = ages_input.split(" ")
    try:
        ages = [float(i) for i in ages]
    except:
        ages = ages 


    tracks = get_mistery_tracks(mass, metallicity)
    isochrones = get_mistery_isochrones(ages, metallicity)

    plot_default_tracks(mass, tracks, ages, isochrones)

    st.sidebar.title("Select graph axes.")

    graph_x_axis = st.sidebar.selectbox(
        "Select x-axis",
        (tracks[0].dtype.names)
    )

    graph_y_axis = st.sidebar.selectbox(
        "Select y-axis",
        (tracks[0].dtype.names)
    )

    plot_new_tracks(mass, tracks, ages, isochrones, graph_x_axis, graph_y_axis)

    #return graph_x_axis, graph_y_axis

if __name__ == "__main__":
    main()