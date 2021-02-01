import discord
import random

import tome

from discord.ext import commands

from Secret import DISCORD_TOKEN
token = DISCORD_TOKEN

prefix = '~'
client = commands.Bot(command_prefix=prefix, case_insensitive=True)

##RACES##
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

HIS_ARace = [EEPC, LR, MTF, PHB, SCAG, VGM, XGE]
CUS_Race = [PHB, SPC]

###CLASSES##
#####ARTIFICER#####
Artificer = ['Alchemist Artificer', 'Armorer Artificer',
             'Artillerist Artificer', 'Battle Smith Artificer']

#####BARBARIAN#####
Barbarian_PHB = ['Path of the Berserker Barbarian',
                 'Path of the Totem Warrior Barbarian']
Barbarian_SCAGa = ['Path of the Battlerager Barbarian',
                   'Path of the Berserker Barbarian', 'Path of the Totem Warrior Barbarian']
Barbarian_SCAGo = ['Path of the Battlerager Barbarian',
                   'Path of the Totem Warrior Barbarian']
Barbarian_TCEa = ['Path of the Beast Barbarian', 'Path of the Wild Magic Barbarian',
                  'Path of the Berserker Barbarian', 'Path of the Totem Warrior Barbarian']
Barbarian_TCEo = ['Path of the Beast Barbarian',
                  'Path of the Wild Magic Barbarian']
Barbarian_XGEa = ['Path of the Ancestral Guardian Barbarian', 'Path of the Berserker Barbarian',
                  'Path of the Totem Warrior Barbarian', 'Path of the Storm Herald Barbarian', 'Path of the Zealot Barbarian']
Barbarian_XGEo = ['Path of the Ancestral Guardian Barbarian',
                  'Path of the Storm Herald Barbarian', 'Path of the Zealot Barbarian']
BRB00 = random.choice(Barbarian_PHB)
BRB01 = random.choice(Barbarian_SCAGo)
BRB11 = random.choice(Barbarian_SCAGa)
BRB02 = random.choice(Barbarian_TCEo)
BRB12 = random.choice(Barbarian_TCEa)
BRB03 = random.choice(Barbarian_XGEo)
BRB13 = random.choice(Barbarian_XGEa)
HIS_Barbarian = [BRB00, BRB01, BRB03]
CUR_Barbarian = [BRB00, BRB02, BRB03]

#####BARD#####
Bard_PHB = ['College of Lore Bard', 'College of Valor Bard']
Bard_SCAG = ['College of Lore Bard', 'College of Valor Bard']
Bard_TCEa = ['College of Creation Bard', 'College of Eloquence Bard',
             'College of Lore Bard', 'College of Valor Bard']
Bard_TCEo = ['College of Creation Bard', 'College of Eloquence Bard']
Bard_XGEa = ['College of Lore Bard', 'College of Valor Bard',
             'College of Glamour Bard', 'College of Whispers Bard']
Bard_XGEo = ['College of Glamour Bard', 'College of Whispers Bard']
BRD00 = random.choice(Bard_PHB)
BRD01 = random.choice(Bard_TCEo)
BRD11 = random.choice(Bard_TCEa)
BRD02 = random.choice(Bard_XGEo)
BRD12 = random.choice(Bard_XGEa)
HIS_Bard = [BRD00, BRD02]
CUR_Bard = [BRD00, BRD01, BRD02]

#####CLERIC#####
Cleric_PHB = ['Knowledge Domain Cleric', 'Life Domain Cleric', 'Light Domain Cleric',
              'Nature Domain Cleric', 'Tempest Domain Cleric', 'Trickery Domain Cleric', 'War Domain Cleric']
Cleric_SCAGa = ['Arcana Domain Cleric', 'Knowledge Domain Cleric', 'Life Domain Cleric', 'Light Domain Cleric',
                'Nature Domain Cleric', 'Tempest Domain Cleric', 'Trickery Domain Cleric', 'War Domain Cleric']
Cleric_SCAGo = ['Arcana Domain Cleric']
Cleric_TCEa = ['Knowledge Domain Cleric', 'Life Domain Cleric', 'Light Domain Cleric', 'Nature Domain Cleric', 'Tempest Domain Cleric',
               'Trickery Domain Cleric', 'War Domain Cleric', 'Order Domain Cleric', 'Peace Domain Cleric', 'Twilight Domain Cleric']
Cleric_TCEo = ['Order Domain Cleric',
               'Peace Domain Cleric', 'Twilight Domain Cleric']
