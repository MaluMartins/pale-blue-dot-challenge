import pandas as pd
import plotly.express as px

path_ch4 = "C:\\pale-blue-dot-challenge\\data\\g4.areaAvgTimeSeries.AIRS3STM_006_CH4_VMR_A.500hPa.20020901-20231130.175W_84S_174E_86N.csv"

data = pd.read_csv(path_ch4, skiprows=9,  usecols=[0,1], names=['Time','Mean AIRS Methane'])

# Read the times as dates and the methane concentrations as numeric values
data['Time'] = pd.to_datetime(data['Time'])
data['Mean AIRS Methane'] = pd.to_numeric(data['Mean AIRS Methane'])

figCH4 = px.line(data, x="Time", y="Mean AIRS Methane")
figCH4.write_html("C:\\pale-blue-dot-challenge\\src\\figures")