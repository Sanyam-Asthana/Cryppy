import re

encoding_patterns = {
    "binary" : r"^[01\s]+$", # all 1s and 0s, with optional spacing
    "octal" : r"^[0-7\s]+$", # 0-7
    "decimal" : r"^[\d\s]+$", # digits
    "hexadecimal" : r"^(0x)?[0-9a-fA-F\s]+$", # optional 0x prefix, 0-9, A-F (case-insensitive)
    "base32" : r"^[A-Z2-7]+=*$", # A-Z, 2-7 digits and '=' padding
    "base58" : r"^[1-9A-HJ-NP-Za-km-z]+$", # base 64 without 0, O, I, l
    "base62" : r"^[A-Za-z0-9]+$", # alphanumeric with no symbols/padding
    "base64" : r"^[A-Za-z0-9+/]+=*$", # alphanumeric with +, / and padding
    "base64_url" : r"^[A-Za-z0-9\-_]+=*$", # - and _ instead of + and /
    "base85" : r"^[!-u]+$", # characters from ! to u
    "url_encoded" : r"(%[0-9a-fA-F]{2})+", # % followed by two hex digits
    "unicode" : r"(\\u[0-9a-fA-F]{4})+", # \u followed by 4 hex digits
    "punycode" : r"^xn--[a-z0-9\-]+$" # starts with xn--, not implemented yet
}

cipher_patterns = {
    "rot_13": r"[a-zA-Z]"
}

def detect_encodings(enc_str: str) -> list[str]:
    """
    detects the encoding by brute forcing and matching against a dictionary of encoding patterns
    """
    predictions: list[str] = []

    for name, pattern in encoding_patterns.items():
        if(re.match(pattern, enc_str)):
            predictions.append(name)

    return predictions

def detect_cipher(enc_str: str) -> list[str]:
    """
    detects the cipher by matching against a dictionary of cipher patterns
    """
    predictions: list[str] = []

    for name, pattern in cipher_patterns.items():
        if(re.match(pattern, enc_str)):
            predictions.append(name)
    
    return predictions

