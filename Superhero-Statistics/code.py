# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'] = data['Gender'].replace('-','Agender')
gender_count = data['Gender'].value_counts()
plt.bar(gender_count, height=500)
#Code starts here 




# --------------
#Code starts here

alignment= data['Alignment'].value_counts()
plt.pie(alignment)
plt.legend('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.cov()['Strength']['Combat']
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)

ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov()['Intelligence']['Combat']
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(1,3)
super_best.boxplot(column='Intelligence',ax=ax_1)
super_best.boxplot(column='Speed',ax=ax_2)
super_best.boxplot(column='Power',ax=ax_3)


