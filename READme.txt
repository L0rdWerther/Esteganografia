# Esteganografia — Trabalho IFB Taguatinga

Descrição
--------
Projeto para inserir e extrair mensagens em imagens usando esteganografia no domínio espacial (LSB).

Pré-requisitos
--------------
- Python 3.8+
- Pillow, numpy, matplotlib
- Instalar: pip install Pillow numpy matplotlib

Uso (exemplos)
--------------
- Inserir mensagem de arquivo:
  python3 codificar.py imagem_entrada.png texto_entrada.txt 0 imagem_saida.png
- Extrair mensagem:
  python3 decodificar.py imagem_saida.png 0 mensagem_recuperada.txt
- Analisar bits
  python3 analisar_bits.py imagem_saida.png

Algoritmo principal
------------------
- LSB (Least Significant Bit): converte a mensagem em bits, adiciona um cabeçalho (assinatura + tamanho) e substitui os bits menos significativos dos canais de cor dos pixels para armazenar os bits da mensagem.

Estruturas de dados
-------------------
- Imagens como arrays (PIL -> numpy.ndarray) para leitura/escrita de pixels.
- Buffer de bits (classe simples) para ler/gravar fluxo de bits.
- Cabeçalho fixo com assinatura e tamanho (para validação/extracção).

Considerações adotadas
----------------------
- Verifica capacidade antes de embutir.
- Usa formatos sem perda (PNG/BMP). JPEG normalmente corrompe LSB.
- Ordem de bits e cabeçalho padronizados para compatibilidade.
- Permutação pseudo-aleatória opcional via semente (se implementada).

Testes executados
-----------------
- Roundtrip: embed -> extract com mensagens curtas e próximas da capacidade.
- Teste de capacidade por número de canais (1 vs 3).
- Verificação de cabeçalho inválido.
- Comparação visual básica entre original e modificado.

Limitações / casos não tratados
-------------------------------
- Não resistente a recompressão, redimensionamento ou recorte.
- Não faz criptografia por padrão (cifrar externamente recomendado).
- Sem correção de erros (FEC) — perda de bits pode tornar mensagem irrecuperável.
- GIFs animados e formatos multi-frame não necessariamente suportados.
- Grandes imagens consomem muita memória.

Estrutura esperada do repositório
---------------------------------
- codificador.py
- decodificador.py
- imagem_entrada.png
- imagem_saida.png
- analisar_bits.py
- texto_entrada.txt
- texto_saida.txt
- READme.txt

- Autor: L0rdWerther
