import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

file = 'data.csv'
data = pd.read_csv(file)

data = data.melt(['turno', 'apurados'], var_name='candidato')
data = data.sort_values('apurados')
data['value'] = data['value'] * 100
data['apurados'] = data['apurados'] * 100

candidato_color = {
    'lula': 'red',
    'bolsonaro': 'blue'
}
candidato_label = {
    'lula': 'Lula',
    'bolsonaro': 'Bolsonaro'
}
turno_alpha = {
    1: .32,
    2: 1
}

fig, ax = plt.subplots()
fig.set_size_inches(8, 4.5, forward=True)

for c in ['lula', 'bolsonaro']:
    for t in [1, 2]:
        sub = data[(data['turno']==t) & (data['candidato']==c)]
        ax.plot(sub['apurados'], sub['value'],
                 c=candidato_color[c],
                 alpha=turno_alpha[t],
                 label='{} {}º turno'.format(c.capitalize(), t))

ax.set_xlabel('Urnas apuradas')
ax.set_ylabel('Votação dos candidatos')

ax.set_xticks([0, 25, 50, 75, 100])
ax.set_yticks([40, 42, 44, 46, 48, 50, 52, 54, 56])

ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
ax.xaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

ax.grid()
#1200px X 675px
#ax.rcParams["figure.figsize"] = (16, 9)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
           fancybox=False, shadow=False, ncol=4)
plt.title('Apuração comparada entre turnos')
plt.savefig('../../plot.png')
