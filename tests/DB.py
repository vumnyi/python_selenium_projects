import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=db-site-stage;DATABASE=Site-Dev;UID=fo;PWD=flfdfqntifhbrfghjlflbv')
cursor = cnxn.cursor()

cnxn.execute("update [Site-Dev].[auction].[Lots] set Status = 1, Closed = NULL, Duration = 1690  where id = 896") #priora
cnxn.execute("update [Site-Dev].[auction].[Lots] set Status = 1, Closed = NULL, Duration = 1690  where id = 735") #audi
cnxn.execute("update [Site-Dev].[auction].[Lots] set Status = 1, Closed = NULL, Duration = 1690  where id = 735 or id = 830 or id = 854 or id = 830 or id = 878 or id = 879 or id = 880 or id = 881 or id = 885 or id = 886 or id = 887 ") #активируем нужные лоты


cnxn.commit()
cnxn.close()
