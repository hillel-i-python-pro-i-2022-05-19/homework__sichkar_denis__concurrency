import time
from typing import Final, TypeAlias, Iterable
from string import ascii_lowercase, digits

T_ALPHABET: TypeAlias = str
T_WORD: TypeAlias = str
T_INDEX_OF_CHARACTER: TypeAlias = int
T_POSITION: TypeAlias = int

DEFAULT_ALPHABET: Final[T_ALPHABET] = ascii_lowercase + digits


def generate(word_length: int, quantity: int, alphabet: T_ALPHABET) -> Iterable[T_WORD]:
    min_index_of_character_in_alphabet: Final[T_INDEX_OF_CHARACTER] = 0
    max_index_of_character_in_alphabet: Final[T_INDEX_OF_CHARACTER] = len(alphabet) - 1

    word_as_list_of_indexes: list[T_INDEX_OF_CHARACTER] = [min_index_of_character_in_alphabet] * word_length

    current_position: T_POSITION = len(word_as_list_of_indexes) - 1
    previous_position: T_POSITION = current_position
    last_position: Final[T_POSITION] = word_length - 1

    count = 0
    while count < quantity:
        if current_position == previous_position == last_position:
            if word_as_list_of_indexes[current_position] <= max_index_of_character_in_alphabet:
                yield ''.join([alphabet[index] for index in word_as_list_of_indexes])
                word_as_list_of_indexes[current_position] += 1
                count += 1
            else:
                word_as_list_of_indexes[current_position] = min_index_of_character_in_alphabet
                previous_position = current_position
                current_position -= 1
        elif current_position >= 0:
            if word_as_list_of_indexes[current_position] < max_index_of_character_in_alphabet:
                word_as_list_of_indexes[current_position] += 1
                current_position = previous_position
            else:
                word_as_list_of_indexes[current_position] = min_index_of_character_in_alphabet
                current_position -= 1
        else:
            print("!Generator Stopped!")
            break


def main():
    start_time = time.time()
    alphabet = DEFAULT_ALPHABET
    characters_of_alphabet = len(alphabet)
    max_combinations = len(alphabet)**4
    word_length = 4
    with open("results_of_generating.txt", "w") as file:
        for word in generate(word_length=word_length, quantity=max_combinations+1, alphabet=alphabet):
            print(word)
            file.write(word + '\n')
    print(f"\nCharacters of Alphabet: {characters_of_alphabet}")
    print(f"Max different {word_length} characters length combinations of alphabet characters = {max_combinations}")
    print(f"\nTime: {time.time() - start_time}")


if __name__ == '__main__':
    main()
