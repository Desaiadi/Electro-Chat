# Creating a new dataset for Electrical Models and related categories

electrical_models_data = [
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Capacitor", "Description": "Linear capacitor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Diode", "Description": "Piecewise linear diode in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Electrical Reference", "Description": "Connection to electrical ground"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Floating Reference", "Description": "Reference for measuring voltage of other nodes in floating electrical network (Since R2023b)"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Gyrator", "Description": "Ideal gyrator in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Ideal Transformer", "Description": "Ideal transformer in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Inductor", "Description": "Linear inductor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Infinite Resistance", "Description": "Electrical element for setting initial voltage difference between two nodes"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Memristor", "Description": "Ideal memristor with nonlinear dopant drift approach"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Mutual Inductor", "Description": "Mutual inductor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Op-Amp", "Description": "Ideal operational amplifier"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Open Circuit", "Description": "Electrical port terminator that draws no current"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Resistor", "Description": "Linear resistor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Rotational Electromechanical Converter", "Description": "Interface between electrical and mechanical rotational domains"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Switch", "Description": "Switch controlled by external physical signal"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Thermal Resistor", "Description": "Resistor with thermal port"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Translational Electromechanical Converter", "Description": "Interface between electrical and mechanical translational domains"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Elements", "Block Name": "Variable Resistor", "Description": "Linear variable resistor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sensors", "Block Name": "Current Sensor", "Description": "Current sensor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sensors", "Block Name": "Voltage Sensor", "Description": "Voltage sensor in electrical systems"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "AC Current Source", "Description": "Ideal sinusoidal current source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "AC Voltage Source", "Description": "Ideal constant voltage source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "Controlled Current Source", "Description": "Ideal current source driven by input signal"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "Controlled Voltage Source", "Description": "Ideal voltage source driven by input signal"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "Current-Controlled Current Source", "Description": "Linear current-controlled current source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "Current-Controlled Voltage Source", "Description": "Linear current-controlled voltage source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "DC Current Source", "Description": "Ideal constant current source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "DC Voltage Source", "Description": "Ideal constant voltage source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "Voltage-Controlled Current Source", "Description": "Linear voltage-controlled current source"},
    {"Category": "Electrical Models", "Subcategory": "Electrical Sources", "Block Name": "Voltage-Controlled Voltage Source", "Description": "Linear voltage-controlled voltage source"},
]

# Creating a DataFrame from the list of dictionaries
df_electrical_models = pd.DataFrame(electrical_models_data)

# Saving the dataset to an Excel file
output_path_electrical_models = "/mnt/data/Electrical_Models.xlsx"
df_electrical_models.to_excel(output_path_electrical_models, index=False)

output_path_electrical_models
