# Creating a new dataset for Position-Based Mechanical Translational Models and related categories

position_based_data = [
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Mass (PB)", "Description": "Point mass with gravitational effects (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Mass With Friction (PB)", "Description": "Point mass with friction and gravitational effects (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Mass With Length & Friction (PB)", "Description": "Mass with length, friction, and gravitational effects (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Mass With Length (PB)", "Description": "Mass with length and gravitational effects (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational Damper (PB)", "Description": "Viscous damper in position-based mechanical translational systems (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational Friction (PB)", "Description": "Resistive frictional contact between surfaces in position-based mechanical translational systems (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational Hard Stop (PB)", "Description": "Hard stop in position-based mechanical translational systems (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational Initial Spacer (PB)", "Description": "Initial distance between blocks (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational Spacer (PB)", "Description": "Fixed length between blocks during simulation (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational Spring (PB)", "Description": "Ideal spring in position-based mechanical translational systems (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Elements", "Block Name": "Translational World (PB)", "Description": "Global reference frame for position-based translational network (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sensors", "Block Name": "Force Sensor (PB)", "Description": "Force sensor in position-based mechanical translational systems (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sensors", "Block Name": "Translational Motion Sensor (PB)", "Description": "Motion sensor in position-based mechanical translational systems (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sources", "Block Name": "External Force Source (PB)", "Description": "Ideal source of mechanical energy that generates force proportional to the input signal (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sources", "Block Name": "External Translational Velocity Source (PB)", "Description": "Ideal source of mechanical energy that generates velocity proportional to the input signal (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sources", "Block Name": "Force Actuator (PB)", "Description": "Ideal force actuator, with length, that generates force proportional to the input signal (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sources", "Block Name": "Length Actuator (PB)", "Description": "Ideal actuator that maintains length proportional to the input signal (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Sources", "Block Name": "Translational Velocity Actuator (PB)", "Description": "Ideal velocity actuator, with length, that maintains velocity proportional to the input signal (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Utilities", "Block Name": "Interface (PB-Translational)", "Description": "Connect position-based and non-position-based mechanical translational ports (Since R2024b)"},
    {"Category": "Position-Based Mechanical Translational Models", "Subcategory": "Utilities", "Block Name": "Mechanical Translational Properties (PB)", "Description": "Specify gravitational acceleration and rail incline angle for circuit (Since R2024b)"},
]

# Creating a DataFrame from the new list of dictionaries
df_position_based = pd.DataFrame(position_based_data)

# Saving the new dataset to an Excel file
output_path_position_based = "Path/Position_Based_Mechanical_Models.xlsx"
df_position_based.to_excel(output_path_position_based, index=False)

output_path_position_based
