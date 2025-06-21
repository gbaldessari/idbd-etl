import mysql.connector
import pandas as pd
from datetime import datetime, timedelta
from config import DB_CONFIG

def extract_from_mysql():
    """Extrae datos de clientes de MySQL (extracción incremental)"""
    try:
        mysql_config = {
            'host': 'localhost',
            'user': 'etl_user',
            'password': 'etl_password',
            'database': 'ecommerce_db'
        }
        
        conn = mysql.connector.connect(**mysql_config)
        
        query = """
        SELECT customer_id, first_name, last_name, email, registration_date 
        FROM customers 
        WHERE registration_date >= %s
        """
        
        cutoff_date = datetime.now() - timedelta(days=7)
        
        df = pd.read_sql(query, conn, params=(cutoff_date,))
        
        conn.close()
        
        df['extraction_source'] = 'mysql'
        df['extraction_date'] = datetime.now()
        
        return df
    
    except Exception as e:
        print(f"Error en extracción MySQL: {e}")
        return None