### Getting started

```bash
# 1. Install uv project manager (if you don't already have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Activate the virtual environment
source .venv/bin/activate

# 4. Run the Notebooks in order 00 -> 01 -> 02
```

### Project Structure
```bash
├── data
│   ├── processed                           # Stores train/val/test splits
│   └── raw                                 # Stores raw, unprocessed dataset
│       └── online_shoppers_intention.csv
├── src
│   └── machinelearningproject_ct4101
│       ├── notebooks                               # The notebook for the project
│       │   ├── 00 - DataAudit.ipynb                # Explores dataset for missing values, outliers etc
│       │   ├── 01 - SplitAndPreProcessData.ipynb   # Log transform, encode, scale and save training splits 
│       │   └── 02 - Baseline.ipynb                 # Train a dummy classifier 
│       └── utils.py                                # Utilities for plotting and save/loading splits
```
