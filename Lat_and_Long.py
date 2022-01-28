#Author: Salik Hassan
#Title: Latitude and Longitude Finder
#Description: The program takes the street address, city, state, and country. 
#Then it outputs the complete address, latitude and longitude. 

from audioop import add
from turtle import bgcolor, color
from geopy.geocoders import ArcGIS
from tkinter import *

#Window
window = Tk()
window.title("Latitude and Longitude Finder")
window.geometry("600x350")

#Function
def findLatLong():
    geolocator = ArcGIS()
    location = geolocator.geocode(street.get() + ", " + city.get() + ", " + state.get() + ", " + country.get())

    address = Label(window, text = location,padx= 10,pady=15, font=("bold",12))
    address.grid(row=4, column=1, columnspan=5, sticky="W")

    latitude = Label(window, text = str(round(location.latitude, 5)), padx= 10,pady=15, font=("bold",12))
    latitude.grid(row=5, column=1, columnspan=5, sticky="W")

    longitude = Label(window, text = str(round(location.longitude, 5)), padx= 10,pady=15, font=("bold",12))
    longitude.grid(row=6, column=1, columnspan=5, sticky="W")


#Street Address
streetLabel = Label(window, text = "Street Address: ", padx= 10,pady=15, font=("bold",12))
streetLabel.grid(row=0, column=0)
street = StringVar()
streetEntry = Entry(window, textvariable=street)
streetEntry.grid(row=0, column=1)

#City
cityLabel = Label(window, text = "City: ", padx= 10,pady=15, font=("bold",12))
cityLabel.grid(row=0, column=2)
city = StringVar()
cityEntry = Entry(window, textvariable=city)
cityEntry.grid(row=0, column=3)

#state
stateLabel = Label(window, text = "State/Province: ", padx= 10,pady=15, font=("bold",12))
stateLabel.grid(row=1, column=0)
state = StringVar()
stateEntry = Entry(window, textvariable=state)
stateEntry.grid(row=1, column=1)

#Country
countryLabel = Label(window, text = "Country: ", padx= 10,pady=15, font=("bold",12))
countryLabel.grid(row=1, column=2)
country = StringVar()
countryEntry = Entry(window, textvariable=country)
countryEntry.grid(row=1, column=3)

#Button
find = Button(window, text="Find", width=20, highlightcolor="red", command=findLatLong, pady=5)
find.grid(row=3, column=1, columnspan=3)

#Output Labels
addressLabel = Label(window, text = "Address: ", padx= 10,pady=15, font=("bold",12))
addressLabel.grid(row=4, column=0)

latitudeLabel = Label(window, text = "Latitude: ", padx= 10,pady=15, font=("bold",12))
latitudeLabel.grid(row=5, column=0)

longitudeLabel = Label(window, text = "Longitude: ", padx= 10,pady=15, font=("bold",12))
longitudeLabel.grid(row=6, column=0)


window.mainloop()