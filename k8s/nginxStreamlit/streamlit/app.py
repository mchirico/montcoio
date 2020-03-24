import requests
import pandas as pd
import numpy as np 
from datetime import datetime

import plotly.express as px

import streamlit as st


@st.cache
def readTZ():
    url="https://storage.googleapis.com/montco-stats/tzsmall.csv"
    d=requests.get(url,verify=True).content
    d=pd.read_csv(url,
                  header=0,names=['lat', 'lng','desc','zip','title','timeStamp','twp','e'],
            dtype={'lat':str,'lng':str,'desc':str,'zip':str,
                  'title':str,'timeStamp':str,'twp':str,'e':int})
    d=pd.DataFrame(d)
    d['timeStamp'] = d['timeStamp'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
    return d


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
d=readTZ()
data_load_state.text('data loaded')

d.sort_values(by=['timeStamp'], ascending=False, inplace=True)


st.title('Sample of most recent calls with fever..')
e = d[d['title']=='EMS: FEVER']
e

st.title('Montco 911 FEVER calls by township per 5 day')

t=d[d['timeStamp']>= '2020-01-01']
# Use for easy totals
t['e']=1
p2 = pd.pivot_table(t, values='e', index=['timeStamp','twp'], columns=['title'], aggfunc=np.sum)
p2 = p2.reset_index()

pp2 = p2.groupby(['twp', pd.Grouper(key='timeStamp', freq='5d')])['EMS: FEVER'].sum()
pp2=pp2.reset_index()

z = pp2[(pp2['timeStamp']>= '2020-01-01') & (pp2['EMS: FEVER'] >= 1)]
zz= pd.pivot_table(z, values='EMS: FEVER', index=['timeStamp'], columns=['twp'], aggfunc=np.sum)
tz= zz.sort_index(axis=0, level=None, ascending=False).fillna(0)
tz= tz.reset_index()

tz['Total']=tz.sum(numeric_only=True, axis=1)
tz



# Plot
fig = px.histogram(z, x="timeStamp", y="EMS: FEVER", color="twp",hover_name="twp")
st.plotly_chart(fig)





# Seaborn

t=d[d['timeStamp']>= '2015-01-01']
t['e']=1
p = pd.pivot_table(t, values='e', index=['timeStamp'], columns=['title'], aggfunc=np.sum)
pp = p.resample('1d').apply(np.sum).reset_index()
pp.columns = pp.columns.get_level_values(0)

pp.fillna(0, inplace=True)
pp.sort_values(by=['timeStamp'], ascending=False, inplace=True)

t = pp

import plotly.express as px
fig = px.line(t, x="timeStamp", y="EMS: FEVER", title='EMS: FEVER/day',
   template='plotly_dark')
st.plotly_chart(fig)
