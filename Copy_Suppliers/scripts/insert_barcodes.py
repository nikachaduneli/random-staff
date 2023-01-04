import sqlite3
import pandas as pd 





def insert_barcodes():
   
    conn = sqlite3.connect('barcodes.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS BARCODES(
                    item text,
                    barcode text)""")

    wb = pd.read_excel(open('Main_Data.xlsx', 'rb'),
              sheet_name='BARCODES') 
    
    
    for i in range(15759):
        barcode = str(wb['barcode'][i])
        item = str(wb['ITEM_CODE'][i])
        cursor.execute("""INSERT INTO BARCODES
                      values(?,?)""", (item, barcode))
    
    conn.commit()
    cursor.close()
    conn.close()                    

insert_barcodes()    



