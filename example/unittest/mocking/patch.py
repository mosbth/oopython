"""
Om du inte har koll på hur Mock fungera kolla på filen mock.py först.

https://docs.python.org/3/library/unittest.mock.html#the-patchers
Patch kan användas för att mocka ett objekt i ett namespace.
Vi kan specificera ett objekt som används någon annanstans i samma
namespace och ersätta det med ett Mock objekt i ett test.

Vilket vi vill göra för att ersätta input() med ett Mock objekt.
"""
from io import StringIO
from unittest import mock, TestCase, main

def func_with_one_input():
    """
    Example of a function with input()
    """
    inp = input("Enter an input value: ")
    return inp



def func_with_while_input_return():
    """
    Function with a while loops asking for input and returns result.
    """
    inp = ""
    result = []
    while inp != "q":
        inp = input("Enter choice: ")
        result.append(inp)
    return result



def func_with_while_input_print():
    """
    Function with a while loops asking for input and prints result
    """
    inp = ""
    counter = 0
    while inp != "q":
        inp = input("Enter choice: ")
        print(inp, counter)
        counter += 1



class TestPatch(TestCase):
    """
    Test class for showing mock.patch
    """

    def test_func_with_input_string(self):
        """
        Test function with one input call using patch
        """
        inp = ["It's working"]
        # Nu ska vi skapa en context manager och referera till input functionen
        # i patch. input() ligger i modulen builtins.
        # Värdet som vi tilldelar side_effect är vad som kommer returneras
        # när man anropar input(). Om det är en sekvens (list, str...)
        # returneras ett element varje gång input() anropas.
        with mock.patch('builtins.input', side_effect=inp):
            # Nu har input() ersatts med ett Mock objekt för all kod som
            # körs i detta scopet/namespace
            self.assertEqual(func_with_one_input(), inp[0])

    def test_func_with_input_list_value(self):
        """
        Test function with a while loop asking for multiple inputs
        """
        inp = ["It's working", "Again", "And again", 3.4, 5, "q"]
        with mock.patch('builtins.input', side_effect=inp):
            self.assertEqual(func_with_while_input_return(), inp)



    def test_func_with_print(self):
        """
        Test that a function prints correct values
        """
        inp = ["It's working", "Again", "And again", 3.4, 5, "q"]
        # Vi kan också mocka hur print() metoden fungerar.
        # Istället för att det skrivs ut i
        # terminalen läggs utskriften till i vårt mock objekt som vi sen kan
        # läsa av och kolla att det är rätt värden.
        # Vi kör två patch, en för input och en för sys.stdout. print() använder
        # sys.stdout för att göra utskrifter i terminalen. Vi använder "new="
        # för att ersätta sys.stdout med ett nytt StringIO object Istället
        # för ett vanligt mock objekt. Det är en memory stream för
        # input och output text.
        # https://docs.python.org/3/library/io.html#io.StringIO
        with mock.patch('builtins.input', side_effect=inp):
            with mock.patch('sys.stdout', new=StringIO()) as fake_out:
                func_with_while_input_print()
                # använder getvalue() på fake_out för att returnera vad
                # som printades i funktionen. Returnerar en sträng.
                content = fake_out.getvalue().strip().split("\n")
                for i, v in enumerate(inp):
                    p_value = "{} {}".format(v, i)
                    self.assertEqual(content[i], p_value)
            # print(fake_out)
            # print(fake_out.getvalue())





if __name__ == "__main__":
    main(verbosity=3)
