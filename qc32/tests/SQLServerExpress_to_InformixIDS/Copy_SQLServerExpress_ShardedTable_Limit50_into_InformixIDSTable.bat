::Test name: SQLServerExpress_ShardedTable Limit50
	::Description:	Copy only 50 rows from SQLServerExpress table into InformixIDSTable.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "SQL Server Express source user."
::	-x[--from_passwd] is "SQL Server Express source user password."
::	-b[--from_db_name] is "SQL Server Express source database."
::	-n[--from_db_server] is "SQL Server Express source instance name."
::	-z[--source_client_home] is "Path to SQL Server Express client home."
::	-a[--to_table] is "Target Informix IDS table."
::	-u[--to_user] is "Target Informix IDS db user."
::	-p[--to_passwd] is "Target Informix IDS db user password."
::	-d[--to_db_name] is "Target Informix IDS database."
::	-s[--to_db_server] is "Target Informix IDS db instance name."
::	-Z[--target_client_home] is "Path to Informix IDS client home bin dir."	
	
echo y|c:\Python27\qc_dist_32\20150723_234254\qc32\qc32.exe ^
-w SSEXP-INFOR ^
-o 1 ^
-r 3 ^
-t "|" ^
-l 50 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150723_234257_187000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j sa ^
-x 198Morgan ^
-b master ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-a Timestamp_test_to ^
-u "informix" ^
-p "test_pwd" ^
-d "test" ^
-s "ol_s_121414_204157" ^
-Z "C:\Program Files (x86)\IBM Informix Software Bundle\bin"