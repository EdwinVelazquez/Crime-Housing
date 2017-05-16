# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:30:26 2017
Crime & Housing in The Bronx
This code is for my Data Science Project 
called "Crime and Housing in The Bronx", It will collect data 
from Government sites and see if there is any corellation with
crime and prices of single family homes.  It will also corelate proximity to police 
precincts and crime.
@author: Edwin Velazquez
"""
import folium
import pandas as pd
from collections import Counter
import  csv 
import matplotlib.pyplot as plt

#read & prepare data from csv files
#Crime
bxCrime = pd.read_csv('BXCRIME5.csv',low_memory=False)
bxHousing = pd.read_csv('HousingFinal.csv',low_memory=False)
avgHood = pd.read_csv('hood.csv',low_memory=False)

mapCrime = folium.Map(location=[40.85, -73.890],zoom_start=13)

#Create Custom Crime markers markers
for index,row in bxCrime.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["OFNS_DESC"]
        logo_url = 'http://pngimg.com/uploads/gun/gun_PNG1352.png'
        icon = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
        folium.Marker([lat, lon],
          popup=name,
          icon=icon).add_to(mapCrime)

#Create Custom Police Precinct Markers
#50th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '50th Precinct-3450 Kingsbridge Rd.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.883550, -73.902366],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#52nd
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '52nd Precinct-3016 Webster Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.869244, -73.879806],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#47th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '47th Precinct-4111 Laconia Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.875092, -73.855056],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#49th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '49th Precinct-2121 Eastchester Rd.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.856074, -73.844369],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#45th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '45th Precinct-2877 Barkley Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.830843, -73.827329],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#43rd
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '43rd Precinct-900 Fteley Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.823136, -73.869810],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#41st
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '41st Precinct-1035 Longwood Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.816343, -73.895511],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#40th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '40th Precinct-257 Alexander Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.810321, -73.925202],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#43rd
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '43rd Precinct-900 Fteley Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.823136, -73.869810],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#42nd
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '42nd Precinct-830 Washington Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.822557, -73.911384],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#44th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '44th Precinct-2 E 169th Street'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.837328, -73.919783],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#48th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '48th Precinct-450 Cross Bronx Expy'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.843923, -73.900446],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#Transit Police
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = 'NYPD Transit Bureau District-460 Morris Park Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.841080, -73.871973],
          popup=jname,
          icon=icon2).add_to(mapCrime)
#46th
logo_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGy-oO5hToVfSMNzykxbtXnFhjuz_aoFhK8T6qldE8Gvvz_SQ6OQ'
jname = '46th Precinct-2121 Ryer Ave.'
icon2 = folium.features.CustomIcon(logo_url,\
                                  icon_size=(20, 20))
folium.Marker([40.854018, -73.900386],
          popup=jname,
          icon=icon2).add_to(mapCrime)
 
#Neighborhood Clusters with average prices
for index,row in avgHood.iterrows():
        lat = row["Latitude"]
        lon = row["Longitude"]
        name = row["AVERAGE"]
        price = row["PRICE"]
        hood = row["HOOD"]
        folium.CircleMarker(location=[lat, lon], radius=50,
                    popup=name, color='#3186cc',
                    fill_color='#3186cc').add_to(mapCrime)
        
#Create Folium map
mapCrime.save(outfile='bxCrime.html')

#Histogram and Plot Code
#Using the dictionary reader to access by column names
f = open('crime3.csv')
reader = csv.DictReader(f)
m = [row['HOOD'] for row in reader]
c = Counter(m)
f.close()

#Crime Histogram
dictionary = plt.figure()
plt.figure(figsize=(12, 8))
plt.bar(range(len(c)), c.values(), align='center')
plt.xticks(range(len(c)), c.keys(),rotation='vertical')

ax1 = dictionary.add_subplot(111)
ax1.bar(range(len(c)), c.values(), align='center')
ax1.set_ylabel("FELONY CRIME (2015)", color="b")
for tl in ax1.get_yticklabels():
    tl.set_color('b')

#Housing Price Plot
plt.title("Felony Crime in The Bronx (2015)")       #Title for plot
plt.xlabel('NEIGHBORHOOD')                     #Label for x-axis
plt.ylabel('Number of Felony Crimes (2015)')                   #Label for the y-axis
#plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner

df = pd.read_csv('hood.csv')
hood = df['HOOD']
price = df['PRICE']
         
ax2 = ax1.twinx()
ax2.plot(hood,price,color='r', label="PRICE")
ax2.set_ylabel("AVERAGE PRICE (2015)", color="r")
for tl in ax2.get_yticklabels():
    tl.set_color('r')

plt.show()
plt.savefig("image.png")
