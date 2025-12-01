*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Source With Valid Source Key And Source Name
    Input Add New Source Command
    Input Source Credentials  testi  testiTutkimus
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan lähde
