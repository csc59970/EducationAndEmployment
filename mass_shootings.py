# import the datasets:
import pandas as pd
shootings_url = 'https://raw.githubusercontent.com/csc59970/GunControl/master/mass_shootings.csv'
shootings_df = pd.read_csv(shootings_url)

shootings_df['Year'] = shootings_df['Incident Date'].str.split().str.get(2)

shootings_df = shootings_df.drop(columns=['Address', 'Incident Date', 'City Or County', 'Operations'])

shootings_df = shootings_df.loc[(shootings_df['Year'] <'2019') & (shootings_df['Year'] >= '2017')]

numKilledInjured = shootings_df.groupby(['State', 'Year'], as_index=False)[["# Killed", "# Injured"]].sum()

numKilledInjured = numKilledInjured.pivot(index='State', columns='Year', values=['# Killed', '# Injured']).reindex(states).reset_index('State')

numKilledInjured.fillna(value=0, inplace=True)


# month,state,permit,permit_recheck,handgun,long_gun,other,multiple,admin,prepawn_handgun,prepawn_long_gun,prepawn_other,redemption_handgun,redemption_long_gun,redemption_other,returned_handgun,returned_long_gun,returned_other,rentals_handgun,rentals_long_gun,private_sale_handgun,private_sale_long_gun,private_sale_other,return_to_seller_handgun,return_to_seller_long_gun,return_to_seller_other,totals





census_url = 'https://raw.githubusercontent.com/csc59970/GunControl/master/census.csv'
census_df = pd.read_csv(census_url, thousands=',') # the thousands parameter gets rid of the commas in the df

census_df = census_df.rename(index=str, columns={"Geographic Area\n\n": "State"})

census_df = census_df.drop(columns=['2010', '2011', '2012', '2013', '2014', '2015', '2016'])
census_monthly = pd.DataFrame({'State': census_df.State, '2017': census_df['2017'] // 12, '2018': census_df['2018'] // 12})





# -------

census_url = 'https://raw.githubusercontent.com/csc59970/GunControl/master/census.csv'
census_df = pd.read_csv(census_url, thousands=',') # the thousands parameter gets rid of the commas in the df

census_df = census_df.rename(index=str, columns={"Geographic Area\n\n": "State"})

census_df = census_df.drop(columns=['2010', '2011', '2012', '2013', '2014', '2015', '2016'])
census_monthly = pd.DataFrame({'State': census_df.State, '2017': census_df['2017'] // 12, '2018': census_df['2018'] // 12})


# import the datasets:
import pandas as pd
shootings_url = 'https://raw.githubusercontent.com/csc59970/GunControl/master/mass_shootings.csv'
shootings_df = pd.read_csv(shootings_url)


shootings_df['Year'] = shootings_df['Incident Date'].str.split().str.get(2)

shootings_df = shootings_df.drop(columns=['Address', 'Incident Date', 'City Or County', 'Operations'])

shootings_df = shootings_df.loc[(shootings_df['Year'] <'2019') & (shootings_df['Year'] >= '2017')]

numKilledInjured = shootings_df.groupby(['State', 'Year'], as_index=False)[["# Killed", "# Injured"]].sum()

# Change order of states to match that of the census df
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
       'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
       'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
       'New Jersey', 'New Mexico', 'New York', 'North Carolina',
       'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
       'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
       'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
       'West Virginia', 'Wisconsin', 'Wyoming']

numKilledInjured = numKilledInjured.pivot(index='State', columns='Year', values=['# Killed', '# Injured']).reindex(states).reset_index('State')

numKilledInjured.fillna(value=0, inplace=True)

killed = numKilledInjured.values[:, 1:3] / census_monthly.values[:, 1:]

injured = numKilledInjured.values[:, 3:] / census_monthly.values[:, 1:]

probs_df = pd.DataFrame({'State':states, 'Killed Prob 2017': killed[:, 0], 'Killed Prob 2018': killed[:, 1], 'Injured Prob 2017': injured[:, 0], 'Injured Prob 2018': injured[:, 1]})

probs_df = probs_df.set_index('State')


probs_df.plot(figsize=(20, 5), kind="bar", align="center")
plt.title("Probability of getting killed or injured from a mass shooting per state in 2017 and 2018")
plt.xlabel("State")
plt.ylabel("Probability")
plt.show()