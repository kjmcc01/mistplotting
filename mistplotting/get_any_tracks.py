import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery

@st.cache_data
def get_mistery_tracks(masses, metallicity):

    if len(masses) > 1:
        tracks = mistery.get_tracks(Ms=masses, FeH=metallicity)

    elif len(masses) == 1:
        tracks = mistery.get_track(M=masses[0], FeH=metallicity)
    
    else:
        tracks = 0

    return tracks

@st.cache_data
def get_mistery_isochrones(ages, metallicity):

    if len(ages) > 1:
        isochrones = mistery.get_isochrones(ts=ages, FeH=metallicity)

    elif len(ages) == 1:
        isochrones = mistery.get_isochrone(t=ages[0], FeH=metallicity)

    else:
        isochrones = 0

    return isochrones