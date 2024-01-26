# High DPI Image Converter
## Overview
This Python script is designed for batch processing of image files, increasing their DPI to a user-specified value while maintaining the original physical dimensions by adjusting the pixel dimensions accordingly. It's particularly useful for preparing images for high-resolution printing or for applications requiring higher DPI settings without creating impractically large files.

## Features
Custom DPI Input: Allows users to specify the desired DPI for conversion.
Size and DPI Maintenance: Resizes images to maintain physical dimensions with the new DPI setting, ensuring high-quality output suitable for printing and high-DPI applications.
Safety Measures: Implements sensible limits to prevent processing excessively large images, mitigating potential decompression bomb DOS attacks.
Batch Processing: Automatically processes all supported image files (PNG, JPG, JPEG) in the current directory.
Detailed Reporting: Provides a comprehensive report for each image processed, including original and new sizes, DPI values, and processing time.
Output Organization: Saves the converted images in a separate "Converted" directory within the current working path, keeping original files unchanged.
## Requirements
Python 3.x
Pillow (PIL Fork) Library
## Installation
Ensure Python and pip are installed on your system. Install the required Python package (Pillow) using pip:

bash
Copy code
```
pip install Pillow
```
## Usage
Place the script in the directory containing the images you wish to convert. Run the script from the command line, and when prompted, enter the target DPI value:

bash
Copy code
```
python high_dpi_image_converter.py
```
The script will then process all applicable image files in the directory, saving the converted files in the "Converted" subdirectory.

## Contributing
Contributions to the High DPI Image Converter are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open source and available under the MIT License.
