import re

texto = "Durante uma manhã ensolarada, Mariana decidiu explorar o universo das expressões regulares para aprimorar suas habilidades em programação. Ao pesquisar na internet, ela encontrou diversos artigos e fóruns interessantes. Em um desses sites, leu um post de **mariana.dev@mailficticio.com** que explicava os fundamentos do assunto.\
Curiosa, ela enviou dúvidas para o suporte técnico do fórum, utilizando o endereço **suporte_regexp@exemplodemail.net**. Logo recebeu uma resposta esclarecedora de **dev.joao@programacao.org**, que sugeria exercícios práticos. Durante uma pausa para o café, Mariana se inscreveu em uma newsletter enviada por **info.tecnologia@noticiasficticias.com**, a qual trazia dicas atualizadas do mundo digital.\
Mais tarde, assistiu a uma aula online ministrada pelo professor Carlos, cujo email de contato era **carlos.professor@aulaonline.edu**. Ao finalizar a aula, ela fez o backup de seus anotações e recebeu um lembrete do sistema, enviado por **backup_info@dadosseguro.net**.\
Animada com o progresso, Mariana participou de um webinar sobre inovação, onde o palestrante usava o email **palestrante_ti@cursoemvideo.org**. Em seguida, ela se juntou a um fórum de discussões técnicas e interagiu com outros profissionais através do endereço **forum_digital@comunidadeficticia.com**.\
Para colaborar com um projeto em grupo, ela entrou em contato com um colega via **dev.collab@colaborativo.tech**. Por fim, ao concluir um desafio de programação, Mariana recebeu um email de parabéns e incentivo, enviado por **agradecimentos@aprendizadoonline.info**.\
Este conjunto de exemplos com diferentes formatos de email pode ser bastante útil para praticar e testar expressões regulares."

# \b Indica onde uma palavra começa ou termina

#No padrao abaixo a utilizacao do \b serve para indicar palavras que comecam com umas das vogais
# que estão dentro de uma classe de caracteres
padrao = r'\b[aeiouAEIOU]\w*'

resultado = re.findall(padrao, texto)

if resultado:
    print(resultado)

print(len(resultado))
print('--------------------------------------Palavras que terminam com vogais:----------------------------------------------------------------')
#Encontrando palavras que terminam com uma vogal

padrao = r'\w*[aeiouAEIOU]\b'

resultado = re.findall(padrao, texto)

if resultado:
    print(resultado)

print(len(resultado))