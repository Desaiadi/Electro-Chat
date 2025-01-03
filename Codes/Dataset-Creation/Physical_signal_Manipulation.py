# Creating a new dataset for Physical Signal Manipulation and related categories

physical_signal_manipulation_data = [
    {"Category": "Physical Signal Manipulation", "Subcategory": "Delays", "Block Name": "PS Constant Delay", "Description": "Delay input physical signal by specified time"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Delays", "Block Name": "PS Variable Delay", "Description": "Delay input physical signal by variable time"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Discrete", "Block Name": "PS Asynchronous Sample & Hold", "Description": "Output sample-and-hold signal with external trigger"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Add", "Description": "Add two physical signal inputs"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Bias", "Description": "Add constant bias to input physical signal (Since R2023b)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Concatenate", "Description": "Concatenate two vector or matrix physical signals (Since R2023b)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Divide", "Description": "Compute element-wise division of two input physical signals"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Dot Product", "Description": "Calculate scalar dot product of two vector or matrix physical signals (Since R2023b)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Gain", "Description": "Multiply input physical signal by constant"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Math Function", "Description": "Apply mathematical function to input physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Product", "Description": "Multiply two physical signal inputs"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Subtract", "Description": "Compute simple subtraction of two input physical signals"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Functions", "Block Name": "PS Sum of Elements", "Description": "Calculate sum of elements of vector or matrix input physical signal (Since R2023b)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Linear Operators", "Block Name": "PS Integrator", "Description": "Integrate physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Linear Operators", "Block Name": "PS Transfer Function", "Description": "Model low-pass and lead-lag filters (Since R2020a)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Lookup Tables", "Block Name": "PS Lookup Table (1D)", "Description": "Approximate one-dimensional function using specified lookup method"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Lookup Tables", "Block Name": "PS Lookup Table (2D)", "Description": "Approximate two-dimensional function using specified lookup method"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Lookup Tables", "Block Name": "PS Lookup Table (3D)", "Description": "Approximate three-dimensional function using specified lookup method"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Lookup Tables", "Block Name": "PS Lookup Table (4D)", "Description": "Approximate four-dimensional function using specified lookup method"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Lookup Tables", "Block Name": "PS Scattered Lookup Table (2D)", "Description": "Approximate two-dimensional function using scattered data lookup (Since R2023a)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Lookup Tables", "Block Name": "PS Scattered Lookup Table (3D)", "Description": "Approximate three-dimensional function using scattered data lookup (Since R2023a)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Abs", "Description": "Output absolute value of input physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Ceil", "Description": "Output the smallest integer larger than or equal to input physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Dead Zone", "Description": "Provide region of zero output for physical signals"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Fix", "Description": "Round input physical signal toward zero"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Floor", "Description": "Output the largest integer smaller than or equal to input physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Max", "Description": "Output maximum of two input physical signals"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Min", "Description": "Output minimum of two input physical signals"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Round", "Description": "Round input physical signal toward nearest integer"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Saturation", "Description": "Limit range of physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Selector", "Description": "Select elements from vector or matrix input physical signal (Since R2023b)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Sign", "Description": "Output sign of input physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Switch", "Description": "Single-pole double-throw switch controlled by external physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Three-Element Demux", "Description": "Convert three-element physical signal vector into scalar physical signals"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Nonlinear Operators", "Block Name": "PS Vector Norm", "Description": "Compute Euclidean norm of vector or matrix physical signal (Since R2023b)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Periodic Operators", "Block Name": "PS Constant Offset Estimator", "Description": "Measure constant offset value of periodic signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Periodic Operators", "Block Name": "PS Harmonic Estimator (Amplitude, Phase)", "Description": "Measure harmonic amplitude and phase of periodic signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Periodic Operators", "Block Name": "PS Harmonic Estimator (Real, Imaginary)", "Description": "Measure real and imaginary parts of periodic signal harmonic"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Periodic Operators", "Block Name": "PS RMS Estimator", "Description": "Measure RMS value of periodic signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sinks", "Block Name": "PS Terminator", "Description": "Terminator for unconnected physical signal outputs"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Constant", "Description": "Generate constant physical signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Counter", "Description": "Increment output signal by 1 with every time step"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Ramp", "Description": "Generate constantly increasing or decreasing physical signal (Since R2021a)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Random Number", "Description": "Generate normally distributed random numbers for physical modeling"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Repeating Sequence", "Description": "Output periodic piecewise linear signal"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Sine Wave", "Description": "Generate sine wave physical signal, using simulation time as time source (Since R2021a)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Step", "Description": "Generate physical signal shaped as step function (Since R2021a)"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Sources", "Block Name": "PS Uniform Random Number", "Description": "Generate uniformly distributed random numbers for physical modeling"},
    {"Category": "Physical Signal Manipulation", "Subcategory": "Utilities", "Block Name": "PS Signal Specification", "Description": "Specify size and unit of physical signal"}
]

# Creating a DataFrame from the list of dictionaries
df_physical_signal_manipulation = pd.DataFrame(physical_signal_manipulation_data)

# Saving the dataset to an Excel file
output_path_physical_signal_manipulation = "/mnt/data/Physical_Signal_Manipulation.xlsx"
df_physical_signal_manipulation.to_excel(output_path_physical_signal_manipulation, index=False)

output_path_physical_signal_manipulation
