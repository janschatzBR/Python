# CarteiraBacktest — versão completa

Este pacote baixa os dados históricos dos **58 ativos** definidos em `tickers.csv`, converte tudo para USD e gera:

- `output/historico_carteira.xlsx`
- `output/historico_carteira.json`
- `output/log.txt`

O arquivo Excel já contém os dois cenários:

1. **Dividendos separados em caixa**
2. **Dividendos reinvestidos**

## Premissas configuradas

- Capital inicial: **US$ 10.000**
- Data-alvo inicial: **20/07/2021**
- Compra: primeiro fechamento disponível em ou após a data-alvo
- Pesos iguais entre os 58 ativos
- Frações de ações/cotas permitidas
- SPCX excluído
- VWCE: `VWCE.DE` (Xetra, EUR)
- VHYL: `VHYL.L` (LSE, GBP)
- BTC e ETH incluídos
- Sem impostos, retenções, corretagem, spread cambial ou slippage
- Dividendos datados pelo ex-dividend date informado pelo Yahoo Finance
- Reinvestimento aproximado pelo fechamento do dia ex-dividendo; na ausência de preço, pelo primeiro fechamento posterior
- O `Close` do Yahoo é tratado como ajustado por splits; os splits são registrados para auditoria, mas não reaplicados às quantidades (evita dupla contagem)

## Execução rápida — Windows

1. Descompacte o ZIP.
2. Dê dois cliques em `executar_windows.bat`.
3. Aguarde a mensagem de conclusão.
4. Envie o arquivo `output/historico_carteira.xlsx` nesta conversa.

## Execução rápida — macOS/Linux

Abra o Terminal dentro da pasta e execute:

```bash
chmod +x executar_mac_linux.sh
./executar_mac_linux.sh
```

## Execução manual

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
```

Ative o ambiente virtual:

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Instale as dependências e execute:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python download.py
```

## Comandos úteis

Validar a configuração sem baixar dados:

```bash
python download.py --validate-only
```

Incluir preços e câmbio diários no arquivo final:

```bash
python download.py --daily
```

A opção `--daily` aumenta bastante o tamanho do Excel e do JSON. Para o backtest solicitado, não é necessária.

## Abas do Excel

- `Resumo`: resultado por ativo e total da carteira
- `Dividendos`: cada evento e os valores nos dois cenários
- `Splits`: desdobramentos e quantidades antes/depois
- `Cotacoes_Chave`: compra, dividendos, splits e último preço
- `Premissas`: metodologia utilizada
- `Erros`: ativos que não puderam ser processados
- `Precos_Diarios`: somente ao usar `--daily`
- `FX_Diario`: somente ao usar `--daily`

## Personalização

Edite `config.py` para alterar:

- data inicial/final
- capital inicial
- nomes dos arquivos
- inclusão de séries diárias

Edite `tickers.csv` para incluir ou excluir ativos. Use `Incluir=0` para ignorar uma linha.

## Atenção

Yahoo Finance/yfinance é uma fonte conveniente, mas não é uma base oficial de custódia ou tributação. Confira os registros na aba `Erros`, no `log.txt` e, para decisões financeiras, compare eventos relevantes com documentos do emissor ou da corretora.
