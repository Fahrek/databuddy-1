echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-l 10 ^
-t | ^
-r 1 ^
-C C:\Users\alex_buz\sessions\My_Sessions\CSV_TimestampFile_to_ORA12C_Table\sqlloader.py ^
-dbg 1 ^
-w CSV-ORA12C ^
-K 1 ^
-Y 20160418_204446_401000 ^
-5 C:\Users\alex_buz\sessions\My_Sessions\CSV_TimestampFile_to_ORA12C_Table\host_map\host_map.py ^
-ps 1 ^
-B qc_job ^
-M C:\Temp\qc_log ^
-y 1000 ^
-i C:\Python35-32\PROJECTS\csv2redshift\Crime.csv ^
-d orcl12 ^
-e "MM/DD/YYYY HH12.MI.SS" ^
-m "MM/DD/YYYY HH12.MI.SS.FF2" ^
-u c##test ^
-O "MM/DD/YYYY HH12:MI:SS.FF2 TZH:TZM" ^
-a c##test.crime_test 