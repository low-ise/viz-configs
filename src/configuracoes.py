import seaborn as sns
import matplotlib.pyplot as plt

def configurar_seaborn(paleta):
    """
    Configura o Seaborn com uma paleta customizada.

    Parâmetros:
        paleta (list): Paleta de cores para gráficos.
    """
    custom_params = {
        'axes.facecolor': '#F5F5F5',
        'axes.spines.right': False,
        'axes.spines.top': False,
        'grid.linestyle': "--",
        'grid.linewidth': 0.3,
        'grid.color': '#342920',
        'text.color': '#342920',
        'font.family': 'monospace',
        'font.monospace': 'DejaVu Sans Mono',
    }
    sns.set_theme(context='notebook', style='darkgrid', palette=paleta, rc=custom_params)
