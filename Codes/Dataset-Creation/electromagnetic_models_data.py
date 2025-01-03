# Creating a new dataset for Electromagnetic Models and related categories

electromagnetic_models_data = [
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Electromagnetic Converter", "Description": "Lossless electromagnetic energy conversion device"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Fundamental Reluctance", "Description": "Simplified implementation of magnetic reluctance"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Magnetic Reference", "Description": "Reference connection for magnetic ports"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Permanent Magnet", "Description": "Permanent magnet that passively generates magnetic field (Since R2023b)"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Reluctance", "Description": "Magnetic reluctance"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Reluctance Force Actuator", "Description": "Magnetomotive device based on reluctance force"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Elements", "Block Name": "Variable Reluctance", "Description": "Variable reluctance in electromagnetic systems"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Sensors", "Block Name": "Flux Sensor", "Description": "Ideal flux sensor"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Sensors", "Block Name": "MMF Sensor", "Description": "Ideal magnetomotive force sensor"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Sources", "Block Name": "Controlled Flux Source", "Description": "Ideal flux source driven by input signal"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Sources", "Block Name": "Controlled MMF Source", "Description": "Ideal magnetomotive force source driven by input signal"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Sources", "Block Name": "Flux Source", "Description": "Ideal flux source"},
    {"Category": "Electromagnetic Models", "Subcategory": "Magnetic Sources", "Block Name": "MMF Source", "Description": "Ideal magnetomotive force source"},
]

# Creating a DataFrame from the list of dictionaries
df_electromagnetic_models = pd.DataFrame(electromagnetic_models_data)

# Saving the dataset to an Excel file
output_path_electromagnetic_models = "/mnt/data/Electromagnetic_Models.xlsx"
df_electromagnetic_models.to_excel(output_path_electromagnetic_models, index=False)

output_path_electromagnetic_models
