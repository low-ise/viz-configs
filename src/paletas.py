import seaborn as sns
from matplotlib.colors import to_hex

# Definição das cores
CORES_SOBRIAS = ['#65000B', '#882D17', '#993366', '#853D91', '#154360', '#055E52']
CORES_GENTIS = ['#B29075', '#C2B280', '#F4C2C2', '#C2A9D5', '#8BA7DB', '#81A57E']

def gerar_paleta_completa(cores_sobrias=CORES_SOBRIAS, cores_gentis=CORES_GENTIS):
    """
    Gera uma paleta completa com tons sóbrios, intermediários e gentis.
    
    Parâmetros:
        cores_sobrias (list): Lista de cores sóbrias em HEX.
        cores_gentis (list): Lista de cores gentis em HEX.
    
    Retorna:
        list: Paleta completa com tons organizados.
    """
    # Gerar tons intermediários
    cores_medias_rgb = []
    for sobria, gentil in zip(cores_sobrias, cores_gentis):
        gradiente = sns.blend_palette([sobria, gentil], n_colors=3, as_cmap=False)
        cores_medias_rgb.append(gradiente[1])

    cores_medias = [to_hex(cor) for cor in cores_medias_rgb]

    # Combinar paletas
    paleta_completa = []
    for n in range(len(cores_sobrias)):
        for paleta in [cores_sobrias, cores_medias, cores_gentis]:
            paleta_completa.append(paleta[n])

    return paleta_completa
