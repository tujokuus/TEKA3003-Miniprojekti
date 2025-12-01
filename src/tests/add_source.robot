*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Source With Valid Source Key And Source Name
    Input Source Credentials  testi  testiTutkimus
    Output Should Contain  Tallennetaan lähde
