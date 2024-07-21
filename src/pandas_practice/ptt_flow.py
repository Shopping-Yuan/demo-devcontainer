import glob

import pandas as pd

COLUMNS = [
    "推",
    "噓",
    "分數",
    "作者",
    "標題",
    "時間",
]
# Define functions
def get_text_file_paths() -> list[str]:
    return glob.glob(
        "/workspaces/demo-devcontainer/res_gossiping/*.txt"
    )

def e_text_file(path: str) -> list[str]:
    with open (path,'r') as f:
        return f.read()

def t_text_to_df_row_list(article_string: str) -> list[str]:
    reply_info_string = article_string.split("---split---")[-1]
    article_info = reply_info_string.split("\n")[1:-1]
    return  [" ".join(x.split(":")[1:]) for x in article_info[:]]


def t_combine_list_to_df(reply_info_list: list[list]) -> pd.DataFrame:
    return pd.DataFrame(
        data = reply_info_list,
        columns = COLUMNS,
    )

def l_df_to_csv(df: pd.DataFrame) -> None:
    df.to_csv("ptt.csv" , index = 0)

if __name__ == '__main__':
    # Get paths of all text files
    path_list = get_text_file_paths()

    # Loop for file paths
    data = []
    for path in path_list:
        # Extract text file
        article_string = e_text_file(path)

        # Text to list-element in DataFrame
        reply_info_list = t_text_to_df_row_list(article_string)
        data.append(reply_info_list)

    # Concat lists to DataFrame
    df = t_combine_list_to_df(data)

    # Load DataFrame to CSV
    l_df_to_csv(df)
