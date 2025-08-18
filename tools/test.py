from .gau import gau

# domaon = "59689"
domaon = "lakoode.ir"
domainList=  ['mail.lakoode.ir', 'www.lakoode.ir', 'lakoode.ir', 'www.api.lakoode.ir', 'api.lakoode.ir']
subs = gau(domaon)
print(subs)
