import json

class Kaffemaskine():
    def __init__(self) -> None:
        def __init__(self, id):
        # Maskinen får maskine Id
        # Maskinen henter oplysninger fra fil
        file = open('../maskiner.json')
        data = json.load(file)
        if str(id) in data:
            # Vores id blev fundet i filen
            # Tilføjer værdier fra filen
            self.navn = data[str(id)]["navn"]
            self.kaffe = data[str(id)]["kaffe"]
            self.maelk = data[str(id)]["maelk"]
            self.vand = data[str(id)]["vand"]
        else:
            return False

    def tilkaldService(self):
        pass

    def brygKaffe(self):
        pass

    def hævPenge(self):
        pass