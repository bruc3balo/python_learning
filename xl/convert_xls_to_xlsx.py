import xls2xlsx as xlsx
from pathlib import Path



def convert_xls_to_xlsx(absPath):
    # path = Path(absPath)
    # if not path.exists():
    #     return
    
    length = len(absPath)
    if length < 3:
        print("Invalid format")
        return
        
    extension = absPath[-3:]
    if extension != 'xls':
        print("Must be xls")
        return 
    
    
    xls = xlsx.XLS2XLSX(absPath)
    xlsxFile = xls.to_xlsx()
    return xlsxFile