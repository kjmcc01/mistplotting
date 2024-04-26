import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks
from plot_default import plot_default_tracks
from plot_mistery_tracks import plot_new_tracks 

def main():
    st.title("MIST stellar evolution plotting")


    st.write("All inputs will plot two default plots: the evolutionary track and isochrones for all given \
             stellar masses and all given ages.  \n \
             Once plots appear, the sidebar can be used to customize further visualizatons for all given stellar masses.")

    mass_input = st.text_input("Enter desired stellar mass (in solar masses, separate by commas): ", placeholder='1.0')
    mass = mass_input.split(",")
    try:
        mass = [float(i) for i in mass]
    except:
        mass = mass

    metallicity_input = st.number_input("Enter desired stellar metallicity: ")
    metallicity = metallicity_input

    ages_input = st.text_input("Enter desired age of isochrones (in Gyr, separate by commas): ", placeholder='1.0')
    ages = ages_input.split(",")
    try:
        ages = [float(i) for i in ages]
    except:
        ages = ages 

    if mass_input == '':
        st.write('Using default mass of 1 $M_☉$...')
        tracks = mistery.get_track(M = 1, FeH = metallicity)
    else:
        tracks = get_mistery_tracks(mass, metallicity)

    if ages_input == '':
        st.write('Using default age of 1 Gyr...')
        isochrones = mistery.get_isochrone(t=1, FeH=metallicity)
    else:
        isochrones = get_mistery_isochrones(ages, metallicity)

    plot_default_tracks(mass, mass_input, tracks, ages, ages_input, isochrones)

    mass_str = f"{len(mass)}"
    z_str = f"{metallicity:.2f}"
    age_str = f"{len(ages)}"
    fn = f"{z_str}_m{mass_str}_t{age_str}.png"
    plt.savefig(fn)
    with open(fn, "rb") as img:
        btn = st.download_button(
            label="Download image",
            data=img,
            file_name=fn,
            mime="image/png"
        )

    st.sidebar.title("Select graph axes.")

    graph_x_axis = st.sidebar.selectbox(
        "Select x-axis",
        (tracks[0].dtype.names)
    )

    graph_y_axis = st.sidebar.selectbox(
        "Select y-axis",
        (tracks[0].dtype.names),
        index = 6
    )

    plot_new_tracks(mass, mass_input, tracks, graph_x_axis, graph_y_axis)

    fn_new = f"{graph_x_axis}_{graph_y_axis}_m{len(mass)}.png"
    plt.savefig(fn_new)
    with open(fn_new, "rb") as img:
        new_btn = st.download_button(
            label="Download image",
            data=img,
            file_name=fn_new,
            mime="image/png"
        )

if __name__ == "__main__":
    main()