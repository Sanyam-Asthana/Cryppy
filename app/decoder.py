import base64
import urllib.parse
import codecs

def decode_binary(enc_str: str) -> str:
    components = enc_str.split()
    result = ""
    for component in components:
        dec = int(component, 2)
        result += chr(dec)

    return result

def decode_octal(enc_str: str) -> str:
    components = enc_str.split()
    result = ""
    for component in components:
        dec = int(component, 8)
        result += chr(dec)

    return result

def decode_decimal(enc_str: str) -> str:
    components = enc_str.split()
    result = ""
    for component in components:
        dec = int(component)
        result += chr(dec)

    return result

def decode_hexadecimal(enc_str: str) -> str:
    try:
        temp = enc_str.replace(" ", "").replace("0x", "")
        result = bytes.fromhex(temp).decode('utf-8')
        return result
    except:
        return ""

def decode_base32(enc_str: str) -> str:
    try:
        result = base64.b32decode(enc_str).decode('utf-8')
        return result
    except:
        return ""

def decode_base64(enc_str: str) -> str:
    try:
        result = base64.b64decode(enc_str).decode('utf-8')
        return result
    except:
        return ""

def decode_base64_url(enc_str: str) -> str:
    try:
        result = base64.urlsafe_b64decode(enc_str).decode('utf-8')
        return result
    except:
        return ""

def decode_base85(enc_str: str) -> str:
    try:
        result = base64.b85decode(enc_str).decode('utf-8')
        return result
    except:
        pass

    try:
        result = base64.a85decode(enc_str).decode('utf-8')
        return result
    except:
        pass

    return ""

def decode_url_encoded(enc_str: str) -> str:
    result = urllib.parse.unquote(enc_str)
    return result

def decode_unicode(enc_str: str) -> str:
    result = enc_str.encode().decode('unicode_escape')
    return result

def decode_encodings(enc_str: str, names: list[str]):
    decodings = {}

    for name in names:

        match name:
            case "binary":
                result = decode_binary(enc_str)
                decodings.update({name : result})

            case "octal":
                result = decode_octal(enc_str)
                decodings.update({name : result})

            case "decimal":
                result = decode_decimal(enc_str)
                decodings.update({name : result})

            case "hexadecimal":
                result = decode_hexadecimal(enc_str)
                decodings.update({name : result})

            case "base32":
                result = decode_base32(enc_str)
                decodings.update({name : result})

            case "base64":
                result = decode_base64(enc_str)
                decodings.update({name : result})

            case "base64_url":
                result = decode_base64_url(enc_str)
                decodings.update({name : result})

            case "base85":
                result = decode_base85(enc_str)
                decodings.update({name : result})

            case "url_encoded":
                result = decode_url_encoded(enc_str)
                decodings.update({name : result})

            case "unicode":
                result = decode_unicode(enc_str)
                decodings.update({name : result})

    return decodings

