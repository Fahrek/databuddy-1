#do not change
aa={'CURL_Url_To_File.SS70_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'CURL-SS70', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150907_231410_066000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'url': ('-url', '--url', 'http://oatsreportable.finra.org/OATSReportableSecurities-SOD.txt', 'URL to work with.'), 'output': ('-o', '--output', 'C:\\tmp\\curl_out\\OATSReportableSecurities-SOD.txt', 'Write output to <file> instead of stdout.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 7.0 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 7.0 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 7.0 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 7.0 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 7.0 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'CURL_UrlFiles.SS70_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'CURL-SS70', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150907_231410_046000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'url_files': ('-urlfiles', '--url_files', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\data\\url_list.txt,C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\data\\url_list.txt', 'Coma separated list of input files containing URLs.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 7.0 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 7.0 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 7.0 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 7.0 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 7.0 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'status_pipe_id': ['-spID', '--status_pipe_id', '', 'Status reporting pipe ID.'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-ps', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'url': ['-url', '--url', '', 'URL to work with.'], 'output': ['-o', '--output', '', 'Write output to <file> instead of stdout.'], 'url_list': ['-urls', '--url_list', '', 'List of input URLs.'], 'url_dirs': ['-urldirs', '--url_dirs', '', 'Coma separated list of input dirs of files containing URLs.'], 'url_files': ['-urlfiles', '--url_files', '', 'Coma separated list of input files containing URLs.']}, {'to_db_name': ['-d', '--to_db_name', '', 'SQL Server 7.0 database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to SQL Server 7.0 client home bin dir.'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'to_user': ['-u', '--to_user', '', 'Target SQL Server 7.0 db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'SQL Server 7.0 user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'SQL Server 7.0 instance name.'], 'to_table': ['-a', '--to_table', '', 'To table.']}], 'CURL_UrlFile.SS70_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'CURL-SS70', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150907_231410_086000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'url_files': ('-urlfiles', '--url_files', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\data\\url_list.txt', 'Coma separated list of input files containing URLs.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 7.0 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 7.0 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 7.0 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 7.0 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 7.0 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'CURL_UrlDirs.SS70_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'CURL-SS70', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150907_231410_057000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'url_dirs': ('-urldirs', '--url_dirs', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\data\\URL_Dir_0,C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\data\\URL_Dir_1', 'Coma separated list of input dirs of files containing URLs.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 7.0 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 7.0 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 7.0 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 7.0 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 7.0 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'CURL_UrlDir.SS70_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'CURL-SS70', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150907_231410_076000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'url_dirs': ('-urldirs', '--url_dirs', 'C:\\Python27\\data_migrator_1239_mongo\\test\\v101\\data\\URL_Dir_0', 'Coma separated list of input dirs of files containing URLs.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 7.0 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 7.0 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 7.0 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 7.0 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 7.0 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'CURL_Url.SS70_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'CURL-SS70', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150907_231410_036000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'url': ('-url', '--url', 'http://oatsreportable.finra.org/OATSReportableSecurities-SOD.txt', 'URL to work with.'), 'output': ('-o', '--output', 'C:\\tmp\\curl_out\\OATSReportableSecurities-SOD.txt', 'Write output to <file> instead of stdout.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 7.0 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 7.0 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 7.0 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 7.0 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 7.0 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}]}