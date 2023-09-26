#Também disponível em https://colab.research.google.com/drive/1-iWogVlg9RZHQUTO9DM18L0TYrfdRXXr?usp=sharing

import pandas as pd
import plotly.express as px
import seaborn as sn
import matplotlib.pyplot as plt

#Criando nosso DataFrame:
df = {'Atleta':["André","Bernardo","Carlos","Daniel","Eduardo","Fernando","Gabriel","Hugo","Ivan","João","Kleber","Luiz","Murilo","Ney","Orlando","Paulo","Queiroz","Renato","Silvio","Tadeu","Ulisses","Vinícius","Washington","Xavier","Yuri","Zózimo"],
          'TempoCorrida_Min':[37,39,40,38,35,35,44,41,39,41,49,36,47,46,41,33,42,38,36,46,37,40,43,38,38,45],
          'Idade': [22,35,26,32,24,24,28,34,28,34,36,23,31,33,36,25,29,22,24,34,25,29,33,32,27,35],
          'TempoTreinamento_Anos':[6,10,9,3,11,8,14,4,7,13,2,6,3,15,3,9,3,4,13,14,9,11,12,6,5,2]
}
df = pd.DataFrame(df)

#gerando nossos gráficos de dispersão:
figura1 = px.scatter(df, x=df.TempoCorrida_Min, y=df.Idade)
figura2 = px.scatter(df, x=df.TempoCorrida_Min, y=df.TempoTreinamento_Anos)
figura3 = px.scatter(df, x=df.Idade, y=df.TempoTreinamento_Anos)

#gerando e visualizando nosso gráfico de correlação:
grafcor = df.corr()
sn.heatmap(grafcor, annot= True)
plt.show()

#visualizando demais gráficos:
figura1.show()
figura2.show()
figura3.show()