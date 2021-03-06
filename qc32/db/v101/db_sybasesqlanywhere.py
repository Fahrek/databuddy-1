import types, re, os, sys
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
from pprint import pprint
import shlex

class SybaseSQLAnywhere(base):
	"""SybaseSqlAny db"""
	def __init__(self,log,login,datadir,args):
		base.__init__(self, log)
		self.log=log
		self.login=login
		
		self.field_term=args.field_term
		self.datadir=datadir
		self.args=args
		self.tab_cols={}
		self.to_pld={}
		self.db_client_loc=None		
		self.ctldir='%s/sqlloader' % self.datadir
		
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir) 
		self.dbg=0
		if args.debug_level:
			self.dbg=int(args.debug_level)	
	

	def get_query_columns(self, qry):
		#if self.tab_cols.has_key(tab_name):
		#	return self.tab_cols[tab_name]
		if 0:
			pass
		else:
			qry="""SELECT * FROM (%s) p WHERE 1=2;""" % qry.strip().strip(';')
			#print qry
			#sys.exit(0)
			regexp=re.compile(r'([\w\ ]+)', re.M|re.I)
			cqfn=self.save_qry('get_query_columns',qry)
			#print cqfn
			(r_int, status,err)=self.do_query(self.log,self.login, query=None,query_file=cqfn,regexp=regexp)
			pprint(r_int)
			
			cols =  [x for x in r_int[0][0].split(' ') if x]
			#print cols
			#sys.exit(0)
			return (cols,status)

	def do_query(self,logger,login, query, query_file=None, regexp=None, grp=None, spset='',field_term='|'):
		f = ""
		(db_user,db_passwd, db_name, db_server)=login
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(login)>0, 'Default login is not set.'
		show=False
		#field_term='|'
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''
			if 0: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				assert os.path.isfile(query_file),'Query file %s is missing' % query_file
			#	q = "%s%s" % ( query_file,'show warnings;')
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:
				q =  query # "%s\n%s\n%s" % ( spset,opt,query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q
			#sys.exit(0)
			#p1 = Popen(['C:\\Python27\\data_mule_mysql\\spool_test.sql'], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				pass
			else: #,'-q','"%s"' % q
				#q='select ''ROW COUNT:'' flt ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t'
				#pprint(q)
				#print ss_db_server
				db_client_loc=self.get_db_client_loc()
			
				#conf=[ db_client_loc ,'-U', pg_user,'-d',pg_db_name, '-h', pg_db_server]
				
				connect_str= '"uid=%s;pwd=%s;dbn=%s;server=%s"' % (db_user,db_passwd, db_name, db_server)
				conf=['"%s"' % db_client_loc ,'-nogui','-c', connect_str,'-onerror', 'exit']
				if query_file:
					conf=conf+ [r'"%s"' % query_file]	
					q=''					
				#conf=[ pgloc ,'-U', self.args.from_user,'-d',self.args.from_db_name]
				#pprint(conf)
				#print q 
				#sys.exit(0)
				#print regexp
				#print login
				#raise
				#set PGPASSWORD=self.args.from_passwd
				#os.environ['PGPASSWORD'] = pg_passwd
				#q='exit;'
				#q='select count(*) from Persons_pipe_datetime;'
				#print q
				#select 'ROW COUNT:' filter ,count(*) cnt from (SELECT * FROM     Persons_pipe_datetime) as t;
				#print conf
				cmd=  ' '.join(conf)
				#print cmd
				#sys.exit(1)			
