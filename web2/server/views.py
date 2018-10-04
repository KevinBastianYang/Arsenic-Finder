# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import os
#from django import forms
from .forms import MyForm

def seq_motif_scan(request):
    
    data = None
    submit = False
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['sequence']
            p_value = form.cleaned_data['p_value']
            file_w = open("/home/yangjc/vir_server2/web2/server/app/readin.txt",'w')
            #file_w.write(data)
            for item in data:
                file_w.write(item)
            file_w.close()
            pre_command = "/home/yangjc/vir_server2/web2/server/app/fimo --oc /home/yangjc/vir_server2/web2/server/app/match_out --verbosity 1 --thresh "
            sub_command = " /home/yangjc/vir_server2/web2/server/app/Arsenical_motif.txt /home/yangjc/vir_server2/web2/server/app/readin.txt"
            command = pre_command + str(p_value) + sub_command
            os.system(command)
            file_r = open("/home/yangjc/vir_server2/web2/server/app/match_out/fimo.txt",'r')
            record = []
            for line in file_r.readlines():
                if line[0] == '#':
                    continue
                else :
                    temp = line.split('\t')
                    tmplist = []
                    for k in range(5,10):
                        tmplist.append(temp[k])
                    record.append(tmplist)
            file_r.close()
            submit = True
            return render(request,'index.html',{'record':record,'submit':submit})
    else:
    
        form = MyForm()
    
        return render(request,'index.html',{'form':form,'submit':submit})

#class NewForm(forms.Form,data):
    
