dbs={	'SYASE':'SAP Sybase ASE', 'SYANY':'Sybase SQL Anywhere','SYIQ':'Sybase IQ',
		'ORA12C':'Oracle 12c','ORA11G':'Oracle 11g','ORA10G':'Oracle 10g','ORA9I':'Oracle 9i','ORA8I':'Oracle 8i','ORA733':'Oracle 7.3.3', 'ORAXE':'Oracle XE', 'ORAEXA':'Exadata',
		'TTEN':'TimesTen', 
		'SLITE':'SQL Lite',		
		'SSEXP':'SQL Server Express','SS2012':'SQL Server 2012','SS2014':'SQL Server 2014','SS2016':'SQL Server 2016',
		'SS70':'SQL Server 7.0', 'SS2000':'SQL Server 2000', 'SS2005':'SQL Server 2005', 'SS2008':'SQL Server 2008', 		
		'MYSQL':'MySQL', 'MARIA':'MariaDB', 'INFOB':'Infobright',
		'PGRES':'PostgreSQL',		
		'DBTAES':'DB2 Advanced Enterprise Server','DBTES':'DB2 Enterprise Server',
		'DBTAWS':'DB2 Advanced Workgroup Server',
		'DBTWS':'DB2 Workgroup Server',
		'DBTE':'DB2 Express', 'DBTEC':'DB2 Express C', 'DBTDE':'DB2 Developer Edition',
		'INFOR':'Informix IDS', 'INFORC':'Informix Innovator C',
		'MONGO':'MongoDB',		
		'CSV':'CSV',
		'FILE':'Generic File',
		'JSON':'JSON',
		'DDL':'DDL',
		'CURL': 'Curl',
		'PSCP': 'Pscp'
		}
dbfam={	'SYASE':'Sybase', 'SYANY':'Sybase','SYIQ':'Sybase',
		'ORA12C':'Oracle','ORA11G':'Oracle','ORA10G':'Oracle','ORA9I':'Oracle','ORA8I':'Oracle','ORA733':'Oracle', 'ORAXE':'Oracle', 'ORAEXA':'Oracle',
		'TTEN':'TimesTen', 
		'SLITE':'SQL Lite',
		#'SSEXP':'SQL Server','SSENT':'SQL Server',
		'SSEXP':'SQL Server','SS2012':'SQL Server','SS2014':'SQL Server','SS2016':'SQL Server',
		'SS70':'SQL Server', 'SS2000':'SQL Server', 'SS2005':'SQL Server', 'SS2008':'SQL Server',		
		'MYSQL':'MySQL', 'MARIA':'MariaDB', 'INFOB':'Infobright',
		'PGRES':'PostgreSQL',		
		'DBTAES':'DB2','DBTES':'DB2','DBTAWS':'DB2','DBTWS':'DB2','DBTE':'DB2', 'DBTEC':'DB2', 'DBTDE':'DB2',
		'INFOR':'Informix', 'INFORC':'Informix',
		'MONGO':'MongoDB',		
		'CURL':'CURL',	
		'PSCP':'PSCP',	'FILE':'Generic File',
		}
dbclients={ 'DBTAES': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'DBTAWS': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'DBTDE': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'DBTE': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'DBTEC': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'DBTES': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'DBTWS': r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'PGRES':'psql.exe','PGRES':r"C:\Program Files\PostgreSQL\9.4\bin",
			'ORA11G':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			'ORA10G':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			'ORA9I':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			'ORA8I':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			'ORA733':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',			
			'ORA12C':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			'ORAXE':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			#'ORA11G':r'C:\ORACLE\product\11.1.0\client_1\BIN',
			'ORAEXA':r'C:\app\alex_buz\product\11.2.0\dbhome_2\BIN',
			'SS2012':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'SS2014':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'SS2016':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'SS70':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'SS2000':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'SS2005':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'SS2008':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',			
			'SSEXP':r'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'MYSQL':r'C:\Temp\mysql\bin',	'INFOB':r'C:\Temp\mysql\bin',	
			#'CSVFILE':r'', 'CSVDIR':r'', 
			'CSV':r'',
			'SYANY': r'C:\Program Files\SQL Anywhere 16\Bin64',
			'SYASE': r'C:\Program Files\SQL Anywhere 16\Bin64',
			'SYIQ': r'C:\Program Files\SQL Anywhere 16\Bin64',
			'TTEN':r'C:\Program Files (x86)\TimesTen\tt1122_64\bin',
			#'DBTUDB':r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN',
			'INFOR':r'C:\Program Files (x86)\IBM Informix Software Bundle\bin',
			'INFORC':r'C:\Program Files (x86)\IBM Informix Software Bundle\bin',
			'MARIA':r'C:\Program Files\MariaDB 10.0\bin',
			'SLITE':'C:\Temp\SqlLite',
			'MONGO':r'C:\Program Files\MongoDB\Server\3.0\bin',
			'CURL':'C:\Python27\data_migrator_1239_mongo\common\Tools',
			'PSCP':'C:\Python27\data_migrator_1239_mongo\common\Tools'}	
