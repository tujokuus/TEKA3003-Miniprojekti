*** Settings ***
Resource  resource.robot
Test Setup  Create Source And Input Save Command

*** Test Cases ***
Add Source With Valid Source Key And Source Name
    Input Source Credentials  testi  testiTutkimus
    Output Should Contain  Tallenetaan lähde

