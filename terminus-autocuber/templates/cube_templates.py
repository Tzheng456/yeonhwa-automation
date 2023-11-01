import cv2
from assets.asset import *


def loadPotentialTemplates():
    print(f"Loading stat line templates...")
    # STR
    base_str_9 = cv2.imread(NINE_STR_LINE)
    base_str_12 = cv2.imread(TWELVE_STR_LINE)

    # DEX
    base_dex_9 = cv2.imread(NINE_DEX_LINE)
    base_dex_12 = cv2.imread(TWELVE_DEX_LINE)

    # INT
    base_int_9 = cv2.imread(NINE_INT_LINE)
    base_int_12 = cv2.imread(TWELVE_INT_LINE)

    # LUK
    base_luk_9 = cv2.imread(NINE_LUK_LINE)
    base_luk_12 = cv2.imread(TWELVE_LUK_LINE)

    # ALL
    base_allstat_9 = cv2.imread(NINE_ALLSTAT_LINE)

    # HP
    base_hp_9 = cv2.imread(NINE_HP_LINE)
    base_hp_12 = cv2.imread(TWELVE_HP_LINE)

    # CRIT DMG
    base_critdmg_8 = cv2.imread(CRIT_DMG_LINE)

    # CD
    base_cd_1 = cv2.imread(ONE_CD_LINE)
    base_cd_2 = cv2.imread(TWO_CD_LINE)

    print(f"Loading weapon lines...")
    base_att_9 = cv2.imread(NINE_ATT_LINE)
    base_att_12 = cv2.imread(TWELVE_ATT_LINE)
    base_matt_9 = cv2.imread(NINE_MATT_LINE)
    base_matt_12 = cv2.imread(TWELVE_MATT_LINE)
    base_dmg_9 = cv2.imread(NINE_DMG_LINE)
    base_dmg_12 = cv2.imread(TWELVE_DMG_LINE)
    base_boss_30 = cv2.imread(BOSS_DMG_LINE)
    base_ied_30 = cv2.imread(IED_LINE)

    print(f"Loading meso & drop lines...")
    base_meso_20 = cv2.imread(MESO_LINE)
    base_drop_20 = cv2.imread(DROP_LINE)

    print(f"done loading templates!")
    base_templates = {
        'base_str_9': base_str_9,
        'base_str_12': base_str_12,
        'base_dex_9': base_dex_9,
        'base_dex_12': base_dex_12,
        'base_int_9': base_int_9,
        'base_int_12': base_int_12,
        'base_luk_9': base_luk_9,
        'base_luk_12': base_luk_12,
        'base_allstat_9': base_allstat_9,
        'base_hp_9': base_hp_9,
        'base_hp_12': base_hp_12,
        'base_critdmg_8': base_critdmg_8,
        'base_att_9': base_att_9,
        'base_att_12': base_att_12,
        'base_matt_9': base_matt_9,
        'base_matt_12': base_matt_12,
        'base_dmg_9': base_dmg_9,
        'base_dmg_12': base_dmg_12,
        'base_boss_30': base_boss_30,
        'base_ied_30': base_ied_30,
        'base_meso_20': base_meso_20,
        'base_drop_20': base_drop_20,
        'base_cd_1': base_cd_1,
        'base_cd_2': base_cd_2
    }

    return base_templates
