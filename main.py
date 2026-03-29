import detector
import decoder

import sys

def main():
    if(len(sys.argv) < 2):
        print("Hi! I am Cryppy!")
        print("Got anything to decode?")
        enc_str = input()

        print("\nJust a sec..")

        predictions = detector.detect_encodings(enc_str)
        decodings = decoder.decode_encodings(enc_str, predictions)

        print(f"I did {len(predictions)} predictions on the encoded string!")

        printable = [v.isprintable() and v != "" for k, v in decodings.items()]
        number_printable = sum(printable)

        print(f"Out of which {number_printable} are printable\n")

        for k, v in decodings.items():
            if v.isprintable() and v != "":
                print(f"{k} -> {v}")
        

if __name__ == "__main__":
    main()
