import cv2
from assets.asset import *
def loadPotentialTemplates():
    print(f"Loading stat lines...")
    # STR
    base_str_6 = bonus_str_6 = cv2.imread(SIX_STR_LINE)
    bonus_str_8 = cv2.imread(EIGHT_STR_LINE)
    base_str_9 = cv2.imread(NINE_STR_LINE)
    base_str_12 = cv2.imread(TWELVE_STR_LINE)
    bonus_strperlevel_1 = cv2.imread(ONE_STR_PER_LEVEL_LINE)
    bonus_strperlevel_2 = cv2.imread(TWO_STR_PER_LEVEL_LINE)

    # DEX
    base_dex_6 = bonus_dex_6 = cv2.imread(SIX_DEX_LINE)
    bonus_dex_8 = cv2.imread(EIGHT_DEX_LINE)
    base_dex_9 = cv2.imread(NINE_DEX_LINE)
    base_dex_12 = cv2.imread(TWELVE_DEX_LINE)
    bonus_dexperlevel_1 = cv2.imread(ONE_DEX_PER_LEVEL_LINE)
    bonus_dexperlevel_2 = cv2.imread(TWO_DEX_PER_LEVEL_LINE)

    # INT
    base_int_6 = bonus_int_6 = cv2.imread(SIX_INT_LINE)
    bonus_int_8 = cv2.imread(EIGHT_INT_LINE)
    base_int_9 = cv2.imread(NINE_INT_LINE)
    base_int_12 = cv2.imread(TWELVE_INT_LINE)
    bonus_intperlevel_1 = cv2.imread(ONE_INT_PER_LEVEL_LINE)
    bonus_intperlevel_2 = cv2.imread(TWO_INT_PER_LEVEL_LINE)

    # LUK
    base_luk_6 = bonus_luk_6 = cv2.imread(SIX_LUK_LINE)
    bonus_luk_8 = cv2.imread(EIGHT_LUK_LINE)
    base_luk_9 = cv2.imread(NINE_LUK_LINE)
    base_luk_12 = cv2.imread(TWELVE_LUK_LINE)
    bonus_lukperlevel_1 = cv2.imread(ONE_LUK_PER_LEVEL_LINE)
    bonus_lukperlevel_2 = cv2.imread(TWO_LUK_PER_LEVEL_LINE)

    # ALL
    bonus_allstat_5 = cv2.imread(FIVE_ALLSTAT_LINE)
    base_allstat_6 = bonus_allstat_6 = cv2.imread(SIX_ALLSTAT_LINE)
    base_allstat_9 = bonus_allstat_9 = cv2.imread(NINE_ALLSTAT_LINE)

    # HP
    bonus_hp_8 = cv2.imread(EIGHT_HP_LINE)
    base_hp_9 = cv2.imread(NINE_HP_LINE)
    bonus_hp_11 = cv2.imread(ELEVEN_HP_LINE)
    base_hp_12 = cv2.imread(TWELVE_HP_LINE)

    # CRIT DMG
    base_critdmg_8 = cv2.imread(CRIT_DMG_LINE)

    # CD
    base_cd_1 = bonus_cd_1 = cv2.imread(ONE_CD_LINE)
    base_cd_2 = bonus_cd_2 = cv2.imread(TWO_CD_LINE)

    print(f"Loading weapon lines...")
    base_att_9 = bonus_att_9 = cv2.imread(NINE_ATT_LINE)
    base_att_12 = bonus_att_12 = cv2.imread(TWELVE_ATT_LINE)
    base_matt_9 = bonus_matt_9 = cv2.imread(NINE_MATT_LINE)
    base_matt_12 = bonus_matt_12 = cv2.imread(TWELVE_MATT_LINE)
    base_dmg_9 = bonus_dmg_9 = cv2.imread(NINE_DMG_LINE)
    base_dmg_12 = bonus_dmg_12 = cv2.imread(TWELVE_DMG_LINE)
    base_boss_30 = cv2.imread(BOSS_DMG_LINE)
    base_ied_30 = cv2.imread(IED_LINE)

    print(f"Loading meso & drop lines...")
    base_meso_20 = cv2.imread(MESO_LINE)
    base_drop_20 = cv2.imread(DROP_LINE)

    print(f"done loading base & bonus templates!")
    base_templates = {
        'base_str_6': base_str_6,
        'base_str_9': base_str_9,
        'base_str_12': base_str_12,
        'base_dex_6': base_dex_6,
        'base_dex_9': base_dex_9,
        'base_dex_12': base_dex_12,
        'base_int_6': base_int_6,
        'base_int_9': base_int_9,
        'base_int_12': base_int_12,
        'base_luk_6': base_luk_6,
        'base_luk_9': base_luk_9,
        'base_luk_12': base_luk_12,
        'base_allstat_6': base_allstat_6,
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
    bonus_templates = {
        'bonus_str_6': bonus_str_6,
        'bonus_str_8': bonus_str_8,
        'bonus_strperlevel_1': bonus_strperlevel_1,
        'bonus_strperlevel_2': bonus_strperlevel_2,
        'bonus_dex_6': bonus_dex_6,
        'bonus_dex_8': bonus_dex_8,
        'bonus_dexperlevel_1': bonus_dexperlevel_1,
        'bonus_dexperlevel_2': bonus_dexperlevel_2,
        'bonus_int_6': bonus_int_6,
        'bonus_int_8': bonus_int_8,
        'bonus_intperlevel_1': bonus_intperlevel_1,
        'bonus_intperlevel_2': bonus_intperlevel_2,
        'bonus_luk_6': bonus_luk_6,
        'bonus_luk_8': bonus_luk_8,
        'bonus_lukperlevel_1': bonus_lukperlevel_1,
        'bonus_lukperlevel_2': bonus_lukperlevel_2,
        'bonus_allstat_5': bonus_allstat_5,
        'bonus_allstat_6': bonus_allstat_6,
        'bonus_allstat_9': bonus_allstat_9,
        'bonus_hp_8': bonus_hp_8,
        'bonus_hp_11': bonus_hp_11,
        'bonus_att_9': bonus_att_9,
        'bonus_att_12': bonus_att_12,
        'bonus_matt_9': bonus_matt_9,
        'bonus_matt_12': bonus_matt_12,
        'bonus_dmg_9': bonus_dmg_9,
        'bonus_dmg_12': bonus_dmg_12,
        'bonus_cd_1': bonus_cd_1,
        'bonus_cd_2': bonus_cd_2
    }
    return [base_templates, bonus_templates]