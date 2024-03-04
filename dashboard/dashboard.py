import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

aoti_df = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
chan_df = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
ding_df = pd.read_csv("PRSA_Data_Dingling_20130301-20170228.csv")
dong_df = pd.read_csv("PRSA_Data_Dongsi_20130301-20170228.csv")

#print(aoti_df.head)

st.header('Air Quality Index CO and PM2.5 :sparkles:')

st.write("Hii! Welcome to my AQI Web. I want to show you the Time Series CO Data in 4 different Place in China")


#Data Cleaning
aoti_df['Date'] = pd.to_datetime(aoti_df[['year', 'month', 'day', 'hour']])
aoti_df = aoti_df.set_index('Date')
aoti_df_interpolated = aoti_df.interpolate(method='time')

chan_df['Date'] = pd.to_datetime(chan_df[['year', 'month', 'day', 'hour']])
chan_df = chan_df.set_index('Date')
chan_df_interpolated = chan_df.interpolate(method='time')

ding_df['Date'] = pd.to_datetime(ding_df[['year', 'month', 'day', 'hour']])
ding_df = ding_df.set_index('Date')
ding_df_interpolated = ding_df.interpolate(method='time')

dong_df['Date'] = pd.to_datetime(dong_df[['year', 'month', 'day', 'hour']])
dong_df = dong_df.set_index('Date')
dong_df_interpolated = dong_df.interpolate(method='time')


#EDA
aoti_monthly_avg_CO = aoti_df_interpolated.groupby(['year', 'month'])['CO'].mean()
chan_monthly_avg_CO = chan_df_interpolated.groupby(['year', 'month'])['CO'].mean()
ding_monthly_avg_CO = ding_df_interpolated.groupby(['year', 'month'])['CO'].mean()
dong_monthly_avg_CO = dong_df_interpolated.groupby(['year', 'month'])['CO'].mean()

#Vsualization
aoti_df = aoti_monthly_avg_CO.reset_index()
chan_df = chan_monthly_avg_CO.reset_index()
ding_df = ding_monthly_avg_CO.reset_index()
dong_df = dong_monthly_avg_CO.reset_index()

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(aoti_df.index, aoti_df['CO'], label='Aoti', marker='o', linestyle='-')
ax.plot(chan_df.index, chan_df['CO'], label='Chan', marker='o', linestyle='-')
ax.plot(ding_df.index, ding_df['CO'], label='Ding', marker='o', linestyle='-')
ax.plot(dong_df.index, dong_df['CO'], label='Dong', marker='o', linestyle='-')

# Customize x-axis labels to show both year and month
xticks_labels = [f"{int(row['year'])}-{int(row['month']):02d}" for index, row in aoti_df.iterrows()]
ax.set_xticks(aoti_df.index)
ax.set_xticklabels(xticks_labels, rotation=90, ha='right')

# Adding labels and title
ax.set_xlabel('Year-Month')
ax.set_ylabel('Monthly Average CO')
ax.set_title('Monthly Average CO for Different Locations Over the Years')

# Adding legend
ax.legend()

# Display the plot using Streamlit
st.pyplot(fig)

st.write("As you can see on the visualization, There was an increase in Carbon Monoxide levels in 2015, precisely at the end of the year, namely December. Not only in one place, but the increase occurred in all places, although with varying intensity")