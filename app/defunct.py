@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print request
    if request.method == 'POST':
        # check if the post request has the file part
        flash("There's an incoming request")
        if "file" not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print "File Object > %s" %  file
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # make the file safe to write
            filename = secure_filename(file.filename)
            print "Going to save %s" %  filename
            try:
                path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
                print path
                file.save(path)
            except Exception as e:
                print e
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("upload.html")

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    path = app.config['DOWNLOAD_FOLDER']
    return send_from_directory(path, filename)
    # return send_file(path, filename)
