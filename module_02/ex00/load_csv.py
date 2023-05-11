import pandas as pd
import csv
import colored_traceback  # for colored traceback
colored_traceback.add_hook()


def load_csv(path) -> pd.DataFrame:  # pandas
    """
    Loads csv file into pandas DataFrame
    Args:
        path (str): path to csv file

    Returns:
        pandas.DataFrame: DataFrame with data from csv file
        none: if file not found, empty, or has wrong format

    Errors:
        FileNotFoundError: if file not found
        pd.errors.ParserError: if file has wrong format
        pd.errors.EmptyDataError: if file is empty
        PermissionError: if no read permissions
        UnicodeDecodeError: if file contains characters that cannot be decoded
    """

    try:
        ds = pd.read_csv(path)
    except FileNotFoundError:
        print(f'load_csv: File {path} not found')
        return None
    except pd.errors.ParserError:
        print('load_csv: Unidentified file format')
        return None
    except pd.errors.EmptyDataError:
        print(f'load_csv: File {path} is empty')
        return None
    except pd.errors.DtypeWarning:
        print('load_csv: Inconsistent data types across the columns')
        return None
    except PermissionError:
        print('load_csv: Permission denied')
        return None
    except UnicodeDecodeError:
        print(f'load_csv: File {path} contains characters '
              f'that cannot be decoded using the specified encoding')
        return None
    except Exception as e:
        print(f'load_csv: {e}')
        return None
    print("Dataset dimensions:", ds.shape)
    return ds


def load_csv_with_csv(path):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f'File {path} not found')
        yield None


def main():
    print(load_csv('population_total.csv'))


if __name__ == '__main__':
    main()
    ...
