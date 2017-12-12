# railwaywebapp
A basic web app build with the help of flask framwwork to get all the trains between given time span of a particular station.

## Requirements
python 3
</br>
Flask Framework
</br>
Python request library
</br>
Python PyQt5 library
</br>
Python dateutil library

## Usage
Create a vurtual environment inside raiwaywebapp directary.
Run the Flask on ocal server
Enter the station code and timestamp between which you want to view the trains.

## Web Scraping
First I tried to use the arrival and departure API from </br>
https://railwayapi.com/
It only gave the data in the window of +-2hours

The site which gave full data of arrival and departure of trains from a particular station was </br>
https://etrain.info/in
Using Pyqt5 and bs4 I tscrap the Html data from thi site
