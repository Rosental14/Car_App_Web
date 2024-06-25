# Projeto de Aplicativo Web para Análise de Dados de Vendas de Carros  

## Link para visualização  

<https://projeto-sprint-5-renan-rosental.onrender.com/>

## Descrição  

Este projeto visa fornecer prática em tarefas comuns de engenharia de software, com intuito de complementar as habilidades em ciência de dados. O objetivo é criar e gerenciar ambientes virtuais Python, desenvolver um aplicativo web e implantar em um serviço de nuvem, tornando-acessível ao público.
O projeto utiliza um conjunto de dados de anúncios de vendas de carros ‘vehicles_us.csv’. O foco principal está na criação do aplicativo web e não na análise dos dados.  

## Funcionalidades  

* Desenvolvimento de um dashboard interativo utilizando Streamlit.
* Implantação do aplicativo web no Render.  
  
## Instalação  

### Pré-requisitos  

* Python 3.x
* Git
* Conta no GitHub
* Conta no Render
### Instruções de Instalação  

1.	Clone repositório do GitHub: git clone https://github.com/Rosental14/Car_App_Web.git  
<br>
2.	Navegue até diretório do projeto: cd Car_App_Web  
<br>
3.	Crie um ambiente virtual: python -m venv vehicles_env  
<br>
4.	Ative ambiente virtual:  
  * **No Windows:** vehicles_env\Scripts\activate  
  * **No macOS/Linux:** source vehicles_env/bin/activate  
<br>
5.	Instale as dependências: pip install pandas plotly_express streamlit  
<br>
6.	Clone repositório no VS Code e configure interpretador Python para usar ambiente virtual criado.  

## Uso
1.	**Baixe conjunto de dados de anúncios de carros (vehicles_us.csv) e coloque-no diretório raiz do projeto.**  
<br>

2.	**Execute a análise exploratória de dados:**
* Crie um diretório chamado notebooks.
* Crie um arquivo Jupyter Notebook chamado EDA.ipynb no diretório notebooks.
* Realize a análise exploratória dos dados utilizando Plotly Express.
<br>

3.	**Desenvolva dashboard do aplicativo web:**
* Crie um arquivo app.py no diretório raiz do projeto.
* Importe streamlit, pandas e plotly_express.
* Leia arquivo CSV dos dados em um DataFrame.
* Crie interatividade no aplicativo utilizando filtros, botões ou caixas de seleção para gerar gráficos.  
<br>

4.	**Configuração do Streamlit para Render:**  

* Adicione um arquivo de configuração .streamlit/config.toml com seguinte conteúdo:  <br>
    [server]
    headless = true
    port = 10000
<br>
    [browser]
    serverAddress = "0.0.0.0"
    serverPort = 10000 
<br>

5. **Execute aplicativo localmente:** streamlit run app.py
<br>

6.	**Implante aplicativo no Render:**  

* Crie um novo serviço web no Render vinculado ao repositório do GitHub.
* Configure comando de compilação:
* pip install --upgrade pip && pip install -r requirements.txt
* Configure comando de início: streamlit run app.py  
* Verifique se aplicativo está acessível no URL fornecido pelo Render.  

## Contribuições  

O Projeto ainda está em desenvolvimento. Portanto, contribuições são muito bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.  

## Créditos  

* **Autor:** Renan Rosental  

## Contato  

Para dúvidas e feedback, entre em contato via e-mail: renan.engal@gmail.com