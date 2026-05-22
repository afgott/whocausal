# whocausal

A lightweight Python package for fetching epidemiological data from the World Health Organization (WHO) OData API, modeling causal hypotheses using Directed Acyclic Graphs (DAGs) and performing basic statistical estimation.

## Project Structure

*   `whocausal/loader.py`: Handles connection to the GHO API, pagination, and data cleaning using Pandas.
*   `whocausal/graph.py`: Manages causal graph topology and structural validation using NetworkX.
*   `whocausal/analyzer.py`: Runs statistical tests and multiple linear regressions using SciPy and Statsmodels.
*   `tests/`: Unit tests for ensuring package reliability via pytest.

## Tech Stack

*   **Data Handling:** Requests, Pandas
*   **Graph Theory:** NetworkX
*   **Statistics:** SciPy, Statsmodels
*   **Testing:** Pytest