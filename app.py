from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport

# Flask App
app = Flask(__name__)
app.config['uploads'] = 'static/uploads'
os.makedirs(app.config['uploads'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if not file.filename.endswith('.csv'):
            return "Only CSV files are allowed!"
        
        filepath = os.path.join(app.config['uploads'], file.filename)
        file.save(filepath)

        try:
            df = pd.read_csv(filepath)

            profile = ProfileReport(df, title="CSV Analysis Report", explorative=True)
            profile_file = os.path.join(app.config['uploads'], "report.html")
            profile.to_file(profile_file)

            plt.figure(figsize=(8, 6))
            sns.histplot(df.iloc[:, 0], kde=True)  # İlk sütunun histogramını oluştur
            graph_path = os.path.join(app.config['uploads'], "graph.png")
            plt.savefig(graph_path)
            plt.close()

            summary = df.describe().to_html()

            return render_template(
                'index.html',
                table=summary,
                graph=graph_path,
                report="report.html"
            )
        except Exception as e:
            return f"Error processing file: {e}"

    return render_template('index.html', table=None, graph=None, report=None)

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['uploads'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
