class Calculadora:
    def __init__(self, valor=0):
        self.valor = valor

    def soma(self, *args):
        self.verifica_argumentos(*args)
        valor = 0
        for i in args:
            valor += i
        return valor
    
    def divisao(self, *args):
        self.verifica_argumentos(*args)
        try: 
            resultado = args[0] / args[1]
            return resultado
        except ZeroDivisionError:
            print('Impossível realizar divisao por zero. ')
            return None
        
    def multiplicao(self, *args):
        self.verifica_argumentos(*args)
        valor = 1
        
        for i in args:
            valor *= i
        return valor
    
    def sub(self, *args):
        self.verifica_argumentos(*args)
        valor = args[0]

        for i in range(1, len(args)):
            valor -= args[i]
        
        return valor

    def verifica_argumentos(self, *args):
        try:
            for i in args:
                if not isinstance(i, (int, float)):
                    raise TypeError(f'Todos os argumentos devem ser numeros. Recebido: {(i)} {type(i).__name__}')
        except TypeError as e:
            print(f'Error: {e}')
            raise

calc = Calculadora()

print(calc.sub(10, 5))

print(calc.soma(3))

print(calc.divisao(4, 2))