import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    eng_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
    eng_abc = 'abcdefghigklmnopqrstuvwxyzabc'

    rus_A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ'
    rus_a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабв'

    a1 = eng_ABC.find(plaintext[0])
    a2 = eng_abc.find(plaintext[0])
    a3 = rus_A.find(plaintext[0])
    a4 = rus_a.find(plaintext[0])
    a = [a1, a2, a3, a4]

    if (a[0] != -1) or (a[1] != -1):
        for i in range(len(plaintext)):
            if plaintext[i].isupper():
                ciphertext += eng_ABC[i + 3]
            else:
                ciphertext += eng_abc[i + 3]
            if plaintext[i].isdigit():
                ciphertext += plaintext[i]

    else:
        for i in range(len(plaintext)):
            if plaintext[i].isupper():
                ciphertext += rus_A[i + 3]
            else:
                ciphertext += rus_a[i + 3]
            if plaintext[i].isdigit():
                ciphertext += plaintext[i]
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    eng_ABC = 'XYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_abc = 'xyzabcdefghigklmnopqrstuvwxyz'

    rus_A = 'ЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬ'
    rus_a = 'эюяабвгдеёжзийклмнопрстуфхцчшщъыь'

    a1 = eng_ABC.find(plaintext[0])
    a2 = eng_abc.find(plaintext[0])
    a3 = rus_A.find(plaintext[0])
    a4 = rus_a.find(plaintext[0])
    a = [a1, a2, a3, a4]

    if (a[0] != -1) or (a[1] != -1):
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                plaintext += eng_ABC[i + 3]
            else:
                plaintext += eng_abc[i + 3]
            if ciphertext[i].isdigit():
                plaintext += ciphertext[i]

    else:
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                plaintext += rus_A[i + 3]
            else:
                plaintext += rus_a[i + 3]
            if ciphertext[i].isdigit():
                plaintext += ciphertext[i]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
