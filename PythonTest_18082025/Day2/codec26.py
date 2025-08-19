"""Простой шифр: каждые две цифры кодируют символ.

Пример:
>>> decode("070411111426152419071413")
'hello python'
>>> encode("hello python")
'070411111426152419071413'
"""

# алфавит и пробел
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
SPACE = " "

# разрешённые символы для текста и числа
ALLOW_TXT = set(ALPHABET + SPACE)
DIGITS = set("0123456789")

def decode(num: str) -> str:
    """Превращаем цифры в текст.

    >>> decode("00")
    'a'
    """
    # проверяем, что в строке только цифры
    bad = set(num) - DIGITS
    if bad:
        raise ValueError(f"недопустимые символы: {''.join(sorted(bad))!r}")
    # длина должна быть чётной
    if len(num) % 2 == 1:
        raise ValueError("нечётное число цифр")

    result = []
    # читаем по две цифры
    for i in range(0, len(num), 2):
        pair = num[i:i + 2]
        if not pair:
            continue
        code = int(pair)
        # 26 — это пробел
        if code == 26:
            result.append(SPACE)
        elif 0 <= code <= 25:
            result.append(ALPHABET[code])
        else:
            raise ValueError(f"неизвестный код: {pair}")
    return "".join(result)

def encode(text: str) -> str:
    """Превращаем текст в цифры.

    >>> encode("a")
    '00'
    """
    text = text.lower()
    # проверяем разрешённые символы через множество
    bad = set(text) - ALLOW_TXT
    if bad:
        raise ValueError(f"недопустимые символы: {''.join(sorted(bad))!r}")

    result = []
    for ch in text:
        if ch == SPACE:
            result.append("26")
        else:
            # позиция буквы в алфавите даёт её код
            idx = ALPHABET.index(ch)
            result.append(f"{idx:02d}")
    return "".join(result)

def main() -> None:
    """Простейший CLI для выбора режима шифрования или расшифровки."""
    print("Mode (encode/decode):")
    mode = input().strip().lower()
    print("Data:")
    data = input()
    try:
        if mode == "encode":
            print(encode(data))
        elif mode == "decode":
            print(decode(data))
        else:
            print("Unknown mode")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
