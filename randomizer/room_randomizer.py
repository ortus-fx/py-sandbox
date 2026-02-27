from collections.abc import Sequence

import numpy as np
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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


def put_in_rooms(grp: pd.Series, n_rooms, fill=pd.NA) -> pd.DataFrame:
    n_in_room = (grp.size + n_rooms - 1) // n_rooms  # ceil dividision
    expected_total_in_rooms = n_rooms * n_in_room

    if grp.size < expected_total_in_rooms:
        # number of missing values that should be added
        pad = pd.Series([fill] * (expected_total_in_rooms - grp.size), dtype=grp.dtype)
        grp = pd.concat([grp, pad], ignore_index=True)

    grp.index = pd.MultiIndex.from_product([np.arange(n_in_room), np.arange(n_rooms)])
    return grp.unstack(level=1)


if __name__ == "__main__":
    for i in range(3):
        try:
            raw = input("Input the Week Number: ")
            seed = int(raw)
            rooms = int(input("Enter Number of Rooms: "))
            mixer = shuffler(group_ls, seed)

            df = put_in_rooms(mixer, rooms).fillna("").astype(str)
            console = Console()

            table = Table(title=f"Room Assignments — Week {seed}", show_lines=True)
            for col in df.columns:
                table.add_column(str(col), justify="center", style="cyan")

            for row in df.values.tolist():
                table.add_row(*row)

            console.print(table)
            break

        except ValueError:
            remaining = 2 - i
            console.print(
                f"[bold red]'{raw}'[/bold red] is not a valid integer. [yellow]{remaining} attempt(s) left.[/yellow]"
            )

    else:
        console.print(
            Panel(
                "[bold red]You've exceeded the max attempts. Rerun the program.[/bold red]"
            )
        )
