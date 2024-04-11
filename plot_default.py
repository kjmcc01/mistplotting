
# plots default tracks and isochrones for given inputs

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks

def plot_default_tracks(masses, times, metallicity):

    track = get_mistery_tracks(masses, metallicity)
    isochrone = get_mistery_isochrones(times, metallicity)

    fig, (ax1, ax2) = plt.subplots(2)
    ax1.semilogy(10**track['log_Teff'], 10**track['log_L'], label='track')
    ax2.semilogy(10**isochrone['log_Teff'], 10**isochrone['log_L'], label='isochrone')
    plt.xlabel('effective temperature (K)')
    plt.ylabel('luminosity (solar units)')
    plt.xlim(8500, 2500)
    plt.legend()
    st.pyplot(fig)