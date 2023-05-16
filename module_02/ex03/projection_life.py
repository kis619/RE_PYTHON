from load_csv import load_csv
from exceptions import YearNotFoundException
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from sys import exit

YEAR = "1900"


def load_data(year):
    """
    Loads the data from the csv files.
    :param year: the year for which the data should be loaded
    :return: the data for the given year
    raises YearNotFoundException if the year is not found in the data
    """
    life_expectancy_df = load_csv("life_expectancy_years.csv")
    gdp_per_capita_df = load_csv(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    try:
        life_expectancy_df_year = life_expectancy_df[year]
        gdp_per_capita_df_year = gdp_per_capita_df[year]
    except KeyError:
        raise YearNotFoundException("load_data: Year not found")
    return gdp_per_capita_df_year, life_expectancy_df_year


def scatter_plot_for_life_expectancy_gdp(year: int):
    """
    Creates a scatter plot for the given year.
    """
    try:
        gdp_x, life_expectancy_y = load_data(year)
    except YearNotFoundException as msg:
        print(msg)
        exit(1)
    except ...:
        print("Something went wrong")
        exit(42)

    plt.scatter(gdp_x, life_expectancy_y)

    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_xticks([300, 1000, 10000])
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda x, _: x if x < 1000 else f"{int(x) // 1000}k"))

    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")


def main():
    """
    main function: gets a year from the user,
    creates a scatter plot which it shows
    """
    scatter_plot_for_life_expectancy_gdp(YEAR)

    plt.show()


if __name__ == '__main__':
    main()
