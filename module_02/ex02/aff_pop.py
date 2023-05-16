from load_csv import load_csv
from matplotlib import pyplot as plt
from sys import exit
import pandas as ps

CUTOFF_YEAR = "2050"
COUNTRY = "country"
THOUSANDS_MARKER = "k"
MILIONS_MARKER = "M"
BILLIONS_MARKER = "B"
LESS_THAN_10000_MARKER = 1 / 1000000


def plot_two_countries(population: ps.DataFrame, country1: str, country2: str):
    """
    Plots the population of two countries over time.
    :param population: the population data of all countries
    :param country1: Name of the first country
    :param country2: Name of the second country
    :return: None
    """

    # Check if the input is valid: the countries should be strings
    if not isinstance(country1, str) or not isinstance(country2, str):
        raise TypeError("Both countries need to be of type string")

    # Check if the input is valid: the population should be a DataFrame
    if not isinstance(population, ps.DataFrame):
        raise TypeError("DataFrame(pandas) expected")

    # Check if the input is valid: the countries should be in the DataFrame
    if country1 == country2:
        raise ValueError("Country one should not be the same as country two")

    if CUTOFF_YEAR not in population.columns:
        raise ValueError(
            "The CUTOFF_YEAR constant value is not contained in the columns")

    population.set_index(COUNTRY, inplace=True)

    population = population.loc[:, :CUTOFF_YEAR]
    population_stats = []
    years_x = population.columns.astype(int)
    scale_factors = {
        THOUSANDS_MARKER: 1 / 1000,
        MILIONS_MARKER: 1,
        BILLIONS_MARKER: 1000,
    }
    for country in [country1, country2]:
        population_in_millions_y = []
        population_stats = population.loc[country].values
        for num in population_stats:
            factor = scale_factors.get(num[-1])
            if factor is None:
                population_in_millions_y.append(
                    float(num) * LESS_THAN_10000_MARKER)
            else:
                population_in_millions_y.append(
                    float(num[:-1]) * scale_factors.get(num[-1]))
        plt.plot(years_x, population_in_millions_y, label=country)

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.grid()
    plt.legend()
    plt.xlim(years_x.min(), years_x.max())
    plt.ylim(0)
    plt.gca().set_yticklabels(
        [str(int(tick)) + 'M' for tick in plt.gca().get_yticks()])


def main():
    df = load_csv("population_total.csv")
    try:
        plot_two_countries(df, 'Germany', "France")
    except Exception as e:
        print("Error: ", e)
        exit(1)
    plt.show()


if __name__ == "__main__":
    main()
