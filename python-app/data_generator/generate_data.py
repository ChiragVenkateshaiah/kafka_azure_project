from flask import Flask, jsonify
import pandas as pd

app = Flask('__name__')

# Load the CSV data when the application starts
csv_file = 'shopping_trends.csv'  # Replace with the path to your CSV file

# Function to read data from CSV file starting from the last checkpoint
def read_csv_sequentially(csv_file, start_from_checkpoint=None):
    df = pd.read_csv(csv_file)
    if start_from_checkpoint:
        # Find the index of the last processed row
        last_index = df[df['CustomerID'] == start_from_checkpoint].index[0]
        # Start reading from the next row
        df = df.iloc[last_index + 1:]
    for _, row in df.iterrows():
        yield row.to_dict()

# Function to save the checkpoint to a file
def save_checkpoint(checkpoint):
    with open("checkpoint.txt", "w") as f:
        f.write(str(checkpoint))

# Function to load the checkpoint from a file
def load_checkpoint():
    try:
        with open("checkpoint.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return None

data_generator = None

@app.route('/api/data', methods=['GET'])
def get_sequential_data():
    global data_generator
    if data_generator is None:
        start_from_checkpoint = load_checkpoint()
        data_generator = read_csv_sequentially(csv_file, start_from_checkpoint)
    try:
        # Get the next row from the generator
        json_data = next(data_generator)
        save_checkpoint(json_data['CustomerID'])  # Save the checkpoint after processing each row
        return jsonify(json_data)
    except StopIteration:
        data_generator = None
        return "No more data available"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
