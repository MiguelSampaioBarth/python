import qrcode
import os

def input_frase(mensagem) :
    entrada = input(mensagem)
    return entrada + ".png"

def gerar_qr_code(conteudo, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(conteudo)
    qr.make(fit=True)

    imagem_qr = qr.make_image(fill_color="black", back_color="white")
    imagem_qr.save(nome_arquivo)

while True :
    os.system('cls' if os.name == 'nt' else 'clear')
    conteudo = input('insira o que quer colocar no qr code:\n')
    nome = input_frase('nomeie o arquivo criado:\n')
    
    gerar_qr_code(conteudo, nome)
    print(f"QR code gerado e salvo como '{nome}' com sucesso.")
