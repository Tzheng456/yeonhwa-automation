class Flame:
    def __init__(self, flame_str=0, flame_dex=0, flame_int=0, flame_luk=0, flame_allstat=0, flame_att=0, flame_matt=0, flame_bossdmg=0, flame_dmg=0, flame_ied=0):

        self.flame_str = flame_str
        self.flame_dex = flame_dex
        self.flame_int = flame_int
        self.flame_luk = flame_luk
        self.flame_allstat = flame_allstat
        self.flame_att = flame_att
        self.flame_matt = flame_matt
        self.flame_bossdmg = flame_bossdmg
        self.flame_dmg = flame_dmg
        self.flame_ied = flame_ied

    def get_flame_str(self):
        return self.flame_str
    def get_flame_dex(self):
        return self.flame_dex
    def get_flame_int(self):
        return self.flame_int
    def get_flame_luk(self):
        return self.flame_luk
    def get_flame_allstat(self):
        return self.flame_allstat
    def get_flame_att(self):
        return self.flame_att
    def get_flame_matt(self):
        return self.flame_matt
    def get_flame_bossdmg(self):
        return self.flame_bossdmg
    def get_flame_dmg(self):
        return self.flame_dmg
    def get_flame_ied(self):
        return self.flame_ied

    def set_flame_str(self, val):
        self.flame_str = int(val)
    def set_flame_dex(self, val):
        self.flame_dex = int(val)
    def set_flame_int(self, val):
        self.flame_int = int(val)
    def set_flame_luk(self, val):
        self.flame_luk = int(val)
    def set_flame_allstat(self, val):
        self.flame_allstat = int(val)
    def set_flame_att(self, val):
        self.flame_att = int(val)
    def set_flame_matt(self, val):
        self.flame_matt = int(val)
    def set_flame_bossdmg(self, val):
        self.flame_bossdmg = int(val)
    def set_flame_dmg(self, val):
        self.flame_dmg = int(val)
    def set_flame_ied(self, val):
        self.flame_ied = int(val)

    def add_flame_str(self, val):
        self.flame_str += int(val)
    def add_flame_dex(self, val):
        self.flame_dex += int(val)
    def add_flame_int(self, val):
        self.flame_int += int(val)
    def add_flame_luk(self, val):
        self.flame_luk += int(val)
    def add_flame_allstat(self, val):
        self.flame_allstat += int(val)
    def add_flame_att(self, val):
        self.flame_att += int(val)
    def add_flame_matt(self, val):
        self.flame_matt += int(val)
    def add_flame_bossdmg(self, val):
        self.flame_bossdmg += int(val)
    def add_flame_dmg(self, val):
        self.flame_dmg += int(val)
    def add_flame_ied(self, val):
        self.flame_ied += int(val)

    def clear_stats(self):
        setters = [
            self.set_flame_str,
            self.set_flame_dex,
            self.set_flame_int,
            self.set_flame_luk,
            self.set_flame_allstat,
            self.set_flame_att,
            self.set_flame_matt,
            self.set_flame_bossdmg,
            self.set_flame_dmg,
            self.set_flame_ied,
        ]
        for setter in setters:
            setter(0)

    def to_string(self):
        stats = self.__dict__
        result = ""
        for stat in stats:
            if stats[stat] > 0:
                if len(result) > 0:
                    result += f"\n{stat}: {stats[stat]}"
                else:
                    result += f"{stat}: {stats[stat]}"
        return result
    
    def get_stats(self):
        stats = self.__dict__
        result = {}
        for stat in stats:
            if stats[stat] > 0:
                result[stat] = stats[stat]
        return result