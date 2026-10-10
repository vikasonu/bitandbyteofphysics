# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:07:59 2026

@author: Vikas Kumar
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.set_page_config(page_title="Kinematics Visualizer", layout="wide")
st.title("Kinematics: Concavity and Acceleration")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Simulation Controls")

curve_mode = st.sidebar.radio(
    "Select Curve Type:",
    ["Mixed / Inflection (Changes)", "Always Concave UP (a > 0)", "Always Concave DOWN (a < 0)"]
)

t = st.sidebar.slider("Current Time (t):", 0.0, 4.0, 0.0, step=0.05)

# --- PHYSICS ENGINE ---
def get_kinematics(t_val, mode):
    if "UP" in mode:
        x = 1.5 * t_val**2 - 2 * t_val + 2
        v = 3.0 * t_val - 2
        a = np.full_like(t_val, 3.0) if isinstance(t_val, np.ndarray) else 3.0
    elif "DOWN" in mode:
        x = -1.5 * t_val**2 + 10 * t_val + 2
        v = -3.0 * t_val + 10
        a = np.full_like(t_val, -3.0) if isinstance(t_val, np.ndarray) else -3.0
    else:
        x = t_val**3 - 6*t_val**2 + 9*t_val + 5
        v = 3*t_val**2 - 12*t_val + 9
        a = 6*t_val - 12
    return x, v, a

# Calculate arrays for the full curves
t_full = np.linspace(0.0, 4.0, 200)
x_full, v_full, a_full = get_kinematics(t_full, curve_mode)

# Calculate exact current state
curr_x, curr_v, curr_a = get_kinematics(t, curve_mode)

# --- LAYOUT: TWO COLUMNS ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Live Data Readouts")
    
    concavity_status = "DOWN (Frowning)" if curr_a < 0 else "UP (Smiling)" if curr_a > 0 else "FLAT (Inflection)"
    vel_status = "Decreasing" if curr_a < 0 else "Increasing" if curr_a > 0 else "Min/Max"
    
    st.code(f"""
Time t       : {t:.2f} s
--------------------------
Position x   : {curr_x:.2f} m
Velocity v   : {curr_v:.2f} m/s
Accel a      : {curr_a:.2f} m/s²
--------------------------
Concavity    : {concavity_status}
Velocity is  : {vel_status}
    """)
    
    st.info("""
    **HOW TO READ THIS:**
    * **Red Zone:** Position is Concave Down (Negative Acceleration).
    * **Green Zone:** Position is Concave Up (Positive Acceleration).
    """)

with col2:
    # --- MATPLOTLIB PLOTTING ---
    fig, (ax_x, ax_v, ax_a) = plt.subplots(3, 1, figsize=(8, 9), sharex=True, constrained_layout=True)
    
    def apply_shading(ax):
        if "Mixed" in curve_mode:
            ax.axvspan(0, 2.0, color='red', alpha=0.1)
            ax.axvspan(2.0, 4.0, color='green', alpha=0.1)
        elif "UP" in curve_mode:
            ax.axvspan(0, 4.0, color='green', alpha=0.1)
        else:
            ax.axvspan(0, 4.0, color='red', alpha=0.1)

    # Position
    ax_x.set_title("Position x(t): Concavity", fontweight='bold')
    ax_x.plot(t_full, x_full, color='black', linewidth=2)
    apply_shading(ax_x)
    ax_x.plot(t, curr_x, 'ko', markersize=8)
    
    # Tangent Line
    t_tan = np.array([t - 0.5, t + 0.5])
    x_tan = curr_v * (t_tan - t) + curr_x
    ax_x.plot(t_tan, x_tan, color='purple', linewidth=2, label=f"Slope = {curr_v:.1f}")
    ax_x.legend(loc="upper right")
    ax_x.grid(True, linestyle=':', alpha=0.7)

    # Velocity
    ax_v.set_title("Velocity v(t): Slope of Position", fontweight='bold')
    ax_v.plot(t_full, v_full, color='#0277bd', linewidth=2)
    apply_shading(ax_v)
    ax_v.axhline(0, color='black', linewidth=1)
    ax_v.plot(t, curr_v, 'ko', markersize=8)
    ax_v.grid(True, linestyle=':', alpha=0.7)

    # Acceleration
    ax_a.set_title("Acceleration a(t): Determines Concavity", fontweight='bold')
    ax_a.plot(t_full, a_full, color='#d32f2f', linewidth=2)
    apply_shading(ax_a)
    ax_a.axhline(0, color='black', linewidth=1)
    ax_a.plot(t, curr_a, 'ko', markersize=8)
    if "UP" in curve_mode: ax_a.set_ylim(0, 6)
    if "DOWN" in curve_mode: ax_a.set_ylim(-6, 0)
    ax_a.grid(True, linestyle=':', alpha=0.7)

    # Render the plot in Streamlit
    st.pyplot(fig)