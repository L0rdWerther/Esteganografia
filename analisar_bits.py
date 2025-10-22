from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import sys  # <-- precisa importar isso!

def analisar_planos_bits(img_path):
    """
    Analisa os 3 planos de bits menos significativos (0, 1 e 2)
    de cada canal (R, G, B) de uma imagem.
    Exibe e retorna os resultados para fins de detecção de esteganografia.
    """

    # --- Carregar imagem ---
    img = Image.open(img_path).convert('RGB')
    arr = np.array(img)

    planos_bits = {}
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))
    fig.suptitle("Planos de bits (0, 1 e 2) dos canais R, G e B", fontsize=14)

    # --- Loop pelos canais e planos ---
    for canal_idx, canal_nome in enumerate(['R', 'G', 'B']):
        planos_bits[canal_nome] = {}
        for plano in [0, 1, 2]:
            # Isolar o plano de bits
            plane = ((arr[:, :, canal_idx] >> plano) & 1) * 255
            planos_bits[canal_nome][plano] = plane.astype(np.uint8)

            # Mostrar o plano de bits no gráfico
            ax = axes[plano, canal_idx]
            ax.imshow(plane, cmap='gray')
            ax.set_title(f'{canal_nome} - Bit {plano}')
            ax.axis('off')

    plt.tight_layout()
    plt.show()

    return planos_bits


# --- Execução direta via terminal ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso correto: python analisar_bits.py <imagem>")
        sys.exit(1)

    caminho = sys.argv[1]
    analisar_planos_bits(caminho)

