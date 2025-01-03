# Creating a new dataset for Gas Models, Moist Air Models, and Thermal Models

gas_moist_air_thermal_models_data = [
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Absolute Reference (G)", "Description": "(Not recommended) Reference point at zero absolute temperature and pressure"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Cap (G)", "Description": "Gas port terminator with zero flow"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Constant Volume Chamber (G)", "Description": "Chamber with fixed volume of gas and variable number of ports"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Controlled Reservoir (G)", "Description": "Boundary conditions for gas network at time-varying pressure and temperature"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Flow Resistance (G)", "Description": "General resistance in a gas branch"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Infinite Flow Resistance (G)", "Description": "Perfectly insulated break in gas network"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Local Restriction (G)", "Description": "Restriction in flow area in gas network"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Pipe (G)", "Description": "Rigid conduit for gas flow"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Reservoir (G)", "Description": "Boundary conditions for gas network at constant pressure and temperature"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Rotational Mechanical Converter (G)", "Description": "Interface between gas and mechanical rotational networks"},
    {"Category": "Gas Models", "Subcategory": "Elements", "Block Name": "Translational Mechanical Converter (G)", "Description": "Interface between gas and mechanical translational networks"},
    {"Category": "Gas Models", "Subcategory": "Sensors", "Block Name": "Flow Rate Sensor (G)", "Description": "Measure mass, energy, and volumetric flow rates in gas networks (Since R2023a)"},
    {"Category": "Gas Models", "Subcategory": "Sensors", "Block Name": "Mach Number Sensor (G)", "Description": "Measure Mach number of internal gas flow (Since R2023b)"},
    {"Category": "Gas Models", "Subcategory": "Sensors", "Block Name": "Pressure & Temperature Sensor (G)", "Description": "Measure pressure and temperature in gas networks"},
    {"Category": "Gas Models", "Subcategory": "Sensors", "Block Name": "Thermodynamic Properties Sensor (G)", "Description": "Measure specific enthalpy, density, specific heat at constant pressure, and specific entropy"},
    {"Category": "Gas Models", "Subcategory": "Sources", "Block Name": "Flow Rate Source (G)", "Description": "Generate constant or time-varying mass flow rate or volumetric flow rate in gas network (Since R2023b)"},
    {"Category": "Gas Models", "Subcategory": "Sources", "Block Name": "Pressure Source (G)", "Description": "Generate constant or time-varying pressure differential"},
    {"Category": "Gas Models", "Subcategory": "Utilities", "Block Name": "Gas Properties (G)", "Description": "Global gas properties for attached circuit"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Absolute Reference (MA)", "Description": "(Not recommended) Reference point at zero absolute temperature and pressure"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Cap (MA)", "Description": "Moist air port terminator with zero flow"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Constant Volume Chamber (MA)", "Description": "Chamber with fixed volume of moist air and variable number of ports"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Flow Resistance (MA)", "Description": "General resistance in a moist air branch"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Infinite Flow Resistance (MA)", "Description": "Perfectly insulated break in moist air network"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Local Restriction (MA)", "Description": "Restriction in flow area in moist air network"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Moisture Separator (MA)", "Description": "Remove water vapor and water droplets from moist air flow (Since R2024b)"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Pipe (MA)", "Description": "Rigid conduit for moist air flow"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Reservoir (MA)", "Description": "Boundary conditions for moist air network at constant pressure, temperature, moisture, and trace gas levels"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Rotational Mechanical Converter (MA)", "Description": "Interface between moist air and mechanical rotational networks"},
    {"Category": "Moist Air Models", "Subcategory": "Elements", "Block Name": "Translational Mechanical Converter (MA)", "Description": "Interface between moist air and mechanical translational networks"},
    {"Category": "Moist Air Models", "Subcategory": "Sensors", "Block Name": "Flow Rate Sensor (MA)", "Description": "Measure mass, energy, and volumetric flow rates in moist air networks (Since R2023a)"},
    {"Category": "Moist Air Models", "Subcategory": "Sensors", "Block Name": "Measurement Selector (MA)", "Description": "Measure pressure, temperature, humidity, and trace gas levels in moist air internal volumes"},
    {"Category": "Moist Air Models", "Subcategory": "Sensors", "Block Name": "Moisture & Trace Gas Sensor (MA)", "Description": "Measure humidity, water droplets, and trace gas levels in moist air network"},
    {"Category": "Moist Air Models", "Subcategory": "Sensors", "Block Name": "Pressure & Temperature Sensor (MA)", "Description": "Measure pressure and temperature in moist air networks"},
    {"Category": "Moist Air Models", "Subcategory": "Sensors", "Block Name": "Thermodynamic Properties Sensor (MA)", "Description": "Measure specific enthalpy, density, specific heat at constant pressure, and specific entropy of air mixture"},
    {"Category": "Moist Air Models", "Subcategory": "Sources", "Block Name": "Flow Rate Source (MA)", "Description": "Generate constant or time-varying mass flow rate or volumetric flow rate in moist air network (Since R2023b)"},
    {"Category": "Moist Air Models", "Subcategory": "Sources", "Block Name": "Pressure Source (MA)", "Description": "Generate constant or time-varying pressure differential"},
    {"Category": "Moist Air Models", "Subcategory": "Moisture & Trace Gas Sources", "Block Name": "Moisture Source (MA)", "Description": "Inject or extract moisture at a constant or time-varying rate"},
    {"Category": "Moist Air Models", "Subcategory": "Moisture & Trace Gas Sources", "Block Name": "Trace Gas Source (MA)", "Description": "Inject or extract trace gas at a constant or time-varying rate"},
    {"Category": "Moist Air Models", "Subcategory": "Utilities", "Block Name": "Moist Air Properties (MA)", "Description": "Global moist air properties for attached circuit"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Conductive Heat Transfer", "Description": "Heat transfer by conduction"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Convective Heat Transfer", "Description": "Heat transfer by convection"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Infinite Thermal Resistance", "Description": "Thermal element for setting initial temperature difference between two nodes"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Perfect Insulator", "Description": "Thermal element with perfect insulation and no thermal mass"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Radiative Heat Transfer", "Description": "Heat transfer by radiation"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Thermal Mass", "Description": "Mass in thermal systems"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Thermal Reference", "Description": "Reference connection for thermal ports"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Thermal Resistance", "Description": "Constant resistance in thermal systems"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Elements", "Block Name": "Variable Thermal Resistance", "Description": "Variable resistance in thermal systems"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Sensors", "Block Name": "Heat Flow Rate Sensor", "Description": "Ideal heat flow meter"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Sensors", "Block Name": "Temperature Sensor", "Description": "Ideal temperature sensor"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Sources", "Block Name": "Controlled Heat Flow Rate Source", "Description": "Variable source of thermal energy, characterized by heat flow"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Sources", "Block Name": "Controlled Temperature Source", "Description": "Variable source of thermal energy, characterized by temperature"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Sources", "Block Name": "Heat Flow Rate Source", "Description": "Constant source of thermal energy, characterized by heat flow"},
    {"Category": "Thermal Models", "Subcategory": "Thermal Sources", "Block Name": "Temperature Source", "Description": "Constant source of thermal energy, characterized by temperature"},
]

# Creating a DataFrame from the list of dictionaries
df_gas_moist_air_thermal_models = pd.DataFrame(gas_moist_air_thermal_models_data)

# Saving the dataset to an Excel file
output_path_gas_moist_air_thermal_models = "/mnt/data/Gas_Moist_Air_Thermal_Models.xlsx"
df_gas_moist_air_thermal_models.to_excel(output_path_gas_moist_air_thermal_models, index=False)

output_path_gas_moist_air_thermal_models
