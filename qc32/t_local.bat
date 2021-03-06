::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-K[--keep_data_file] is "Keep data dump."
::-M[--log_dir] is "Log destination."
::-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::-B[--job_name] is "Job name (log_dir/job_name)."
::-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::-C[--loader_profile] is "SQL*Loader profile (user defined)."
::-5[--host_map] is "Host-to-shard map."
::-q[--query_sql_file] is "Input file with Oracle 11G query sql."
::-j[--from_user] is "Oracle 11G source user."
::-x[--from_passwd] is "Oracle 11G source user password."
::-b[--from_db_name] is "Oracle 11G source database."
::-e[--nls_date_format] is "nls_date_format for source."
::-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::-z[--source_client_home] is "Path to Oracle 11G client home."
::-u[--to_user] is "Target Oracle 11G db user."
::-p[--to_passwd] is "Oracle 11G user password."
::-d[--to_db_name] is "Oracle 11G database."
::-e[--nls_date_format] is "nls_date_format for target."
::-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
::-Z[--target_client_home] is "Path to Oracle 11G client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Python27\python datamule.py ^
-w ora11g2ora11g ^
-o 1 ^
-r 1 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150413_111128_290000 ^
-C "C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml" ^
-q "c:\Python27\data_migrator_1239_ddl\test\v101\query\SCOTT.TIMESTAMP_TEST_TO.0.sql" ^
-j SCOTT ^
-x tiger2 ^
-b orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-u SCOTT ^
-p tiger2 ^
-d orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"