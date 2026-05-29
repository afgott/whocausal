# whocausal

A lightweight Python package for fetching public health and socioeconomic data from the World Health Organization (WHO) OData API, modeling causal hypotheses using Directed Acyclic Graphs (DAGs), and performing statistical estimation.

This tool demonstrates the end-to-end pipeline of causal inference: from automated data collection to structural validation and basic Ordinary Least Squares (OLS) regression.

## Key Features
* **Automated Data Fetching:** Downloads, cleans, and merges WHO indicators directly into pandas DataFrames.
* **Causal Graph Validation:** Builds structural models using `NetworkX`, with built-in safeguards to enforce acyclic logic (DAGs).
* **Statistical Engine:** Estimates relationships between variables using `statsmodels` to address potential confounders.

## Project Structure
* `whocausal/loader.py`: Handles connection to the GHO API, pagination, and data cleaning.
* `whocausal/graph.py`: Manages causal graph topology and structural validation.
* `whocausal/analyzer.py`: Runs statistical tests and multiple linear regressions.
* `tests/`: Mock-based unit tests for ensuring package reliability via pytest.

## Quick Start

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/afgott/whocausal.git](https://github.com/afgott/whocausal.git)
cd whocausal
pip install pandas requests networkx statsmodels pytest
```

### 2. Usage Example
Create a `main.py` in the root directory to run a basic pipeline (e.g., testing the relationship between Obesity and Premature Mortality):

```python
from whocausal.loader import WHODataloader
from whocausal.graph import CausalGraph
from whocausal.analyzer import CausalAnalyzer

# 1. Define the causal structure safely
graph = CausalGraph()
graph.add_edge("NCD_BMI_30A", "WHOSIS_000004")

# 2. Fetch real-world data from WHO API
loader = WHODataloader()
df_obesity = loader.fetch_indicator("NCD_BMI_30A")
df_mortality = loader.fetch_indicator("WHOSIS_000004")

# 3. Merge and analyze the effect
analyzer = CausalAnalyzer()
df_merged = analyzer.merge_datasets(df_obesity, df_mortality)

report = analyzer.estimate_effect(
    df=df_merged, 
    cause_col="ncd_bmi_30a", 
    effect_col="whosis_000004"
)
print(report)
```

## Running Tests
To verify the data loader using mock API responses, run:
```bash
pytest
```