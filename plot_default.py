
# plots default tracks and isochrones for given inputs

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks

@st.cache_data
def plot_default_tracks(masses, times, metallicity):

    track = get_mistery_tracks(masses, metallicity)
    isochrone = get_mistery_isochrones(times, metallicity)

    fig, (ax1, ax2) = plt.subplots(2, figsize=(5,8))

    ax1.semilogy(10**track['log_Teff'], 10**track['log_L'], label='track')
    ax2.semilogy(10**isochrone['log_Teff'], 10**isochrone['log_L'], label='isochrone')

    ax1.set_title('evolutionary track')
    ax1.set_xlabel('effective temperature (K)')
    ax1.set_ylabel('luminosity (solar units)')
    ax2.set_title('isochrone')
    ax2.set_xlabel('effective temperature (K)')
    ax2.set_ylabel('luminosity (solar units)')

    plt.xlim(8500, 2500)
    plt.legend()
    st.pyplot(fig)