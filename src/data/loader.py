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