<h1 align="center">Sistema de Gerenciamento de Projetos</h1>

## Descrição do Projeto
<p align="justity">
  O sistema prover uma API RESTfull para cadastro de projetos e orçamentos. As principais funcionalidades são:
</p>
<ul>
  <li>Cadastro, listagem, atualização e remoção de projetos.</li>
  <li>Cadastro, listagem, atualização e remoção de dados de gerenciamento (valor orçado e valor gasto).</li>
  <li>Aprovar ou cancelar projetos</li>  
  <li>Listar projetos com valor disponível</li>  
</ul>

## Restrições
<p align="justity">
  Todas as funcionalidades são restritas a usuários autenticados, exceto o cadastro de usuários. </p> 
<p align="justity">
  Além disso, a autenticação é por meio de token enviado no header da requisição no seguinte formato:
</p>
<p align="justity">
  <strong>key:</strong> Authorization
</p>
<p align="justity">
   <strong>value:</strong> Token "token_gerado" (sem aspas)  
</p>

## Executando do Projeto
<ol>
  <li>Clonar o repositório</li>
  <li>Criar o ambiente virtual - virtualenv [nome_do_ambiente]</li>
  <li>Entre na pasta do projeto - cd pasta_do_projeto </li>
  <li>Ativar o ambiente virtual - source /caminho_do_ambiente/bin/activate</li>
  <li>Executar a instalação das dependências - pip install -r requirements.txt </li>
  <li>Executar a aplicação - ./manage.py runserver</li>
</ol>

## Links de acesso
