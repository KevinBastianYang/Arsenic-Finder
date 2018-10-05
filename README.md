<div align = "center"><img src="https://github.com/KevinBastianYang/arsenic_webserver/blob/master/web2/server/static/af.png"  height = "150" alt="af"></div>

Arsenic Finder is an web server designed to identify the potential arsenic binding site motif given the query amino acid sequences.   

### Getting started
The website is [here](http://47.254.78.183:8000/server/). The input should be fasta-format amino acid sequences or a plain sequence using single letter amino acid codes. Also, you should input a statistical threshold (p-value) for the arsenic binding site motif. The results would be the binding site motifs in your query, including the strand, score, p-value, q-value, matched sequence segments. 

An example input:
```
>1NLX:A|PDBID|CHAIN|SEQUENCE
MGKATTEEQKLIEDVNASFRAAMATTANVPPADKYKTFEAAFTVSSKRNLADAVSKAPQLVPKLDEVYNAAYNAADHAAP
EDKYEAFVLHFSEALRIIAGTPEVHAVKPGA
```

### Built with
* [django](https://www.djangoproject.com/), a python-written web framework
* [Nginx](https://www.nginx.com/), a revserse proxy
* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/), used as the interface server



