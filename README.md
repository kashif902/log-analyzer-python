# Log Analyser

A small command-line program that counts ERROR, WARNING, INFO, and DEBUG lines in a log file.

## Run it

Open a terminal in this folder and run:

```powershell
py log_analyser.py app.log
```

To also print the ERROR lines:

```powershell
py log_analyser.py app.log --errors
```

## Run the tests

Install pytest once if needed, then run the tests:

```powershell
py -m pip install pytest
py -m pytest -v
```