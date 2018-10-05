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

### Find more
Our methodology will soon be published.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details

### Acknowledgement
* The motif searching step is built with the help of [FIMO](https://academic.oup.com/bioinformatics/article/27/7/1017/232614) (*Charles E. Grant, Timothy L. Bailey, and William Stafford Noble, "FIMO: Scanning for occurrences of a given motif", Bioinformatics, 27(7):1017-1018, 2011.*)
* Great thanks to Dr.Jingfang Wang and Shichao Pang who supported and inspired me a lot along the way.

