import detector
import decoder
import decipher

import sys


def main():
    if len(sys.argv) < 2:
        print("Hi! I am Cryppy!")
        print("Got anything to decode?")
        enc_str = input()

        print("\nJust a sec..")

        encoding_predictions = detector.detect_encodings(enc_str)
        decodings = decoder.decode_encodings(enc_str, encoding_predictions)

        cipher_predictions = detector.detect_cipher(enc_str)
        deciphers = decipher.decipher(enc_str, cipher_predictions)

        print(f"I did {len(encoding_predictions)} predictions for encodings on the string!")

        printable = [v.isprintable() and v != "" for k, v in decodings.items()]
        number_printable = sum(printable)

        print(f"Out of which {number_printable} are printable\n")

        for k, v in decodings.items():
            if v.isprintable() and v != "":
                print(f"{k} -> {v}")

        print()

        print(f"I did {len(cipher_predictions)} predictions for ciphers on the string!")

        printable = [v.isprintable() and v != "" for k, v in deciphers.items()]
        number_printable = sum(printable)

        print(f"Out of which {number_printable} are printable\n")

        for k, v in deciphers.items():
            if v.isprintable() and v != "":
                print(f"{k} -> {v}")


if __name__ == "__main__":
    main()
