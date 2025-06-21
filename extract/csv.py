import pandas as pd
from config import CSV_PATH

def extract_from_csv():
    """Extrae datos de ventas desde archivo CSV"""
    try:
        df = pd.read_csv(CSV_PATH)
        
        df['extraction_source'] = 'csv_file'
        df['extraction_date'] = pd.Timestamp.now()
        
        return df
        
    except Exception as e:
        print(f"Error en extracción CSV: {e}")
        return None