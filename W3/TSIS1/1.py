class Notmy:
    def __init__(self):
        self.test1 = ""
        """
        __init__: Этот метод является конструктором класса. 
        Он инициализирует атрибут test1 объекта класса Notmy пустой строкой.
        """
    def getString(self):
        self.test1 = input()
        """
        getString: Этот метод запрашивает у пользователя 
        ввод строки и сохраняет её в атрибуте test1 объекта класса Notmy.
        """
    def printString(self):
        print(self.test1.upper())
        """
        printString: Этот метод выводит на экран строку, 
        сохранённую в атрибуте test1 объекта класса Notmy, 
        преобразованную к верхнему регистру.
        """

test = Notmy()
test.getString()
test.printString()
"""
После определения класса Notmy, 
создаётся объект test этого класса. 
Затем вызывается метод getString, 
который запрашивает ввод строки пользователя 
и сохраняет её в атрибуте test объекта test1. 
После этого вызывается метод printString, 
который выводит на экран содержимое атрибута test, 
преобразованное к верхнему регистру.
"""