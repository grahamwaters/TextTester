import pandas as pd
import plotly.express as px
df = pd.read_csv('owid-covid-data.csv')
df.head()
print("Shape of Data Set is: ", df.shape)
print("Min and Max dates are: ", df.date.min(), df.date.max())
## Drop rows corresponding to the World
df = df[df.location != 'World']
## Sort df by date
df = df.sort_values(by=['date'])
df_latest = df[df.date == df.date.max()]
print("Date from the last date: ", df_latest.shape)

df_latest.head()

fig = px.choropleth(df, locations="iso_code",
                    color="new_cases",
                    hover_name="location",
                    animation_frame="date",
                    title = "Daily new COVID cases",
                    color_continuous_scale=px.colors.sequential.PuRd)

fig["layout"].pop("updatemenus")
fig.show()

df['new_date'] = pd.to_datetime(df['date'])
df['Year-Week'] = df['new_date'].dt.strftime('%Y-%U')
df['Year-Week'].head()

fig = px.choropleth(df, locations="iso_code",
                    color="total_cases",
                    hover_name="location", # column to add to hover information
                    animation_frame="Year-Week",
                    title = "Weekly total COVID cases",
                    color_continuous_scale=px.colors.sequential.PuRd)

# fig["layout"].pop("updatemenus")
fig.show()
df_us = pd.read_csv('covid-19-data/us-counties.csv')
df_us['new_date'] = pd.to_datetime(df_us['date'])
df_us['Year-Week'] = df_us['new_date'].dt.strftime('%Y-%U')
df_us.head()
df_us.shape

df_us = df_us.sort_values(by=['county', 'state', 'new_date'])
df_us_week = df_us.groupby(['county', 'state', 'fips', 'Year-Week']).first().reset_index()
df_us_week
df_us_week.head(100)
df_us_week['cases'].max(), df_us_week['cases'].min()
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][100]
df_us_week = df_us_week.sort_values(by=['Year-Week'])
fig = px.choropleth(df_us_week, geojson=counties, locations='fips', color='cases',
                           color_continuous_scale=px.colors.sequential.OrRd,
                           title = "Total Weekly Cases by Counties",
                           scope="usa",
                           animation_frame="Year-Week",
                          )
fig["layout"].pop("updatemenus")
fig.show()
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
df_us_week['state_code'] = df_us_week['state'].map(us_state_abbrev)
df_us_week.head()
test = df_us_week[df_us_week.cases > 15000]
test
df_us_week = df_us_week.sort_values(by=['Year-Week'])
fig = px.choropleth(df_us_week, locations='state_code', color='cases',
                           color_continuous_scale=px.colors.sequential.OrRd,
                           hover_name = 'state_code',
                           locationmode = 'USA-states',
                           animation_frame="Year-Week",
                          )
fig.update_layout(
    title_text = 'Weekly Total Deaths by State', # Create a Title
    geo_scope='usa',  # Plot only the USA instead of globe
)
fig.show()  # Output the plot to the screen