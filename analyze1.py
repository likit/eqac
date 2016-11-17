'''Usage: python analyzer.py [database.db] [trial_no]

'''

import sqlite3
import sys
import pandas as pd
import numpy

dbpath = sys.argv[1]
trial = sys.argv[2]

engine = sqlite3.connect(sys.argv[1])
cursor = engine.cursor()

#tests = [rec for rec in c.execute('select * from tests')]

#methods = [rec for rec in c.execute('select * from methods')]

def run(test_id, method_id, trial):
    df = pd.read_sql_query('select * from results where test_id=%s and method_id=%s and trial=%s' % (str(test_id), str(method_id), str(trial)), engine)
    print(df)
    mean = df['value'].mean()
    sd = df['value'].std()
    print(mean, sd, mean+2*sd, mean-2*sd)
    
    
    df1 = df[(df['value'] >= mean-sd) & (df['value'] <= mean+sd)]
    df15 = df[(df['value'] >= mean-(sd*1.5)) & (df['value'] <= (mean+sd*1.5))]
    df2 = df[(df['value'] >= mean-(sd*2.0)) & (df['value'] <= (mean+sd*2.0))]
    df25 = df[(df['value'] >= mean-(sd*2.5)) & (df['value'] <= (mean+sd*2.5))]
    df3 = df[(df['value'] >= mean-(sd*3.0)) & (df['value'] <= (mean+sd*3.0))]
    

    print('df1', max(df1['value']), min(df1['value']))
    print('df15', max(df15['value']), min(df15['value']))
    print('df2', max(df2['value']), min(df2['value']))
    print('df25', max(df25['value']), min(df25['value']))
    print('df3', max(df3['value']), min(df3['value']))

    df['dv1'] = df1['value'].mean()
    df['dv15'] = df15['value'].mean()
    df['dv2'] = df2['value'].mean()
    df['dv25'] = df25['value'].mean()
    df['dv3'] = df3['value'].mean()
    
    df['sd1'] = df1['value'].std()
    df['sd15'] = df15['value'].std()
    df['sd2'] = df2['value'].std()
    df['sd25'] = df25['value'].std()
    df['sd3'] = df3['value'].std()
    
    df['sdi1'] = numpy.abs(df.eval('((value-dv1)/sd1)'))
    df['sdi15'] = numpy.abs(df.eval('((value-dv15)/sd15)'))
    df['sdi2'] = numpy.abs(df.eval('((value-dv2)/sd2)'))
    df['sdi25'] = numpy.abs(df.eval('((value-dv25)/sd25)'))
    df['sdi3'] = numpy.abs(df.eval('((value-dv3)/sd3)'))
    
    df.loc[df['sdi1']>2, 'sdi1res'] = 'U'
    df.loc[df['sdi1']<1, 'sdi1res'] = 'G'
    df.loc[(df['sdi1']>=1) & (df['sdi1']<=2), 'sdi1res'] = 'A'

    df.loc[df['sdi15']>2, 'sdi15res'] = 'U'
    df.loc[df['sdi15']<1, 'sdi15res'] = 'G'
    df.loc[(df['sdi15']>=1) & (df['sdi15']<=2), 'sdi15res'] = 'A'

    df.loc[df['sdi2']>2, 'sdi2res'] = 'U'
    df.loc[df['sdi2']<1, 'sdi2res'] = 'G'
    df.loc[(df['sdi2']>=1) & (df['sdi2']<=2), 'sdi2res'] = 'A'

    df.loc[df['sdi25']>2, 'sdi25res'] = 'U'
    df.loc[df['sdi25']<1, 'sdi25res'] = 'G'
    df.loc[(df['sdi25']>=1) & (df['sdi25']<=2), 'sdi25res'] = 'A'

    df.loc[df['sdi3']>2, 'sdi3res'] = 'U'
    df.loc[df['sdi3']<1, 'sdi3res'] = 'G'
    df.loc[(df['sdi3']>=1) & (df['sdi3']<=42), 'sdi3res'] = 'A'
    df['summary'] = df.eval('sdi1res+sdi15res+sdi2res+sdi25res+sdi3res')
    df.to_excel('chol-sdi-enzcol-240.xls')


if __name__=='__main__':
    run(9,22,trial)
