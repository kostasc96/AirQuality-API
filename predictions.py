class Prediction:
    def __init__(self):
        self.marousi = []
        self.aristotelous = []
        self.neasmirni = []
        self.agiaparaskevi = []
        self.pireus = []
        self.peristeri = []
        self.thrakomakedones = []
        self.elefsina = []
        self.lykovrisi = []
        self.athens = []
        self.geoponiki = []
        self.koropi = []
        self.liosia = []
        self.patision = []

    def update_station_pred(self, station_id, pred):
        if station_id == 1:
            return self.update_pireus(pred)
        elif station_id == 2:
            return self.update_agiaparaskevi(pred)
        elif station_id == 3:
            return self.update_neasmirni(pred)
        elif station_id == 4:
            return self.update_lykovrisi(pred)
        elif station_id == 5:
            return self.update_thrakomakedones(pred)
        elif station_id == 6:
            return self.update_aristotelous(pred)
        elif station_id == 7:
            return self.update_athens(pred)
        elif station_id == 8:
            return self.update_elefsina(pred)
        elif station_id == 9:
            return self.update_koropi(pred)
        elif station_id == 10:
            return self.update_liosia(pred)
        elif station_id == 11:
            return self.update_marousi(pred)
        elif station_id == 12:
            return self.update_patision(pred)
        elif station_id == 13:
            return self.update_geoponiki(pred)
        else:
            return self.update_peristeri(pred)

    def update_marousi(self, pred):
        self.marousi = pred

    def update_aristotelous(self, pred):
        self.aristotelous = pred

    def update_neasmirni(self, pred):
        self.neasmirni = pred

    def update_agiaparaskevi(self, pred):
        self.agiaparaskevi = pred

    def update_pireus(self, pred):
        self.pireus = pred

    def update_peristeri(self, pred):
        self.peristeri = pred

    def update_thrakomakedones(self, pred):
        self.thrakomakedones = pred

    def update_elefsina(self, pred):
        self.elefsina = pred

    def update_lykovrisi(self, pred):
        self.lykovrisi = pred

    def update_athens(self, pred):
        self.athens = pred

    def update_geoponiki(self, pred):
        self.geoponiki = pred

    def update_koropi(self, pred):
        self.koropi = pred

    def update_liosia(self, pred):
        self.liosia = pred

    def update_patision(self, pred):
        self.patision = pred

    def get_prediction(self, station_id):
        if station_id == 1:
            return self.pireus
        elif station_id == 2:
            return self.agiaparaskevi
        elif station_id == 3:
            return self.neasmirni
        elif station_id == 4:
            return self.lykovrisi
        elif station_id == 5:
            return self.thrakomakedones
        elif station_id == 6:
            return self.aristotelous
        elif station_id == 7:
            return self.athens
        elif station_id == 8:
            return self.elefsina
        elif station_id == 9:
            return self.koropi
        elif station_id == 10:
            return self.liosia
        elif station_id == 11:
            return self.marousi
        elif station_id == 12:
            return self.patision
        elif station_id == 13:
            return self.geoponiki
        else:
            return self.peristeri