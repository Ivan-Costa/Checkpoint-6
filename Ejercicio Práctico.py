# Cree una clase de Python llamada Usuario que use el método init y cree un nombre 
# de usuario y una contraseña. Crea un objeto usando la clase.
class Usuario:
    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    def __str__(self):
        return f'Username: {self.user}, Password: {self.password}'


usuario_uno = Usuario('navyblue', 'contraseña')
print(str(usuario_uno))