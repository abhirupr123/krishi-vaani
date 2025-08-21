import pandas as pd
import os

def ingest_agmarknet_data(file_path: str):
    """
    Ingests and processes raw AGMARKNET data.
    """
    print(f"Processing AGMARKNET data from: {file_path}")
    try:
        # Load the raw data (e.g., from a CSV)
        df = pd.read_csv(file_path)

        # Example preprocessing steps
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        df = df[['commodity_name', 'market_name', 'arrival_date', 'modal_price']]
        df['modal_price'] = pd.to_numeric(df['modal_price'], errors='coerce')
        df.dropna(inplace=True)

        # Save the processed data to the processed directory
        output_path = os.path.join(os.path.dirname(file_path), '../processed/agmarknet_clean.csv')
        df.to_csv(output_path, index=False)
        print(f"Successfully processed and saved AGMARKNET data to: {output_path}")
    except Exception as e:
        print(f"Error processing AGMARKNET data: {e}")

if __name__ == "__main__":
    # Assuming raw data files are in the data/raw/ directory
    agmarknet_file = 'data/raw/agmarknet_data.csv'
    ingest_agmarknet_data(agmarknet_file)
