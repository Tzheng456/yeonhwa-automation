import cv2
from assets.asset import *


def loadFlameTemplates():
    print(f"Loading flame line templates...")

    # STAT
    flame_str = cv2.imread(FLAME_STR_LINE)
    flame_dex = cv2.imread(FLAME_DEX_LINE)
    flame_int = cv2.imread(FLAME_INT_LINE)
    flame_luk = cv2.imread(FLAME_LUK_LINE)
    flame_allstat = cv2.imread(FLAME_ALLSTAT_LINE)

    # WEP
    flame_att = cv2.imread(FLAME_ATT_LINE)
    flame_matt = cv2.imread(FLAME_MATT_LINE)
    flame_bossdmg = cv2.imread(FLAME_BOSSDMG_LINE)
    flame_dmg = cv2.imread(FLAME_DMG_LINE)
    # flame_ied = cv2.imread(FLAME_IED_LINE)

    templates = {
        "flame_str": flame_str,
        "flame_dex": flame_dex,
        "flame_int": flame_int,
        "flame_luk": flame_luk,
        "flame_allstat": flame_allstat,
        "flame_att": flame_att,
        "flame_matt": flame_matt,
        "flame_bossdmg": flame_bossdmg,
        "flame_dmg": flame_dmg,
        # "flame_ied": flame_ied,
    }

    return templates
