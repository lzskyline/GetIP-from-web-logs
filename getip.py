#-*- coding: UTF-8 -*-
import os,sys,re
if __name__ == "__main__":
    print """
 =================================
|                                 |
|   Name:    GetIP From WebLogs   |
|   Author:  LzSkyline            |
|   WebSite: LzSkyline.com        |
|                                 |
 =================================
"""
    if len(sys.argv)<2:
        exit('You must provide at least one argument. ')
    fpath = sys.argv[1]
    if not os.path.isfile(fpath):
        exit("The file seems not exist. ")
    fopen = open(fpath)
    sname=re.match(r'(.*)\.[^\.]+$',fpath).group(1)+'_ip.txt'
    if os.path.isfile(sname):
        choose = raw_input("""
The results file is already existed. \n
Do you want to rewrite it? (n=NO,default=YES):
""")
        if choose=='n':
            exit("Good bye~")
    fsave = open(sname,'w')
    flist=set([])
    tmp=re.match(r'(.*) - -.*',fopen.readline())
    while(tmp is not None):
        flist.add(tmp.group(1))
        tmp=re.match(r'(.*) - -.*',fopen.readline())
    for i in flist:
        fsave.write(i+'\n')
    print "The result is saved in "+sname
