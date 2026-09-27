from flask import Flask, render_template, request, send_file, redirect
import qrcode
import io
import sqlite3

app = Flask(__name__)

qr_image_data = None


def init_db():
    conn = sqlite3.connect("qrvault.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS qr_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


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

            conn = sqlite3.connect("qrvault.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO qr_codes (content) VALUES (?)",
                (content,)
            )

            conn.commit()
            conn.close()

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

@app.route("/history")
def history():
    search = request.args.get("search", "").strip()

    conn = sqlite3.connect("qrvault.db")
    cursor = conn.cursor()

    if search:
        cursor.execute(
            "SELECT id, content FROM qr_codes "
            "WHERE content LIKE ? ORDER BY id DESC",
            (f"%{search}%",)
        )
    else:
        cursor.execute(
            "SELECT id, content FROM qr_codes ORDER BY id DESC"
        )

    qr_codes = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        qr_codes=qr_codes,
        search=search
    )

@app.route("/delete/<int:qr_id>", methods=["POST"])
def delete_qr(qr_id):
    conn = sqlite3.connect("qrvault.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM qr_codes WHERE id = ?",
        (qr_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/history")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)