from vars.init_val_72 import init_value


def shift_elements(request_list, val, len_list = 72):
    req_list = request_list[0]
    for i in range(1, len_list):
        req_list[i - 1] = req_list[i]
    req_list[len_list - 1] = val
    request_list[0] = req_list


class Meteo:
    def __init__(self):
        self.marousi = init_value
        self.aristotelous = init_value
        self.neasmirni = init_value
        self.agiaparaskevi = init_value
        self.pireus = init_value
        self.peristeri = init_value
        self.thrakomakedones = init_value
        self.elefsina = init_value
        self.lykovrisi = init_value
        self.athens = init_value
        self.geoponiki = init_value
        self.koropi = init_value
        self.liosia = init_value
        self.patision = init_value

    def get_values(self, station_id):
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

    def update_meteo_value(self, station_id, val):
        shift_elements(self.get_values(station_id), val)
        return self.get_values(station_id)