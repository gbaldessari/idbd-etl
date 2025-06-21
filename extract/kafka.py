import pandas as pd
from datetime import datetime
from config import KAFKA_TOPIC
import random
import time

def simulate_kafka_stream():
    """Simula la extracción de un stream de datos desde Kafka"""
    try:
        print(f"Simulando extracción de topic: {KAFKA_TOPIC}")
        
        data = []
        for i in range(10):
            record = {
                'event_id': f"evt_{random.randint(1000, 9999)}",
                'event_type': random.choice(['click', 'view', 'purchase']),
                'user_id': f"user_{random.randint(1, 100)}",
                'timestamp': datetime.now().isoformat(),
                'value': round(random.uniform(10, 100), 2)
            }
            data.append(record)
            time.sleep(0.1) 
            
        df = pd.DataFrame(data)
        
        df['extraction_source'] = 'kafka_stream'
        df['extraction_date'] = pd.Timestamp.now()
        
        return df
        
    except Exception as e:
        print(f"Error en extracción simulada de Kafka: {e}")
        return None