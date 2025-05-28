from sqlalchemy import select
from db_config import engine, metadata
from mapper import column_mapping


def build_dynamic_query(excel_columns: list, filter_column="serial_no", filter_value="XYZ123"):
    join_tables = set()
    selected_columns = []

    # Step 1: Resolve columns and track which tables are needed
    for excel_col in excel_columns:
        if excel_col in column_mapping:
            table_name, column_name = column_mapping[excel_col]
            table = metadata.tables.get(table_name)
            if table is not None and column_name in table.c:
                selected_columns.append(table.c[column_name])
                join_tables.add(table_name)

    # Step 2: Start with the base table
    base = metadata.tables["product"]
    joins = base

    # Step 3: Perform joins if needed
    if "warranty" in join_tables:
        joins = joins.join(
            metadata.tables["warranty"],
            base.c.serial_no == metadata.tables["warranty"].c.serial_no
        )
    if "part" in join_tables:
        joins = joins.join(
            metadata.tables["part"],
            base.c.part_id == metadata.tables["part"].c.id
        )

    # Step 4: Build the WHERE clause safely
    if filter_column not in base.c:
        raise ValueError(f"Invalid filter column: {filter_column}")

    stmt = select(*selected_columns).select_from(joins).where(
        base.c[filter_column] == filter_value
    )

    return stmt