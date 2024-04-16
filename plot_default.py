
# plots default tracks and isochrones for given inputs

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks

@st.cache_data
def plot_default_tracks(mass, tracks, ages, isochrones):

    plt.rcParams.update({'font.size': 8})
    fig, (ax1, ax2) = plt.subplots(2, figsize=(5,8))

    if len(mass)==1:
        ax1.semilogy(10**tracks['log_Teff'], 10**tracks['log_L'], label='track')
    else:
        for i in range(0, len(tracks)):
            ax1.semilogy(10**tracks[i]['log_Teff'], 10**tracks[i]['log_L'], label='track')
    
    if len(ages)==1:
        ax2.semilogy(10**isochrones['log_Teff'], 10**isochrones['log_L'], label='isochrone')
    else:
        for i in range(0, len(ages)):
            ax2.semilogy(10**isochrones[i]['log_Teff'], 10**isochrones[i]['log_L'], label='isochrone')
            


    ax1.set_title('evolutionary track')
    ax1.set_xlabel('effective temperature (K)')
    ax1.set_ylabel('luminosity (solar units)')
    ax2.set_title('isochrone')
    ax2.set_xlabel('effective temperature (K)')
    ax2.set_ylabel('luminosity (solar units)')

    plt.xlim(8500, 2500)
    plt.legend()
    st.pyplot(fig)