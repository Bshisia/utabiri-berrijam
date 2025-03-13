import ui


def show_data_preview(df):
    """
    Show data preview table with pagination.

    This function displays a preview of the data in a table format with pagination.
    It shows the first 5 rows of the DataFrame and includes row numbers.
    
    Args:
        df (pd.DataFrame): The input data as a pandas DataFrame.
    """
    with ui.card().tight().classes("w-full mx-auto my-4"):
        ui.label("Data Preview").classes("text-xl font-bold p-4")

        preview_data = df.head().to_dict("records")
        
        for i, row in enumerate(preview_data):
            row["#"] = i + 1
        
        columns = [
            {"name": "#", "label": "#", "field": "#"},
            *[
                {"name": str(col), "label": str(col), "field": str(col)}
                for col in df.columns
            ],
        ]
        
        ui.table(columns=columns, rows=preview_data, row_key="#").classes("w-full")
        
        ui.label(f"Showing 5 of {len(df)} records").classes("text-sm text-gray-600 p-4")