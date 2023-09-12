#dictionary= changeable unordered collection of unique
#key:value paires
#fast becuase they using hashing allow as value quickly
capitals= {'usa': 'Newywork',
            'india':'New Delhi',
            'china':'Beijing',
            'Russia':'Moscow'}
capitals.update({'Geramny':'Berlin'})
capitals.update({'usa':'DC'})
capitals.pop('china')#remove
capitals.clear

#print(capitals['Germany'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, values in capitals.items():
    print(key,values)