import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=db-site-stage;DATABASE=Site-Dev;UID=fo;PWD=flfdfqntifhbrfghjlflbv')
cursor = cnxn.cursor()

cnxn.execute("update [Site-Dev].[auction].[Lots] set Status = 1, Closed = NULL, Duration = 1690  where id = 896") #priora
cnxn.execute("update [Site-Dev].[auction].[Lots] set Status = 1, Closed = NULL, Duration = 1690  where id = 735") #audi


cnxn.commit()
cnxn.close()
