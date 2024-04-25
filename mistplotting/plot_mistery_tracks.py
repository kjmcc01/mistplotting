import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery
from mistplotting.get_any_tracks import get_mistery_isochrones, get_mistery_tracks

@st.cache_data

def plot_new_tracks(mass, tracks, x_axis, y_axis):

    plt.rcParams.update({'font.size': 8})
    fig, ax = plt.subplots(figsize=(5,5))
    if len(mass)==1:
        x_data = tracks[x_axis]
        y_data = tracks[y_axis] 
        ax.plot(x_data, y_data)
        ax.grid('on')
    else:

        n = len(tracks)
        color = (plt.cm.tab20(np.linspace(0, 1, n)))

        for i in range(0, n):
            x_data = tracks[i][x_axis]
            y_data = tracks[i][y_axis]
            ax.plot(x_data, y_data, c = color[i])
            ax.grid('on')

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    mass_labels = [f'{label:.1f} $M_☉$' for label in mass]
    ax.legend(mass_labels)

    st.pyplot(fig)
