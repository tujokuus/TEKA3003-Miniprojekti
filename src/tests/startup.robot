*** Settings ***
Library    Process
Library    OperatingSystem

*** Variables ***
${MAIN}    ${CURDIR}/../main.py
${BIB}     ${CURDIR}/../test_data/test.bib

*** Test Cases ***
Check Poetry Python
    ${result}=    Run Process    poetry    run    python    -c    "import sys; print(sys.executable)"    stdout=TEXT
    Log    Python used by Poetry: ${result.stdout}

Program Starts With Bib File
    ${main_path}=    Normalize Path    ${MAIN}
    ${bib_path}=     Normalize Path    ${BIB}

    Log    MAIN PATH: ${main_path}
    Log    BIB PATH: ${bib_path}

    Run Process    poetry    run    python    ${main_path}    ${bib_path}    stdout=TEXT    stderr=TEXT    timeout=3s

 #   Log    STDOUT: ${result.stdout}
 #   Log    STDERR: ${result.stderr}

    Output Should Contain  Warning: provided bibtex file not found, generating one when saved
