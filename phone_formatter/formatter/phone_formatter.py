import re

def format_phone_number(number: str, *, min_length: int = 10, max_length: int = 15) -> str | None:

  if not number:
      return None

  formatted = re.sub(r"[^\d+]", "", number)

  if formatted.count('+') > 1 or (formatted and formatted[0] != '+'):
      formatted = '+' + re.sub(r'\+', '', formatted)

  digits_only = re.sub(r'\D', '', formatted)
  if not (min_length <= len(digits_only) <= max_length):
      return None

  return formatted