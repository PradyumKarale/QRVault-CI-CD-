from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

qr_image_data = None


@app.route("/", methods=["GET", "POST"])
def home():
    global qr_image_data

    if request.method == "POST":
        content = request.form.get("content", "").strip()

        if content:
            qr = qrcode.make(content)

            image_stream = io.BytesIO()
            qr.save(image_stream, format="PNG")
            qr_image_data = image_stream.getvalue()

    return render_template(
        "index.html",
        qr_available=qr_image_data is not None
    )


@app.route("/qr-image")
def qr_image():
    if qr_image_data is None:
        return "No QR code generated yet.", 404

    return send_file(
        io.BytesIO(qr_image_data),
        mimetype="image/png"
    )

@app.route("/download-qr")
def download_qr():
    if qr_image_data is None:
        return "No QR code generated yet.", 404

    return send_file(
        io.BytesIO(qr_image_data),
        mimetype="image/png",
        as_attachment=True,
        download_name="qrvault.png"
    )


if __name__ == "__main__":
    app.run(debug=True)