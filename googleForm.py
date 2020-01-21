import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
# Let's define all the constants 
fileForCreds = 'ex.json'
googleSheetName =  'Name of your google sheets'
outputFileName = 'put.csv'

# Craete scope for google drive and read credentials from ex.json
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(fileForCreds, scope)
# Authorize the credentials and open teh spreadsheet
client = gspread.authorize(creds)
sheet = client.open(googleSheetName).sheet1
## get all values - returns the entire data in the spreadsheet as list of rows
responses = sheet.get_all_values()
print(responses)
with open (outputFileName,'w',newline='') as f:
   writer = csv.writer(f)
   for i in responses:
       # write one response row at a time converting it to a List as [i]'
       writer.writerows([i])
 
