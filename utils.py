import re

# Allow SELECT with optional leading whitespace
ALLOWED_SQL_PATTERN = re.compile(r"^\s*select\b", re.IGNORECASE)

# Block dangerous keywords explicitly
BLOCKED_KEYWORDS = re.compile(
    r"\b(insert|update|delete|drop|alter|truncate|create|replace|grant|revoke)\b",
    re.IGNORECASE,
)

def clean_sql(sql: str) -> str:
    """
    Remove markdown code fences and extra formatting
    """
    sql = sql.strip()

    # Remove ```sql ... ``` or ``` ... ```
    if sql.startswith("```"):
        sql = re.sub(r"```[\w]*", "", sql)  # remove ```sql
        sql = sql.replace("```", "")

    return sql.strip()


def is_safe_sql(sql: str) -> bool:
    sql = clean_sql(sql)

    print("Cleaned SQL =====", repr(sql))

    # Must start with SELECT
    if not ALLOWED_SQL_PATTERN.match(sql):
        return False

    # Must not contain blocked keywords
    if BLOCKED_KEYWORDS.search(sql):
        return False

    return True