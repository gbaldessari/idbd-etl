import requests
import pandas as pd
from config import API_URL
import json

def extract_from_api():
    """Extrae datos de usuarios desde API REST"""
    try:
        url = f"{API_URL}/users"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)

            df['address'] = df['address'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)
            df['company'] = df['company'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)

            df['extraction_source'] = 'api_rest'
            df['extraction_date'] = pd.Timestamp.now()

            df = df[['id', 'name', 'username', 'email', 'phone', 'website', 'extraction_source', 'extraction_date']]
            
            return df
        else:
            print(f"Error API: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error en extracción API: {e}")
        return None