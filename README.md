<div align = "center"><img src="https://github.com/KevinBastianYang/arsenic_webserver/blob/master/web2/server/static/af.png"  height = "150" alt="af"></div>

Arsenic Finder is an web server designed to identify the potential arsenic binding site motif given the query amino acid sequences.   

### Getting started
The website is [here](http://47.254.78.183:8000/server/). The input should be fasta-format amino acid sequences or a plain sequence using single letter amino acid codes. Also, you should input a statistical threshold (p-value) for the arsenic binding site motif. The results would be the binding site motifs in your query, including the strand, score, p-value, q-value, matched sequence segments. 

An example input:
```
>1NLX:A|PDBID|CHAIN|SEQUENCE
MGKATTEEQKLIEDVNASFRAAMATTANVPPADKYKTFEAAFTVSSKRNLADAVSKAPQLVPKLDEVYNAAYNAADHAAP
EDKYEAFVLHFSEALRIIAGTPEVHAVKPGA
>1NLX:B|PDBID|CHAIN|SEQUENCE
MGKATTEEQKLIEDVNASFRAAMATTANVPPADKYKTFEAAFTVSSKRNLADAVSKAPQLVPKLDEVYNAAYNAADHAAP
EDKYEAFVLHFSEALRIIAGTPEVHAVKPGA

```

### Web server structure
This server is built based on django, a python-written web framework, and deployed by Nginx (revserse proxy) and uWSGI(interface server).



