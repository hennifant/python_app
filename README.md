## Setup and run instructions

To run the app in VS Code:

1. Clone the repo by running `git clone git@github.com:hennifant/python_app.git`
2. In Terminal, run `python -m venv env` to create a virtual environment.
3. Press Ctrl + Shift + P and run command `Python: Select Interpreter`. If possible, select the interpreter ending with "('env': venv)"
4. Activate the virtual environment by running `env/scripts/activate` if you are on Windows or run `source env/bin/activate` if you are on Linux/MacOS.
5. In terminal, run `pip install -r requirements.txt`, which includes - flask
6. From Run and Debug section, select `Python: Flask` launch configuration and hit F5.
7. Run the `python -m unittest` command
