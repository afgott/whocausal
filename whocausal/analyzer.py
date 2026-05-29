import pandas as pd
import statsmodels.api as sm

class CausalAnalyzer:
    """Class for merging datasets and conducting causal analysis."""

    def __init__(self):
        pass

    def merge_datasets(self, df_cause: pd.DataFrame, df_effect: pd.DataFrame) -> pd.DataFrame:

        """Merge two datasets on 'country_code' and 'year' to ensure we have aligned data for analysis"""
        merged_df = pd.merge(df_cause, df_effect, on=['country_code', 'year'], how='inner')
        
        if merged_df.empty:
            raise ValueError("After merging, no data remains. Possible mismatch in years or countries.")
            
        return merged_df

    def estimate_effect(self, df: pd.DataFrame, cause_col: str, effect_col: str):
        
        """Conducts a basic OLS, estimates the effect of cause_col on effect_col """
        # Check if the required columns exist
        if cause_col not in df.columns or effect_col not in df.columns:
            raise KeyError(f"Columns {cause_col} or {effect_col} not found in the dataset")

        # X - our independent variable (cause)
        X = df[cause_col]
        # Add a constant (intercept) for proper regression calculation
        X = sm.add_constant(X)
        
        # y - our dependent variable (effect)
        y = df[effect_col]

        # Train the model
        model = sm.OLS(y, X).fit()
        
        # Return the summary
        return model.summary()