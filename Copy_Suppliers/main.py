import sqlite3 
import time
import pandas as pd
start = time.process_time()

def load_barcodes(items):
    print('Loading barcodes...')
    conn = sqlite3.connect('scripts/barcodes.db')
    cursor = conn.cursor()   
    barcodes = []
    for item in items:
        cursor.execute("""SELECT barcode FROM BARCODES 
                        WHERE item = ?""", (item,))
        barcode = cursor.fetchone()

        if barcode != None:
            barcodes.append(barcode[0])
        else: barcodes.append(barcode)  
    return pd.DataFrame({'BARCODE' : barcodes})    

def filter_data():
    print('Loading Data...')
    wb_suppliers = pd.read_excel(open('Main_Data.xlsx','rb'), sheet_name='SUPPLIERS',)
    suppliers = wb_suppliers['suppliers']
  
    wb_data = pd.read_excel(open('Main_Data.xlsx','rb'), sheet_name='DATA',)
    ITEM = wb_data['ITEM']

    BARCODE = load_barcodes(ITEM)    
    
    print('Filtering Data...')
    columns_to_drop = ['DEP','GRN','USER','SP','CPVAL','QTYRCV','SPVAL','RESPLY','PICBRK','ASSORT','RANGCD','STATUS','XPRO','GRNDAT','CPUNT','CPVAL1','LSTUSR',	'LPOSTS','PRODGP']     
    wb_data = wb_data.drop(columns_to_drop, axis = 1)
    wb_data.insert(9, 'BARCODE',BARCODE.values)

    # wb_data = wb_data.loc[wb_data['BARCODE'].notnull()]

    wb_data.to_excel('excel_files/results.xlsx',index=False)

    

    for supplier in suppliers:

        wb_data_sup = wb_data.loc[wb_data['SUPLR'] == supplier]

        
        wb_data_sup.to_excel(f'excel_files/{supplier}.xlsx',  index=False)
        print(f'Supplier-{supplier} Done ...')
    

def main():
    
    filter_data()
    print(f'Time-{time.process_time()-start}') 
    input("\nPress Enter To Finish...") 

if __name__ == '__main__':
    main()
