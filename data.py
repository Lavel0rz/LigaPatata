from pathlib import Path
import pandas as pd
entries = Path('dfs/')
dfs =[]
for entry in entries.iterdir():
    dfs.append(pd.read_csv(entry))


