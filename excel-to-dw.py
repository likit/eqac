import pandas as pd
import glob
import sys
import sqlite3
from collections import namedtuple

Customer = namedtuple('Customer', ['id', 'cid', 'name'])

dbpath = sys.argv[1]

conn = sqlite3.connect(dbpath)
c = conn.cursor()

all_tests = {
                2: [(3,4,5), (2,3,1), 7.5], # albumin: [(columns),(method ids), ccv]
                1: [(6,7,8,9,10,11), (4,5,6,1,7,8), 15.5], # alp
                3: [(13,14,15,16,17,18), (10,11,9,1,8,7), 17.3], # alt
                4: [(19,20,21,22,23,24), (10,11,9,1,8,7), 15.5], # ast
                5: [(25,26,27,28), (12,13,1,8), 5.7], # bun
                6: [(29,30,31,32,33,34), (14,15,1,8,16,17), 19.2] # bilirubin
                7: [(35,36,37), (18,1,19), 4.0] # calcium
                8: [(39,40,41), (20,21,1), 2.2] # chloride
                9: [(45,46,47,48,49), (22,1,8,9,7), 7.6] # cholesterol
                10: [(50,51,52,53), (23,24,1,8), 18.5] # ck
                11: [(54,55,56,57,58), (25,26,1,13,8), 8.9] # creatinine
                12: [(59,60,61,62,63), (12,22,9,1,8), 15.7] # ggt
                13: [(64,65,66,67,68), (27,28,1,8,29), 7.7] # glucose
                14: [(71,72,73,74,75), (30,31,1,8,29), 20.0] # hdl
                15: [(76,77,78,79,80), (4,33,6,1,7), 20.0] # ldh
            }

for excel_file in glob.glob('*.xls*'):
    print('Loading data from {}'.format(excel_file))
    data = pd.read_excel(excel_file, sheetname="data", skiprows=range(13))
    data.rename(columns={
            '  NUM': 'NUM',
            '  LAB   NAME': 'CUSTNAME'
        }, inplace=True)

    trial_id = int(excel_file.split('Report')[0]) # file name
    for _, d in data.iterrows():
        if pd.isnull(d['NUM']):
            continue

        # add a customer if not exists
        customer_id = int(d['NUM'])
        custname = d['CUSTNAME']
        c.execute('SELECT * FROM customers WHERE cid=%d' % customer_id)
        customer = c.fetchone()
        if not customer:
            c.execute('INSERT INTO customers (cid, name) VALUES (?, ?)', (customer_id, custname))
            conn.commit()
            # query a customer
            c.execute('SELECT * FROM customers WHERE cid=%d' % customer_id)
            customer = c.fetchone()

        # create a customer object
        this_customer = Customer(*customer)

        for test_id, results in all_tests.iteritems():
            methods = [data.columns[i] for i in results[0]]
            for i in range(len(methods)):
                if pd.notnull(d[methods[i]]):
                    c.execute('SELECT * FROM results WHERE customer_id=%d AND test_id=%d AND method_id=%d AND trial=%d' % (this_customer.id, test_id, results[1][i], trial_id))
                    # if the result exists, skip
                    if not c.fetchone():
                        c.execute('INSERT INTO results(customer_id, test_id, method_id, value, trial, ccv) VALUES (?,?,?,?,?,?)', (this_customer.id, test_id, results[1][i], d[methods[i]], trial_id, results[2]))
                        conn.commit()
                    else:
                        print('The result exists in the database..')
