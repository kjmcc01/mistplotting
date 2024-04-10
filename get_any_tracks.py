import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import mistery

def get_mistery_tracks(masses, metallicity):

    if len(masses) > 1:
        tracks = mistery.get_tracks(Ms=masses, FeH=metallicity)

    elif len(masses) == 1:
        tracks = mistery.get_track(M=masses, FeH=metallicity)


    return tracks


def get_mistery_isochrones(times, metallicity):

    if len(times) > 1:
        isochrones = mistery.get_isochrones(ts=times, FeH=metallicity)

    elif len(masses) == 1:
        isochrones = mistery.get_isochrone(t=times, FeH=metallicity)


    return isochrones