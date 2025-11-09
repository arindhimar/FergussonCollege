import base64

text="asdjkahsjdaskhd"

encoded = base64.b64encode(text.encode())
decoded = base64.b64decode(encoded)

print("\nBase64 Encoding/Decoding:")
print("Encoded:", encoded)
print("Decoded:", decoded)