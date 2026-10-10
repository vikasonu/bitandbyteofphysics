# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:18:13 2026

@author: Vikas Kumar
"""

import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Interactive Physics",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HEADER SECTION ---
st.title("⚛️ Interactive Physics Visualizer")
st.markdown("### Master kinematics and vectors through real-time simulations.")

st.write("---")

st.write("""
Welcome! This platform is designed to help students and educators visualize fundamental physics concepts. 
Instead of just memorizing equations, you can manipulate variables, scrub through time, and watch how 
vectors, velocity, and acceleration change dynamically.

👈 **Open the sidebar on the left to select a lesson and start learning!**
""")

st.write("---")

# --- SIMULATION DIRECTORY ---
st.header("📚 Available Modules")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    #### 🚗 1. Relative Velocity
    Understand frames of reference in 1D space. Watch how the speed of a car changes completely 
    depending on whether you are standing on the ground or sitting in a moving vehicle.
    """)
    
    st.info("""
    #### ↗️ 2. 2D Vectors & Math
    A visual sandbox for position vectors, displacement, and the parallelogram law. See 
    vector addition, subtraction, and scalar multiplication happen in real-time.
    """)
    
    st.info("""
    #### 📉 3. Concavity & Acceleration
    Learn how to read a Position vs. Time graph. Watch how positive acceleration creates 
    a "concave up" curve, and negative acceleration creates a "concave down" curve.
    """)

with col2:
    st.success("""
    #### ⚾ 4. Projectile Motion Vectors
    Launch a projectile off a building and watch the velocity vectors break down. See visual 
    proof that horizontal velocity stays constant while vertical velocity changes due to gravity.
    """)
    
    st.success("""
    #### 📐 5. Velocity as a Derivative
    Watch the exact moment an Average Velocity (secant line) becomes Instantaneous Velocity 
    (tangent line) as the time step $\Delta t$ approaches zero.
    """)

# --- FOOTER ---
st.write("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built with Python and Streamlit. Math is beautiful when you can see it."
    "</div>", 
    unsafe_allow_html=True
)