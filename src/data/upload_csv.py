import os
import tempfile
from pathlib import Path
import shutil
from nicegui import ui
from typing import Dict

ALLOWED_EXTENSIONS = {'.csv'}
MAX_FILE_SIZE = 10 * 1024 * 1024
TEMP_DIR = Path(tempfile.gettempdir()) / 'utabiri_data'

def is_valid_csv(filename: str) -> bool:
    """
    Validate if the file has a .csv extension.

    Args:
        filename (str): Name of the file to validate

    Returns:
        bool: True if file has .csv extension, False otherwise
    """
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
            
        ui.notify('File uploaded successfully! Navigate to Reports for insights.', type='positive')
        
    except Exception as e:
        ui.notify(f'Upload failed: {str(e)}', type='negative')
        raise

def setup_data_upload() -> None:
    """
    Create and configure the data upload UI component.
    
    Sets up a card with file upload functionality, supporting:
    - CSV file validation
    - Automatic upload on file selection
    - User feedback notifications
    """
    # Create a container with center alignment
    with ui.row().classes('w-full flex justify-center'):
        with ui.card().classes('w-[32rem] p-6 transition-shadow hover:shadow-xl'):
            ui.label('Upload Your Data').classes('text-xl font-bold mb-2')
            ui.upload(
                label='Upload CSV File',
                on_upload=handle_upload,
                multiple=False,
                auto_upload=True
            ).props('accept=.csv color=primary label="Select File"').classes('w-full')
            with ui.row().classes('items-center gap-2 mt-2'):
                ui.icon('info').classes('text-blue-600')
                ui.label('Only CSV files are supported').classes('text-sm text-gray-500')