class Animal:
    # Atributos de classe
    planeta = "Terra"

    # Métodos
    def nascer(self):
        print(f"Nascido no planeta {self.planeta}")

    def comer(self):
        print("Comendo.. crunch crunch")


class Predador(Animal):
    def comer(self):
        print("Precisa caçar para comer.")

    def shape(self):
        print("Se é predador, o shape ta em dia")


class Presa(Animal):
    def perigo(self):
        print("Cuidado com o predador")


# Para evitar usar heranças multiplas e fazer com que os animais hibridos
# sejam ao mesmo tempo Predador e presa altera o __init__() da classe
class Hibridos(Animal):
    def __init__(self):
        self.Predador = Predador()
        self.Presa = Presa()

    def comer(self):
        print("Animais híbridos podem ou não caçar para comer.")

    def fofura(self):
        print("Hibridos são fofos")


"""
No caso de desenvolvimento web, substituiria as classes por produtos
se caso se tratasse de uma e-commerce, produtos que podem ter classes
digitais ou físicas, ser gamer ou periféricos


Não é uma boa pratica do python ter múltiplas heranças dentro de uma classe
por que pode abrir brechas para bugs no código e dificultar o processo de
debug do mesmo.


__init__() é uma função que tem em toda classe
"""
