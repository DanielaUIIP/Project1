class Persona:
    def __init__(self, nome, cognome,sesso, dataNascita):
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.dataNascita = dataNascita

    def stampadettagli(self):
        print(self.nome)
        print(self.cognome)
        print(self.sesso)
        print(self.dataNascita)
        #IN ALTERNATIVA
        #return self.nome + self.cognome + self.sesso + self.dataNascita

class Studente(Persona):
    def __init__(self, nome, cognome, sesso,dataNascita, matricola):
        super().__init__(nome, cognome, sesso,dataNascita)  # super fa riferimento alla classe Persona
        self.matricola = matricola

    def stampadettagli(self):
        super().stampadettagli() #questo va eliminato
        #return super().stampadettagli() + self.matricola
        print(self.matricola) #questo va eliminato

class Docente(Persona):
    def __init__(self, nome, cognome, sesso, dataNascita, email):
        super().__init__(nome, cognome, sesso, dataNascita)  # super fa riferimento alla classe Persona
        self.email = email

    def stampadettagli(self):
        super().stampadettagli() #va eliminato
        # return super().stampadettagli() + self.email
        print(self.email) #va eliminato

d=Docente('daniela','cammarano','F','5/7/94','dani@gmail.com')
d.stampadettagli()
#print(d.stampadettagli())