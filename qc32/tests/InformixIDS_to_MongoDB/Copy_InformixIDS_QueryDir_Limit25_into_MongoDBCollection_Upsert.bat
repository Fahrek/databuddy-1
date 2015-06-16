::Test name: InformixIDS_QueryDir Limit25
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_infor".Copy only 25 rows from InformixIDS query results into MongoDBCollection Upsert.
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
::	-Q[--query_sql_dir] is "Input dir with Informix IDS query files sql."
::	-j[--from_user] is "Informix IDS source user."
::	-x[--from_passwd] is "Informix IDS source user password."
::	-b[--from_db_name] is "Informix IDS source database."
::	-n[--from_db_server] is "Informix IDS source instance name."
::	-z[--source_client_home] is "Path to Informix IDS client home."
::	-u[--to_user] is "Target MongoDB db user."
::	-p[--to_passwd] is "MongoDB user password."
::	-d[--to_db_name] is "MongoDB database."
::	-s[--to_db_server] is "Target MongoDB instance name."
::	-T[--to_db_port] is "Target MongoDB port."
::	-a[--to_collection] is "To table."
::	-Z[--to_column_names] is "To column list for MongoDB."
::	-G[--upsert] is "Upsert rows into MongoDB."
::	-numIW[--numInsertionWorkers] is "Upsert rows into MongoDB."	
	
echo y|C:\Python27\qc_dist_32\20150614_220157\qc32\qc32.exe ^
-w infor-mongo ^
-o 1 ^
-r 1 ^
-t "," ^
-l 25 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150614_220317_369000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-Q C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_infor ^
-j "informix" ^
-x "test_pwd" ^
-b "test" ^
-n "ol_s_121414_204157" ^
-z "C:\Program Files (x86)\IBM Informix Software Bundle\bin" ^
-u test_user ^
-p tast_pwd ^
-d test ^
-s localhost ^
-T 27017 ^
-a test ^
-Z "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" ^
-G 1 ^
-numIW 1