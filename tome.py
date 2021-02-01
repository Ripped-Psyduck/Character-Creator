#########
# RACES #
#########
EEPC = ['Genasi (Air) (EEPC)', 'Genasi (Earth) (EEPC)',
        'Genasi (Fire) (EEPC)', 'Genasi (Water) (EEPC)']
LR = ['Locathah (LR)']
MTF = ['Dwarf (Duergar) (MTF)', 'Elf (Eladrin) (MTF)', 'Elf (Sea) (MTF)', 'Elf (Shadar-kai) (MTF)', 'Gith (Githyanki) (MTF)', 'Gith (Githzerai) (MTF)', 'Gnome (Deep) (MTF)', 'Tiefling (Asmodeus) (MTF)', 'Tiefling (Baalzebul) (MTF)',
       'Tiefling (Dispater) (MTF)', 'Tiefling (Fierna) (MTF)', 'Tiefling (Glasya) (MTF)', 'Tiefling (Levistus) (MTF)', 'Tiefling (Mammon) (MTF)', 'Tiefling (Mephistopheles) (MTF)', 'Tiefling (Zariel) (MTF)']
PHB = ['Aasimar (Fallen) (VGM but is PHB for Historic)', 'Aasimar (Protector) (VGM but is PHB for Historic)', 'Aasimar (Scourge) (VGM but is PHB for Historic)', 'Dragonborn (Black)', 'Dragonborn (Blue)', 'Dragonborn (Brass)', 'Dragonborn (Copper)', 'Dragonborn (Gold)', 'Dragonborn (Green)',
       'Dragonborn (Red)', 'Dragonborn (Silver)', 'Dragonborn (White)', 'Dwarf (Hill)', 'Dwarf (Mountain)', 'Elf (Drow)', 'Elf (High)', 'Elf (Wood)', 'Gnome (Forest)', 'Gnome (Rock)', 'Half-Elf', 'Half-Orc', 'Halfling (Lightfoot)', 'Halfling (Stout)', 'Human (Standard)', 'Human (Variant)', 'Tiefling']
SCAG = ['Gnome (Deep/Svirfneblin) (SCAG)', 'Half-Elf (Aquatic Elf Descent) (SCAG)', 'Half-Elf (Drow Descent) (SCAG)', 'Half-Elf (Moon Elf or Sun Elf Descent) (SCAG)',
        'Half-Elf (Wood Elf Descent) (SCAG)', 'Halfling (Ghostwise) (SCAG)', "Tiefling (Devil's Tongue) (SCAG)", 'Tiefling (Hellfire) (SCAG)', 'Tiefling (Infernal Legacy) (SCAG)']
VGM = ['Bugbear (VGM)', 'Firbolg (VGM)', 'Goblin (VGM)', 'Goliath (VGM)', 'Hobgoblin (VGM)', 'Kenku (VGM)',
       'Kobold (VGM)', 'Lizardfolk (VGM)', 'Orc (VGM)', 'Tabaxi (VGM)', 'Triton (VGM)', 'Yuan-Ti Pureblood (VGM)']
XGE = ['Tortle (XGE)']
SPC = ['Aasimar (Fallen)', 'Aasimar (Protector)', 'Aasimar (Scourge)', 'Dwarf (Duergar)', 'Elf (Eladrin)', 'Elf (Shadar-kai)', 'Firbolg', 'Gith (Githyanki)', 'Gith (Githzerai)', 'Gnome (Deep)', 'Goliath', 'Kenku', 'Kobold',
       'Orc', 'Tabaxi', 'Tiefling (Asmodeus)', 'Tiefling (Baalzebul)', 'Tiefling (Dispater)', 'Tiefling (Fierna)', 'Tiefling (Glasya)', 'Tiefling (Levistus)', 'Tiefling (Mammon)', 'Tiefling (Mephistopheles)', 'Tiefling (Zariel)']

# List of all races for Historic Campaign
HIS_RACE = PHB + EEPC + LR + MTF + SCAG + VGM + XGE

# List of all races for Seasonal Campaign
CUR_RACE = PHB + SPC

###########
# CLASSES #
###########

## BARBARIAN ##
BARB_PHB = ['Path of the Berserker Barbarian',
            'Path of the Totem Warrior Barbarian']
BARB_SCAG = ['Path of the Battlerager Barbarian',
             'Path of the Totem Warrior Barbarian']
BARB_TCE = ['Path of the Beast Barbarian',
            'Path of the Wild Magic Barbarian']
BARB_XGE = ['Path of the Ancestral Guardian Barbarian',
            'Path of the Storm Herald Barbarian',
            'Path of the Zealot Barbarian']
HIS_BARB = BARB_PHB + BARB_SCAG + BARB_XGE
CUR_BARB = BARB_PHB + BARB_TCE + BARB_XGE


## BARD ##
BARD_PHB = ['College of Lore Bard',
            'College of Valor Bard']
BARD_SCAG = ['College of Lore Bard',
             'College of Valor Bard']
BARD_TCE = ['College of Creation Bard',
            'College of Eloquence Bard']
BARD_XGE = ['College of Glamour Bard',
            'College of Whispers Bard']
HIS_BARD = BARD_PHB + BARD_SCAG + BARD_XGE
CUR_BARD = BARD_PHB + BARD_TCE + BARD_XGE


# List of all classes for Historic Campaign
HIS_CLASSES = HIS_BARB + HIS_BARD

# List of all classes for Seasonal Campaign
CUR_CLASSES = CUR_BARB + CUR_BARD
