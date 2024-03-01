import pandas as pd
import matplotlib.pyplot as plt

mi_dataset = pd.read_csv('text.csv')

mis_emociones = {
    0: 'tristeza',
    1: 'alegria',
    2: 'amor',
    3: 'enojo',
    4: 'miedo',
    5: 'sorpresa'
}

mi_dataset['emocion'] = mi_dataset['label'].map(mis_emociones)

mi_dataset

valor_y = mi_dataset['emocion'].value_counts()
valor_x = mi_dataset['emocion'].unique()

array(['miedo', 'tristeza', 'amor', 'alegria', 'sorpresa', 'enojo'],
      dtype=object)

fig, ax = plt.subplot()
ax.bar(valor_x, valor_y)

plt.show()

import neattext.functions as nfx
