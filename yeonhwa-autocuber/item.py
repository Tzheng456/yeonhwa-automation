class Item:
    def __init__(self, base_str=0, base_dex=0, base_int=0, base_luk=0, base_allstat=0, base_hp=0, critdmg=0, ied=0, boss=0, base_dmg=0, base_att=0, base_matt=0, meso=0, drop=0, base_cd=0, bonus_str=0, bonus_dex=0, bonus_int=0, bonus_luk=0, bonus_allstat=0, bonus_hp=0, strperlevel=0, dexperlevel=0, intperlevel=0, lukperlevel=0, bonus_att=0, bonus_matt=0, bonus_dmg=0, bonus_cd=0):
        # base stats
        # STR
        self.base_str = base_str
        # DEX
        self.base_dex = base_dex
        # INT
        self.base_int = base_int
        # LUK
        self.base_luk = base_luk
        # ALLSTAT
        self.base_allstat = base_allstat
        # HP
        self.base_hp = base_hp
        # CRIT DMG
        self.base_critdmg = critdmg
        # IED
        self.base_ied = ied
        # BOSS DMG
        self.base_boss = boss
        # DMG
        self.base_dmg = base_dmg
        # ATT
        self.base_att = base_att
        # MATT
        self.base_matt = base_matt
        # MESO
        self.base_meso = meso
        # DROP
        self.base_drop = drop
        # CD
        self.base_cd = base_cd

        # bonus stats
        # STR
        self.bonus_str = bonus_str
        # DEX
        self.bonus_dex = bonus_dex
        # INT
        self.bonus_int = bonus_int
        # LUK
        self.bonus_luk = bonus_luk
        # ALLSTAT
        self.bonus_allstat = bonus_allstat
        # HP
        self.bonus_hp = bonus_hp
        # STR/LVL
        self.bonus_strperlevel = strperlevel
        # DEX/LVL
        self.bonus_dexperlevel = dexperlevel
        # INT/LVL
        self.bonus_intperlevel = intperlevel
        # LUK/LVL
        self.bonus_lukperlevel = lukperlevel
        # ATT
        self.bonus_att = bonus_att
        # MATT
        self.bonus_matt = bonus_matt
        # DMG
        self.bonus_dmg = bonus_dmg
        # CD
        self.bonus_cd = bonus_cd
    
    def get_basestr(self):
        return self.base_str

    def set_basestr(self, val):
        self.base_str = int(val)

    def add_basestr(self, val):
        self.base_str += int(val)

    def get_basedex(self):
        return self.base_dex

    def set_basedex(self, val):
        self.base_dex = int(val)

    def add_basedex(self, val):
        self.base_dex += int(val)

    def get_baseint(self):
        return self.base_int

    def set_baseint(self, val):
        self.base_int = int(val)

    def add_baseint(self, val):
        self.base_int += int(val)

    def get_baseluk(self):
        return self.base_luk

    def set_baseluk(self, val):
        self.base_luk = int(val)

    def add_baseluk(self, val):
        self.base_luk += int(val)

    def get_baseallstat(self):
        return self.base_allstat

    def set_baseallstat(self, val):
        self.base_allstat = int(val)

    def add_baseallstat(self, val):
        self.base_allstat += int(val)
        self.base_str += int(val)
        self.base_dex += int(val)
        self.base_int += int(val)
        self.base_luk += int(val)

    def get_basehp(self):
        return self.base_hp

    def set_basehp(self, val):
        self.base_hp = int(val)

    def add_basehp(self, val):
        self.base_hp += int(val)

    def get_basecritdmg(self):
        return self.base_critdmg

    def set_basecritdmg(self, val):
        self.base_critdmg = int(val)

    def add_basecritdmg(self, val):
        self.base_critdmg += int(val)

    def get_baseied(self):
        return self.base_ied

    def set_baseied(self, val):
        self.base_ied = int(val)

    def add_baseied(self, val):
        self.base_ied += int(val)

    def get_baseboss(self):
        return self.base_boss

    def set_baseboss(self, val):
        self.base_boss = int(val)

    def add_baseboss(self, val):
        self.base_boss += int(val)

    def get_basedmg(self):
        return self.base_dmg

    def set_basedmg(self, val):
        self.base_dmg = int(val)

    def add_basedmg(self, val):
        self.base_dmg += int(val)

    def get_baseatt(self):
        return self.base_att

    def set_baseatt(self, val):
        self.base_att = int(val)

    def add_baseatt(self, val):
        self.base_att += int(val)

    def get_basematt(self):
        return self.base_matt

    def set_basematt(self, val):
        self.base_matt = int(val)

    def add_basematt(self, val):
        self.base_matt += int(val)

    def get_basemeso(self):
        return self.base_meso

    def set_basemeso(self, val):
        self.base_meso = int(val)

    def add_basemeso(self, val):
        self.base_meso += int(val)

    def get_basedrop(self):
        return self.base_drop

    def set_basedrop(self, val):
        self.base_drop = int(val)

    def add_basedrop(self, val):
        self.base_drop += int(val)

    def get_basecd(self):
        return self.base_cd

    def set_basecd(self, val):
        self.base_cd = int(val)

    def add_basecd(self, val):
        self.base_cd += int(val)

    def get_bonusstr(self):
        return self.bonus_str

    def set_bonusstr(self, val):
        self.bonus_str = int(val)

    def add_bonusstr(self, val):
        self.bonus_str += int(val)

    def get_bonusdex(self):
        return self.bonus_dex

    def set_bonusdex(self, val):
        self.bonus_dex = int(val)

    def add_bonusdex(self, val):
        self.bonus_dex += int(val)

    def get_bonusint(self):
        return self.bonus_int

    def set_bonusint(self, val):
        self.bonus_int = int(val)

    def add_bonusint(self, val):
        self.bonus_int += int(val)

    def get_bonusluk(self):
        return self.bonus_luk

    def set_bonusluk(self, val):
        self.bonus_luk = int(val)

    def add_bonusluk(self, val):
        self.bonus_luk += int(val)

    def get_bonusallstat(self):
        return self.bonus_allstat

    def set_bonusallstat(self, val):
        self.bonus_allstat = int(val)

    def add_bonusallstat(self, val):
        self.bonus_allstat += int(val)
        self.bonus_str += int(val)
        self.bonus_dex += int(val)
        self.bonus_int += int(val)
        self.bonus_luk += int(val)

    def get_bonushp(self):
        return self.bonus_hp

    def set_bonushp(self, val):
        self.bonus_hp = int(val)

    def add_bonushp(self, val):
        self.bonus_hp += int(val)

    def get_bonusstrperlevel(self):
        return self.bonus_strperlevel

    def set_bonusstrperlevel(self, val):
        self.bonus_strperlevel = int(val)

    def add_bonusstrperlevel(self, val):
        self.bonus_strperlevel += int(val)

    def get_bonusdexperlevel(self):
        return self.bonus_dexperlevel

    def set_bonusdexperlevel(self, val):
        self.bonus_dexperlevel = int(val)

    def add_bonusdexperlevel(self, val):
        self.bonus_dexperlevel += int(val)

    def get_bonusintperlevel(self):
        return self.bonus_intperlevel

    def set_bonusintperlevel(self, val):
        self.bonus_intperlevel = int(val)

    def add_bonusintperlevel(self, val):
        self.bonus_intperlevel += int(val)

    def get_bonuslukperlevel(self):
        return self.bonus_lukperlevel

    def set_bonuslukperlevel(self, val):
        self.bonus_lukperlevel = int(val)

    def add_bonuslukperlevel(self, val):
        self.bonus_lukperlevel += int(val)

    def get_bonusatt(self):
        return self.bonus_att

    def set_bonusatt(self, val):
        self.bonus_att = int(val)

    def add_bonusatt(self, val):
        self.bonus_att += int(val)

    def get_bonusmatt(self):
        return self.bonus_matt

    def set_bonusmatt(self, val):
        self.bonus_matt = int(val)

    def add_bonusmatt(self, val):
        self.bonus_matt += int(val)

    def get_bonusdmg(self):
        return self.bonus_dmg

    def set_bonusdmg(self, val):
        self.bonus_dmg = int(val)

    def add_bonusdmg(self, val):
        self.bonus_dmg += int(val)

    def get_bonuscd(self):
        return self.bonus_cd

    def set_bonuscd(self, val):
        self.bonus_cd = int(val)

    def add_bonuscd(self, val):
        self.bonus_cd += int(val)

    def clear_stats(self):
        setters = [self.set_basestr,
            self.set_basedex,
            self.set_baseint,
            self.set_baseluk,
            self.set_baseallstat,
            self.set_basehp,
            self.set_basecritdmg,
            self.set_baseied,
            self.set_baseboss,
            self.set_basedmg,
            self.set_baseatt,
            self.set_basematt,
            self.set_basemeso,
            self.set_basedrop,
            self.set_basecd,
            self.set_bonusstr,
            self.set_bonusdex,
            self.set_bonusint,
            self.set_bonusluk,
            self.set_bonusallstat,
            self.set_bonushp,
            self.set_bonusstrperlevel,
            self.set_bonusdexperlevel,
            self.set_bonusintperlevel,
            self.set_bonuslukperlevel,
            self.set_bonusatt,
            self.set_bonusmatt,
            self.set_bonusdmg,
            self.set_bonuscd]
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