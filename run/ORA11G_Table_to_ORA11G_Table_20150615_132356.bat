echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-t | ^
-r 1 ^
-o 1 ^
-w ora11g-ora11g ^
-K 1 ^
-F C:\tmp\TEST_default_spool ^
-Y 20150615_132247_206000 ^
-5 C:\Users\alex_buz\sessions\My_Sessions\ORA11G_Table_to_ORA11G_Table\host_map_v2.py ^
-B qc_job ^
-C C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml ^
-M C:\Temp\qc_log ^
-b "orcl_ol7 " ^
-c SCOTT.Timestamp_test_from ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-j SCOTT ^
-d orcl_ol7 ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-u SCOTT ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-a SCOTT.Timestamp_test_to 