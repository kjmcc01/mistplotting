
# plots default tracks and isochrones for given inputs

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from get_any_tracks import get_mistery_isochrones, get_mistery_tracks

@st.cache_data
def plot_default_tracks(mass, tracks, ages, isochrones):

    plt.rcParams.update({'font.size': 12})
    fig, (ax1, ax2) = plt.subplots(2, figsize=(8,10))
    fig.tight_layout()
    plt.subplots_adjust(hspace=0.4)

    if len(mass)==1:
        ax1.semilogy(10**tracks['log_Teff'], 10**tracks['log_L'], c=plt.cm.tab20(1))
    else:        
        for i in range(0, len(tracks)):
            ax1.semilogy(10**tracks[i]['log_Teff'], 10**tracks[i]['log_L'], c=plt.cm.tab20(i % 20))
    
    if len(ages)==1:
        ax2.semilogy(10**isochrones['log_Teff'], 10**isochrones['log_L'], c=plt.cm.tab20(1))
    else:
        for i in range(0, len(ages)):
            ax2.semilogy(10**isochrones[i]['log_Teff'], 10**isochrones[i]['log_L'], c=plt.cm.tab20(i % 20))


    ax1.set_title('evolutionary track')
    ax1.set_xlabel('effective temperature (K)')
    ax1.set_ylabel(f'Luminosity ($L_☉$)')

    mass_labels = [f'{label:.1f} $M_☉$' for label in mass]
    ax1.legend(mass_labels)

    ax2.set_title('isochrone')
    ax2.set_xlabel('effective temperature (K)')
    ax2.set_ylabel(f'Luminosity ($L_☉$)')

    age_labels = [f'{label:.1f} Gyr' for label in ages]
    ax2.legend(age_labels)

    plt.xlim(8500, 2500)

    st.pyplot(fig)