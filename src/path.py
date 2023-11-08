import os

PATH_INDEX = os.path.dirname(os.path.abspath(__file__))
PATH_DATA = os.path.abspath(f'{PATH_INDEX}/../data')
PATH_DB = os.path.abspath(f'{PATH_INDEX}/../data/outputs')
PAHT_ENV = os.path.abspath(f'{PATH_INDEX}/../.env')

if __name__ == '__main__':
    print(f"PATH_INDEX = {PATH_INDEX}")
    print(f"PATH_DATA = {PATH_DATA}")