Cleric_XGEa = ['Knowledge Domain Cleric', 'Life Domain Cleric', 'Light Domain Cleric', 'Nature Domain Cleric',
               'Tempest Domain Cleric', 'Trickery Domain Cleric', 'War Domain Cleric', 'Forge Domain Cleric', 'Grave Domain Cleric']
Cleric_XGEo = ['Forge Domain Cleric', 'Grave Domain Cleric']
CLE00 = random.choice(Cleric_PHB)
CLE01 = random.choice(Cleric_SCAGo)
CLE11 = random.choice(Cleric_SCAGa)
CLE02 = random.choice(Cleric_TCEo)
CLE12 = random.choice(Cleric_TCEa)
CLE03 = random.choice(Cleric_XGEo)
CLE13 = random.choice(Cleric_XGEa)
HIS_Cleric = [CLE00, CLE01, CLE03]
CUR_Cleric = [CLE00, CLE02, CLE03]

#####DRUID#####
Druid_PHB = ['Circle of the Land Druid', 'Circle of the Moon Druid']
Druid_SCAG = ['Circle of the Land Druid', 'Circle of the Moon Druid']
Druid_TCEa = ['Circle of the Land Druid', 'Circle of the Moon Druid',
              'Circle of the Spores Druid', 'Circle of the Stars Druid', 'Circle of the Wildfire Druid']
Druid_TCEo = ['Circle of the Spores Druid',
              'Circle of the Stars Druid', 'Circle of the Wildfire Druid']
Druid_XGEa = ['Circle of the Land Druid', 'Circle of the Moon Druid',
              'Circle of the Dreams Druid', 'Circle of the Shepherd Druid']
Druid_XGEo = ['Circle of the Dreams Druid', 'Circle of the Shepherd Druid']
DRU00 = random.choice(Druid_PHB)
DRU01 = random.choice(Druid_TCEo)
DRU11 = random.choice(Druid_TCEa)
DRU02 = random.choice(Druid_XGEo)
DRU12 = random.choice(Druid_XGEa)
HIS_Druid = [DRU00, DRU02]
CUR_Druid = [DRU00, DRU01, DRU02]

#####FIGHTER#####
Fighter_PHB = ['Battle Master Fighter',
               'Champion Fighter', 'Eldritch Knight Fighter']
Fighter_SCAGa = ['Battle Master Fighter',
                 'Champion Fighter', 'Eldritch Knight Fighter']
Fighter_SCAGo = ['Purple Dragon Knight (Banneret) Fighter']
Fighter_TCEa = ['Battle Master Fighter',
                'Champion Fighter', 'Eldritch Knight Fighter']
Fighter_TCEo = ['Psi Warrior Fighter', 'Rune Knight Fighter']
Fighter_XGEa = ['Battle Master Fighter', 'Champion Fighter', 'Eldritch Knight Fighter',
                'Arcane Archer Fighter', 'Cavalier Fighter', 'Samurai Fighter']
Fighter_XGEo = ['Arcane Archer Fighter', 'Cavalier Fighter', 'Samurai Fighter']
FIG00 = random.choice(Fighter_PHB)
FIG01 = random.choice(Fighter_SCAGo)
FIG11 = random.choice(Fighter_SCAGa)
FIG02 = random.choice(Fighter_TCEo)
FIG12 = random.choice(Fighter_TCEa)
FIG03 = random.choice(Fighter_XGEo)
FIG13 = random.choice(Fighter_XGEa)
HIS_Fighter = [FIG00, FIG01, FIG03]
CUR_Fighter = [FIG00, FIG02, FIG03]

#####MONK#####
Monk_PHB = ['Way of the Four Elements Monk',
            'Way of the pen Hand Monk', 'Way of Shadow Monk']
Monk_SCAGa = ['Way of the Four Elements Monk', 'Way of the Open Hand Monk',
              'Way of Shadow Monk', 'Way of the Long Death Monk', 'Way of the Sun Soul Monk']
Monk_SCAGo = ['Way of the Long Death Monk', 'Way of the Sun Soul Monk']
Monk_TCEa = ['Way of the Astral Self Monk', 'Way of the Mercy Monk',
             'Way of the Four Elements Monk', 'Way of the Open Hand Monk', 'Way of Shadow Monk']
Monk_TCEo = ['Way of the Astral Self Monk', 'Way of the Mercy Monk']
Monk_XGEa = ['Way of the Four Elements Monk', 'Way of the Open Hand Monk', 'Way of Shadow Monk',
             'Way of the Drunken Master Monk', 'Way of the Kensei Monk', 'SWay of the un Soul Monk']
