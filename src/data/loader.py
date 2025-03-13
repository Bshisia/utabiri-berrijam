def load_data():
    try:
        if not os.path.exists(DATA_PATH):
            ui.notify(f"Error: Data file not found at {DATA_PATH}", type="negative")
            return None
        return pd.read_csv(DATA_PATH)
    except Exception as ex:
        ui.notify(f"Error loading data: {ex}", type="negative")
        return None


def init_dashboard():
    # Load the data
    df = load_data()
    if df is not None:
        # Create age group first
        df = create_age_groups(df)

        with ui.column().classes("w-full"):

            # Add results section (will be updated)
            global results_section
            results_section = ui.column().classes("w-full")

  
def create_age_groups(df):
    try:
        df_copy = df.copy()
        bins = [0, 40, 60, 80, 100]
        labels = ["<40", "40-60", "60-80", ">80"]
        df_copy["Age Group"] = pd.cut(
            df_copy["age"], bins=bins, labels=labels, right=False
        )
        return df_copy
    except Exception as ex:
        ui.notify(f"Error creating age groups: {ex}", type="negative")
        return df     
    

def show_data_preview(df):
    """Show data preview table with pagination"""
    with ui.card().tight().classes("w-full mx-auto my-4"):
        ui.label("Data Preview").classes("text-xl font-bold p-4")

        # Convert the first 5 rows to a list of dictionaries
        preview_data = df.head().to_dict("records")
        
        # Add row numbers
        for i, row in enumerate(preview_data):
            row["#"] = i + 1
        
        # Define columns including row number
        columns = [
            {"name": "#", "label": "#", "field": "#"},
            *[
                {"name": str(col), "label": str(col), "field": str(col)}
                for col in df.columns
            ],
        ]
