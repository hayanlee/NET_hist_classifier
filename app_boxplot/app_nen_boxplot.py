import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image


st.title('NEN PD/WD gene expression')

df = pd.read_csv('app_boxplot/NECPath.all.data.gene.h.pval.tsv.gz', sep='\t').set_index('Name')
df.sort_index( axis = 0, inplace = True )

#st.text( df )

genes = df.index

gene_choice = st.sidebar.selectbox('Select a gene', genes )
#index=st.session_state['selection']

#st.success("Done! {}".format( gene_choice ) )

#gene = 'GNG7'
#gene = 'TTK'
#gene = 'SFN'
#gene = 'CHEK1'
gene = gene_choice


fig = go.Figure()

fig.add_trace(go.Box(y=df.loc[gene,:][21:-1], boxpoints = 'all', name = 'PD (N=15)', marker_color='orangered' ) )
fig.add_trace(go.Box(y=df.loc[gene,:][:21], boxpoints = 'all', name = 'WD (N=21)', marker_color='dodgerblue' ) )

fig.update_layout(    
    width = 500, height= 500,
    title_font_size = 20,
    plot_bgcolor = 'rgb(255,255,255)',
    title={
        'text': "NEN {} expression (p-val={:.2e})".format(gene, df.loc[gene,:][-1]),
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_range=[ min(df.loc[gene,:]), max(df.loc[gene,:]) + 1 ],          
    yaxis=dict(
       title_text="log(count+1)",
        tickfont = dict(size=20),
        showgrid=False,
        zeroline=False,
        titlefont=dict(size=20),
        mirror=True,
        ticks='outside',
        showline=True, linewidth=2, linecolor='black',
    ),
    xaxis=dict(
        title_text="FCCC NEN cohort",
        tickfont = dict(size=20),
        zeroline=False,
        titlefont=dict(size=20),
        mirror=True,
        ticks='outside',
        showline=True, linewidth=2, linecolor='black',
    ),
    legend=dict(
        x=1.05,
        y=1,
        #traceorder="reversed",
        #title_font_family="Times New Roman",
        font=dict(
            #family="Courier",
            size=14,
            color="gray"
        ),
        #bgcolor="LightSteelBlue",
        #bordercolor="Black",
        #borderwidth=1
    )
)

#fig.show()
st.plotly_chart(fig ) 
#, use_container_width=True)

#images = ['logo_lee_lab_nospace.png', 'fox-chase-epigenetics-institute-logo.jpg', 'FCCC.png']
#st.image(images, width=200 )

st.text('\n')
image = Image.open('app_boxplot/logo_three.png')
#st.image(image, caption='Sunrise by the mountains' )
st.image(image, width=520)

