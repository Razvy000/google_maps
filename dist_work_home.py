import csv
import googlemaps
from datetime import datetime
from pprint import pprint

with open('adr.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

# print data

work = data[2]
home = data[3]

'''
print work
print home

# google stuff

gmaps = googlemaps.Client(key='xxx')

workplace = gmaps.places(work[0])
loc = workplace['results'][0]['geometry']['location']

pprint(workplace)
pprint(loc)

dist = gmaps.distance_matrix([loc], ['N19 3RE'])

pprint(dist)
'''

gmaps = googlemaps.Client(key='xxx')


dist_time = [-1] * len(work)
for i in range(len(work)):
    try:
        workplace = gmaps.places(work[i])
        loc = workplace['results'][0]['geometry']['location']
        dist = gmaps.distance_matrix([loc], [home[i]])
        duration = dist['rows'][0]['elements'][0]['duration']['value']
        dist_time[i] = float(duration) / 60
    except:
        pass

print dist_time
