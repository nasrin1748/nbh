import streamlit as st

# Streamlit Sliders for HSL values
h = st.slider("Hue", 0, 360, 0)                # Hue: 0 to 360 degrees
s = st.slider("Saturation (%)", 0, 100, 50)   # Saturation: 0% to 100%
l = st.slider("Luminance (%)", 0, 100, 50)    # Luminance: 0% to 100%
a = st.slider("Alpha (Transparency)", 0.0, 1.0, 1.0)  # Alpha: 0.0 (transparent) to 1.0 (opaque)

# Input text from the user
text_input = st.text_input("Enter text", value="text")

# Update text style using HSL and transparency values
text_style = f"""
<div style="color: hsla({h}, {s}%, {l}%, {a}); font-size: 20px;">
    {text_input}
</div>
"""

# Display the styled text
st.markdown(text_style, unsafe_allow_html=True)
