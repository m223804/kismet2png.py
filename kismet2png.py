#Process the Kismet into Csv

def parse_kismet(filename):
  sqlite3 filename
  .headers on
  .mode csv
  .output data.csv
  SELECT destmac, lat, lon, signal FROM packets
  .quit

  


