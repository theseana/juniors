class Game:
    year = None
    company = None
    name = None
    mode = None

    def call(self):
        # The Last of Us released in 2015
        print(f'{self.name} released in {self.year}')


lou = Game()
lou.name = 'The Last of Us'
lou.company = 'Naughti Dog'
lou.year = 2015
lou.mode = 'Third Person'
print(lou.name)

lou.call()