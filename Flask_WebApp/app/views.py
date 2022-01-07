import os
import cv2
from flask import Blueprint
from flask import flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from app.align_images import align_images


basedir = os.path.abspath(os.path.dirname(__file__))
server_bp = Blueprint('main', __name__)


@server_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Write uploaded file to disk.
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir, 'static/uploads', filename))

            # Read template image
            refFilename = os.path.join(basedir, 'static/', 'yahtzee_template.jpg')
            imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

            # Read image to be aligned
            imFilename = os.path.join(basedir, 'static/uploads', filename)
            im = cv2.imread(imFilename, cv2.IMREAD_COLOR)

            # Registered image will be restored in imReg.
            imReg, _ = align_images(im, imReference)

            # Write aligned image to disk.
            outFilename = os.path.join(basedir, 'static/uploads', filename)
            cv2.imwrite(outFilename, imReg)
            return redirect(url_for('main.upload_file'))
    return render_template('upload.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {"png", "jpg", "jpeg"}


@server_bp.route('/')
def hello():
    return "hello"
