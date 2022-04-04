"""
Составить описание класса одномерных массивов строк, каждая строка задается
длиной и указателем на выделенную для нее память. Предусмотреть возможность обращения к отдельным строкам массива по индексам,
контроль выхода за пределы массивов, выполнения операций сцепления двух
массивов с образованием нового массива, слияния двух массивов с исключением повторяющихся элементов,
вывод на экран элемента массива и всего массива.
Программа должна содержать меню, позволяющее осуществить проверку всех методов класса"""


def check_value_int(var):
    if not isinstance(var, int):
        raise ValueError


class Stringmassiv:
    def __init__(self):
        self.__array = []

    def add_element(self, string: str):
        if not isinstance(string, str):
            raise ValueError
        string_list = list(string.split())
        self.__array.append(string_list)

    def show_element(self, index1: int, index2: int):
        check_value_int(index1)
        check_value_int(index2)
        try:
            print(self.__array[index1][index2])
        except IndexError:
            print("индексы за пределом массива")

    def show_array(self):
        for i in self.__array:
            print(i)

    def combining(self, index1, index2):
        new_mas = []
        try:
            min_len = min(len(self.__array[index1]), len(self.__array[index2]))
        except IndexError:
            print("Индексы за границей массива")
            return

        for i in range(min_len):
            new_mas.append(self.__array[index1][i])
            new_mas.append(self.__array[index2][i])
        if len(self.__array[index1]) > len(self.__array[index2]):
            new_mas + self.__array[index1][index2:]
        else:
            new_mas + self.__array[index2][index1:]
        return new_mas

    def combining_norep(self, index1, index2):
        try:
            return list(set(self.__array[index1] + self.__array[index2]))
        except IndexError:
            print("Индексы за границей массива")


def main():
    new_obj = Stringmassiv()
    while True:
        input_ = input(
            "0: Добавить элемент\n1: Вывод массива\n2: Вывод элемента\n3: Обьединение массивов\n4: Обьединение массивов без повторов\n5: выход\n>>> "
        )
        if input_ == "0":
            new_obj.add_element(input("Новое значение: "))
        elif input_ == "1":
            new_obj.show_array()
        elif input_ == "2":
            input_string = int(input("номер строки: "))
            input_index = int(input("номер индекса: "))
            new_obj.show_element(input_string, input_index)
        elif input_ == "3":
            index1 = int(input("индекс первоой строки: "))
            index2 = int(input("индекс второй строки: "))
            print(new_obj.combining(index1, index2))
        elif input_ == "4":
            index1 = int(input("индекс первой строки: "))
            index2 = int(input("индекс второй строки: "))
            print(new_obj.combining_norep(index1, index2))
        elif input_ == "5":
            break
        else:
            print("Введено неверное значение")


if __name__ == "__main__":
    main()
