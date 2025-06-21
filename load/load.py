import psycopg2
from config import DB_CONFIG
from sqlalchemy import create_engine


def create_staging_tables():
    """Crea tablas de staging en PostgreSQL si no existen"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staging_customers (
            customer_id VARCHAR(50),
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(100),
            registration_date TIMESTAMP,
            extraction_source VARCHAR(50),
            extraction_date TIMESTAMP,
            PRIMARY KEY (customer_id, extraction_date)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staging_users (
            id INTEGER,
            name VARCHAR(100),
            username VARCHAR(50),
            email VARCHAR(100),
            phone VARCHAR(50),
            website VARCHAR(100),
            extraction_source VARCHAR(50),
            extraction_date TIMESTAMP,
            PRIMARY KEY (id, extraction_date)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staging_sales (
            transaction_id VARCHAR(50),
            product_id VARCHAR(50),
            quantity INTEGER,
            unit_price DECIMAL(10,2),
            sale_date DATE,
            customer_id VARCHAR(50),
            extraction_source VARCHAR(50),
            extraction_date TIMESTAMP,
            PRIMARY KEY (transaction_id, extraction_date)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staging_profiles (
            user_id VARCHAR(50),
            full_name VARCHAR(100),
            age INTEGER,
            preferences JSONB,
            last_login TIMESTAMP,
            extraction_source VARCHAR(50),
            extraction_date TIMESTAMP,
            PRIMARY KEY (user_id, extraction_date)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS staging_events (
            event_id VARCHAR(50),
            event_type VARCHAR(50),
            user_id VARCHAR(50),
            timestamp TIMESTAMP,
            value DECIMAL(10,2),
            extraction_source VARCHAR(50),
            extraction_date TIMESTAMP,
            PRIMARY KEY (event_id, extraction_date)
        )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Error al crear tablas de staging: {e}")


def load_to_postgres(df, table_name):
    """Carga un DataFrame a la tabla especificada en PostgreSQL"""
    try:
        create_staging_tables()

        db_url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
        engine = create_engine(db_url)

        df.to_sql(
            name=f"staging_{table_name}",
            con=engine,
            if_exists='append',
            index=False,
            method='multi'
        )

        engine.dispose()
        print(f"Datos cargados exitosamente en staging_{table_name}")

    except Exception as e:
        print(f"Error al cargar datos en PostgreSQL: {e}")