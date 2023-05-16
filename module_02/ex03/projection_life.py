from load_csv import load_csv

# Create a program that calls the load function from the first exercise,
# loads the files "income_per_person_gdppercapita_ppp_inflation_adjusted.csv" and "life_expectancy_years.csv",
# and displays the projection of life expectancy in relation to the gross national product of
# the year 1900 for each country.
# Your graph must have a title, a legend for each axis and a legend for each graph.
# You must display the year 1900.

def main():
    life_expectancy_df = load_csv("life_expectancy_years.csv")
    gdp_per_capita_df = load_csv("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_df_1900 = life_expectancy_df.loc[:, "1900"]
    gdp_per_capita_df_1900 = gdp_per_capita_df.loc[:, "1900"]
    print(life_expectancy_df_1900)
    print(gdp_per_capita_df_1900)

    
if __name__ == '__main__':
	main()