import os
import json
import pandas as pd


def merge(path: str) -> str:
    """Read json files from folder and merge content of into one dataframe and save it as csv file.

    Args:
        path (str): Pass folder path

    Returns:
        str: Return csv file path
    """

    files = os.listdir(path)

    for i, file in enumerate(files):
        if file.endswith(".json"):
            with open(os.path.join(path, file), "r") as f:
                data_file = json.load(f)

            if i == 0:
                df = pd.DataFrame([data_file])
            else:
                df_file = pd.DataFrame([data_file])
                df = pd.concat([df, df_file])

    return df.to_csv(os.path.join("data", "merge_json.csv"), index=False)


if __name__ == "__main__":
    merge("data")