spoolers={	'DBTAES': 'db2.exe',
			'DBTAWS': 'db2.exe',
			'DBTDE': 'db2.exe',
			'DBTE': 'db2.exe',
			'DBTEC': 'db2.exe',
			'DBTES': 'db2.exe',
			'DBTWS': 'db2.exe',
			'PGRES':'psql.exe',
			'PGRES':'psql.exe',
			'ORA12C':	'sqlplus.exe','ORA11G':	'sqlplus.exe', 'ORAXE':	'sqlplus.exe', 'ORAEXA':	'sqlplus.exe',
			'ORA10G':	'sqlplus.exe','ORA9I':	'sqlplus.exe','ORA8I':	'sqlplus.exe','ORA733':	'sqlplus.exe',
			#'SSENT':	'sqlcmd.exe',
			'SSEXP':	'sqlcmd.exe','SS2012':	'sqlcmd.exe','SS2014':	'sqlcmd.exe','SS2016':	'sqlcmd.exe',
			'SS70':	'sqlcmd.exe','SS2000':	'sqlcmd.exe', 'SS2005':	'sqlcmd.exe','SS2008':	'sqlcmd.exe',			
			#'SSEXP':	'sqlcmd.exe',
			'MYSQL':'mysql.exe', 'MARIA':'mysql.exe', 'INFOB':'mysql.exe',
			'SYANY':'dbisql.com',
			'SYASE':'dbisql.com',
			'SYIQ': 'dbisql.com',
			'TTEN': 'ttBulkCp.exe',
			#'DBTUDB': 'db2.exe',
			'INFOR': 'dbaccess.exe',
			'INFORC': 'dbaccess.exe',
			'SLITE':'sqlite3.exe',
			'MONGO':'mongoexport.exe',
			'CURL':'curl.exe',
			'PSCP':'pscp.exe'}

	
loaders={ 	'DBTAES': 'db2.exe',
			'DBTAWS': 'db2.exe',
			'DBTDE': 'db2.exe',
			'DBTE': 'db2.exe',
			'DBTEC': 'db2.exe',
			'DBTES': 'db2.exe',
			'DBTWS': 'db2.exe',
			'PGRES':'psql.exe',
			'ORA12C':	'sqlldr.exe','ORA11G':	'sqlldr.exe', 'ORAXE':	'sqlldr.exe',
			'ORA10G':	'sqlldr.exe','ORA9I':	'sqlldr.exe','ORA8I':	'sqlldr.exe','ORA733':	'sqlldr.exe',
			'ORAEXA':	'sqlldr.exe',
			#'SSENT':	'sqlcmd.exe','SSEXP':	'sqlcmd.exe',
			'SSEXP':	'sqlcmd.exe','SS2012':	'sqlcmd.exe','SS2014':	'sqlcmd.exe','SS2016':	'sqlcmd.exe',
			'SS70':	'sqlcmd.exe','SS2000':	'sqlcmd.exe', 'SS2005':	'sqlcmd.exe','SS2008':	'sqlcmd.exe',
			'MYSQL':'mysql.exe', 'MARIA':'mysql.exe', 'INFOB':'mysql.exe',
			'SYANY':'dbisql.com',
			'SYASE':'dbisql.com',
			'SYIQ': 'dbisql.com',
			'TTEN': 'ttBulkCp.exe',
			#'DBTUDB': 'db2.exe',
			'INFOR': 'dbaccess.exe',
			'INFORC': 'dbaccess.exe',			
			'SLITE':'sqlite3.exe',
			'MONGO':'mongoimport.exe',
			'PSCP':'pscp.exe'}

		
dbshell={ 'DBTAES': 'db2.exe',
			'DBTAWS': 'db2.exe',
			'DBTDE': 'db2.exe',
			'DBTE': 'db2.exe',
			'DBTEC': 'db2.exe',
			'DBTES': 'db2.exe',
			'DBTWS': 'db2.exe',
			'PGRES':'psql.exe',
			'PGRES':'psql.exe',
			'PGRES':'psql.exe',
			'ORA12C':	'sqlplus.exe','ORA11G':	'sqlplus.exe','ORAXE':	'sqlplus.exe',
			'ORAEXA':	'sqlplus.exe',
			'ORA10G':	'sqlplus.exe','ORA9I':	'sqlplus.exe','ORA8I':	'sqlplus.exe','ORA733':	'sqlplus.exe',
			#'SSENT':	'sqlcmd.exe','SSEXP':	'sqlcmd.exe',
			'SSEXP':	'sqlcmd.exe','SS2012':	'sqlcmd.exe','SS2014':	'sqlcmd.exe','SS2016':	'sqlcmd.exe','SS70':	'sqlcmd.exe',
			'SS2000':	'sqlcmd.exe','SS2005':	'sqlcmd.exe','SS2008':	'sqlcmd.exe',
			'MYSQL':'mysql.exe', 'MARIA':'mysql.exe', 'INFOB':'mysql.exe',
			'SYANY':'dbisql.com',
			'SYASE':'dbisql.com',
			'SYIQ': 'dbisql.com',
			'TTEN': 'ttIsql.exe',
			#'DBTUDB': 'db2.exe',
			'INFOR': 'dbaccess.exe',
			'INFORC': 'dbaccess.exe',			
			'SLITE':'sqlite3.exe',
			'MONGO':'mongo.exe','CURL':'curl.exe',
			'PSCP':'pscp.exe'}		
