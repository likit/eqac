import pandas as pd
import glob
import sqlite3
from collections import namedtuple

Customer = namedtuple('Customer', ['id', 'cid', 'name'])

conn = sqlite3.connect('warehouse.db')
c = conn.cursor()

all_tests = {
                2: [(3,4,5), (2,3,1), 7.5], # albumin: [(columns),(test ids), ccv]
                1: [(6,7,8,9,10,11), (4,5,6,1,7,8), 15.5] # alp
            }

for excel_file in glob.glob('*.xls*'):
    print('Loading data from {}'.format(excel_file))
    data = pd.read_excel(excel_file, sheetname="data", skiprows=range(13))
    data.rename(columns={
            '  NUM': 'NUM',
            '  LAB   NAME': 'CUSTNAME'
        }, inplace=True)

    trial_id = 238# file name
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
            print(this_customer.name, test_id)
            methods = [data.columns[i] for i in results[0]]
            for i in range(len(methods)):
                if pd.notnull(d[methods[i]]):
                    c.execute('INSERT INTO results(customer_id, test_id, method_id, value, trial, ccv) VALUES (?,?,?,?,?,?)',
                         (this_customer.id, test_id, results[1][i], d[methods[i]], trial_id, results[2]))
            conn.commit()
