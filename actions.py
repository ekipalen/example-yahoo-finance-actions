from sema4ai.actions import action
from phi.tools.yfinance import YFinanceTools as yft
import json

@action
def get_stock_prices(symbol: str) -> str:
    """Gets stock prices based on the symbol. 

    Args:
        symbol: Company's stock symbol in string format.
            Example: "NVDA"

    Returns:
        Stock price as a string.
    """
    stock_price = yft().get_current_stock_price(symbol=symbol)
    print(f"Stock price for {symbol} is {stock_price}")
    return f"Stock price for {symbol} is {stock_price}"

@action
def get_company_info(symbol: str) -> str:
    """Gets company profile and overview based on the symbol.

    Args:
        symbol: Company's stock symbol in string format.
            Example: "AAPL"

    Returns:
        Company information as a string.
    """
    company_info = yft().get_company_info(symbol=symbol)
    print(f"Company info for {symbol}: {company_info}")
    return f"Company info for {symbol}: {company_info}"

@action
def get_stock_fundamentals(symbol: str) -> str:
    """Gets stock fundamentals based on the symbol.

    Args:
        symbol: Company's stock symbol in string format.
            Example: "GOOGL"

    Returns:
        Stock fundamentals as a string.
    """
    stock_fundamentals = yft().get_stock_fundamentals(symbol=symbol)
    print(f"Stock fundamentals for {symbol}: {stock_fundamentals}")
    return f"Stock fundamentals for {symbol}: {stock_fundamentals}"

@action
def get_income_statements(symbol: str) -> str:
    """Gets income statements based on the symbol.

    Args:
        symbol: Company's stock symbol in string format.
            Example: "AMZN"

    Returns:
        Income statements as a string.
    """
    income_statements = yft().get_income_statements(symbol=symbol)
    print(f"Income statements for {symbol}: {income_statements}")
    return f"Income statements for {symbol}: {income_statements}"

@action
def get_key_financial_ratios(symbol: str) -> str:
    """Gets key financial ratios based on the symbol, including officers and their salaries. 

    Args:
        symbol: Company's stock symbol in string format.
            Example: "MSFT"

    Returns:
        Key financial ratios as a string.
    """
    key_financial_ratios = yft().get_key_financial_ratios(symbol=symbol)
    print(f"Key financial ratios for {symbol}: {key_financial_ratios}")
    return f"Key financial ratios for {symbol}: {key_financial_ratios}"

@action
def get_analyst_recommendations(symbol: str) -> str:
    """Gets analyst recommendations based on the symbol.

    Args:
        symbol: Company's stock symbol in string format.
            Example: "NFLX"

    Returns:
        Analyst recommendations as a string.
    """
    analyst_recommendations = yft().get_analyst_recommendations(symbol=symbol)
    print(f"Analyst recommendations for {symbol}: {analyst_recommendations}")
    return f"Analyst recommendations for {symbol}: {analyst_recommendations}"

@action
def get_company_news(symbol: str, num_stories: int) -> str:
    """Gets company news based on the symbol.

    Args:
        symbol: Company's stock symbol in string format.
            Example: "TSLA"
        num_stories: Number of stories as integer. 
            Example: 2
    Returns:
        Company news as a string.
    """
    formatted_news: list[str] = []
    company_news = yft().get_company_news(symbol=symbol, num_stories=num_stories)
    news_data = json.loads(company_news)
    for news_item in news_data:
        title = news_item.get('title')
        publisher = news_item.get('publisher')
        link = news_item.get('link')        
        formatted_news.append(f"Title: {title}\nPublisher: {publisher}\nLink: {link}\n")
    output_string = "\n".join(formatted_news)
    print (output_string)
    return f"Company news for {symbol}: \n{output_string}"
