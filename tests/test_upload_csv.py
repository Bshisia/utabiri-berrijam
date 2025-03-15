from nicegui import ui
import os
import tempfile
from pathlib import Path
import shutil

ALLOWED_EXTENSIONS = {'.csv'}
MAX_FILE_SIZE = 10 * 1024 * 1024
TEMP_DIR = Path(tempfile.gettempdir()) / 'utabiri_data'

def is_valid_csv(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

async def handle_upload(event) -> None:
    try:
        temp_file = event.content
        filename = event.name

        if not is_valid_csv(filename):
            ui.notify('Only CSV files are allowed', type='negative')
            return

        temp_file.seek(0, os.SEEK_END)
        size = temp_file.tell()
        if size > MAX_FILE_SIZE:
            ui.notify(f'File too large. Maximum size is {MAX_FILE_SIZE/1024/1024}MB', type='negative')
            return

        TEMP_DIR.mkdir(parents=True, exist_ok=True)
        
        file_path = TEMP_DIR / filename
        temp_file.seek(0)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(temp_file, f)
            
        ui.notify('File uploaded successfully!', type='positive')
        
    except Exception as e:
        ui.notify(f'Upload failed: {str(e)}', type='negative')
        raise

def setup_data_upload() -> None:
    with ui.card().classes('w-full max-w-4xl p-6'):
        ui.label('Upload Your Data').classes('text-xl font-bold mb-2')
        ui.upload(
            label='Upload CSV File',
            on_upload=handle_upload,
            multiple=False,
            auto_upload=True
        ).props('accept=.csv color=primary label="Select File"').classes('w-full')