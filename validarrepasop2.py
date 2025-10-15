



class Validar():
    def __init__(self):
        self.index = 0

    def ValidarAscii(self, valor):
        con = 0
        con2 = 0
        for i in valor:
            if ord(i) >= 48 and ord(i)<= 57:
                con += 1
            if (ord(i)>= 65 and ord(i)<=90) or (ord(i)>= 97 and ord(i)<=122):
                con2 += 1

        if con == len(valor):
            return "Numeros"
        elif con2 == len(valor):
            return "Letras"
        else:
            return "Letras y numeros"


    def ValidarConError(self, valor):
        a = 0
        b = 0.0
        try:
            a = int(valor)
            return "numeros"
        except ValueError:
            try:
                b = float(valor)
                return "Es numero real o con decimales"
            except ValueError:
                return "letras o numeros"
            
    def ValidarConString(self, valor):
        print(valor)
        if self.index < len(valor):
            if valor[self.index] == '@':
                self.index = 0
                return "se es un correo"
            else:
                if self.index < len(valor):
                    self.index += 1
                    return self.ValidarConString(valor)
                else:
                    self.index = 0
                    return "no es un correo"
        else:
            self.index = 0
            return "no es un correo"
        
        # if "@" in valor:
        #     return "si es un correo"
        # else:
        #     return "no es in correo"
    
