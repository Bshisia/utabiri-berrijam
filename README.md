![Berrijam](https://static.wixstatic.com/media/fd277b_9a440733fa364d559cc6742473d0617d~mv2.png/v1/fill/w_97,h_54,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Berrijam%20Logo.png)
## 
**Berrijam-AI** is an AI-powered data analysis tool designed to simplify the process of deriving insights from data for non-technical users. The application guides users through defining their problem or goal, uploading CSV data files, previewing the data, and presenting a final discoveries report in a clean, accessible, and user-friendly manner. The UI is built using NiceGUI in Python to create an engaging and visually compelling web-based interface.

## Table of Contents
- Features
- Installation
- Usage
- Configuration
- Technologies
- Contributing
- Acknowledgments

## Features
- User-friendly interface for defining problems or goals
- CSV data file upload and validation
- Data preview functionality
- Interactive filters for data analysis
- Summary tab with key metrics and clinical findings
- PDF report generation

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
```sh
    git clone https://learn.zone01kisumu.ke/git/hokwach/utabiri-reimagines.git
    cd utabiri-reimagines
```

2. Create a virtual environment:
```sh
    python -m venv myenv
```

3. Activate the virtual environment:
- On Windows:
```sh
        myenv\Scripts\activate
```
- On macOS/Linux:
```sh
        source myenv/bin/activate
```

4. Install the required dependencies:
```sh
    pip install -r requirements.txt
```

5. Run the application:
```sh
    python src/main.py
```

## Usage
To use the application, follow these steps:

1. Open the application in your web browser.
2. Define your problem or goal using the provided interface.
3. Upload your CSV data file.
4. Preview the data file to ensure it is correctly formatted.
5. Apply interactive filters to analyze the data.
6. View the final discoveries report in the summary tab.
7. Generate a PDF report of the findings.

Example code snippet for uploading a CSV file:
```python
from nicegui import ui

def setup_data_upload():
    with ui.card().classes('w-full max-w-4xl p-6'):
        ui.label('Upload Your Data').classes('text-xl font-bold mb-2')
        ui.upload(
            label='Upload CSV File',
            on_upload=handle_upload,
            multiple=False,
            auto_upload=True
        ).props('accept=.csv color=primary label="Select File"').classes('w-full')
```

## Configuration
The following options can be configured in the application:

- `ALLOWED_EXTENSIONS`: Set of allowed file extensions for upload (default: `['.csv']`)
- `MAX_FILE_SIZE`: Maximum allowed file size for upload in bytes (default: `10 * 1024 * 1024`)
- `TEMP_DIR`: Temporary directory for storing uploaded files (default: `tempfile.gettempdir() / 'health_data'`)

## Testing

### Running Tests
tests/
├── __init__.py
├── test_combined_factors.py
├── test_data_loader.py
├── test_filters.py
├── test_key_factors.py
├── test_loader.py
├── test_preview.py
└── test_risk_distribution.py

Run all tests:
```
python3 -m unittest discover tests
```
Run specific test:
```
python3 -m unittest tests/test_combined_factors.py
```
## Technologies
- [NiceGUI](https://nicegui.io/) for the web-based interface
- [Pandas](https://pandas.pydata.org/) for data manipulation
- [Plotly](https://plotly.com/) for data visualization
- [PDFKit](https://pypi.org/project/pdfkit/) for PDF generation

## Contributing
We welcome contributions to the project! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```sh
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```sh
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-name
    ```
5. Create a pull request on GitHub.

## Acknowledgments
- Special Thanks to:

[Berrijam](https://www.berrijam.com/) for supporting the Project 

[Zone01Kisumu](https://zone01kisumu.ke) for providing us with space to innovate and push our limits

## Contributors
- Hezron Okwach [Github](https://github.com/hezronokwach)

- Brian Bantu   [Github](https://github.com/Bantu-art)

- Steve Omotto  [Github](https://github.com/bshisia)

- Brian Shisia  [Github](https://github.com/somotto)

- Ferdynand Odhiambo [Github](https://github.com/MeFerdi)

