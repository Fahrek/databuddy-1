#do not change
aa={'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'status_pipe_id': ['-spID', '--status_pipe_id', '', 'Status reporting pipe ID.'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-ps', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'from_remote_dirs': ['-frdl', '--from_remote_dirs', '', 'From remote dir list.  One or more coma separated dir names  (in command line).'], 'from_remote_file': ['-frm', '--from_remote_file', '', 'From remote file.'], 'from_remote_dir': ['-frd', '--from_remote_dir', '', 'From remote dir.'], 'from_server': ['-fsrv', '--from_server', '', 'From server.'], 'from_user': ['-fusr', '--from_user', '', 'From user.'], 'from_remote_files': ['-frfl', '--from_remote_files', '', 'From remote file list. One or more coma separated file names (in command line).'], 'from_passwd': ['-pw', '--from_passwd', '', 'Password.']}, {'to_db_name': ['-d', '--to_db_name', '', 'SQL Server 2005 database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to SQL Server 2005 client home bin dir.'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'to_user': ['-u', '--to_user', '', 'Target SQL Server 2005 db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'SQL Server 2005 user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'SQL Server 2005 instance name.'], 'to_table': ['-a', '--to_table', '', 'To table.']}], 'PSCP_Dir.SS2005_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'PSCP-SS2005', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150908_000257_743000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_passwd': ('-pw', '--from_passwd', 'oracle', 'Password.'), 'from_server': ('-fsrv', '--from_server', '192.168.15.227', 'From server.'), 'from_remote_dir': ('-frd', '--from_remote_dir', '/tmp/qctest', 'From remote dir.'), 'from_user': ('-fusr', '--from_user', 'oracle', 'From user.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 2005 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2005 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 2005 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 2005 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2005 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'PSCP_FileList.SS2005_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'PSCP-SS2005', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150908_000257_710000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_remote_files': ('-frfl', '--from_remote_files', '/tmp/qctest/pscp_test.zip,/tmp/qctest/ProcessExplorer.zip', 'From remote file list. One or more coma separated file names (in command line).'), 'from_passwd': ('-pw', '--from_passwd', 'oracle', 'Password.'), 'from_server': ('-fsrv', '--from_server', '192.168.15.227', 'From server.'), 'from_user': ('-fusr', '--from_user', 'oracle', 'From user.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 2005 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2005 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 2005 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 2005 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2005 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}], 'PSCP_File.SS2005_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'PSCP-SS2005', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150908_000257_726000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_passwd': ('-pw', '--from_passwd', 'oracle', 'Password.'), 'from_server': ('-fsrv', '--from_server', '192.168.15.227', 'From server.'), 'from_remote_file': ('-frm', '--from_remote_file', '/tmp/qctest/pscp_test.zip', 'From remote file.'), 'from_user': ('-fusr', '--from_user', 'oracle', 'From user.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server 2005 database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2005 client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server 2005 db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server 2005 user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2005 instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')}]}