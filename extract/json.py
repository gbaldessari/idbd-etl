import pandas as pd
import json
from config import JSON_PATH

def extract_from_json():
    """Extrae datos de perfil de usuario desde archivo JSON"""
    try:
        with open(JSON_PATH, 'r') as f:
            data = json.load(f)
        
        df = pd.DataFrame(data)
        
        df['preferences'] = df['preferences'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else x)
        
        df['extraction_source'] = 'json_file'
        df['extraction_date'] = pd.Timestamp.now()
        
        return df
        
    except Exception as e:
        print(f"Error en extracción JSON: {e}")
        return None