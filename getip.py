#-*- coding: UTF-8 -*-
import os,sys,re,thread,threading

def getaddress( ip ):
    import urllib,urllib2

    url = "http://ip.cn/index.php?ip=" + ip
    req = urllib2.Request(url)

    res_data = urllib2.urlopen(req,timeout=10)
    res = res_data.read().decode("UTF-8").encode(sys.getfilesystemencoding())
    return re.search(r'<code>([^\.]+)</code>',res,re.MULTILINE).group(1)

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
    sname=re.match(r'(.*)\.[^\.]+$',fpath).group(1)
    if os.path.isfile(sname+'_ip.txt'):
        choose = raw_input("""
The results file is already existed. \n
Do you want to rewrite it? (n=NO,default=YES):
""")
        if choose=='n':
            exit("Good bye~")
    fsave = open(sname+'_ip.txt','w')
    flist=set([])
    tmp=re.match(r'(.*) - -.*',fopen.readline())
    while(tmp is not None):
        flist.add(tmp.group(1))
        tmp=re.match(r'(.*) - -.*',fopen.readline())
    for i in flist:
        fsave.write(i + '\n')
    print "The ip results is saved in '"+sname+"_ip.txt'\n"
    fsave.close()
    choose = raw_input("IP counts: " + str(len(flist)) + ".\n\
Do you want to search address of those? (n=NO,default=YES):")
    if choose=='n':
        exit("Good bye~")
    f2save = open(sname+'_ipAddress.txt','w')
    print "Need some time, waiting..."
    for i in flist:
        try:
            a = getaddress(i)
            print i + '\t\t' + a
            f2save.write(i + ('\t' if len(i)==15  else '\t\t') + a + '\n')
        except IOError, e:
            f2save.write(i + ('\t' if len(i)==15  else '\t\t') + 'SUSPEND!\n')
    print "The address results is saved in '"+sname+"_ipAddress.txt'"
