#slicng=create substring from another string
#indexing[]or slice()
#[start:stop:step]
name="karthik raja"
firstname=name[3:6]#starting index
lastname=name[8:12]
funkyname=name[::2]
reversedname=name[::-3]
#print(firstname)
#print(lastname)
#print(funkyname)
#print(reversedname)
website1="http://google.com"
website2="http://wikipedia.com"
slice=slice(7,-4)
print(website1[slice])
print(website2[slice])