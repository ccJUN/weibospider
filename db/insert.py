
from db import common

def mysqlInsert(mysqldb,mysqlstring):
    mysqlString = '('
    mysqlKey = '('
    for key,value in mysqlstring:
        print(key)
        mysqlString+=value+','
        mysqlKey +=key+','
    mysqlString+=')'
    mysqlKey+=')'
    sql = " INSERT INFO  " +mysqldb + mysqlKey + " VALUES  " +mysqlString
    print(sql)
    return True