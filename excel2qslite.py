import pandas as pd
import sqlite3

folder_path = ".\\"
file_name = "LibDB.xls"

# Excel dosyasını oku ve verileri düzenle
excel_file = pd.read_excel(folder_path+file_name, sheet_name=None, header=0)

# SQLite veritabanına bağlan
conn = sqlite3.connect(file_name[0:-4] +'.db')

# Her sayfayı bir tablo olarak veritabanına ekle
for sheet_name, df in excel_file.items():
    df.to_sql(sheet_name, conn, if_exists='replace', index=True)

# Veritabanı bağlantısını kapat
conn.close()
