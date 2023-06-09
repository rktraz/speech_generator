from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass
        # Get the user's input text or uploaded file
        # Make the API call to Azure ML and generate audio
        # Save the audio file locally
        # Return the rendered template with the audio file path
    return render_template('index.html')

@app.route('/audio/<path:filename>')
def download(filename):
    pass
    # Serve the audio file for download


if __name__ == '__main__':
    app.run(debug=True)