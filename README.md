## Sistema de busca em dados do Twitter

Seu objetivo como desenvolvedor, será o de construir um Sistema de busca de tweets por determinado padrão (por data, termo no tweet, ou por assunto). Esse sistema deverá conter os seguintes requisitos:

### Menu Principal

Ao iniciar o programa, o seguinte menu deve ser apresentado ao usuário:

```
Boas vindas ao nosso sistema:

1 - Buscar tweets por data
2 - Buscar tweets por termo
3 - Buscar tweets por assunto
4 - Salvar resultado da busca
5 - Sair
```

### Base de dados de tweets
<div align="justify";>
<p>O sistema ser desenvolvido, contará com uma base de dados coletada diretamente do Twitter.</p>

<p>Esta base dados está armazenada em um arquivo com extensão CSV, e o sistema deverá ser capaz de manipulá-la em tempo de execução de suas funcionalidades.</p>

<p>A base de dados é composta por cerca de 4 mil tweets separados por 4 assuntos distintos: <b>covid-19</b>; <b>ciência de dados</b>; <b>copa do mundo</b> e; <b>eleições</b>.</p>

<p>Além disso, é possível observar na base, campos contendo a data, a URL, o conteúdo, os nomes de usuários, e o assunto de cada tweet coletado.</p>

<p>Você pode baixar a base de dados <a href="https://drive.google.com/file/d/103GvlCjiVVBl03_sjPvUCCrR7Zb3uXwN/view?usp=sharing">AQUI</a></p>

</div>

### 1 - Buscar tweets por data

<div align="justify">
<p>A busca de tweets por <b>data</b> consiste em permitir que o usuário digite uma data no formato dd/mm/aaaa, e o sistema imprima na tela, os tweets referentes a data solicitada.</p>

<p>Exemplo:</p>
data informada: 16/10/2022

<p>Saída na tela:</p>

```
data  |  conteúdo   |   assunto
16/10/2022  |  To doido pra começar a copa logo , parece que nós ta a muito mais q 4 anos sem copa do mundo  |  copa do mundo
16/10/2022  |  Eba, 2022 tem copa do mundo no Qatar!!!  |  copa do mundo
16/10/2022  |  COVID-19 é um mal que assola a nossa sociedade em todos os sentidos |  covid-19
...
...
```
</div>

### 2 - Buscar tweets por termo

<div align="justify">
<p>A busca de tweets por <b>termo</b> consiste em permitir que o usuário digite uma palavra ou termo qualquer, e o sistema imprima na tela, os tweets que contenham a palavra informada.</p>

<p>Exemplo:</p>
palavra informada: copa

<p>Saída na tela:</p>

```
data  |  conteúdo   |   assunto
16/10/2022  |  To doido pra começar a copa logo , parece que nós ta a muito mais q 4 anos sem copa do mundo  |  copa do mundo
16/10/2022  |  Eba, 2022 tem copa do mundo no Qatar!!!  |  copa do mundo
...
...
```
</div>

### 3 - Buscar tweets por assunto

<div align="justify">
<p>A busca de tweets por <b>assunto</b> consiste em permitir que o usuário filtre na base de dados, todos os tweets que são referentes ao assunto solicitado. O sistema deve mostrar ao usuário, quais são os assuntos disponíveis, e permitir que o usuário escolha o que irá consultar.</p>

<p>Exemplo:</p>
assuntos disponíveis:
  1. Copa do Mundo
  2. Eleições
  3. Ciência de Dados
  4. COVID-19

Assunto escolhido pelo usuário: 1

<p>Saída na tela:</p>

```
data  |  conteúdo   |   assunto
16/10/2022  |  To doido pra começar a copa logo , parece que nós ta a muito mais q 4 anos sem copa do mundo  |  copa do mundo
16/10/2022  |  Eba, 2022 tem copa do mundo no Qatar!!!  |  copa do mundo
...
...
```
</div>

### 4 - Salvar resultado da busca

<div align="justify">
<p>Permita que o usuário salve em arquivo cada busca que ele fizer, independente da forma: data, termo ou assunto.</p>


<p>O arquivo deve ser em formato JSON (extensão .json) em que contenha a <b>data</b>, <b>conteúdo</b> e <b>assunto</b> de cada tweet retornado na busca feita pelo usuário</p>
</div>

### 5 - Sair

<div align="justify">
<p>Permita que o usuário finalize o programa quando desejar.</p>
