import pandas as pd

df = pd.read_csv(
    "../Subway_base_network/seoul.txt",
    delimiter=" ",
    names=["no", "name", "line"],
    encoding="UTF-8",
)

# only nodes
df = df.iloc[
    :705,
]


def no_to_name(no):
    """
    parameter: stNO
    return: stName, line
    """
    name = df[df["no"] == no]["name"].values[0]
    line = df[df["no"] == no]["line"].values[0]
    return name, line
