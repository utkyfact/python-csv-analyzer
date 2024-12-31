# CSV Analyzer

The **CSV Analyzer** is a Flask-based web application that allows users to upload CSV files, analyze their contents, and generate detailed reports and visualizations. The application provides a user-friendly interface to explore data, create histograms, and download comprehensive analysis reports.

## Features

- **CSV File Upload**: Users can upload CSV files directly through the web interface.
- **Data Analysis**: The application automatically generates a detailed analysis report using the `ydata_profiling` library.
- **Visualization**: A histogram of the first column in the CSV file is created using `seaborn` and `matplotlib`.
- **Report Download**: Users can download the full analysis report in HTML format.
- **Responsive Design**: The interface is built with Bootstrap for a clean and responsive user experience.

## How It Works

1. **Upload a CSV File**: 
   - Navigate to the homepage and upload a CSV file using the file input field.
   
2. **Analyze the Data**:
   - Once the file is uploaded, the application processes the data, generates a histogram, and creates a detailed analysis report.

3. **View Results**:
   - The histogram is displayed on the page, and a summary of the data is provided.
   - Users can download the full analysis report by clicking the "Download Full Report" button.

## Installation

To run the CSV Analyzer locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/utkyfact/python-csv-analyzer.git
   cd csv-analyzer
   ````
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ````
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ````
4. **Run the Application**:
    ```bash
   python app.py
   ````
5. **Access the Application**:
   Open your web browser and go to http://127.0.0.1:5000/

### Dependencies

- Flask
- pandas
- matplotlib
- seaborn
- ydata_profiling
- Bootstrap (included in the project)

### Project Structure
csv-analyzer/
│
├── app.py                # Flask application
├── static/               # Static files (CSS, JS, images)
│   ├── bootstrap.min.js
│   ├── bootstrap.min.css
│   └── flask.jpg
├── templates/            # HTML templates
│   └── index.html
└── uploads/              # Uploaded files and generated reports

### Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Flask for the web framework.
pandas for data manipulation.
ydata_profiling for generating analysis reports.
Bootstrap for the responsive design.
