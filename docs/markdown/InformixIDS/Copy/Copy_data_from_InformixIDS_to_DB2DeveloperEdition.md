
# Migrating InformixIDS table data to DB2DeveloperEdition.
In this example we are going to migrate InformixIDS table data to DB2DeveloperEdition.
Migration steps:
- Extract InformixIDS table data to CSV.
- Load CSV file into DB2DeveloperEdition.

##Open Databuddy
[Download](https://github.com/data-buddy/DataBuddy/releases/tag/v0.3.3), [configure](https://github.com/data-buddy/DataBuddy/blob/master/Docs/Configure_Databuddy0.3.3.md#configuration-for-mongdb), and [start](https://github.com/data-buddy/DataBuddy/blob/master/Docs/How_to_start_Databuddy.md) Databuddy. 
It opens to a state where no sessions are selected and all tabs are disabled:

![Starter view with no sessions defined](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/open_databuddy_no_sessions.png "Starter view with no sessions defined")

## Define "Copy Vector"
Click "New" button located in top right corner. It will open to "New session" dialog. 
Define data extraction `Copy Vector` by zooming through popup menu items:
```python
  Copy Vector
  --------------
  |     ->     |
  --------------
  From InformixIDS-
				|
				From InformixIDS-
									  |
									  To DB2DeveloperEdition
```  
(sample image)
![Define copy vector for InformixIDS-to-DB2DeveloperEdition extract pipeline](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Define_copy_vector_for_Oracle12c-to-MongoDB_copy_pipeline.png "Define copy vector for InformixIDS-to-DB2DeveloperEdition copy pipeline.")

## Select Source and Target templates
Next and last step is template selection. Pick one from the source list on the left (`INFOR_TimestampTable`) and one from the target list on the right (`DBTDE_Table`):
(sample image)
![Source and target template selection](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Copy_from_Oracle12c_to_MongoDB_Templates.png "Source and target template selection.")

## Define arguments.
After you click `Create` button new session is created and right panel is populated with default values.
Please, ignore __Common__ argument section for now. Go through __Source__ and __Target__ arguments and set each argument to appropriate value. 
(sample image)
![Define arguments](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Oracle12c_to_MongoDB_Define_Arguments.png "Define arguments.")

## Run Session.
After you click __Run__ button black CLI window will pop-up executing QueryCopy (`qc32\qc.exe`).
(sample image)
![Session executed](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Oracle12c_to_MongoDB_Copy_CLI_Window.png "Session executed.")


##Checking the results
Check job results at the bottom of the black CLI window:
```
############################################################
2015-06-01 11:30:09,022 - INFOR-DBTDE - INFO - Done.
2015-06-01 11:30:09,022 - INFOR-DBTDE - INFO - Elapsed: 00:00:00
Press any key to continue . . .
```
Status __"Done"__ means export job executed successfully. 
- [x] Temporary InformixIDS CSV spool data file will be at `C:	mp\TEST_default_spool\qc_job\[timestamp]\[table_name].data` as defined by __Common__ section `default_spool_dir` argument.

	