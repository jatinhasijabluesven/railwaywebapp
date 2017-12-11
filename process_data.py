import sys
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import QUrl 
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from bs4 import BeautifulSoup
from datetime import datetime

# Store the webpage from etrain.info for parsing train data from it.   
class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Web Page Loaded')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

# Returns the arriving and departing train from str_name in the provided interval
def func(stn_name = None , start_time = None , end_time = None):
	url = 'https://etrain.info/in?PAGE=howto-arrivaldeparture#!STATION=' + stn_name
	source = Page(url)

	start_t = datetime.strptime(start_time,"%H:%M")
	print("Starting time is " + str(start_t))
	end_t = datetime.strptime(end_time,"%H:%M")
	print("Ending time is " + str(end_t))
	
	#Retrieve the train table from HTML
	soup = BeautifulSoup(source.html , "html.parser")
	table = soup.find('table',class_ = 'myTable data nocps nolrborder')
	rows = table.findAll('tr')
	print('Table Parsed')
	#Stores the final result - trains arriving and departing in between provided interval.
	html_str = str()
	count=0
	
	#Iterate on all the trains to and from the stations irrespective of time, and store the train records which are arriving or departing
	#between provided interval
	for row in rows:
		flag = 0
		columns = row.findAll('td')
		try:
			arrival_time = datetime.strptime(str(columns[4].string),"%H:%M") #The 5th column in parsed train table contains arrival time
		except ValueError:
			arrival_time=None
			pass
		try:	
			dept_time = datetime.strptime(str(columns[5].string),"%H:%M") #The 5th column in parsed train table contains departure time
		except ValueError:
			dept_time=None
			pass
		
		#for instance : 0600 to 0900
		if start_t <= end_t:
			try:
				if start_t<= arrival_time <= end_t:
					html_str += str(row)
					flag = 1
					count+=1
			except (UnboundLocalError, TypeError):
				pass
			
			try:
				if start_t<= dept_time <= end_t and flag == 0:
					html_str += str(row)
					flag = 1
					count+=1
			except (UnboundLocalError , TypeError):
				pass
		#for instance when : 2100 to 0300
		else:
			time24 = datetime.strptime("23:59","%H:%M")
			time0 = datetime.strptime("00:00","%H:%M")
			try:
				if start_t <= arrival_time<=time24 or time0<=arrival_time <=end_t:
					html_str += str(row)
					count=count+1
					flag = 1
			except (UnboundLocalError , TypeError):
				pass
			try:
				if (start_t<= dept_time<=time24 or time0<=dept_time <=end_t) and flag == 0:
					html_str += str(row)
					count=count+1
					flag = 1
				else:
					pass
			except (UnboundLocalError , TypeError):
				pass
	return html_str,count
