# Updating the dataset to include the category change for Utilities

utilities_data = [
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Connection Label", "Description": "Virtual connection between conserving ports"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Connection Port", "Description": "Physical Modeling connector port for subsystem"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Probe", "Description": "Output block variables as signals during simulation (Since R2020a)"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "PS-Simulink Converter", "Description": "Convert physical signal into Simulink output signal"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Simscape Bus", "Description": "Bus for conserving connection lines"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Simscape Component", "Description": "Deploy Simscape language component as custom block in model diagram"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Simulink-PS Converter", "Description": "Convert Simulink input signal into physical signal"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Solver Configuration", "Description": "Physical network environment and solver configuration"},
    {"Category": "Utilities", "Subcategory": "Utility Blocks", "Block Name": "Variant Connector", "Description": "Remove or disconnect physical components from network (Since R2020b)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Capacitor)", "Description": "Split network at an electrical connection by replacing a capacitor (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Compressible Link)", "Description": "Split network at a mechanical translational connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Constant Volume Chamber (IL))", "Description": "Split network at an isothermal liquid connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Constant Volume Chamber (TL))", "Description": "Split network at a thermal liquid connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Current-Voltage)", "Description": "Split network at an electrical connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Flexible Shaft)", "Description": "Split network at a mechanical rotational connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Inductor)", "Description": "Split network at an electrical connection by replacing an inductor (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Thermal Mass)", "Description": "Split network at a thermal connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Voltage-Current)", "Description": "Split network at an electrical connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Network Couplers", "Block Name": "Network Coupler (Voltage-Voltage)", "Description": "Split network at an electrical connection (Since R2022a)"},
    {"Category": "Utilities", "Subcategory": "Other", "Block Name": "Spectrum Analyzer", "Description": "Display frequency spectrum"},
]

# Creating a DataFrame for the Utilities category
df_utilities = pd.DataFrame(utilities_data)

# Saving the Utilities dataset to an Excel file
output_path_utilities = "/mnt/data/Utilities.xlsx"
df_utilities.to_excel(output_path_utilities, index=False)

output_path_utilities
