import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys

# Use a non-interactive backend for headless environments
target = sys.argv[1] if len(sys.argv) > 1 else "cert-matrix.png"
matplotlib.use('Agg')

# Read CSV
df = pd.read_csv("cert-matrix/cert-matrix.csv")

# Style the table
table = plt.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center',
    colColours=["#cccccc"]*len(df.columns)
)
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)

plt.axis('off')
plt.gcf().set_size_inches(8, 2 + 0.5*len(df))
plt.tight_layout()
plt.savefig(target, bbox_inches='tight', dpi=150)
