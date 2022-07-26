"""
Aplicação Web diretamente com python usa o protocolo WSGI que é um protocolo
de comunicação do python com o servidor web.

O protocolo é, o WSGI espera que na aplicação web feita em python tenha
uma função chamada application e espera também que nessa função tenha um
start_response que é um callback.

callback é um uma função de parâmetro para outra função, ou seja
quando chamada a primeira função ela vai executar e no meio ou no final dela
ela vai chamar essa outra função que foi passada de parâmetro.

então, depois do WSGI chamar a função application, a função vai chamar
o callback, start_response, pra dizer que começou a resposta

essa função até então ta só seguindo o protocolo WSGI, pra conseguir
utilizar ela, precisa de um application server, no próprio python tem um
mas no dia a dia usa algum mais poderoso com mais funcionalidades.
Temos os servidores web, uwsgi e o gunicorn

Nesse ex to usando o gunicorn

No terminal chama o servidor web, no caso gunicorn e depois passa o nome do
arquivo e o nome da função que o WSGI vai se conectar

gunicorn wsgi:application

pra usar o servidor proprio do python escreve o seguinte codigo:

if __name__ == "__main__" :
    from wsgiref.simple_server import make_server
    make_server( '0.0.0.0' , 8000 , application).serve_forever()
"""

def application (environ, start_response):
    body = b"<h1>Restaurante da Natal</h1><button>Login</button>"
    status = '200 OK'
    headers = [( 'Content-type' , 'text/html' )]
    start_response(status, headers)
    return [body]