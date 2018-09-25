
from alphabet_check import string_to_set, has_alphabet

input_one = ",;z+@e\87a<*~QMp"
input_two = "Cozy lummox gives smart squid who asks for job pen"
input_three = "The quick brown fox jumps over the lazy dog"
input_four = "The quick%#$$%>>> brown' fox ^jjjjjumps567 over the lazy dog}{||,.,."
input_five = "m)e%$z9tMKeKR?h3MJ.6v4&Gs#KkZA"
input_six = "the sick brown fox jumps over the lazy dog"


def test_string_to_set():
    set_example = string_to_set(input_one)
    for i in [input_one, input_two, input_five]:
        set_example = string_to_set(i)
        assert "A" in set_example
        assert isinstance(set_example, set)


def test_has_alphabet():
    for i in [input_two, input_three, input_four]:
        assert has_alphabet(i) is True


def test_has_not_alphabet():
    for j in [input_one, input_five, input_six]:
        assert has_alphabet(j) is False
