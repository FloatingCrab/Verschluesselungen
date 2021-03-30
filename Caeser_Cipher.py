# Die Caesar-Verschlüsselung verschiebt jeden Buchstaben um einen Gewissen Wert. Umlaute nicht einbezogen.
def coder(message, offset):
    output = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Damit Satzzeichen nicht verschoben werden.
    for letter in message.lower():
        if letter not in alphabet:
            output += letter

        for index in range(0, len(alphabet), 1):
            if letter == alphabet[index]:
                output += alphabet[index - offset]
    return output


beispiel = coder("Guten morgen! Schoenes Wetter, nicht wahr?", 10)
print(beispiel)

def decoder(message, offset):
    output = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in message.lower():
        if letter not in alphabet:
            output += letter

        for index in range(0, len(alphabet), 1):
            if letter == alphabet[index]:
                #Die Verschiebung fängt wieder am Anfang vom Alphabet an, wenn der Index die Länge vom Alphabet überschreitet.
                if index + offset >= len(alphabet):
                    offset_past_end = (index + offset) % len(alphabet)
                    output += alphabet[offset_past_end]
                else:
                    output += alphabet[index + offset]
    return output

print(decoder(beispiel, 10))