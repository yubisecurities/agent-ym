def get_company_info(ticker: str) -> dict:
    """
    Retrieves basic information for a given stock ticker.
    This is a mock tool for demonstration purposes.
    """
    print(f"\n--- TOOL CALLED: get_company_info for ticker: {ticker} ---\n")
    mock_db = {
        "GOOGL": {"name": "Alphabet Inc.", "sector": "Communication Services"},
        "MSFT": {"name": "Microsoft Corporation", "sector": "Technology"},
        "ADBE": {"name": "Adobe Inc.", "sector": "Technology"}
    }
    return mock_db.get(
        ticker.upper(),
        {"error": f"Information for ticker '{ticker}' not found."}
    )