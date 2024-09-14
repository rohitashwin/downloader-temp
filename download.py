import pandas as pd
from tqdm import tqdm
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("jenhsia/ragged", "kilt_wikipedia")
df = pd.DataFrame(dataset['train'])

# Write JSONL with progress tracking
with open("/ashwin-1/kilt_wikipedia.jsonl", "w") as f:
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Writing to JSONL"):
        f.write(row.to_json() + "\n")
