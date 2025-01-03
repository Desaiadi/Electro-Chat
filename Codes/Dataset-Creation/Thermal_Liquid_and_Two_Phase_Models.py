# Creating a new dataset for Thermal Liquid Models and Two-Phase Fluid Models

thermal_liquid_and_two_phase_models_data = [
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Absolute Reference (TL)", "Description": "(Not recommended) Reference point at zero absolute temperature and pressure"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Cap (TL)", "Description": "Perfectly insulated stop to fluid flow"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Constant Volume Chamber (TL)", "Description": "Chamber with fixed volume of thermal liquid and variable number of ports"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Controlled Reservoir (TL)", "Description": "Thermal liquid reservoir at time-varying temperature"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Flow Resistance (TL)", "Description": "General resistance in a thermal liquid branch"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Infinite Flow Resistance (TL)", "Description": "Perfectly insulated break in thermal liquid network"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Local Restriction (TL)", "Description": "Restriction in flow area in thermal liquid network"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Pipe (TL)", "Description": "Rigid conduit for fluid flow in thermal liquid systems"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Reservoir (TL)", "Description": "Thermal liquid reservoir at constant temperature and pressure"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Rotational Mechanical Converter (TL)", "Description": "Interface between thermal liquid and mechanical rotational networks"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Elements", "Block Name": "Translational Mechanical Converter (TL)", "Description": "Interface between thermal liquid and mechanical translational networks"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Sensors", "Block Name": "Flow Rate Sensor (TL)", "Description": "Measure mass, energy, and volumetric flow rates in thermal liquid networks (Since R2023a)"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Sensors", "Block Name": "Pressure & Temperature Sensor (TL)", "Description": "Measure pressure and temperature in thermal liquid networks"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Sensors", "Block Name": "Thermodynamic Properties Sensor (TL)", "Description": "Measure specific internal energy, density, and specific heat at constant pressure in thermal liquid networks"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Sources", "Block Name": "Flow Rate Source (TL)", "Description": "Generate constant or time-varying mass flow rate or volumetric flow rate in thermal liquid network (Since R2023b)"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Sources", "Block Name": "Pressure Source (TL)", "Description": "Generate constant or time-varying pressure differential"},
    {"Category": "Thermal Liquid Models", "Subcategory": "Utilities", "Block Name": "Thermal Liquid Settings (TL)", "Description": "Physical properties of a thermal liquid"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Absolute Reference (2P)", "Description": "(Not recommended) Reference point at zero absolute pressure and specific internal energy"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Cap (2P)", "Description": "Perfectly insulated stop to fluid flow"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Constant Volume Chamber (2P)", "Description": "Chamber with fixed volume of two-phase fluid and variable number of ports"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Controlled Reservoir (2P)", "Description": "Two-phase fluid reservoir at variable pressure and temperature"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Flow Resistance (2P)", "Description": "General resistance in a two-phase fluid branch"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Infinite Flow Resistance (2P)", "Description": "Perfectly insulated break in two-phase fluid network"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Local Restriction (2P)", "Description": "Restriction in flow area in two-phase fluid network"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Pipe (2P)", "Description": "Rigid conduit for fluid flow in two-phase fluid systems"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Reservoir (2P)", "Description": "Two-phase fluid reservoir at constant temperature and pressure"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Rotational Mechanical Converter (2P)", "Description": "Interface between two-phase fluid and mechanical rotational networks"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Elements", "Block Name": "Translational Mechanical Converter (2P)", "Description": "Interface between two-phase fluid and mechanical translational networks"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sensors", "Block Name": "Flow Rate Sensor (2P)", "Description": "Measure mass, energy, and volumetric flow rates in two-phase fluid networks (Since R2023a)"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sensors", "Block Name": "Pressure, Temperature & Internal Energy Sensor (2P)", "Description": "Measure pressure, temperature, and specific internal energy in two-phase fluid networks"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sensors", "Block Name": "Saturation Properties Sensor (2P)", "Description": "Measure liquid and vapor saturation properties in two-phase fluids (Since R2021a)"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sensors", "Block Name": "Thermodynamic Properties Sensor (2P)", "Description": "Measure temperature, density, specific enthalpy, specific entropy, and specific volume in two-phase fluid networks"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sensors", "Block Name": "Vapor Quality Sensor (2P)", "Description": "Measure vapor fraction in two-phase fluids"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sources", "Block Name": "Flow Rate Source (2P)", "Description": "Generate constant or time-varying mass flow rate or volumetric flow rate in two-phase fluid network (Since R2023b)"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Sources", "Block Name": "Pressure Source (2P)", "Description": "Generate constant or time-varying pressure differential"},
    {"Category": "Two-Phase Fluid Models", "Subcategory": "Utilities", "Block Name": "Two-Phase Fluid Properties (2P)", "Description": "Fluid properties for two-phase fluid network"},
]

# Creating a DataFrame from the list of dictionaries
df_thermal_and_two_phase_models = pd.DataFrame(thermal_liquid_and_two_phase_models_data)

# Saving the dataset to an Excel file
output_path_thermal_and_two_phase_models = "/mnt/data/Thermal_Liquid_and_Two_Phase_Models.xlsx"
df_thermal_and_two_phase_models.to_excel(output_path_thermal_and_two_phase_models, index=False)

output_path_thermal_and_two_phase_models
