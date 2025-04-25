Building the Executable
If you want to build the executable version of this script using PyInstaller, follow the steps below.

1. Install PyInstaller
If you don’t have PyInstaller installed, you can install it using pip:
pip install pyinstaller

2 Build the Executable
Once you have PyInstaller installed, you can convert the Python script into a standalone executable using the following command:
python -m pyinstaller --noconfirm --onefile --windowed keylog.py

This will generate the executable file inside the dist folder.

3. Run the Executable
Navigate to the dist folder and run the executable:

cd dist
keylog.exe
