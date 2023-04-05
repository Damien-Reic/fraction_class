class Fraction:
    def __init__(self,num : int or float,denom : int or float = 1) -> 'Fraction':
        if denom < 0:
            num,denom = -num,-denom         # s'assure que le négatif est toujours sur au numérateur 
        is_int = lambda x: int(x) == x
        if isinstance(num, float):          # fait en sorte de prendre en charge les floats
            multiplicateur = 2
            temp = num
            while not is_int(temp):
                temp = num * multiplicateur
            num = int(num * multiplicateur)
            denom = denom * multiplicateur
        if isinstance(denom, float):
            multiplicateur = 2
            temp = denom
            while not is_int(temp):
                temp = denom * multiplicateur
            num = num * multiplicateur
            denom = int(denom * multiplicateur)


        self.plus_grand_diviseur_commun = Fraction.get_pgdc(num,denom)          # permet de simplifier la fraction
        self.__num = num // self.plus_grand_diviseur_commun
        self.__denom = denom // self.plus_grand_diviseur_commun



    def __repr__(self) -> str:
        return f"Fraction({self.__num},{self.__denom})"

    def __str__(self) -> str:
        return f"({self.__num}/{self.__denom})"
    
    def __eq__(self, other : 'Fraction', int) -> bool:
        if isinstance(other, Fraction):
            return self.__num == other.__num and self.__denom == other.__denom
        elif isinstance(other, int):
            return self.__num == other and self.__denom == 1
        else:
            return NotImplemented
    
    def __lt__(self, other: 'Fraction', int) -> bool:
        if isinstance(other, Fraction):
            return self.__num * other.__denom < other.__num * self.__denom
        elif isinstance(other, int):
            return self.__num < other * self.__denom
        else:
            return NotImplemented
    
    def __gt__(self, other: 'Fraction', int) -> bool:
        if isinstance(other, Fraction):
            return self.__num * other.__denom > other.__num * self.__denom
        elif isinstance(other, int):
            return self.__num > other * self.__denom
        else:
            return NotImplemented
    
    def __int__(self) -> int:
        return self.__num // self.__denom
    
    def __float__(self) -> float:
        return self.__num / self.__denom

    def __abs__(self) -> 'Fraction':
        return Fraction(abs(self.__num), abs(self.__denom))

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__denom)
    
    def __add__(self,autre) -> 'Fraction': 
        if isinstance(autre,Fraction):
            return Fraction((self.__num*autre.__denom)+(autre.__num * self.__denom),self.__denom*autre.__denom)
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__add__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")


    def __sub__(self, autre) -> 'Fraction': 
        if isinstance(autre, Fraction):
            return Fraction((self.__num * autre.__denom) - (autre.__num * self.__denom), self.__denom * autre.__denom)
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__sub__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")

    def __mul__(self, autre) -> 'Fraction': 
        if isinstance(autre, Fraction):
            return Fraction(self.__num * autre.__num, self.__denom * autre.__denom)
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__mul__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")

    def __truediv__(self, autre) -> 'Fraction': 
        if isinstance(autre, Fraction):
            return self.__mul__(Fraction(autre.__denom, autre.__num))
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__truediv__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")
        
    def __pow__(self, autre : int) -> 'Fraction':
        if isinstance(autre, int):
            if autre < 0:
                return Fraction(self.__denom ** abs(autre), self.__num ** abs(autre))
            else:
                return Fraction(self.__num ** autre, self.__denom ** autre)
        else:
            raise TypeError(f"La puissance doit être un entier, pas un {type(autre)}")
            
    @staticmethod
    def get_pgdc(num : int, denom : int) -> int:
        if num == 0 or denom == 0:
            return num
        if num<0 or denom<0:
            return Fraction.get_pgdc(abs(num),abs(denom))
        if denom != 0:
            return Fraction.get_pgdc(denom,num % denom)
        
    def to_decimal(self) -> float:
        return self.__num / self.__denom

    def to_string(self) -> str:
        if self.__denom == 1:
            return str(self.__num)
        else:
            return f"{self.__num}/{self.__denom}"

    def invert(self) -> 'Fraction':
        return Fraction(self.__denom,self.__num)
    
    def simplify(self) -> 'Fraction':
        return Fraction(self.__num,self.__denom)
    
    def get_num(self) -> int:
        return self.__num
    
    def get_denom(self) -> int:
        return self.__denom

