# Doby, a Flask app wrapper to Stroman

A Flask app that provides a web app interface to my previous Stroman library. By removing the need for running scripts it can be hosted on my personal website and does not require interaction with the command line to be used. 

It is very much *under development*

It is named after [Larry Doby, the first Black player in the American League in baseball, and the second in the Major Leagues](https://sabr.org/bioproj/person/larry-doby/).

The main pages are:

* Plot Season Playoff Odds
* Get Information About Season Between Dates
* Generate Playoff Odds Prediction Table
* Team Historical Elo
* Team Historical SRS

Descriptions of the files are provided in the Stroman library. Sample plots are provided below.

![Elo ratings history of the Cubs](doby/stroman_src/Elo%20rating%20history%20of%20CHC.png)

![Elo ratings history of the NYM](doby/stroman_src/Elo%20rating%20history%20of%20NYM.png)

![SRS rating history of the Blue Jays](doby/stroman_src/SRS%20rating%20history%20of%20TOR.png)

![SRS ratings history of the Brewers](doby/stroman_src/SRS%20rating%20history%20of%20MIL.png) 

## <u>To Do</u>
- Add an example of the table for in season results above
- Better data ingestion methods (current method is to process a CSV and run two C++ files, SRSCalc and ELOCalc)
- Deployment to live!
- More unit and functional tests
- CSS improvements


## <u>Attributions</u>
This project incorporates source from the Armadillo C++ Linear Algebra Library.
As such, the attributions of Armadillo will be included in this project in accordance with their wishes:

Copyright 2008-2018 Conrad Sanderson (http://conradsanderson.id.au)

Copyright 2008-2016 National ICT Australia (NICTA)

Copyright 2017-2018 Arroyo Consortium

Copyright 2017-2018 Data61, CSIRO

This product includes software developed by Conrad Sanderson (http://conradsanderson.id.au)

This product includes software developed at National ICT Australia (NICTA)

This product includes software developed at Arroyo Consortium

This product includes software developed at Data61, CSIRO




