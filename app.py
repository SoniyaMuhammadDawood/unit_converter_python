import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        # Fix: Use the correct conversion formula
        # Convert to base unit then to target unit
        return value * (conversion_dict[from_unit] / conversion_dict[to_unit])
    return None

# Conversion dictionaries - Fixed values to be more accurate
# Each value represents conversion to base unit (mm, sec, g)
length_units = {"Millimeters": 1, "Centimeters": 10, "Meters": 1000, "Kilometers": 1000000, 
                "Miles": 1609344, "Inches": 25.4, "Feet": 304.8, "Yards": 914.4}
time_units = {"Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400, 
              "Weeks": 604800, "Months": 2628000, "Years": 31536000}
weight_units = {"Grams": 1, "Kilograms": 1000, "Pounds": 453.592, "Ounces": 28.3495, "Tons": 1000000}
temperature_units = {"Celsius": 1, "Fahrenheit": 1.8, "Kelvin": 1}

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    .title-container {
        background-color: #4527a0;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .title-container h1 {
        margin-bottom: 0;
    }
    .title-container p {
        margin-top: 5px;
        margin-bottom: 0;
    }
    .converter-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .result-container {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        border-left: 5px solid #4caf50;
    }
    .stButton>button {
        background-color: #4527a0;
        color: white;
        font-weight: bold;
        width: 100%;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# App title with styling - Fixed to remove blank space
st.markdown('<div class="title-container"><h1>🔄 Unit Converter App</h1><p>Convert between commonly used units! ✨</p></div>', unsafe_allow_html=True)

# Select conversion type - Moved inside the converter container
st.markdown('<div class="converter-container">', unsafe_allow_html=True)

# Select conversion type
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Time", "Weight", "Temperature"])

if conversion_type == "Length":
    units = length_units
elif conversion_type == "Time":
    units = time_units
elif conversion_type == "Weight":
    units = weight_units
else:
    # Fix: Corrected temperature conversion function
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return None
    
    units = temperature_units

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # User input
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", list(units.keys()))

with col2:
    st.write("")  # Empty space to align with number input
    to_unit = st.selectbox("To", list(units.keys()))

# Convert button with full width
if st.button("Convert"):
    if conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        # Fix: Corrected the conversion formula in convert_units function
        result = convert_units(value, from_unit, to_unit, units)
    
    if result is not None:
        # Display result with nice styling
        st.markdown(f'<div class="result-container">{value} {from_unit} = {result:.4f} {to_unit}</div>', unsafe_allow_html=True)
    else:
        st.error("Invalid conversion!")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed with ❤️ by Soniya</div>', unsafe_allow_html=True)