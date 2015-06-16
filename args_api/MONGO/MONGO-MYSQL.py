#do not change
aa={'MONGO_Query.MYSQL_Table': [{'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'mongo-mysql', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150616_073430_068000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'json_query': ('-jsonq', '--json_query', '"{\'COUNTRY\':\'United States\'}"', 'Inline MongoDB JSON qry.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target MySQL db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'MONGO_Collection_Skip10.MYSQL_Table': [{'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'mongo-mysql', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150616_073430_068000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_skip_rows': ('-S', '--from_skip_rows', 1, 'Number of rows tto skip in source MongoDBtream.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target MySQL db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'arg_8': ['-8', '--arg_8', '', 'Generic string argument 8.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'arg_7': ['-7', '--arg_7', '', 'Generic string argument 7.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'arg_9': ['-9', '--arg_9', '', 'Generic string argument 9.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'from_column_names': ['-P', '--from_column_names', '', 'From column list.'], 'from_db_name': ['-b', '--from_db_name', '', 'MongoDB source database.'], 'header': ['-A', '--header', '', 'Include header to MongoDB extract.'], 'from_db_port': ['-z', '--from_db_port', '', 'MongoDB source database port.'], 'json_query_file': ['-q', '--json_query_file', '', 'Input file with MongoDB JSON query file.'], 'from_skip_rows': ['-S', '--from_skip_rows', '', 'Number of rows tto skip in source MongoDBtream.'], 'json_query_dir': ['-Q', '--json_query_dir', '', 'Input dir with MongoDB JSON query files.'], 'json_query': ['-jsonq', '--json_query', '', 'Inline MongoDB JSON qry.'], 'from_user': ['-j', '--from_user', '', 'MongoDB source user.'], 'from_passwd': ['-x', '--from_passwd', '', 'MongoDB source user password.'], 'from_db_server': ['-n', '--from_db_server', '', 'MongoDB source instance name.'], 'from_collection': ['-c', '--from_collection', '', 'From collection.']}, {'to_db_name': ['-d', '--to_db_name', '', 'Target database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to mysql client home.'], 'to_user': ['-u', '--to_user', '', 'Target MySQL db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Target db user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'Target db instance name.'], 'to_table': ['-a', '--to_table', '', 'Target table.']}], 'MONGO_Collection_Limit10.MYSQL_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'mongo-mysql', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150616_073430_068000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target MySQL db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'MONGO_Collection_withHeader.MYSQL_Table': [{'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'mongo-mysql', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150616_073430_068000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'header': ('-A', '--header', 1, 'Include header to MongoDB extract.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target MySQL db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'MONGO_Collection_JSON.MYSQL_Table': [{'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'mongo-mysql', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150616_073430_068000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target MySQL db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}]}