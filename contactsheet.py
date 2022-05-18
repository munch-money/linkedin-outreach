from curses import raw
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# import linkedin



# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Contact Database").get_worksheet_by_id(776675191)

def addtospreadsheet(platform, userinitial, name, outreach):
    data = [platform, userinitial, name, outreach]
    sheet.append_row(data)
    # addlink()
    
# def addlink():
#     namecell = sheet.find(name)
#     # print(namecell)
#     namecellloc = "C" + str(namecell.row)
#     # sheet.acell(namecellloc, 'FORMULA').value = hyperlink
#     formula = sheet.get(namecellloc)
#     formula.update({
#         "hyperlink": hyperlink
#     })
#     # values = formula.get('values', [])
#     # sheet.acell('C308', value_render_option='formula')
#     print(formula.hyperlink)
#     # sheet.get_values('C308', value_render_option = 'formula')
    

    
    


# for n in profiles :
#     letters = profiles[n].replace('https://www.linkedin.com/in/', '')
#     letters = letters.replace(/[^A-Za-z]+/g, ' ');
#     var richValue = SpreadsheetApp.newRichTextValue()
#       .setText(letters)
#       .setLinkUrl(row[n])
#       .build();
#     var resrow = ['Linkedin', 'RM', letters, 'sent template-gen']
#     var sheet = SpreadsheetApp.getActiveSheet().appendRow(resrow);
#     var lrow = sheet.getLastRow();
#     var lrange = sheet.getRange(lrow, 3, 3)
#     var richValue = SpreadsheetApp.newRichTextValue()
#       .setText(letters)
#       .setLinkUrl(row[n])
#       .build();
#     lrange.setRichTextValue(richValue);