Monk_XGEo = ['Way of the Drunken Master Monk',
             'Way of the Kensei Monk', 'Way of the Sun Soul Monk']
MON00 = random.choice(Monk_PHB)
MON01 = random.choice(Monk_SCAGo)
MON11 = random.choice(Monk_SCAGa)
MON02 = random.choice(Monk_TCEo)
MON12 = random.choice(Monk_TCEa)
MON03 = random.choice(Monk_XGEo)
MON13 = random.choice(Monk_XGEa)
HIS_Monk = [MON00, MON01, MON03]
CUR_Monk = [MON00, MON02, MON03]

#####PALADIN#####
Paladin_PHB = ['Oath of the Ancients Paladin',
               'Oath of Devotion Paladin', 'Oath of Vengeance Paladin']
Paladin_SCAGa = ['Oath of the Ancients Paladin', 'Oath of the Crown Paladin',
                 'Oath of Devotion Paladin', 'Oath of Vengeance Paladin']
Paladin_SCAGo = ['Oath of the Crown Paladin']
Paladin_TCEa = ['Oath of the Ancients Paladin',
                'Oath of Devotion Paladin', 'Oath of Vengeance Paladin']
Paladin_TCEo = ['Oath of Glory Paladin', 'Oath of the Watchers Paladin']
Paladin_XGEa = ['Oath of the Ancients Paladin', 'Oath of Devotion Paladin',
                'Oath of Vengeance Paladin', 'Oath of Conquest Paladin', 'Oath of Redemption Paladin']
Paladin_XGEo = ['Oath of Conquest Paladin', 'Oath of Redemption Paladin']
PAL00 = random.choice(Paladin_PHB)
PAL01 = random.choice(Paladin_SCAGo)
PAL11 = random.choice(Paladin_SCAGa)
PAL02 = random.choice(Paladin_TCEo)
PAL12 = random.choice(Paladin_TCEa)
PAL03 = random.choice(Paladin_XGEo)
PAL13 = random.choice(Paladin_XGEa)
HIS_Paladin = [PAL00, PAL01, PAL03]
CUR_Paladin = [PAL00, PAL02, PAL03]

#####RANGER#####
Ranger_PHB = ['Beast Master Ranger', 'Hunter Ranger']
Ranger_SCAG = ['Beast Master Ranger', 'Hunter Ranger']
Ranger_TCEa = ['Beast Master Ranger', 'Hunter',
               'Fey Wanderer Ranger', 'Swarm Keeper Ranger']
Ranger_TCEo = ['Fey Wanderer Ranger', 'Swarm Keeper Ranger']
Ranger_XGEa = ['Beast Master Ranger', 'Hunter Ranger',
               'Gloom Stalker Ranger', 'Horizon Walker Ranger', 'Monster Slayer Ranger']
Ranger_XGEo = ['Gloom Stalker Ranger',
               'Horizon Walker Ranger', 'Monster Slayer Ranger']
RAN00 = random.choice(Ranger_PHB)
RAN01 = random.choice(Ranger_TCEo)
RAN11 = random.choice(Ranger_TCEa)
RAN02 = random.choice(Ranger_XGEo)
RAN12 = random.choice(Ranger_XGEa)
HIS_Ranger = [RAN00, RAN02]
CUR_Ranger = [RAN00, RAN01, RAN02]

#####ROGUE#####
Rogue_PHB = ['Arcane Trickster Rogue', 'Assassin Rogue', 'Thief Rogue']
Rogue_SCAGa = ['Arcane Trickster Rogue', 'Assassin Rogue',
               'Thief Rogue', 'Mastermind Rogue', 'Swashbuckler Rogue']
Rogue_SCAGo = ['Mastermind Rogue', 'Swashbuckler Rogue']
Rogue_TCEa = ['Arcane Trickster Rogue', 'Assassin Rogue',
              'Thief Rogue', 'Phantom Rogue', 'Soulknife Rogue']
Rogue_TCEo = ['Phantom Rogue', 'Soulknife Rogue']
Rogue_XGEa = ['Arcane Trickster Rogue', 'Assassin Rogue', 'Thief Rogue']
Rogue_XGEo = ['Inquisitive Rogue', 'Mastermind Rogue',
              'Scout Rogue', 'Swashbuckler Rogue']
