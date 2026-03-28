import detector
import decoder

enc_str = "65 66 67"
predictions = detector.detect_encodings(enc_str)
print(decoder.decode_encodings(enc_str, predictions))
