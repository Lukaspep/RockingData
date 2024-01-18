from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./uploads/"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "csv"}
app.config["SECRET_KEY"] = "random string"

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = os.path.join(app.config["UPLOAD_FOLDER"], f.filename)
            f.save(filename)
            flash("Archivo subido correctamente")
            return render_template("correctamente.html", name=f.filename)
        else:
            flash("Formato invalido.: txt, pdf, png, jpg, jpeg, gif, csv", "error")
            return redirect(url_for('main'))

@app.route('/list_files')
def list_files():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("list_files.html", files=files)

@app.route('/delete_file/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    try:
        os.remove(file_path)
        flash(f"File '{filename}' eliminado correctamente")
    except OSError:
        flash(f"Error eliminando el archivo'{filename}'", "error")

    return redirect(url_for('list_files'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)