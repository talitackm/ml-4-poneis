# %%
import pandas as pd

with open("../data/dados_clones.csv", 'r') as open_file:
    data = open_file.read()

data_df = "\n".join([i.strip('"') for i in data.replace('""', '"').splitlines()])

with open("../data/dados_clone_fixed.csv", "w") as open_file:
    open_file.write(data_df)


# %%
df = pd.read_csv("../data/dados_clone_fixed.csv", low_memory=True)
df = (df[~df['General Jedi encarregado'].isna()]
        .drop_duplicates(subset=['p2o_master_id'], keep='first')
      )

df['p2o_master_id'] = df['p2o_master_id'].astype(int)

# %%
df.to_parquet("../data/dados_clone.parquet", index=False)
