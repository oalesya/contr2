# -*- coding: utf-8 -*-
"""contr2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c0QB4ITSDv2tu-mPtHqY56GJLA00Quym
"""

# Commented out IPython magic to ensure Python compatibility.
# a.Выведите количество строк файла
import numpy as np
import pandas as pd
# %matplotlib inline
df3=pd.read_csv('df3.csv',index_col=0)
print(len(df3))

# Commented out IPython magic to ensure Python compatibility.
#b.Выведите заголовок файла (header) из нескольких строк. 
import numpy as np
import pandas as pd
# %matplotlib inline
df3=pd.read_csv('df3.csv',index_col=0)
df3.head()

#c.Воссоздайте график разброса «произведенных» и «дефектных деталей.
#(используйте функцию  scatter).
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 3))
plt.scatter(df3['produced'], df3['defective'], s = 20, c = 'r')
plt.xlabel('produced')
plt.ylabel('defective')

# d.Создайте гистограмму для колонки 'produced'
df3['produced'].plot.hist()

# e.Перерисуйте гистограмму как на рисунке ниже
df3['produced'].plot.hist(edgecolor='k').autoscale(enable=True, axis='both',tight=True)

# f.Создайте boxplot для 'produced' в каждый из дней недели 'weekday'
#(используйте группировку).

df3.boxplot(column = 'produced', by = 'weekday', grid = False)

# g.Создайте KDE (ядерная оценка плотности) для колонки 'defective'.
df3['defective'].plot.kde()

# h.Видоизмените график KDE, как на рисунке ниже
df3.defective.plot.kde(linewidth=5, linestyle='dashed')

# Commented out IPython magic to ensure Python compatibility.
# i.Для первых 30 строк постройте графики областей «произведенных» 
#и«дефектных» деталей. (используйте .loc)
import numpy as np
import pandas as pd
# %matplotlib inline
df3=pd.read_csv('df3.csv',index_col=0)
df=df3.head(30)
colors=['steelblue','peru']
df.plot.area(stacked=False, color=colors)



# Commented out IPython magic to ensure Python compatibility.
#j.Поменяйте расположение легенды на графике 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline
df3=pd.read_csv('df3.csv',index_col=0)
df=df3.head(30)
colors=['steelblue','peru']
df.plot.area(stacked=False, color=colors)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))