
import pickle
import numpy as np
import pandas as pd
from os.path import join

# run_id = 'c5836949a63e446bab1b0e2b74d748b5/artifacts'
# file_path = f"mlruns/1/{run_id}/pred.pkl"
# with open(file_path, "rb") as file_dataset:
#     dataset = pickle.load(file_dataset)

file_path = f"data/order/test/SH600004.pkl.target"
with open(file_path, "rb") as file_dataset:
    dataset = pickle.load(file_dataset)

print('Done')
# download own data https://qlib.readthedocs.io/en/latest/component/data.html#qlib-format-dataset