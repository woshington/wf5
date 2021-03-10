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
