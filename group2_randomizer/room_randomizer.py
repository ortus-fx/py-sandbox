from collections.abc import Sequence

import numpy as np
import pandas as pd

# from tabulate import tabulate   # I commented this line out bcos you will need to `pip install tabulate` before use
from group2 import first_lastname, group_ls


@first_lastname  # this decorator adds selects the first and last names
def shuffler(
    grp_ls: Sequence[str], seed: int
) -> pd.Series:  # I like type check validation bcos it help my IDE catch errors quicker
    """
    Takes a Sequence of string elements and a seed value as arguements
    shuffles the Sequence and ...
    Returns a pandas series with string data types
    """
    rng = np.random.default_rng(seed=seed)
    rng.shuffle(grp_ls)
    return pd.Series(grp_ls, dtype="string")


def into_rooms(grp_ls: pd.Series) -> pd.DataFrame:
    """
    Takes a panda Series as arguement
    reshapes the values to 7 columns, leaving the rows flexible
    Returns a panada dataframe with column name Room 1 - 7
    """
    df = pd.DataFrame(
        grp_ls.values.reshape(-1, 7),
        columns=["Room 1", "Room 2", "Room 3", "Room 4", "Room 5", "Room 6", "Room 7"],
    )
    return df


if __name__ == "__main__":
    for i in range(3):
        try:
            raw = input("Input the Week Number: ")
            seed = int(raw)
            mixer = shuffler(group_ls, seed)
            print(into_rooms(mixer).to_string(index=False, justify="center"))

            # incase you install the `tabulate` you can unccoment the print below an comment the one above
            # print(
            #     tabulate(
            #         into_rooms(mixer),
            #         headers="keys",
            #         tablefmt="pretty",
            #         colalign=("left", "right", "center"),
            #     )
            # )
            break
        except ValueError:
            remaining = 2 - i
            print(f"'{raw}' is not a valid integer. {remaining} attempt(s) left.")
    else:
        print("You've exceeded the max attempts. Rerun the program.")
