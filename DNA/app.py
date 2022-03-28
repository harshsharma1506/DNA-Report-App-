from msilib import sequence
from numpy import char
import pandas as pd #for data 
import streamlit as st #framework to make webapps 
import altair as alt #framework for data models 
from PIL import Image #for loading images inside the app in python 

image=Image.open('dna-logo.png')
st.image(image,use_column_width=True)
st.write("""
#DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA !

***
""")

sequence_input=">DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTGGTTRESSSSFFFFGGGGGGAAAAACCCTTCTCTC\nGTCYTCGCTCTGTCCGCTCCGCTCTGVCTCFCGTCGCTCVGFTFGCTCGCTTGVGCTGCGG\nGTCTGTCTGTCTCGTCCTGGTGTCTGTTCTCTCGTC"
sequence=st.text_area("Sequence input",sequence_input,height=250)
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence)

st.write("""
***
""")
st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nuclrotide Count)')

st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d=dict([
    ('A',seq.count('A')),
    ('T',seq.count('T')),
    ('G',seq.count('G')),
    ('C',seq.count('C'))
    ])
    return d 
X=DNA_nucleotide_count(sequence)
X_label=list(X)
X_values=list(X.values())

X
st.subheader('2. Print text')
st.write('There are '+str(X['A'])+' adenine(A)')
st.write('There are '+str(X['T'])+' thymine(T)')
st.write('There are '+str(X['G'])+ 'adenine (guanine)' )
st.write('There are '+str(X['C'])+' thymine (cytosine)')

st.subheader('3. Display DataFrame')
df=pd.DataFrame.from_dict(X, orient='index')
df=df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p=(alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
))
p=p.properties(
    width=alt.Step(80)
)

st.write(p)
