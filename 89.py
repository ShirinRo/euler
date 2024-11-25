NUMERALS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

def minimize_numeral(numeral_str):
    value = get_numeral_value(numeral_str)
    minimized_string = ''
    for numeral_str, numeral_value in NUMERALS.items():
        minimized_string, value = greedy_add(minimized_string, value, numeral_value, numeral_str)
    return minimized_string


def greedy_add(minimized_string, value, numeral, numeral_letter):
    number_to_add = value // numeral
    minimized_string += numeral_letter * number_to_add
    value -= number_to_add * numeral
    return [minimized_string, value]

def add_if_possible(minimized_string, value, numeral, numeral_letter):
    if value >= numeral:
        minimized_string += numeral_letter
        value -= numeral
    return [minimized_string, value]

def get_numeral_value(numeral_str):
    value = 0
    i = 0
    while i < len(numeral_str):
        current_letter = numeral_str[i]
        if i == len(numeral_str) - 1:
            value += NUMERALS[current_letter]
            return value
        next_letter = numeral_str[i+1]
        if NUMERALS[next_letter] > NUMERALS[current_letter]:
            value += NUMERALS[current_letter + next_letter]
            i += 1
        else:
            value += NUMERALS[current_letter]
        i += 1
    return value


myinput = open('89_roman.txt', 'r')
lines = myinput.readlines()

original_characters_count = 0
minimal_characters_count = 0
for line in lines:
    line = line.strip()
    original_characters_count += len(line)
    minimized = minimize_numeral(line)
    # if len(minimized) == len(line):
    #     print(f"same length: {line} -> {minimized} (value: {get_numeral_value(line)})")
    if len(minimized) > len(line):
        print(f"bigger length: {line} -> {minimized} (value: {get_numeral_value(line)})")
    minimal_characters_count += len(minimized)


print(original_characters_count)
print(minimal_characters_count)
print(original_characters_count - minimal_characters_count)


def decode_vigenere_hebrew(ciphertext, key):
    # Hebrew alphabet (standard order)
    hebrew_alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'

    def char_to_num(char):
        return hebrew_alphabet.find(char)

    def num_to_char(num):
        return hebrew_alphabet[num % len(hebrew_alphabet)]

    # Remove non-Hebrew characters from input
    cleaned_ciphertext = ''.join(c for c in ciphertext if c in hebrew_alphabet)

    # Extend key to match ciphertext length
    full_key = (key * (len(cleaned_ciphertext) // len(key) + 1))[:len(cleaned_ciphertext)]

    # Decrypt
    plaintext = ''
    for i in range(len(cleaned_ciphertext)):
        if cleaned_ciphertext[i] in hebrew_alphabet:
            pi = char_to_num(cleaned_ciphertext[i])
            ki = char_to_num(full_key[i])
            # Perform shift decryption
            di = (pi - ki) % len(hebrew_alphabet)
            plaintext += num_to_char(di)
        else:
            plaintext += cleaned_ciphertext[i]

    return plaintext


# Decrypt the message
ciphertext = "חוהט כגהכחכק יקגחלעסם צפ כשזג, חסיס הפזדע כצסהס, אכפקזם רשחגקעסם יאעשזם צחמפ זיסם, קעהסוסם לויקלה ששחכאה עט. כדח דם שצגכם צילו טו נקגה הפ יצה, ושפ נקגה הפ צכג."
key = "זורו"

decrypted = decode_vigenere_hebrew(ciphertext, key)
print(f"Decrypted message: {decrypted}")