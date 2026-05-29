from whocausal.loader import WHODataloader
from whocausal.graph import CausalGraph
from whocausal.analyzer import CausalAnalyzer

def main():
    print("Initializing causal graph...")
    graph = CausalGraph()
    graph.add_edge("NCD_BMI_30A", "WHOSIS_000004")

    print("Loading data from WHO (this may take a few seconds)...")
    loader = WHODataloader()
    df_obesity = loader.fetch_indicator("NCD_BMI_30A")
    df_mortality = loader.fetch_indicator("WHOSIS_000004")

    print("Analyzing data and calculating OLS regression...")
    analyzer = CausalAnalyzer()
    df_merged = analyzer.merge_datasets(df_obesity, df_mortality)

    report = analyzer.estimate_effect(
        df=df_merged, 
        cause_col="ncd_bmi_30a", 
        effect_col="whosis_000004"
    )
    
    print("\n=== Results ===")
    print(report)

if __name__ == "__main__":
    main()