ROG00 = random.choice(Rogue_PHB)
ROG01 = random.choice(Rogue_SCAGo)
ROG11 = random.choice(Rogue_SCAGa)
ROG02 = random.choice(Rogue_TCEo)
ROG12 = random.choice(Rogue_TCEa)
ROG03 = random.choice(Rogue_XGEo)
ROG13 = random.choice(Rogue_XGEa)
HIS_Rogue = [ROG00, ROG01, ROG03]
CUR_Rogue = [ROG00, ROG02, ROG03]

#####SORCERER#####
Sorcerer_PHB = ['Draconic Bloodline Sorcerer', 'Wild Magic Sorcerer']
Sorcerer_SCAGa = ['Draconic Bloodline Sorcerer',
                  'Wild Magic Sorcerer', 'Storm Sorcerer']
Sorcerer_SCAGo = ['Storm Sorcerer']
Sorcerer_TCEa = ['Aberrant Mind Sorcerer', 'Clockwork Soul Sorcerer',
                 'Draconic Bloodline Sorcerer', 'Wild Magic Sorcerer']
Sorcerer_TCEo = ['Aberrant Mind Sorcerer', 'Clockwork Soul Sorcerer']
Sorcerer_XGEa = ['Draconic Bloodline Sorcerer', 'Divine Soul Sorcerer',
                 'Shadow Magic Sorcerer', 'Wild Magic Sorcerer', 'Storm Sorcerer']
Sorcerer_XGEo = ['Divine Soul Sorcerer',
                 'Shadow Magic Sorcerer', 'Storm Sorcerer']
SOR00 = random.choice(Sorcerer_PHB)
SOR01 = random.choice(Sorcerer_SCAGo)
SOR11 = random.choice(Sorcerer_SCAGa)
SOR02 = random.choice(Sorcerer_TCEo)
SOR12 = random.choice(Sorcerer_TCEa)
SOR03 = random.choice(Sorcerer_XGEo)
SOR13 = random.choice(Sorcerer_XGEa)
HIS_Sorcerer = [SOR00, SOR01, SOR03]
CUR_Sorcerer = [SOR00, SOR02, SOR03]

#####WARLOCK#####
Warlock_PHB = ['The Archfey Warlock',
               'The Fiend Warlock', 'The Great Old One Warlock']
Warlock_SCAGa = ['The Archfey Warlock', 'The Fiend Warlock',
                 'The Great Old One Warlock', 'The Undying Warlock']
Warlock_SCAGo = ['The Undying Warlock']
Warlock_TCEa = ['The Archfey Warlock', 'The Fiend Warlock',
                'The Fathomless Warlock', 'The Genie Warlock', 'The Great Old One Warlock']
Warlock_TCEo = ['The Fathomless Warlock', 'The Genie Warlock']
Warlock_XGEa = ['The Archfey Warlock', 'The Celestial Warlock',
                'The Hexblade Warlock', 'The Fiend Warlock', 'The Great Old One Warlock']
Warlock_XGEo = ['The Celestial Warlock', 'The Hexblade Warlock']
WAR00 = random.choice(Warlock_PHB)
WAR01 = random.choice(Warlock_SCAGo)
WAR11 = random.choice(Warlock_SCAGa)
WAR02 = random.choice(Warlock_TCEo)
WAR12 = random.choice(Warlock_TCEa)
WAR03 = random.choice(Warlock_XGEo)
WAR13 = random.choice(Warlock_XGEa)
HIS_Warlock = [WAR00, WAR01, WAR03]
CUR_Warlock = [WAR00, WAR02, WAR03]

#####WIZARD#####
Wizard_PHB = ['School of Abjuration Wizard', 'School of Conjuration Wizard', 'School of Divination Wizard', 'School of Enchantment Wizard',
              'School of Evocation Wizard', 'School of Illusion Wizard', 'School of Necromancy Wizard', 'School of Transmutation Wizard']
Wizard_SCAGa = ['School of Abjuration Wizard', 'School of Conjuration Wizard', 'School of Divination Wizard', 'School of Enchantment Wizard',
                'School of Evocation Wizard', 'School of Illusion Wizard', 'School of Necromancy Wizard', 'School of Transmutation Wizard']
Wizard_SCAGo = ['Bladesinging Wizard']
Wizard_TCEa = ['School of Abjuration Wizard', 'School of Conjuration Wizard', 'School of Divination Wizard', 'School of Enchantment Wizard', 'School of Evocation Wizard',
               'School of Illusion Wizard', 'School of Necromancy Wizard', 'School of Transmutation Wizard', 'Bladesinging Wizard', 'Order of Scribes Wizard']
