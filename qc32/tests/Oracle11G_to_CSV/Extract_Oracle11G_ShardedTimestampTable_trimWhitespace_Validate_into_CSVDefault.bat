::Test name: Oracle11G_ShardedTimestampTable trimWhitespace Validate
	::Description:	Extract Oracle11G table into CSVDefault.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-V[--validate] is "Check if source and target objects exist."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "Oracle 11G source user."
::	-x[--from_passwd] is "Oracle 11G source user password."
::	-b[--from_db_name] is "Oracle 11G source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-z[--source_client_home] is "Path to Oracle 11G client home."
::	-W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle 11G" extract."	
	
echo y|C:\Python27\qc_dist_32\20150226_103047\qc32\qc32.exe ^
-w ora11g2csv ^
-o 3 ^
-r 3 ^
-t "|" ^
-V 1 ^
-c SCOTT.Timestamp_test_from ^
-j SCOTT ^
-x tiger2 ^
-b orcl ^
-e "YYYY/MM/DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF" ^
-z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-W 1