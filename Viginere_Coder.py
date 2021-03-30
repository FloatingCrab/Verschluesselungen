def viginere_coder(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    keyword_message = ""

    # Füllt die Nachricht mit dem Schlüsselwort.
    while len(keyword_message) < len(message):
        keyword_message += keyword.lower()
        keyword_message = keyword_message[:len(message)]
    # Erstellt eine Liste aus den Indexen der Buchstaben des Schlüsselwortes.
    keyword_message_indexes = []
    for letter in keyword_message:
        for index in range(0, len(alphabet), 1):
            if letter == alphabet[index]:
                keyword_message_indexes.append(index)
    # Verschiebt die Buchstaben der Nachricht um die Indexe der Buchstaben des Schlüsselwortes.
    for message_index in range(0, len(message), 1):
        if message[message_index].lower() not in alphabet:
            output += message[message_index]
        else:
            for alphabet_index in range(0, len(alphabet), 1):
                if message[message_index] == alphabet[alphabet_index]:
                    output += alphabet[(alphabet_index + keyword_message_indexes[message_index]) % len(alphabet)]

    return output


beispiel = viginere_coder("Hallo, wie geht es ihnen?", "Schuhe")
print(beispiel)