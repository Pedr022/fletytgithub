import flet as ft

def main(pagina):
    titulo = ft.Text('chat dos crias')

    def enviar_msg_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = caixa_chat.value
        mensagem = f'{nome_usuario}: {texto_campo_mensagem}'
        pagina.pubsub.send_all(mensagem)

        caixa_chat.value = ''
        pagina.update()

    caixa_chat = ft.TextField(label='escreva sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('enviar', on_click=enviar_mensagem)
    linha_chat = ft.Row([caixa_chat, botao_enviar])
    chat = ft.Column()

    def abrir_chat(evento):
        print('clicou para entrar')
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)

        pagina.add(chat)
        pagina.add(linha_chat)
      
        nome_usuario = caixa_nome.value
        mensagem = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()
    
    titulo_popup = ft.Text('bem-vindo ao chat')
    caixa_nome = ft.TextField(label='escreva seu nome no chat', on_submit=abrir_chat)
    botao_popup = ft.ElevatedButton('entrar no chat', on_click=abrir_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print('clicou no botão')

    botao = ft.ElevatedButton('iniciar chat', on_click=abrir_popup)
    
    pagina.add(titulo)
    pagina.add(botao)

ft.app(main)
