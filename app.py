from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load the foundation dataset
current_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = r'C:\Users\Nimisha Majgawali\Desktop\foundation-recommender\foundation_dataset.csv'
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    skin_type = request.form.get('skin_type')
    finish = request.form.get('finish')

    # Filter the dataset based on user input
    recommendations = df[
        (df['skin_type'] == skin_type) & 
        (df['finish'] == finish)
    ]

    # Convert to a list of dictionaries for easy HTML rendering
    recommendations_list = recommendations[['Product Name', 'Brand', 'finish', 'Price (INR)']].to_dict(orient='records')
    
    return render_template('index.html', recommendations=recommendations_list)

if __name__ == '__main__':
    app.run(debug=True)
