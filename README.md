# QR Code Generator

QR Code Generator is a simple Python desktop application built with Tkinter that generates QR codes from user-provided URLs and saves them locally.

## Features

* Generate QR codes from URLs, text, numbers, etc.
* Simple and user-friendly GUI
* Automatic QR code saving
* Input validation for empty fields
* Displays generation status messages

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the source code.
3. Install the required dependencies:

```bash
pip install qrcode Pillow
```

4. Open a terminal in the project folder.
5. Run:

```bash
python main.py
```

## Usage

* Enter a URL.
* Click **Generate QR**.
* The generated QR code is saved automatically.

## Project Structure

```text
qr-code-generator/
│
├── main.py
├── README.md
├── LICENSE
│
└── Generated QRs/
    └── qrcode.png
```

## Files

* `main.py` – Application source code
* `Generated QRs/qrcode.png` – Generated QR code image

## Author

**Harshad Sawant**

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
