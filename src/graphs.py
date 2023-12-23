import pandas as pd
import plotly.express as px

data_paths = {
    "ch4": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRS3STM_006_CH4_VMR_A.500hPa.20020901-20231130.175W_84S_174E_86N.csv",
    "co2": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3C2M_005_mole_fraction_of_carbon_dioxide_in_free_troposphere.20020901-20120229.175W_60S_174E_86N.csv",
    "o3": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3STM_006_O3_VMR_A.1000hPa.20020901-20161031.175W_60S_172E_86N.csv",
    "temp_celsius": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3STD_006_Temperature_A.500hPa.20020831-20160925.175W_60S_172E_86N.csv",
    "temp_kelvin": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3STD_006_Temperature_A.500hPa.20020801-20160925.175W_60S_172E_86N_K.csv",
    "veg_grn": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.M2TMNXLND_5_12_4_GRN.19800101-20231130.180W_90S_180E_90N.csv",
    "veg_lai": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.M2TMNXLND_5_12_4_LAI.19800101-20231130.180W_90S_180E_90N.csv",
    "soil_moisture": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.LPRM_AMSR2_A_SOILM3_001_soil_moisture_c1.20120703-20231222.180W_90S_180E_90N.csv",
    "soil_wetness": "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.M2TMNXLND_5_12_4_GWETTOP.19800101-20231130.180W_90S_180E_90N.csv",
}

y_names = {
    "ch4": "Mean AIRS Methane (ppbv)",
    "co2": "Mean AIRS Carbon Dioxide (ppm)",
    "o3": "Mean AIRS Ozone (ppbv)",
    "temp_celsius": "Air temperature average (Celsius)",
    "temp_kelvin": "Air temperature average (Kelvin)",
    "veg_grn": "Greenness fraction",
    "veg_lai": "Leaf area index",
    "soil_moisture": "Volumetric soil moisture percentage",
    "soil_wetness": "Surface soil wetness",
}

def create_chart(path, y_name, html_file, chart_title):
    data = pd.read_csv(path, skiprows=9,  usecols=[0,1], names=['Time',f'{y_name}'])

    # Read the times as dates and the methane concentrations as numeric values
    data['Time'] = pd.to_datetime(data['Time'])
    data[f'{y_name}'] = pd.to_numeric(data[f'{y_name}'])

    fig = px.line(data, x="Time", y=f'{y_name}', title=f'{chart_title}')
    fig.update_layout(title_x=0.5)
    fig.write_html(f"C:/pale-blue-dot-challenge/src/figures/{html_file}.html")

create_chart(data_paths["ch4"], y_names["ch4"], "ch4", "Methane")
create_chart(data_paths["co2"], y_names["co2"], "co2", "Carbon Dioxide")
create_chart(data_paths["o3"], y_names["o3"], "o3", "Ozone")
create_chart(data_paths["temp_celsius"], y_names["temp_celsius"], "temp_celsius", "Air temperature")
create_chart(data_paths["veg_grn"], y_names["veg_grn"], "veg_grn", "Greenness fraction")
create_chart(data_paths["veg_lai"], y_names["veg_lai"], "veg_lai", "Leaf area index")
create_chart(data_paths["soil_moisture"], y_names["soil_moisture"], "soil_moisture", "Soil moisture")