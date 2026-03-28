import base64
import urllib

def decode_encodings(enc_str: str, names: list[str]):
    decodings = {}

    components = enc_str.split() 

    for name in names:

        match name:
            case "binary":
                result = ""
                for component in components:
                    dec = int(component, 2)
                    result += chr(dec)
                decodings.update({name : result})

            case "octal":
                result = ""
                for component in components:
                    dec = int(component, 8)
                    result += chr(dec)
                decodings.update({name : result})

            case "decimal":
                result = ""
                for component in components:
                    dec = int(component)
                    result += chr(dec)
                decodings.update({name : result})

    return decodings

