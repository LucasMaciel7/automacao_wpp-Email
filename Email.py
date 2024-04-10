import imaplib
import email
import time
from wpp import send_message
import datetime



imap_server = "imap.gmail.com"
email_address ="lucasmacielcampos27@gmail.com"
password = "kpos qbst jqtj hqgt"
port = 993

while True:
    try:
        # Estabelece a conexão com o servidor IMAP
        mail = imaplib.IMAP4_SSL(imap_server, port)
        mail.login(email_address, password)

        # Seleciona a caixa de entrada
        mail.select('inbox')

        # obtem a data atual e Formata a data no formato desejado
        now = datetime.datetime.now()
        date = now.strftime('%d-%b-%Y')

        # Realiza uma pesquisa no meu inbox que retorne somente os Emails do remetente desejado e somente da data atual
        status, data = mail.search(None, 'UNSEEN FROM "gguimaraes647@gmail.com" SINCE "{}"'.format(date))


        email_ids = data[0].split()
        for email_id in email_ids:
            # Busca o email pelo ID
            status, data = mail.fetch(email_id, '(RFC822)')
            raw_email = data[0][1]
            print("Processando email com ID:", email_id)
            
            # Converte o email para um objeto da classe EmailMessage
            msg = email.message_from_bytes(raw_email)

            # Pucha informações sobre o corpo do Email
            assunto = msg ['Subject'] 
            endereco = msg['From']
            mensagem = ""
            
            # Verifica se a mensagem é multipart
            if msg.is_multipart():

                # Itera sobre as partes do e-mail
                for part in msg.get_payload():

                    # Verifica se a parte é texto
                    if part.get_content_type() == "text/plain":

                        # Obtém o corpo do e-mail
                        mensagem = part.get_payload(decode=True).decode("utf-8")

                        break  # Interrompe o loop após encontrar o corpo do e-mail
            
            print(f"From:{endereco}\nAssunto:{assunto}\n Mensagem {mensagem}")

            # Corpo do Email completo para o envio da mensagem
            body = f" Novo chamado aberto \n{'-'*30}\nDe: {endereco}\nAssunto: {assunto}\nMensagem: {mensagem}"     
                   
            # Confere so a istancia esta em bytes 
            if isinstance(endereco, bytes):
                endereco = endereco.decode('utf-8')  #Converte bytes para string

            # Confirma se realmente é do Email correto
            if endereco == 'Guilherme Guimaraes <gguimaraes647@gmail.com>':
                print("Email localizado")
                send_message(body)

        print("Procurando E-mail")
        print('\nRealizando pausa de 60 Segundos')
        time.sleep(60)
    
    except:
        #Chame a função de enviar mensagem após o erro
        print('Ocorreu um erro')