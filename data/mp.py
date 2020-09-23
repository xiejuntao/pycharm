import pandas as pd
import pymysql
import numpy as np
import redis
import memcache
# def db_to_xlsx(db_name, queries, file_name):
#     db = pymysql.connect('localhost', 'root', 'xjt123456', charset='utf8', db=db_name)
#     writer = pd.ExcelWriter(file_name)
#     for sheet_name, query in queries.items():
#         df = pd.read_sql_query(query, db)
#         df.to_excel(writer, sheet_name=sheet_name, index=False)
#     writer.save()
#
# queries = {'sheet1': 'SELECT * FROM t;','sheet2': 'SELECT id FROM t;','sheet3': 'SELECT stat_date,v FROM t;'}
# db_to_xlsx('grafana', queries, 't_out2.xlsx')

def op_mysql():
    con = db = pymysql.connect('localhost', 'root', 'xjt123456', charset='utf8', db='grafana')
    t = pd.read_sql_query("select * from t",con)
    results = []
    for tmp in t.values:
        tt = pd.read_sql("select e_name,e_p from t_extra where id="+str(tmp[0]),con)
        #print(tmp.size)
        if len(tt.values)>0:
            tr = tt.values[0]
            # print(type(tr))
            # print(type(tmp))
            # print(n)
            results.append(np.append(tmp,tr))
        # print(tmp[0])
    # for r in results:
    #     print(r)
    # xls = pd.read_excel('r,xlsv')
    cc = ['ID', '日期', '数值', '名字', '人生', '旅途']
    df = pd.DataFrame(results,columns=cc)
    # pd.DataFrame.to_excel('r.xlsx','s',results)
    # pd.DataFrame.to_excel

    df.to_excel('rr.xlsx',index=False)
#sql()

def export():
    con = db = pymysql.connect('localhost', 'root', 'xjt123456', charset='utf8', db='grafana')
    rd = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
    t = pd.read_sql_query("select * from t",con)
    results = []
    for tmp in t.values:
        tt = pd.read_sql("select e_name,e_p from t_extra where id="+str(tmp[0]),con)
        #print(tmp.size)
        if len(tt.values)>0:
            tr = tt.values[0]
            # print(type(tr))
            # print(type(tmp))
            # print(n)
            result = np.append(tmp,tr)
            rd_val = rd.get(tmp[3])
            if rd_val is None:
                rd_val = ''
            e_result = np.append(result,rd_val)
            print(e_result)
            results.append(e_result)
        # print(tmp[0])
    # for r in results:
    #     print(r)
    # xls = pd.read_excel('r,xlsv')
    cc = ['ID', '日期', '数值', '名字', '人生', '旅途','终']
    df = pd.DataFrame(results,columns=cc)
    # pd.DataFrame.to_excel('r.xlsx','s',results)
    # pd.DataFrame.to_excel

    df.to_excel('rrr.xlsx',index=False)

#get_redis()

def op_redis():
    r = redis.StrictRedis(host='localhost',port=6379,decode_responses=True)
    # for num in range(0,100):
    #     r.sadd('fl','object_'+str(num))
    for v in r.sscan_iter('fl'):
        print(v)

# r()
# which memcached
def op_mc():
    mc = memcache.Client(['localhost:11211'])
    mc.set('name','xjt')
    print(mc.get('name'))
    mc.delete('name')
    print(mc.get('name') is None)
mc()


