import codecs

def decipher_rot13(enc_str: str) -> str:
    return codecs.decode(enc_str, "rot_13")

def decipher(enc_str: str, names: list[str]):
    deciphers = {}

    for name in names:
        match name:
            case "rot_13":
                result = decipher_rot13(enc_str)
                deciphers.update({name: result})
        
        return deciphers
