import gpaCaculator as gcl
import pandas as pd
url = input(f"your grade url(default: {'gradeExcel.xlsx'}):") or 'gradeExcel.xlsx'
print('''                                                  
        _   _      _ _                            _     _   
        | | | | ___| | | ___   __      _____  _ __| | __| |  
        | |_| |/ _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` |
        |  _  |  __/ | |  _ |  \ V  V /   _ | |  | |   _| |
        |_| |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_| 
        ''')                                                                  
data = pd.read_excel(url)
cal = gcl.gpaCaculator(data)
cal.caculateCreditAvg()
cal.CheckDelay()

