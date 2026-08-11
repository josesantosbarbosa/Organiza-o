Script em Python que organiza automaticamente os arquivos de uma pasta, movendo cada um para uma subpasta de acordo com o seu tipo (extensão).

Projeto capstone do curso Google IT Automation with Python (Coursera), desenvolvido em conjunto com colegas de turma.

Índice
Problema que resolve
Como funciona
Categorias mapeadas
Estrutura do repositório
Como executar
Tecnologias usadas
Desafios e aprendizados
Melhorias futuras
Autor
Problema que resolve

Pastas como "Downloads" costumam acumular arquivos de todo tipo misturados: imagens, PDFs, planilhas, vídeos etc. Esse script organiza tudo automaticamente, criando subpastas como Imagens/, Documentos/, Planilhas/ e movendo cada arquivo para o lugar certo, sem precisar arrastar nada manualmente.

Como funciona
O usuário informa o caminho de uma pasta.
O script lê todos os arquivos dessa pasta.
Para cada arquivo, identifica a extensão (ex: .jpg, .pdf, .xlsx).
Cria (se não existir) uma subpasta para aquela categoria.
Move o arquivo para a subpasta correspondente.
Registra tudo em um arquivo log_organizacao.txt, com data e hora (na versão completa).
Categorias mapeadas
Categoria	Extensões
Imagens	.jpg, .jpeg, .png, .gif, .bmp, .webp
Documentos	.pdf, .doc, .docx, .txt, .odt
Planilhas	.xls, .xlsx, .csv
Apresentacoes	.ppt, .pptx
Compactados	.zip, .rar, .7z
Programas	.exe, .msi
Audios	.mp3, .wav
Videos	.mp4, .mkv, .avi, .mov
Outros	qualquer extensão não mapeada
Estrutura do repositório
organizador-arquivos/
├── organizador.py              # versão completa, com log de organização
├── organizador-simples.py      # versão enxuta, sem log
├── desfazer-organizacao.py     # reverte a organização
├── aprendizados-aplicados.md   # conexão entre o projeto e os cursos da minha formação
└── README.md
Como executar

Pré-requisito: Python 3 instalado (python.org).

Organizar uma pasta (versão completa, com log):

bash
python organizador.py

Organizar uma pasta (versão simples, sem log):

bash
python organizador-simples.py

Desfazer a organização (devolver arquivos ao lugar original):

bash
python desfazer-organizacao.py

Em qualquer um dos casos, o script pede o caminho da pasta. Exemplo:

Windows:   C:\Users\SeuNome\pasta
Linux/Mac: /home/usuario/pasta
Tecnologias usadas
Python 3
Bibliotecas nativas: os, shutil, datetime (nenhuma instalação extra necessária)
Desafios e aprendizados

O maior desafio foi entender a fundo o funcionamento do continue dentro do loop principal. No começo, a lógica de "pular a iteração atual sem interromper o restante do processo" não estava clara, e o problema parecia estar mais adiante no código, quando na verdade estava na base da estrutura de repetição. Revisitar esse conceito ajudou a consolidar o entendimento de estruturas de controle de fluxo em Python.

Mais detalhes em aprendizados-aplicados.md, com o mapeamento de quais cursos embasaram cada parte do projeto (Google IT Automation with Python, formação técnica em Engenharia de Software e IBM Data Management).

Melhorias futuras
Adicionar interface gráfica simples (Tkinter)
Gerar relatório da organização em planilha (Excel/CSV)
Permitir categorias personalizadas via arquivo de configuração externo
Automatizar a execução periódica
Autor

José Estudante de Análise e Desenvolvimento de Sistemas | Técnico em Engenharia de Software Em transição de carreira para a área de TI