Wizard_TCEo = ['Bladesinging Wizard', 'Order of Scribes Wizard']
Wizard_XGEa = ['School of Abjuration Wizard', 'School of Conjuration Wizard', 'School of Divination Wizard', 'School of Enchantment Wizard',
               'School of Evocation Wizard', 'School of Illusion Wizard', 'School of Necromancy Wizard', 'School of Transmutation Wizard', 'War Magic Wizard']
Wizard_XGEo = ['War Magic Wizard']
WIZ00 = random.choice(Wizard_PHB)
WIZ01 = random.choice(Wizard_SCAGo)
WIZ11 = random.choice(Wizard_SCAGa)
WIZ02 = random.choice(Wizard_TCEo)
WIZ12 = random.choice(Wizard_TCEa)
WIZ03 = random.choice(Wizard_XGEo)
WIZ13 = random.choice(Wizard_XGEa)
HIS_Wizard = [WIZ00, WIZ01, WIZ03]
CUR_Wizard = [WIZ00, WIZ02, WIZ03]

HIS_AClass = HIS_Barbarian, HIS_Bard, HIS_Cleric, HIS_Druid, HIS_Fighter, HIS_Monk, HIS_Paladin, HIS_Ranger, HIS_Rogue, HIS_Sorcerer, HIS_Warlock, HIS_Wizard
HIS_BClass = BRB11, BRD00, CLE11, DRU00, FIG11, MON11, PAL11, RAN00, ROG11, SOR11, WAR11, WIZ11
HIS_CClass = BRB12, BRD11, CLE12, DRU11, FIG12, MON12, PAL12, RAN11, ROG12, SOR12, WAR12, WIZ12
HIS_DClass = BRB13, BRD12, CLE13, DRU12, FIG13, MON13, PAL13, RAN12, ROG13, SOR13, WAR13, WIZ13
HIS_EClass = BRB00, BRD00, CLE00, DRU00, FIG00, MON00, PAL00, RAN00, ROG00, SOR00, WAR00, WIZ00

CUR_AClass = Artificer, CUR_Barbarian, CUR_Bard, CUR_Cleric, CUR_Druid, CUR_Fighter, CUR_Monk, CUR_Paladin, CUR_Ranger, CUR_Rogue, CUR_Sorcerer, CUR_Warlock, CUR_Wizard

val1A = random.choice(random.choices(HIS_ARace))


def race_roller1A():
    return random.choice(random.choice(HIS_ARace))


def race_roller1B():
    return random.choice(random.choices(CUS_Race))


def class_roller1A():
    return random.choice(HIS_AClass)


def class_roller1B():
    return random.choice(HIS_BClass)


def class_roller1C():
    return random.choice(HIS_CClass)


def class_roller1D():
    return random.choice(HIS_DClass)


def class_roller1E():
    return random.choice(HIS_EClass)


def class_roller3():
    return random.choice(random.choice(CUR_AClass))


def race_rollerB():
    return random.choice(random.choice(CUS_Race))


def roller(list):
    """Returns a random choice from the given list.

    Args:
        list ([str]): A list of choices.

    Returns:
        str: A random choice from the given list.
    """
    return random.choice(list)


def Past():
    # msg = 'Your race is ' + race_roller1A() + '\n'
    #
    # if val1A in PHB:
    #     msg = msg + 'Your Historical Class is ' + class_roller1A()
    # elif val1A in SCAG:
    #     msg = msg + 'Your Historical Class is ' + class_roller1B()
    # elif val1A in XGE:
    #     msg = msg + 'Your Historical Class is ' + class_roller1D()
    # elif val1A in EEPC or LR or MTF or VGM:
    #     msg = msg + 'Your Historical Class is ' + class_roller1E()

    msg = 'Your race is ' + roller(tome.HIS_RACE) + '\n' + \
          'Your Historical Class is ' + roller(tome.HIS_CLASSES)

    # print(ms6g)
    return msg


def Curr():
    msg = 'Your race is ' + roller(tome.CUR_RACE) + '\n' + \
          'Your Seasonal Class is ' + roller(tome.CUR_CLASSES)

    # print(msg)
    return msg


@client.event
async def on_ready():
    print('The Archarchmage has awoken.')


@client.command()
async def quote(ctx):
    await ctx.send('Tama may point siya.')


@client.command()
async def Old(ctx):
    await ctx.send(Past())


@client.command()
async def New(ctx):
    await ctx.send(Curr())


if __name__ == '__main__':
    client.run(token)
