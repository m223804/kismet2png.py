import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=SQLSRV01;DATABASE=DATABASE;UID=USER;PWD=PASSWORD')
cursor = cnxn.cursor()

#edit .kismet into .csv to be readable
def parse_csv(filename):
  destmac = []
  lat = []
  lon = []
  signal = []
  
  cursor.execute("SELECT destmac, lat, lon, signal FROM packets")
  for row in cursor.fetchall():
      print row
