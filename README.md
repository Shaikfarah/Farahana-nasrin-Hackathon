# Color Detection Tool

Automatically extract dominant colors from images, providing HEX and RGB codes plus an exportable palette.

## Features
- Upload an image file or provide an image URL
- Detect top *k* dominant colors using k‑means clustering
- Display color swatches with HEX & RGB values
- Export palette as JSON

## Quick Start
```bash
git clone <repo-url>
cd color_detection_project
pip install -r requirements.txt
python color_detection.py --image path/to/image.jpg --colors 5
```

## Folder Structure
```
.
├── color_detection.py   # CLI entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project overview (this file)
├── LICENSE              # MIT License
└── .gitignore
```

## Tech Stack
- Python 3.10+
- OpenCV‑Python
- Pillow
- scikit‑learn
- numpy

## License
MIT
