First run this if you use anaconda environment:

    conda install -c conda-forge pyinstaller

Then use the following command to create the executable file for the program:

    pyinstaller main.py --noconfirm --onefile --windowed --exclude-module sqlalchemy

Now in the folder 'dist/', the program can be run by executing 'main.exe'.