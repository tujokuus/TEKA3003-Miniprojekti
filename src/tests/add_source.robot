*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Source With Valid Source Key And Source Name
    Input Add New Source Command
    Input Article  source_key=testiavain  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan lähde

Add Source With New Type
    Input Add New Source Command
    Input  kissa
    Input  Y
    Input  kissa-avain
    Input Nothing
    Input Yes Command
    Input Quit Command
    Run Application
    Output Should Contain  Tallennetaan lähde

Add Source With No Key
    Input Add New Source Command
    Input  article
    Input Nothing
    Input  avain
    Input  Pertti
    Input  Pertin Purinat
    Input  Lahde
    Input  1967
    Input No Optionals
    Input Quit Command
    Run Application
    Output Should Contain  Syotetty avain on tyhjä, lisää parempi

Add Source With No Author
    Input Add New Source Command
    Input  article
    Input  avain
    Input Nothing
    Input  Pertti
    Input  Pertin Purinat
    Input  Lahde
    Input  1967
    Input No Optionals
    Input Quit Command
    Run Application
    Output Should Contain  Syotetty author on tyhjä, lisää parempi

Add Source With Duplicate Key
    Input Add New Source Command
    Input Article  source_key=testiavain  source_author=Jaska Jokunen  source_title=Jaska Jokusen elämänkerta  source_journal=Epäluotettava lähde  source_year=2030
    Input Add New Source Command
    Input  article
    Input  testiavain
    Input  avain
    Input  Pertti
    Input  Pertin Purinat
    Input  Lahde
    Input  1967
    Input No Optionals
    Input Quit Command
    Run Application
    Output Should Contain  Syotetty avain on jo olemassa, lisää parempi

Dont Add Anything Just Quit
    Input Quit Command
    Run Application
    Output Should Contain  Kiitoksia käytöstä

Give False Command
    Input  kissa
    Input Quit Command
    Run Application
    Output Should Contain  Antamaanne käskyä ei tunnistettu, antakaa se uudestaan

Add Source By Doi
    Input Source By Doi  doi:10.1016/j.chemgeo.2024.122148
    Input Sort Sources According To Field Command  author
    Input Quit Command
    Run Application
    Output Should Contain  Mineralogical and environmental effects on the δ13C, δ18O, and clumped isotope composition of modern bryozoans

Add Source By Nonexistent Doi
    Input Source By Doi  doi:10.404/nonexistent.2024.122148
    Input Sort Sources According To Field Command  author
    Input Quit Command
    Run Application
    Output Should Contain  Ei lähteitä annetulle DOI-tunnukselle

Add Source By Doi In Http Form
    Input Source By Doi  https://doi.org/10.1016/j.chemgeo.2024.122148
    Input Sort Sources According To Field Command  author
    Input Quit Command
    Run Application
    Output Should Contain  Mineralogical and environmental effects on the δ13C, δ18O, and clumped isotope composition of modern bryozoans

Add Source By Acm.org Link
    Input Source By Acm.org Link  https://dl.acm.org/doi/10.1145/2380552.2380613
    Input Sort Sources According To Field Command  author
    Input Quit Command
    Run Application
    Output Should Contain  Three years of design-based research to reform a software engineering curriculum

Add Source By Invalid Acm.org Link
    Input Source By Acm.org Link  https://dl.acm.org/doi/10.1145/2380552.nonexistent
    Input Sort Sources According To Field Command  author
    Input Quit Command
    Run Application
    Output Should Contain  Ei lähteitä annetulle ACM linkille