#				  SELECT * FROM (SELECT * FROM (SELECT * FROM     Persons_pipe_datetime)) p WHERE 1=2
				cmdList=shlex.split(cmd)
				#pprint (cmdList)
				p2 = Popen(cmdList,stdin=PIPE,  stdout=PIPE,  shell=True) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				#out, err = p2.communicate(file("C:\\Python27\\data_mule_mysql\\spool_test.sql").read())
				#print q
				#if not query_file:				
				output, err = p2.communicate("%s\nexit;\n" % q)
				#pprint( output)
				#print err
				#print p2.communicate('source C:\\Python27\\data_mule_mysql\\spool_test.sql;')
				#output=' '
				status=0
				er='none.'
				#print type(out)
				#pprint(out.split('\n'))
				#pstatus=p2.wait()
				#sys.exit(1)
				pstatus=p2.wait()
				if err:
					if 'Warning: Using a password on the' in err:
						logger.warn(err)
					else:
						logger.error(err)							
				#print output.split('\n')	
				for o in output.split(os.linesep):
				#while output:
					#output = p2.stdout.readline()
					#pprint(o)
					#if o.strip():					
					#	logger.info( output.strip())
					if 1:
						if regexp:
							#print regexp, o
							#pprint(dir(re))
							m = re.match(regexp, o) 
							#print m
							if m:
								if grp:
									out.append(m.group(grp))
								else:
									groups=m.groups()
									if groups:

										#print 'groups', groups
										out.append(groups)
									#self._logger.info(output.rstrip())
								#else out.append(m.group(grp))
						else:
							
							out.append(output)

				#print "====================", out,status
				#sys.exit(0)
				return (out,status, err)					
	def do_query_spool(self,logger,conf, query, query_file=None, regexp=None, grp=None, spset='',field_term='|'):
		f = ""
		(ss_user,ss_passwd, ss_db_name, ss_db_server)=conf
		out=[]
		err=[]
		ora_err =False
		errpos=-1
		pstatus=0
		status=0
		#errreg=re.compile(r'.*(ERROR).*')
		assert  len(conf)>0, 'Default login is not set.'
		show=False
		#field_term='|'
		if 1:			
			#from subprocess import Popen, PIPE
			q=''
			opt=''
			if 1: #self.p_if('IF_SHOW_SERVEROUTPUT'):
				#opt='set serveroutput on echo on termout on feedback on timing off'
				show =True
			if query_file:
				q = "%s\n%s\n@%s" % ( spset,opt,query_file)
				#q = "%s\nset autotrace on page 3 timing on echo on serveroutput on\n%s\n%s" % ('-'*20, query,'-'*20) 
			else:		

				q =  query # "%s\n%s\n%s" % ( spset,opt,query)
			
			#self._logger.info(login)
			#self._logger.sql(q)
			#print q
			#sys.exit(0)
			#p1 = Popen(['C:\\Python27\\data_mule_mysql\\spool_test.sql'], stdout=PIPE,stderr=PIPE, shell=True)
			output=' '
			status=0
			if 0:
				pass
			else: #,'-q','"%s"' % q
				#q='select ''ROW COUNT:'' flt ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t'
				#pprint(q)
				#print ss_db_server
				mysqlloc='%s\mysql' % self.args.mysql_client_home.strip("'").strip('\\').strip('\\')
				conf=[ mysqlloc ,'-u', ss_user, '-p%s' % ss_passwd,'-D',ss_db_name, '-h', ss_db_server]
				#pprint(conf)
				#sys.exit(1)
				p2 = Popen(conf,stdin=PIPE,  stdout=PIPE  ) # '-S',  stdin=p1.stdout,
				#p2 = Popen([ 'sqlplus', "-s", login], stdin=p1.stdout, stdout=PIPE,stderr=PIPE) , 
				out, err = p2.communicate(file("C:\\Python27\\data_mule_mysql\\spool_test.sql").read())
				#print out
				#print err
				#print p2.communicate('source C:\\Python27\\data_mule_mysql\\spool_test.sql;')
				output=' '
				status=0
				er='none.'
				if 1:
					while er:
						er = p2.stderr.readline()
						if er.strip():
							
							if 'Warning: Using a password on the' in er:
								logger.warn(er)
							else:
								logger.error(er)
							
				while output:
					output = p2.stdout.readline()
					#print output
					if output.strip():					
						logger.info( output.strip())
					if 1:
						if regexp:
							#print regexp
							m = re.match(regexp, output) 
							if m:
								if grp:
									out.append(m.group(grp))
								else:
									groups=m.groups()
									if groups:
										if groups[0]:
											out.append(groups)
									#self._logger.info(output.rstrip())
								#else out.append(m.group(grp))
						else:
							out.append(output)
							if show:
								print output.strip()
								#self._logger.info(output.rstrip())	
						if errpos>-1:
							#self._logger.error(output.rstrip())	
							status=1					
						#errpos=output.find('ERROR') 
						#print  output.find('2COLUMN.')
						if output.find('COLUMN.')==-1:
							errpos=output.find('ERROR ')
							#print "%s, %s ,%s" % (errpos, output, output.find('COLUMN.'))
							if errpos>-1:
								status=1
								
								#self._logger.error(output.rstrip())	
				
				pstatus=p2.wait()
				#print 'status:', pstatus
				er='none.'
				if pstatus:
					while er:
						er = p2.stderr.readline()
						if er:
							print 'P2-ERROR: ',er
					
				if int(status)+int(pstatus)>0:
					print 'error', status,pstatus
					#self._logger.error(string.join(err,'\n'))	
				if status!=0:
					return (err,status)
				#print "====================", out,status
				return (out,status+pstatus)					