# EstudoFlow API 🚀

API para gestão e monitoramento de carga horária e fluxos de estudo acadêmicos.

## 💻 Descrição do Ambiente de Desenvolvimento Utilizado
O ambiente técnico para construção, depuração e validação desta aplicação consistiu em:
* **Sistema Operacional:** Windows 11
* **IDE / Editor de Código:** Visual Studio Code (VS Code)
* **Terminais de Execução:** PowerShell Integrado e Git Bash para controle de versão


## 🛠️ Especificação da Linguagem, Frameworks e Banco de Dados
* **Linguagem de Programação:** Python 3.13
* **Framework Web Principal:** FastAPI (Construção de rotas com alto desempenho e assincronismo)
* **Validação de Dados:** Pydantic v2 (Definição de tipos e validação de payloads)
* **ORM (Mapeamento Objeto-Relacional):** SQLAlchemy v2 (Modelagem de entidades e abraçar o SQL)
* **Banco de Dados:** PostgreSQL (Instância oficial hospedada em nuvem na plataforma Render)


## 🖥️ Requisitos de Sistema para Executar a Aplicação
Para que o projeto seja instalado e executado localmente de forma correta, o ambiente necessita de:
* Python na versão 3.10 ou superior devidamente configurado no PATH do sistema.
* Gerenciador de pacotes pip instalado e updated.
* Acesso ativo à internet para que a aplicação consiga se comunicar com o banco de dados hospedado externamente na nuvem do Render.


## 🚀 Instruções Sobre Como Instalar e Executar a Aplicação

### 1. Clonar o Repositório
Abra o seu terminal na pasta desejada e execute o comando abaixo para clonar e acessar a pasta do projeto:
```bash
git clone [https://github.com/Ketsiane/EstudoFlow.git](https://github.com/Ketsiane/EstudoFlow.git)
cd EstudoFlow

### 2. Instalar as dependências
Instale as dependências estáveis utilizando os parâmetros recomendados para o ambiente Windows:
```bash
pip install -r requirements.txt --only-binary :all:
pip install psycopg2-binary --only-binary :all:

### 3. Executar o Servidor Local
Inicie o servidor Uvicorn para rodar a aplicação em modo de desenvolvimento:
```bash
uvicorn main:app --reload

A aplicação iniciará automaticamente e estará acessível pelo endereço local [http://127.0.0.1:8000](http://127.0.0.1:8000)


🧼 Descrição da Aplicação de Práticas de Código Limpo (Clean Code)
O desenvolvimento seguiu critérios rigorosos de boas práticas e arquitetura limpa:

Separação de Conceitos (SoC): Cada arquivo no projeto possui uma única responsabilidade central estruturada (main.py gerencia rotas, database.py inicializa a sessão, models.py define tabelas estruturais e schemas.py manipula a tipagem do Pydantic).

Nomes Significativos: Funções, variáveis e métodos utilizam nomenclatura descritiva clara em português que expressa fielmente sua função lógica (ex: criar_disciplina, carga_horaria).

Funções Pequenas: Cada bloco de rota foca exclusivamente em executar uma única tarefa do ciclo de vida do CRUD.


🏗️ Identificação da Aplicação de Padrões de Projeto (Design Patterns)
Data Transfer Object (DTO): Aplicado através dos esquemas e classes do Pydantic no arquivo schemas.py (DisciplinaCreate e DisciplinaResponse), isolando as regras de recebimento e envio de dados da rede das tabelas físicas do banco.

Injeção de Dependência: Utilizada nativamente através do construtor Depends(database.get_db) nas assinaturas das rotas da API, isolando o gerenciamento de abertura e fechamento de conexões com o banco de dados.


🧪 Identificação da Criação de Testes Automatizados para a Aplicação
O ecossistema conta com documentação técnica interativa gerada automaticamente via Swagger UI, que atua diretamente como interface gráfica para realização de testes automatizados e assíncronos das rotas do CRUD.

Como executar os testes: Com a aplicação ativa localmente, abra o navegador e acesse [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). Clique no botão "Try it out" de qualquer rota disponível (POST, GET, PUT, DELETE), informe os parâmetros necessários e clique em "Execute" para realizar o teste e conferir o retorno, validações e persistência em tempo real.


🤝 Informações Sobre Como Contribuir para o Projeto
Realize o Fork deste repositório para sua conta pessoal.

Crie uma branch específica para codificar a sua melhoria: git checkout -b feature/nova-funcionalidade.

Adicione suas alterações ao histórico local e realize o commit: git commit -m "Add: Implementa nova funcionalidade".

Envie as modificações via push para o seu repositório remoto: git push origin feature/nova-funcionalidade.

Abra um Pull Request detalhado apontando para a ramificação principal deste repositório original para que o código seja analisado.