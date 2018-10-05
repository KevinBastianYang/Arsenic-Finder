<div align = "center"><img src="https://github.com/KevinBastianYang/arsenic_webserver/blob/master/web2/server/static/af.png"  height = "150" alt="af"></div>

Arsenic Finder is an web server designed to identify the potential arsenic binding site given the query amino acid sequences.   

### Getting started
The web site is [here](http://47.254.78.183:8000/server/). You can input the query sequence and the p-value, and the server will search whether the sequence contains the possible binding site and report the results.

### Web server structure
This server is built based on django, a python-written web framework, and deployed by Nginx (revserse proxy) and uWSGI(interface server).



