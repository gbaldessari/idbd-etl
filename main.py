# main.py
from extract.db import extract_from_mysql
from extract.api import extract_from_api
from extract.csv import extract_from_csv
from extract.json import extract_from_json
from extract.kafka import simulate_kafka_stream
from load.load import load_to_postgres

def main():
    print("Iniciando proceso ETL - Extracción desde 5 fuentes")
    
    # 1. Extracción desde MySQL (base de datos relacional)
    print("\nExtrayendo datos de MySQL...")
    customers_df = extract_from_mysql()
    if customers_df is not None:
        load_to_postgres(customers_df, 'customers')
    
    # 2. Extracción desde API REST
    print("\nExtrayendo datos de API REST...")
    users_df = extract_from_api()
    if users_df is not None:
        load_to_postgres(users_df, 'users')
    
    # 3. Extracción desde archivo CSV
    print("\nExtrayendo datos de archivo CSV...")
    sales_df = extract_from_csv()
    if sales_df is not None:
        load_to_postgres(sales_df, 'sales')
    
    # 4. Extracción desde archivo JSON
    print("\nExtrayendo datos de archivo JSON...")
    profiles_df = extract_from_json()
    if profiles_df is not None:
        load_to_postgres(profiles_df, 'profiles')
    
    # 5. Extracción simulada desde Kafka (stream)
    print("\nExtrayendo datos simulados de Kafka...")
    events_df = simulate_kafka_stream()
    if events_df is not None:
        load_to_postgres(events_df, 'events')
    
    print("\nProceso de extracción completado!")

if __name__ == "__main__":
    main()