import pandas as pd
import json

def get_data(clean_dataset):
    with open("../data/Clean_Dataset.csv", "r") as data:
        json.dump(clean_dataset, data)

    print(data)
get_data()
