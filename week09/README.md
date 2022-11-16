# Trabalho 02 - Unidade 02 - Algoritmo e Estrutura de Dados

## Membros

- Efrain Marcelo Pulgar Pantaleon | 20220080507
- Pedro Leandro Batista Marques | 20220080427

## Assuntos

Este trabalho é centrado na analise de dados de voos dentro do território brasileiro.As 4 análises
a serem feitas serão :
 
- Assortatividade
- Análise bivariada
- Grau de conexões
- Análise do caminho mais curto

## Solução do Trabalho

Como base para desenvolvimento de código e afins, utilizamos do repositório [rep](https://github.com/alvarofpp/dataset-flights-brazil) do github.

A resolução e códigos envolvendo todas as analises podem ser encontradas aqui [![Jupyter](https://img.shields.io/badge/-Notebook-191A1B?style=flat-square&logo=jupyter)](week09.ipynb)</p>

## Explicações

Em nosso trabalho, primeiro fizemos a transformação do dataset air_traffic em um grafo utilizando da biblioteca do 
[networkx](https://networkx.org/).Trabalharemos com o grafo e nós pelo resto do trabalho.

### Requisito 1 - Assortatividade

Para esse requisito, faremos um estudo de assortatividade da rede considerando como atributo a REGIÃO onde está localizado o aeroporto.

O primeiro passo é visualizar a rede, e para isso, fizemos o plot a seguir de uma figura que mostra as conexões de cada nó

![assortatividade](../week09/imagens/r1_assortatividade.png)

Após criar uma representação visual, criaremos uma representação matricial (mixing matrix) da imagem acima considerando a REGIÃO que o aeroporto está localizado.

Trabalhando essa matriz, encontramos que o coeficiente de assortatividade dessa rede é de aproximadamente ```0.372```. Por definição, uma rede á desassortativa se o coeficiente de assortatividade está entre -1 e 0 (elementos do mesmo grupo tendem a se conectar com elementos de outros grupos) e a rede é assortativa se o coeficiente é entre 0 e 1 (elementos do mesmo grupo tendem a se conectar com elementos do mesmo grupo). Como o coeficiente dessa rede está entre 0 e 1, então a rede é assortativa. Neste exemplo em específico, isso significa que aeroportos de uma região tendem a "se conectar" com aeroportos da mesma região, ou seja, os voos que saem da região sul, por exemplo, tendem a ter como destino a própria região sul.

### Requisito 2 - Análise Bivariada

Para esse segundo requisito, teremos a análise bivariada entre o grau do vértice e o número médio de vizinhos.Contará com os seguintes processos.

- criando subgrafos da rede do brasil, cada subgrafo representa uma região diferente
- Pegando os graus médios dos vizinhos de cada região
- Pegando os graus médios dos vizinhos do Brasil
- Transformando os graus médios em listas
- Análise Bivariada da rede do Brasil

Como resultados temos os seguintes gráficos:

![grauBrasil](../week09/imagens/r2_grauBrasil.png)


![grauBrasil](../week09/imagens/r2_grauNorte.png)

![grauBrasil](../week09/imagens/r2_grauNordeste.png)

![grauBrasil](../week09/imagens/r2_grauCentroOeste.png)

![grauBrasil](../week09/imagens/r2_grauSudeste.png)

![grauBrasil](../week09/imagens/r2_grauSul.png)

Mediante a analise dos gráficos e dados encontrados, encontramos os graus de assortatividade :

Grau de assortatividade da rede do  Brasil:  -0.19522933769365391
Grau de assortatividade da subrede do Norte:  -0.2201013510739867
Grau de assortatividade da subrede do Nordeste:  -0.31740910282280993
Grau de assortatividade da subrede do Sul:  -0.353730950502798
Grau de assortatividade da subrede do Sudeste:  -0.36429315092441866
Grau de assortatividade da subrede do Centro-Oeste:  -0.3459713170990661

Em uma rede desassortativa com relação ao grau, nós de alto grau tendem a se conectar com nós de baixo grau. Em uma rede assortativa com relação ao grau, nós de alto grau tendem a se conectar com nós de alto grau. Quando observamos o gráfico ```Análise Bivariada da rede do Brasil```, observa-se que nós de grau alto tendem a se conectar com nós de grau baixo, ou seja, a rede do brasil é uma rede desassortativa em relação ao grau. Isso é confirmado ao observar os coeficientes de assortatitivade das 5 regiões do Brasil: ambos seguem a tendência da rede do brasil, pois todos são graus desassortativos. As regiões ```Sudeste``` e ```Sul```, são, respectivamente as regiões com maior grau de desassortividade. Na prática, isso signigica que essas são as regiões que mais se conectam com outras regiões, em particular, com as que menos se conectam com outras regiões (```Norte``` e ```Nordeste```).

### Requisito 3 - Quantos componentes conectados existem na malha aérea brasileira? 

Para começar, buscaremos a vizualização de todos os nós da rede do Brasil (sem separação por grupo).

![grauBrasil](../week09/imagens/r3_grafroRedeBrasil.png)

Depois a vizualização das outras regiões: 

- Norte
![grauBrasil](../week09/imagens/r3_grafroSubredeNorte.png)

- Nordeste
![grauBrasil](../week09/imagens/r3_grafroSubredeNordeste.png)

- Centro Oeste
![grauBrasil](../week09/imagens/r3_grafroSubredeCentroOeste.png)

- Sudeste
![grauBrasil](../week09/imagens/r3_grafroSubredeSudeste.png)

-Sul
![grauBrasil](../week09/imagens/r3_grafroSubredeSul.png)

Analisando a quantidade de Componentes conectados temos que:

Componentes conectados são componentes que estão ligados entre si por meio de uma aresta. Podemos utilizar esse fato para gerar subgrafos de cada região, e enteder como ocorrem as conexões em cada região do Brasil.

#### Perguntas Respondidas 

- Como resposta para a pergunta se a rede do Brasil é conectada, temos que não é.

- Quantos ***COMPONENTES*** conectados existem na rede do brasil? 6

- Análise de conexões, caracterizando cada componente por: quantidade e porcentagem por região

```
Análise do componente {'SNIG', 'SNPC', 'SBSM', 'SDWQ', 'SBDO', 'SNOX', 'SNMZ', 'SDNM', 'SNPX', 'SBPV', 'SWBR', 'SWGN', 'SJCW', 'SBLN', 'SWNO', 'SWBZ', 'SDOU', 'SWMW', 'SNUC', 'SSIJ', 'SNAT', 'SBPC', 'SNUB', 'SDLU', 'SNBU', 'SBAU', 'SDDM', 'SBCO', 'SWNA', 'SWOW', 'SBJC', 'SBRB', 'SNTF', 'SNUU', 'SBMQ', 'SNKB', 'SBPI', '2NHT', 'SBMO', 'SBLO', 'SBQV', 'SSCR', 'SWKO', 'SWHG', 'SBAG', 'SWLC', 'SWXM', 'SBSP', 'SSCC', 'SSOE', 'SBBI', 'SDZC', 'SJVO', 'SBMD', 'SNGA', 'SNPV', 'SWTP', 'SNAX', '1AON', 'SBAM', 'SNIC', 'SBPB', 'SNSW', 'SBNF', 'SBNT', 'SWTU', 'SSTD', 'SSCL', 'SBTS', 'SSAE', 'SBCZ', 'SBTE', 'SSSB', 'SDBB', 'SWJV', 'SBBZ', 'SSGY', 'SNJM', 'SSTL', 'SBMC', 'SWFN', 'SNEE', 'SBAA', 'SNWR', 'SNWS', 'SDCO', 'SIGP', 'SNBM', 'SBPJ', 'SWBC', 'SSPI', 'SDJA', 'SBUA', 'SWUQ', 'SBCT', 'SBMS', 'SSUW', 'SWDB', 'SWVC', 'SSTE', 'SBUL', 'SNCX', 'SNCB', 'SWKN', 'SBPN', 'SDMC', 'SNKK', 'SWAE', 'SBBG', 'SISO', 'SBOI', 'SBCB', 'SNQD', 'SBCV', 'SBAR', 'SNGV', 'SBAX', 'SBCA', 'SBSL', 'SBRD', 'SBJE', 'SJRG', 'SWNK', 'SWDM', 'SDBK', 'SSOG', 'SSBG', 'SBAV', 'SNZA', 'SSLS', 'SNSG', 'SWII', 'SBAS', 'SJTC', 'SWKK', 'SBCC', 'SBCI', 'SSPG', 'SJNP', 'SNPP', 'SBHT', 'SBML', 'SWSQ', 'SNPJ', 'SBTF', 'SNKI', 'SNSM', 'SBDN', 'SSJA', 'SNXL', 'SNQW', 'SBGP', 'SBCD', 'SNQY', 'SBLJ', 'SBBV', 'SDSC', 'SWPJ', 'SNUH', 'SBBQ', 'SBBW', 'SDLK', 'SBCP', 'SSAC', 'SNBA', 'SWUI', 'SBIZ', 'SNLO', 'SNEB', 'SWEK', 'SWRD', 'SSGG', 'SNYA', 'SDVG', 'SBLS', 'SBSI', 'SWNH', 'SWJP', 'SNIU', 'SDTK', 'SNML', 'SBCR', 'SWJN', 'SWBU', 'SWIQ', 'SWOB', 'SWFJ', 'SSCP', 'SSSK', 'SNNC', 'SSKM', 'SSLT', 'SBKG', 'SSOU', 'SSPK', 'SBCF', 'SWWU', 'SNAB', 'SNFX', 'SBJF', 'SBAF', 'SBTD', 'SSND', 'SNTS', 'SDRS', 'SNVV', 'SWJW', 'SNMH', 'SBIH', 'SNYB', 'SWMP', 'SSUV', 'SBEG', 'SSEP', 'SDAG', 'SBFE', 'SWZM', 'SDTF', 'SSNC', 'SBSO', 'SDOV', 'SSRS', 'SBBT', 'SNQM', 'SBJI', 'SBSV', 'SJKB', 'SBMM', 'SBVT', 'SWJU', 'SWHT', 'SBZM', 'SWGI', 'SNBI', 'SWPD', 'SWBE', 'SNHS', 'SBMI', 'SBBH', 'SNMD', 'SBRF', 'SBTB', 'SWCB', 'SBEK', 'SNKE', 'SBGS', 'SDVE', 'SBRG', 'SBGU', 'SNIP', 'SWWA', 'SBGL', 'SBRP', 'SWJQ', 'SBCX', 'SBPK', 'SDPA', 'SSVL', 'SWGP', 'SNLA', 'SNXW', 'SNJO', 'SJLM', 'SSSC', 'SDIM', 'SBLP', 'SBIL', 'SBMK', 'SSNM', 'SJGU', 'SBCY', 'SWPF', 'SBMH', 'SWCD', 'SBST', 'SWDE', 'SNCI', 'SWBI', 'SBTL', 'SNMX', 'SBMY', 'SNUO', 'SNRB', '6ASO', 'SNJK', 'SBTC', 'SWVR', 'SNBR', 'SBUR', 'SNNG', 'SNMJ', 'SWKC', 'SNAR', 'SNDR', 'SNGQ', 'SJHG', 'SBDB', 'SNTO', 'SNCP', 'SNOS', 'SSCN', 'SNOB', 'SWRF', 'SSCK', 'SWEE', 'SNTP', 'SBMT', 'SJTS', 'SWUY', 'SBAN', 'SNBX', 'SBPG', 'SNTI', 'SNJN', 'SNCL', 'SNJB', 'SJQP', 'SBGR', 'SNVS', 'SBPO', 'SBPP', 'SDFR', 'SWYK', 'SBJA', 'SWWD', 'SBPM', 'SWUA', 'SBYA', 'SNMA', 'SSAP', 'SNBV', 'SNXB', 'SNUI', 'SNRJ', 'SBBP', 'SNDV', 'SBVC', 'SNDH', 'SBLE', 'SBUG', 'SBCM', 'SBUF', 'SNRU', 'SJUR', 'SDAA', 'SBVH', 'SNMK', 'SWXV', 'SSPB', 'SSNH', 'SWCA', 'SIBU', 'SWEI', 'SBTU', 'SDOW', 'SWJI', 'SSER', 'SNPY', 'SBTK', 'SBFL', 'SSKW', 'SNNU', 'SILC', 'SBTR', 'SIFV', 'SNBS', 'SBTT', 'SWPI', 'SNAV', 'SBJU', 'SBTG', 'SBSG', 'SWNQ', 'SWBV', 'SWHP', 'SWJH', 'SBFN', 'SBJR', 'SNSH', 'SBPS', 'SBGV', 'SWCP', 'SNNT', 'SNDT', 'SBCN', 'SBJP', 'SWCI', 'SNQX', 'SNGI', 'SWSI', 'SNCC', 'SSFB', 'SDH2', 'SBBU', 'SBUY', 'SBBR', 'SWEU', 'SNPG', 'SBGM', 'SBNM', 'SNDB', 'SIQE', 'SBKP', 'SNVR', 'SWCQ', 'SDUN', 'SDAM', 'SNFE', 'SNMU', 'SBVG', 'SWPY', 'SNJD', 'SNVB', 'SSBN', 'SDUB', 'SSVI', 'SNCT', 'SIRI', 'SWQR', 'SNYV', 'SBIT', 'SBPL', 'SBRJ', 'SNZR', 'SWFE', 'SBMG', 'SWPH', 'SSUM', 'SSZW', 'SNGX', 'SDZG', 'SNJR', 'SJQK', 'SBIP', 'SIKC', 'SNAP', 'SBGO', 'SJDB', 'SBCG', 'SIXE', 'SBFZ', 'SNFO', 'SNRS', 'SNDC', 'SBCH', 'SWLV', 'SWMK', 'SNQG', 'SWNS', 'SWNB', 'SBYS', 'SJLU', 'SILJ', 'SBMA', 'SDAN', 'SSZR', 'SBIC', 'SSDO', 'SBSN', 'SWLF', 'SSAB', 'SBMN', 'SBSR', 'SNBW', 'SBPA', 'SWTS', 'SWYY', 'SBBE', 'SWFX', 'SWYN', 'SNDQ', 'SWPC', 'SBAQ', 'SWRP', 'SDCG', 'SNVC', 'SSCT', 'SSBB', 'SBTV', 'SBJV', 'SBFC', 'SIZX', 'SBCJ', 'SBFI', 'SWLB', 'SIMK', 'SNPD', 'SBSC', 'SBJD', 'SBPF', 'SBAE', 'SBAC', 'SBAT', 'SWBG', 'SSHZ', 'SNDM', 'SBME', 'SWPQ', 'SBSJ', 'SNAH'} 

Componentes connectados por região: 

Norte: 126 

Nordeste:  92 

Sul:  74 

Sudeste:  118 

Centro-Oeste  90 

Porcentagem de componentes connectados por região: 

Norte:  25.2  %

Nordeste:  18.4 

Sul:  14.8  %

Sudeste:  23.6  %

Centro-Oeste  18.0  %

-----------------------------------------------------------------

Análise do componente {'SNGR'} 

Componentes connectados por região: 

Norte: 1 

Nordeste:  0 

Sul:  0 

Sudeste:  0 

Centro-Oeste  0 

Porcentagem de componentes connectados por região: 

Norte:  100.0  %

Nordeste:  0.0 

Sul:  0.0  %

Sudeste:  0.0  %

Centro-Oeste  0.0  %

-----------------------------------------------------------------

Análise do componente {'SNBG'} 

Componentes connectados por região: 

Norte: 0 

Nordeste:  0 

Sul:  0 

Sudeste:  1 

Centro-Oeste  0 

Porcentagem de componentes connectados por região: 

Norte:  0.0  %

Nordeste:  0.0 

Sul:  0.0  %

Sudeste:  100.0  %

Centro-Oeste  0.0  %

-----------------------------------------------------------------

Análise do componente {'SBER'} 

Componentes connectados por região: 

Norte: 1 

Nordeste:  0 

Sul:  0 

Sudeste:  0 

Centro-Oeste  0 

Porcentagem de componentes connectados por região: 

Norte:  100.0  %

Nordeste:  0.0 

Sul:  0.0  %

Sudeste:  0.0  %

Centro-Oeste  0.0  %

-----------------------------------------------------------------

Análise do componente {'SSBE'} 

Componentes connectados por região: 

Norte: 0 

Nordeste:  0 

Sul:  0 

Sudeste:  0 

Centro-Oeste  1 

Porcentagem de componentes connectados por região: 

Norte:  0.0  %

Nordeste:  0.0 

Sul:  0.0  %

Sudeste:  0.0  %

Centro-Oeste  100.0  %

-----------------------------------------------------------------

Análise do componente {'SBJH'} 

Componentes connectados por região: 

Norte: 0 

Nordeste:  0 

Sul:  0 

Sudeste:  1 

Centro-Oeste  0 

Porcentagem de componentes connectados por região: 

Norte:  0.0  %

Nordeste:  0.0 

Sul:  0.0  %

Sudeste:  100.0  %

Centro-Oeste  0.0  %

-----------------------------------------------------------------
```


