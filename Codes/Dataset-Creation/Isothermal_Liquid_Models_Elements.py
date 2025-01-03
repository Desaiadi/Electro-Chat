# Creating a new dataset for Isothermal Liquid Models and related categories

isothermal_liquid_models_data = [
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Constant Volume Chamber (IL)", "Description": "Chamber with one port and fixed volume of isothermal liquid (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Flow Resistance (IL)", "Description": "General resistance in an isothermal liquid branch (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Infinite Flow Resistance (IL)", "Description": "Isothermal liquid element for setting initial pressure difference between two nodes (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Laminar Leakage (IL)", "Description": "Isothermal liquid element that models laminar leakage flow for various geometries (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Local Restriction (IL)", "Description": "Restriction in flow area in isothermal liquid network (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Pipe (IL)", "Description": "Rigid conduit for fluid flow in isothermal liquid systems (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Reservoir (IL)", "Description": "Isothermal liquid reservoir at constant or time-varying pressure (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Rotational Mechanical Converter (IL)", "Description": "Interface between isothermal liquid and mechanical rotational networks (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Elements", "Block Name": "Translational Mechanical Converter (IL)", "Description": "Interface between isothermal liquid and mechanical translational networks (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Sensors", "Block Name": "Flow Rate Sensor (IL)", "Description": "Measure mass flow rate and volumetric flow rate (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Sensors", "Block Name": "Liquid Properties Sensor (IL)", "Description": "Measure density, bulk modulus, and fraction of entrained air in isothermal liquid network (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Sensors", "Block Name": "Pressure Sensor (IL)", "Description": "Measure pressure differences, absolute pressure, or gauge pressure (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Sources", "Block Name": "Flow Rate Source (IL)", "Description": "Generate specified mass flow rate or volumetric flow rate (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Sources", "Block Name": "Pressure Source (IL)", "Description": "Generate specified pressure differential in isothermal liquid network (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Utilities", "Block Name": "Isothermal Liquid Properties (IL)", "Description": "Physical properties of isothermal liquid (Since R2020a)"},
    {"Category": "Isothermal Liquid Models", "Subcategory": "Utilities", "Block Name": "Interface (H-IL)", "Description": "Flow connection between hydraulic and isothermal liquid networks (Since R2020a)"},
]

# Creating a DataFrame from the list of dictionaries
df_isothermal_liquid_models = pd.DataFrame(isothermal_liquid_models_data)

# Saving the dataset to an Excel file
output_path_isothermal_liquid_models = "/mnt/data/Isothermal_Liquid_Models.xlsx"
df_isothermal_liquid_models.to_excel(output_path_isothermal_liquid_models, index=False)

output_path_isothermal_liquid_models
