import sys
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv
from exceptions import InvalidDataError, CityNotFoundError


def get_countries_for_city(city: str, cities_data: pd.DataFrame):
    try:
        countries = cities_data[cities_data['city']
                                == city]['country'].unique().tolist()
        if not countries:
            raise CityNotFoundError(f"City '{city}' not found.")
    except KeyError:
        raise InvalidDataError(
            "InvalidDataError: Data file is missing required columns.")
    except TypeError:
        raise InvalidDataError(
            "InvalidDataError: Data file is not a pandas DataFrame.")
    return countries


def user_selects_country(city_and_one_or_more_countries):
    while True:
        try:
            country_index = int(input("Choose a country: "))
        except ValueError:
            print("Invalid choice")
            continue
        except KeyboardInterrupt:
            print("\b\bInvalid choice")
            continue
        except EOFError:
            print("Invalid choice")
            sys.exit(69)
        if (country_index > 0 and
                country_index <= len(city_and_one_or_more_countries)):
            return city_and_one_or_more_countries[country_index - 1]
        print("Invalid choice")


def get_country(city):
    country = None
    cities = load_csv("worldcities.csv")

    if cities is None:
        print("Error loading file")
        return None

    try:
        city_and_one_or_more_countries = get_countries_for_city(city, cities)
    except Exception as e:
        print("\033[1;31;40mError", e, "\033[0m", sep="")
        return None
    possible_countries = len(city_and_one_or_more_countries)
    if possible_countries == 1:
        country = city_and_one_or_more_countries[0]
    elif possible_countries > 1:
        print('\n'.join([f"{idx+1}. {country}" for idx,
              country in enumerate(city_and_one_or_more_countries)]))
        country = user_selects_country(city_and_one_or_more_countries)
    return country


def create_plot(country):

    ds = load_csv("life_expectancy_years.csv")
    if ds is None:
        print("Error loading file")
        return None
    country_data = (ds[ds['country'] == country].iloc[:, 1:])
    years = country_data.columns.astype(int)
    population = country_data.iloc[0]
    plt.title(f"Life expectancy in {country}")
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.plot(years, population)


def main():
    country = get_country("Wolfsburg")
    if country is None:
        return None
    create_plot(country)
    plt.show()


if __name__ == "__main__":
    main()
