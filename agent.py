from services import ask_agent

def generate_sql(question: str, schema: str):
    prompt= f"""
    You are a SQL-making agent for a SQLite database. 
    
    Schema:
    {schema}

    User question:
    {question}

    Only output a valid SELECT SQL query (no explanation).
"""
    sql = ask_agent(prompt).strip()
    return sql