"""Configurações do coletor/backtest."""

START_DATE = "2021-07-20"
END_DATE = None  # None = data atual; o script inclui o último fechamento disponível.
INITIAL_CAPITAL_USD = 10_000.00

TICKERS_FILE = "tickers.csv"
OUTPUT_FOLDER = "output"
OUTPUT_EXCEL = "historico_carteira.xlsx"
OUTPUT_JSON = "historico_carteira.json"
LOG_FILE = "log.txt"

# False deixa o arquivo bem menor. O backtest, dividendos e auditoria continuam completos.
SAVE_DAILY_PRICES = False
SAVE_DAILY_FX = False

# Reinvestimento: usa o fechamento do dia ex-dividendo; se não houver cotação,
# usa o primeiro fechamento disponível depois do evento.
REINVEST_DIVIDENDS = True

# O Yahoo pode tentar reparar erros de preço/moeda automaticamente.
YFINANCE_REPAIR = True
REQUEST_TIMEOUT_SECONDS = 30
