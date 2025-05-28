from query_builder import build_dynamic_query
from db_config import engine

def main():
    excel_columns = ["ItemPrice", "ItemCategory"]  # Simulating Excel headers
    query = build_dynamic_query(excel_columns, filter_value="XYZ123")

    print("Generated SQL Query:")
    print(query)

    with engine.connect() as conn:
        result = conn.execute(query)
        for row in result.fetchall():
            print(row)

if __name__ == "__main__":
    main()
