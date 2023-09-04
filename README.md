If using anaconda, first activate environment:

    conda activate

and run this (if pyinstaller isn't already installed):

    conda install -c conda-forge pyinstaller

Then use the following command to create the executable file for the program:

    pyinstaller main.py --noconfirm --onefile --windowed --exclude-module sqlalchemy

Now in the folder 'dist/', the program can be run by executing 'main.exe'.

If 'dist/' is empty, you might just need to run the last command again.

Also make sure you have geckodriver installed on your pc. It can be found on this link:

https://github.com/mozilla/geckodriver/releases

Remember to add it to your path like this on windows 10:

1. Open the Start menu and type "Environment Variables."
2. Click on "Edit the system environment variables."
3. In the "System Properties" window, click the "Environment Variables..." button.
4. In the "Environment Variables" window, under the "System variables" section, scroll down and find the "Path" variable. Select it and click "Edit..."
5. Click the "New" button and add the directory path where geckodriver is located (e.g., C:\path\to\geckodriver).
6. Click "OK" to save your changes in all the open windows.

