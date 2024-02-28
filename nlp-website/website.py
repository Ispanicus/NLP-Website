from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Set the upload folder to a directory named 'files' in the same location as this script
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'files')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '''
        No file part
        <br><br>
            <form action="/">
                <input type="submit" value="Return to Upload Page">
            </form>
        '''
    
    file = request.files['file']
    
    if file.filename == '':
        return '''
        No selected file
        <br><br>
            <form action="/">
                <input type="submit" value="Return to Upload Page">
            </form>
        '''

    # Check if file already exists
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    if os.path.exists(file_path):
        return '''
            A file with this name already exists. Please choose a different file name.
            <br><br>
            <form action="/">
                <input type="submit" value="Return to Upload Page">
            </form>
            '''

    # Save the file if it doesn't exist
    file.save(file_path)
    return f'{file.filename} uploaded successfully'

if __name__ == '__main__':
    app.run()