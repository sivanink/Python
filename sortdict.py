y={'Sree':50,'Dora':100,'Siva':60,'Meghu':80,'Anakha':120,'Ashna':90}
l=list(y.items())
l.sort()
print("Ascending Order:",l)
l=list(y.items())
l.sort(reverse=True)
print("Descending Order:",l)
dict=dict(l)
