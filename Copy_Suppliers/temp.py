import time
start = time.process_time()
import timeit
import pandas as pd

def load_barcodes():
    print('Loading barcodes...')
    wb = pd.read_excel(open('Main_Data.xlsx', 'rb'),
              sheet_name='BARCODES')
    wb_items = pd.read_excel(open('Main_Data.xlsx', 'rb'), 
              sheet_name='DATA')['ITEM']
    barcodes = []
    for i in range(len(wb_items)):
      barcode = wb.loc[wb['ITEM_CODE']==wb_items[i]]['BARCODE']
      if barcode.empty:
        barcode = '#N/A'
      else: barcode = str(barcode.values[0])
      barcodes.append(barcode) 
    return pd.DataFrame({'BARCODE' : barcodes})   

def filter_data(BARCODE):
    print('Loading Data...')
    wb_suppliers = pd.read_excel(open('Main_Data.xlsx','rb'), sheet_name='SUPPLIERS',)
    suppliers = wb_suppliers['suppliers']
    wb_data = pd.read_excel(open('Main_Data.xlsx','rb'), sheet_name='DATA',)
    

    # BARCODE = load_barcodes()    
    
    print('Filtering Data...')
    columns_to_drop = ['DEP','GRN','USER','SP','CPVAL',
                      'QTYRCV','SPVAL','RESPLY','PICBRK',
                      'ASSORT','RANGCD','STATUS','XPRO',
                      'GRNDAT','CPUNT','CPVAL1','LSTUSR',	
                      'LPOSTS','PRODGP']     
    wb_data = wb_data.drop(columns_to_drop, axis = 1)
    wb_data.insert(9, 'BARCODE',BARCODE.values)

    # wb_data = wb_data.loc[wb_data['BARCODE'].notnull()]

    wb_data.to_excel('Store/results.xlsx',index=False)

    

    for supplier in suppliers:

        wb_data_sup = wb_data.loc[wb_data['SUPLR'] == supplier]

        
        wb_data_sup.to_excel(f'Store/{supplier}.xlsx',  index=False)
        print(f'Supplier-{supplier} Done...')
    

def main():
    BARCODE = load_barcodes() 
    filter_data(BARCODE)
    print(f'Time-{time.process_time()-start}') 
    


if __name__ == '__main__':
  print(f"Timeee - {timeit.timeit('main()', setup='from __main__ import main', number=1)}")
  input("\nPress Enter To Finish...") 