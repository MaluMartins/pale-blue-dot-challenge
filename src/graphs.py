import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

path_ch4_data = "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRS3STM_006_CH4_VMR_A.500hPa.20020901-20231130.175W_84S_174E_86N.csv"
path_co2_data = "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3C2M_005_mole_fraction_of_carbon_dioxide_in_free_troposphere.20020901-20120229.175W_60S_174E_86N.csv"
path_ozone_data = "C:/pale-blue-dot-challenge/data/g4.areaAvgTimeSeries.AIRX3STM_006_O3_VMR_A.1000hPa.20020901-20161031.175W_60S_172E_86N.csv"

y_name_ch4 = "Mean AIRS Methane (ppbv)"
y_name_co2 = "Mean AIRS Carbon Dioxide (ppm)"
y_name_o3 = "Mean AIRS Ozone (ppbv)"

file_ch4 = "ch4"
file_co2 = "co2"
file_o3 = "o3"

def create_chart(path, y_name, html_file, chart_title):
    data = pd.read_csv(path, skiprows=9,  usecols=[0,1], names=['Time',f'{y_name}'])

    # Read the times as dates and the methane concentrations as numeric values
    data['Time'] = pd.to_datetime(data['Time'])
    data[f'{y_name}'] = pd.to_numeric(data[f'{y_name}'])

    fig = px.line(data, x="Time", y=f'{y_name}', title=f'{chart_title}')
    fig.update_layout(title_x=0.5)
    fig.write_html(f"C:/pale-blue-dot-challenge/src/figures/{html_file}.html")

create_chart(path_ch4_data, y_name_ch4, file_ch4, "Methane")
create_chart(path_co2_data, y_name_co2, file_co2, "Carbon Dioxide")
create_chart(path_ozone_data, y_name_o3, file_o3, "Ozone")