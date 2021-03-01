"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"
"""
import re

def main():
    text = "hi world, hi python. i am very cool but i am still learning."
    frequent_word(text)


def frequent_word(text):
    words = re.findall(r"\w+", text)
    words = sorted(words)
    count = None
    data = {}
    for char in words:
        if char not in data:
            data[char] = words.count(char)
            if count is None:
                count = char
            elif len(count) < words.count(char):
                count = char
    print(count)
    return count


if __name__ == "__main__":
    main()

t_1 = "hi hi hi hi hi world, hi python. i am very cool but i am still learning."
assert frequent_word(t_1) == "hi"

t_2 = "world world world world world world, hi python"
assert frequent_word(t_2) == "world"

t_3 = "i i i i am am am am still learning."
assert frequent_word(t_3) == "i"

t_4 = "i am very very cool cool cool "
assert frequent_word(t_4) == "cool"

print("All tests passed successfully!")