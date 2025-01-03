# Creating a list of dictionaries for better organization and Excel representation
data = [
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sensors", "Block Name": "Ideal Force Sensor", "Description": "Force sensor in mechanical translational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sensors", "Block Name": "Ideal Rotational Motion Sensor", "Description": "Motion sensor in mechanical rotational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sensors", "Block Name": "Ideal Torque Sensor", "Description": "Torque sensor in mechanical rotational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sensors", "Block Name": "Ideal Translational Motion Sensor", "Description": "Motion sensor in mechanical translational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sources", "Block Name": "Ideal Angular Velocity Source", "Description": "Ideal angular velocity source in mechanical rotational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sources", "Block Name": "Ideal Force Source", "Description": "Ideal source of mechanical energy that generates force proportional to the input signal"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sources", "Block Name": "Ideal Torque Source", "Description": "Ideal source of mechanical energy that generates torque proportional to the input signal"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanical Sources", "Block Name": "Ideal Translational Velocity Source", "Description": "Ideal velocity source in mechanical translational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanisms", "Block Name": "Gear Box", "Description": "Gear box in mechanical systems"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanisms", "Block Name": "Lever", "Description": "Generic mechanical lever"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanisms", "Block Name": "Slider-Crank", "Description": "Generic slider-crank mechanism"},
    {"Category": "Mechanical Models", "Subcategory": "Mechanisms", "Block Name": "Wheel and Axle", "Description": "Wheel and axle mechanism in mechanical systems"},
    {"Category": "Mechanical Models", "Subcategory": "Multibody Interfaces", "Block Name": "Rotational Multibody Interface", "Description": "Interface between mechanical rotational networks and Simscape Multibody joints (Since R2021a)"},
    {"Category": "Mechanical Models", "Subcategory": "Multibody Interfaces", "Block Name": "Translational Multibody Interface", "Description": "Interface between mechanical translational networks and Simscape Multibody joints (Since R2021a)"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Inertia", "Description": "Ideal mechanical rotational inertia"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Mechanical Rotational Reference", "Description": "Reference connection for mechanical rotational ports"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Rotational Damper", "Description": "Viscous damper in mechanical rotational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Rotational Free End", "Description": "Rotational port terminator with zero torque"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Rotational Friction", "Description": "Friction in contact between rotating bodies"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Rotational Hard Stop", "Description": "Double-sided rotational hard stop"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Rotational Inerter", "Description": "Two-port inertia in mechanical rotational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Rotational Elements", "Block Name": "Rotational Spring", "Description": "Ideal spring in mechanical rotational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Mass", "Description": "Ideal mechanical translational mass"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Mechanical Translational Reference", "Description": "Reference connection for mechanical translational ports"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Translational Damper", "Description": "Viscous damper in mechanical translational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Translational Free End", "Description": "Translational port terminator with zero force"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Translational Friction", "Description": "Friction in contact between moving bodies"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Translational Hard Stop", "Description": "Double-sided translational hard stop"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Translational Inerter", "Description": "Two-port inertia in mechanical translational systems"},
    {"Category": "Mechanical Models", "Subcategory": "Translational Elements", "Block Name": "Translational Spring", "Description": "Ideal spring in mechanical translational systems"},
]

# Creating a DataFrame from the list of dictionaries
df_hierarchical = pd.DataFrame(data)

# Saving the updated dataset to an Excel file
output_path_final = "path/Dataset_name.xlsx"
df_hierarchical.to_excel(output_path_final, index=False)

