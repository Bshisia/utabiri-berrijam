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