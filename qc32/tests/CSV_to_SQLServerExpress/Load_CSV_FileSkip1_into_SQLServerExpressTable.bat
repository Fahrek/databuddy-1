::Test name: CSV_FileSkip1
	::Description:	Skip 1 rows and load CSV file into SQLServerExpressTable.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-k[--skip_rows] is "Header size. Number of rows to skip in input file."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target SQL Server Express db user."
::	-p[--to_passwd] is "SQL Server Express user password."
::	-d[--to_db_name] is "SQL Server Express database."
::	-s[--to_db_server] is "SQL Server Express instance name."
::	-a[--to_table] is "To table."
::	-Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
	
echo y|c:\Python27\qc_dist_32\20150723_234254\qc32\qc32.exe ^
-w CSV-SSEXP ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150723_234302_632000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\ss_shard_0.data ^
-k 1 ^
-y 100 ^
-u sa ^
-p 198Morgan ^
-d master ^
-s ALEX_BUZ-PC\SQLEXPRESS ^
-a dbo.Timestamp_test_to ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"