# QRVault

QRVault is a Flask-based QR Code Generator and History Manager.

The application allows users to generate QR codes from URLs or text, download generated QR codes, store QR history in SQLite, search previous QR entries, and delete unwanted history records.

The project also includes automated testing and a GitHub Actions CI pipeline.

## Features

- Generate QR codes from URLs or text
- Download generated QR codes as PNG files
- Store generated QR content in SQLite
- View QR code history
- Search QR history
- Delete individual history entries
- Input validation and error handling
- Application health check endpoint
- Automated testing with pytest
- GitHub Actions CI pipeline

## Technology Stack

- Python
- Flask
- SQLite
- qrcode
- Pillow
- pytest
- Git
- GitHub
- GitHub Actions

## Project Structure

QRVault/

- .github/
  - workflows/
    - ci.yml
- static/
  - style.css
- templates/
  - index.html
  - history.html
- tests/
  - test_app.py
- app.py
- requirements.txt
- README.md
- .gitignore

## Installation

Clone the repository:

~~~bash
git clone https://github.com/PradyumKarale/QRVault-CI-CD-.git
~~~

Move into the project directory:

~~~bash
cd QRVault-CI-CD-
~~~

Create a virtual environment:

~~~bash
python -m venv .venv
~~~

Activate the virtual environment on Windows:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

Install dependencies:

~~~bash
pip install -r requirements.txt
~~~

## Running the Application

Start the Flask application:

~~~bash
python app.py
~~~

Open the application in your browser:

http://127.0.0.1:5000

## Application Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET/POST | Generate QR codes |
| `/qr-image` | GET | Display generated QR image |
| `/download-qr` | GET | Download generated QR code |
| `/history` | GET | View and search QR history |
| `/delete/<id>` | POST | Delete a QR history entry |
| `/health` | GET | Application health check |

## Running Tests

Run the automated test suite with:

~~~bash
python -m pytest
~~~

The project currently tests:

- Home page availability
- Health check endpoint
- QR history page

## Continuous Integration

QRVault uses GitHub Actions for Continuous Integration.

The CI workflow automatically runs when code is pushed to the `main` branch or when a pull request targets `main`.

The pipeline performs:

~~~text
Push / Pull Request
        |
        v
Checkout repository
        |
        v
Set up Python 3.10
        |
        v
Install dependencies
        |
        v
Run pytest
        |
        v
CI result
~~~

If the tests pass, the GitHub Actions workflow succeeds.

If a test fails, the workflow fails and the issue must be fixed before the test suite can pass again.

## Health Check

QRVault provides a health check endpoint:

~~~text
/health
~~~

Example response:

~~~json
{
    "status": "healthy"
}
~~~

## Database

QRVault uses SQLite to store generated QR content.

The database contains a `qr_codes` table with:

- `id`
- `content`

The database is automatically initialized when the Flask application starts.

## Development Workflow

The project follows a Git-based development workflow:

~~~text
Develop feature
      |
      v
Test locally
      |
      v
Commit changes
      |
      v
Push to GitHub
      |
      v
GitHub Actions
      |
      v
Automated tests
      |
      v
CI result
~~~

## Author

**Pradyum Karale**

B.Tech Computer Science and Engineering