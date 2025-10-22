import sys
from PIL import Image
import numpy as np

def get_bit(value, bit_index):
    return (value >> bit_index) & 1

def main():
    if len(sys.argv) != 4:
        print("Usage: python decodificar.py imagem_saida.png plano_bits texto_saida.txt")
        return

    in_image_path = sys.argv[1]
    plano_bits = int(sys.argv[2])
    out_text_path = sys.argv[3]

    img = Image.open(in_image_path)
    img = img.convert('RGB')
    arr = np.array(img)
    h, w, _ = arr.shape

    # Extrair bits dos planos
    bits = []
    for i in range(h):
        for j in range(w):
            for c in range(3):
                bits.append(get_bit(arr[i, j, c], plano_bits))

    # Extrair tamanho da mensagem
    msg_len = 0
    for i in range(32):
        msg_len = (msg_len << 1) | bits[i]
    # Extrair mensagem
    msg_bits = bits[32:32+msg_len*8]
    msg_bytes = bytearray()
    for i in range(0, len(msg_bits), 8):
        b = 0
        for j in range(8):
            if i+j < len(msg_bits):
                b = (b << 1) | msg_bits[i+j]
        msg_bytes.append(b)

    with open(out_text_path, 'wb') as f:
        f.write(msg_bytes)
    print(f"Mensagem recuperada em {out_text_path}.")

if __name__ == "__main__":
    main()
