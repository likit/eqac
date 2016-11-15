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
    df['vis1'] = numpy.abs(df.eval('((value-dv1)/dv1)*100*(100/ccv)'))
    df['vis15'] = numpy.abs(df.eval('((value-dv15)/dv15)*100*(100/ccv)'))
    df['vis2'] = numpy.abs(df.eval('((value-dv2)/dv2)*100*(100/ccv)'))
    df['vis25'] = numpy.abs(df.eval('((value-dv25)/dv25)*100*(100/ccv)'))
    df['vis3'] = numpy.abs(df.eval('((value-dv3)/dv3)*100*(100/ccv)'))
    df.loc[df['vis1']>400, 'vis1res'] = 'U'
    df.loc[df['vis1']<150, 'vis1res'] = 'G'
    df.loc[(df['vis1']>=150) & (df['vis1']<=400), 'vis1res'] = 'A'

    df.loc[df['vis15']>400, 'vis15res'] = 'U'
    df.loc[df['vis15']<150, 'vis15res'] = 'G'
    df.loc[(df['vis15']>=150) & (df['vis15']<=400), 'vis15res'] = 'A'

    df.loc[df['vis2']>400, 'vis2res'] = 'U'
    df.loc[df['vis2']<150, 'vis2res'] = 'G'
    df.loc[(df['vis2']>=150) & (df['vis2']<=400), 'vis2res'] = 'A'

    df.loc[df['vis25']>400, 'vis25res'] = 'U'
    df.loc[df['vis25']<150, 'vis25res'] = 'G'
    df.loc[(df['vis25']>=150) & (df['vis25']<=400), 'vis25res'] = 'A'

    df.loc[df['vis3']>400, 'vis3res'] = 'U'
    df.loc[df['vis3']<150, 'vis3res'] = 'G'
    df.loc[(df['vis3']>=150) & (df['vis3']<=400), 'vis3res'] = 'A'
    df['summary'] = df.eval('vis1res+vis15res+vis2res+vis25res+vis3res')
    df.to_excel('chol-vis-enzcol-240.xls')


if __name__=='__main__':
    run(9,22,trial)
