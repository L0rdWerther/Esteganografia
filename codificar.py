import sys
from PIL import Image
import numpy as np

def get_bit(byte, bit_index):
    return (byte >> (7 - bit_index)) & 1

def set_bit(value, bit_index, bit):
    # Convert to Python int to avoid numpy uint8 / negative-int issues
    v = int(value)
    mask = 1 << bit_index
    # Clear the target bit within 8 bits, then set it if needed
    v &= (0xFF ^ mask)
    if bit:
        v |= mask
    return v

def main():
    if len(sys.argv) != 5:
        print("Usage: python codificar.py imagem_entrada.png texto_entrada.txt plano_bits imagem_saida.png")
        return

    in_image_path = sys.argv[1]
    in_text_path = sys.argv[2]
    try:
        plano_bits = int(sys.argv[3])
    except ValueError:
        print("plano_bits must be an integer between 0 and 7.")
        return
    out_image_path = sys.argv[4]

    if not (0 <= plano_bits <= 7):
        print("plano_bits must be between 0 and 7.")
        return

    # Carregar imagem
    img = Image.open(in_image_path)
    img = img.convert('RGB')
    arr = np.array(img)

    # Ler texto
    with open(in_text_path, 'rb') as f:
        text_bytes = f.read()
    msg_len = len(text_bytes)
    # Codificar tamanho da mensagem nos primeiros 4 bytes (32 bits)
    msg_bits = []
    for b in msg_len.to_bytes(4, 'big'):
        for i in range(8):
            msg_bits.append(get_bit(b, i))
    # Codificar mensagem
    for b in text_bytes:
        for i in range(8):
            msg_bits.append(get_bit(b, i))

    # Verificar tamanho
    h, w, _ = arr.shape
    max_bits = h * w * 3
    if len(msg_bits) > max_bits:
        print("Mensagem muito grande para esta imagem!")
        return

    # Inserir bits
    idx = 0
    for i in range(h):
        for j in range(w):
            for c in range(3):  # canais R,G,B
                if idx < len(msg_bits):
                    arr[i, j, c] = set_bit(arr[i, j, c], plano_bits, msg_bits[idx])
                    idx += 1

    # Salvar imagem
    out_img = Image.fromarray(arr.astype('uint8'))
    out_img.save(out_image_path)
    print(f"Mensagem escondida em {out_image_path} usando plano {plano_bits}.")

if __name__ == "__main__":
    main()
