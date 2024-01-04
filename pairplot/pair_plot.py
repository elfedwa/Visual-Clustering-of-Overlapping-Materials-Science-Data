import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Change the file name here 
r = pd.read_csv('./10bar_DATA_NODIM.csv')
################################
sns.set_theme(style="ticks")

pairplot = sns.pairplot(r)

# Retrieve the column names from the DataFrame
column_names = r.columns.tolist()

# Set x-axis and y-axis labels using the column names and increase font size
for i, ax in enumerate(pairplot.axes.flat):
    if i < len(column_names):
        ax.set_xlabel(column_names[i], fontweight='bold')
    if i % len(column_names) == 0:
        ax.set_ylabel(column_names[i // len(column_names)], fontweight='bold')
    
    # Remove tick numbers on x-axis and y-axis
    ax.set_xticks([])
    ax.set_yticks([])
     # Increase font size of x-axis and y-axis labels
    ax.xaxis.label.set_fontsize(16)
    ax.xaxis.label.set_fontweight('bold')
    ax.yaxis.label.set_fontsize(16)
    ax.yaxis.label.set_fontweight('bold')

plt.show()
