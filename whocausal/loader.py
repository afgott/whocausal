import requests
import pandas as pd

class WHODataloader:
    """ A class to load and clean WHO data from the official API."""

    Base_URL = "https://ghoapi.azureedge.net/api/"

    def __init__(self):
        pass

    def fetch_indicator(self, indicator_code: str) -> pd.DataFrame:
        """Fetches data for a specific indicator code from the WHO API and returns it as a cleaned DataFrame."""
        url = f"{self.Base_URL}{indicator_code}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(f"Connection error: {e}")
        
        raw_data = response.json()
        
        if 'value' not in raw_data or not raw_data['value']:
            raise ValueError(f"Indicator {indicator_code} not found or empty.")
            
        df = pd.DataFrame(raw_data['value'])

        required_columns = ['SpatialDim', 'TimeDim', 'NumericValue']
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"Column {col} is missing from the API response.")
            
        # Data cleaning and transformation
        df_cleaned = df[required_columns].dropna().copy()
        df_cleaned['TimeDim'] = df_cleaned['TimeDim'].astype(int)
        df_cleaned['NumericValue'] = pd.to_numeric(df_cleaned['NumericValue'])
        
        df_cleaned = df_cleaned.rename(columns={
            'SpatialDim': 'country_code',
            'TimeDim': 'year',
            'NumericValue': indicator_code.lower()
        })
        
        # Filter out rows with invalid country codes
        df_cleaned = df_cleaned[df_cleaned['country_code'].str.len() == 3]
        
        return df_cleaned.reset_index(drop=True)