"""
The purpose of this module is to define the Persona class and create a 2D array containing all the Personas
obtainable in Persona 4 Golden along with  information about them and the ability to display that info.
The array is sorted by arcana in the same manner as the "arcanas" array in fusion_chart.py for the ease of the
implementation of the actual fusion calculator. I also added in the World arcana, for completion's sake, and so that
users may search for information about Izanagi-no-Okami in the PersonaSearch.py file.
"""


class Persona:

    def __init__(self, name, arcana, base_lv, base_stats, resistances,
                 max_sl_req=False, special_fusion=None, is_kami=False):
        """
        Define a Persona's attributes

        :param name: string - Name of Persona
        :param arcana: string - Arcana of Persona
        :param base_lv: int - Base Level of Persona
        :param base_stats: List of ints - Define base stats of a Persona - Order is St, Ma, En, Ag, Lu
        :param resistances: List of strings - Define resistances of a Persona.
            Order is Phys, Fire, Ice, Elec, Wind, Light, Dark. Valid values are 0, 1, 2, 3, 4, 5.
            0 = Wk, 1 = Normal, 2 = Str, 3 = Nul, 4 = Rpl, 5 = Dr
        :param max_sl_req: boolean - Requires max Social Link? False by default.
        :param special_fusion: List of strings - Ingredients if the Persona requires a Special Fusion. None by default.
        :param is_kami: Boolean - Is the Persona Izanagi-no-Okami? False by default.
        """
        self.name = name
        self.arcana = arcana
        self.base_lv = base_lv
        self.base_stats = base_stats
        self.resistances = resistances
        self.max_sl_req = max_sl_req
        self.special_fusion = special_fusion
        self.is_kami = is_kami

    def info(self):
        """

        :return string - An info message about the Persona
        """
        base_stats_strings = ["St: ", " | Ma: ", " | En: ", " | Ag: ", " | Lu: "]
        stat_msg = ""   # Placeholder
        elements = ["Phys: ", " | Fire: ", " | Ice: ", " | Elec: ", " | Wind: ", " | Light: ", " | Dark: "]
        resistances = ["Wk", "--", "Str", "Nul", "Rpl", "Dr"]
        resist_msg = ""  # Placeholder

        persona_info = "\nPersona: " + self.name + "\nArcana: " + self.arcana + "\nBase Level: " + str(self.base_lv) +\
                       "\n\nBase Stats:\n"

        for stat in range(len(base_stats_strings)):
            stat_msg += base_stats_strings[stat] + str(self.base_stats[stat])

        persona_info += stat_msg + "\n\nResistances:\n"

        for element in range(len(elements)):
            resist_msg += elements[element] + resistances[self.resistances[element]]

        persona_info += resist_msg + "\n"

        if self.max_sl_req:
            persona_info += "\nRequires Max Social Link Rank!\n"
        elif self.is_kami:
            persona_info += "\nRequires New Game +!\n"

        if self.special_fusion is not None:
            req_string = ""

            for req in range(len(self.special_fusion)):

                if req != len(self.special_fusion) - 1:
                    req_string += self.special_fusion[req] + ", "
                else:
                    req_string += self.special_fusion[req]

            persona_info += "\nRequires Special Fusion!\nRequired Personas: " + req_string

        return persona_info


Fool = [
    Persona("Izanagi", "Fool", 1, [3, 2, 2, 3, 2], [1, 1, 1, 2, 0, 1, 3]),
    Persona("Yomotsu-Shikome", "Fool", 7, [2, 7, 7, 8, 4], [1, 2, 2, 1, 1, 0, 2]),
    Persona("Obariyon", "Fool", 13, [11, 6, 11, 9, 9], [2, 2, 1, 1, 1, 1, 1]),
    Persona("Legion", "Fool", 21, [14, 14, 18, 13, 11], [1, 2, 2, 1, 1, 0, 2]),
    Persona("Ose", "Fool", 31, [28, 12, 29, 25, 15], [2, 1, 1, 1, 4, 0, 1]),
    Persona("Black Frost", "Fool", 38, [23, 31, 22, 23, 22], [1, 5, 5, 1, 1, 1, 4],
            special_fusion=["Jack Frost", "Pyro Jack", "King Frost", "Pixie", "Ghoul"]),
    Persona("Decarabia", "Fool", 40, [27, 36, 25, 26, 31], [0, 1, 1, 3, 2, 3, 1]),
    Persona("Shiki-Ouji", "Fool", 56, [50, 29, 31, 41, 24], [1, 3, 3, 1, 0, 1, 1]),
    Persona("Loki", "Fool", 64, [48, 50, 31, 47, 23], [1, 0, 5, 1, 1, 1, 3], max_sl_req=True)
]

Magician = [
    Persona("Pixie", "Magician", 2, [2, 3, 2, 4, 2], [1, 0, 1, 1, 2, 1, 1]),
    Persona("Orobas", "Magician", 8, [4, 10, 6, 10, 6], [1, 2, 0, 1, 1, 1, 1]),
    Persona("Jack Frost", "Magician", 16, [10, 14, 12, 11, 8], [1, 0, 3, 1, 1, 1, 1]),
    Persona("Hua Po", "Magician", 25, [14, 21, 15, 17, 15], [1, 3, 0, 1, 1, 1, 1]),
    Persona("Pyro Jack", "Magician", 32, [16, 26, 19, 22, 20], [1, 5, 0, 1, 1, 1, 1]),
    Persona("Dis", "Magician", 39, [25, 31, 24, 26, 21], [1, 4, 1, 1, 1, 1, 1]),
    Persona("Rangda", "Magician", 47, [24, 37, 30, 25, 32], [4, 1, 0, 1, 1, 1, 1]),
    Persona("Jinn", "Magician", 62, [37, 51, 38, 39, 28], [1, 5, 1, 0, 1, 1, 1]),
    Persona("Surt", "Magician", 69, [41, 54, 39, 40, 40], [1, 4, 0, 1, 3, 1, 1]),
    Persona("Mada", "Magician", 78, [45, 63, 52, 38, 43], [1, 5, 0, 1, 1, 1, 1], max_sl_req=True)
]

Priestess = [
    Persona("Saki Mitama", "Priestess", 11, [5, 12, 5, 8, 10], [1, 1, 2, 1, 0, 1, 1]),
    Persona("Sarasvati", "Priestess", 17, [9, 16, 10, 13, 10], [1, 1, 3, 1, 0, 1, 1]),
    Persona("High Pixie", "Priestess", 22, [10, 21, 10, 19, 13], [1, 1, 0, 3, 1, 1, 1]),
    Persona("Ganga", "Priestess", 29, [16, 22, 16, 19, 21], [1, 0, 5, 1, 1, 1, 0]),
    Persona("Parvati", "Priestess", 37, [20, 29, 17, 25, 27], [1, 0, 3, 1, 1, 1, 1]),
    Persona("Kikuri-Hime", "Priestess", 48, [26, 36, 28, 21, 30], [1, 3, 1, 2, 1, 1, 0]),
    Persona("Hariti", "Priestess", 59, [31, 47, 33, 34, 39], [1, 1, 3, 0, 2, 1, 1]),
    Persona("Tzitzimitl", "Priestess", 70, [46, 56, 41, 39, 35], [1, 1, 1, 4, 0, 1, 3]),
    Persona("Scathach", "Priestess", 79, [54, 59, 37, 49, 45], [1, 0, 5, 1, 3, 1, 1], max_sl_req=True)
]

Empress = [
    Persona("Senri", "Empress", 9, [7, 7, 4, 14, 7], [1, 3, 1, 0, 1, 1, 1]),
    Persona("Yaksini", "Empress", 18, [13, 16, 10, 12, 10], [1, 0, 3, 2, 1, 1, 1]),
    Persona("Titania", "Empress", 26, [12, 13, 15, 19, 16], [1, 0, 2, 1, 1, 1, 1]),
    Persona("Gorgon", "Empress", 34, [20, 21, 15, 24, 19], [1, 1, 3, 1, 1, 0, 1]),
    Persona("Gabriel", "Empress", 44, [28, 34, 22, 30, 25], [1, 2, 1, 1, 5, 3, 0]),
    Persona("Skadi", "Empress", 52, [27, 37, 32, 36, 31], [1, 0, 5, 1, 2, 1, 1]),
    Persona("Mother Harlot", "Empress", 60, [38, 47, 37, 29, 36], [1, 1, 2, 4, 0, 0, 3]),
    Persona("Alilat", "Empress", 70, [39, 48, 49, 39, 42], [1, 1, 3, 0, 1, 1, 1]),
    Persona("Isis", "Empress", 79, [52, 48, 42, 48, 54], [1, 1, 4, 0, 1, 1, 1], max_sl_req=True)
]

Emperor = [
    Persona("Oberon", "Emperor", 12, [10, 12, 8, 8, 5], [1, 2, 1, 3, 0, 1, 1]),
    Persona("King Frost", "Emperor", 22, [11, 20, 17, 13, 12], [1, 0, 5, 1, 1, 1, 1]),
    Persona("Setanta", "Emperor", 34, [23, 21, 25, 24, 16], [1, 0, 1, 3, 1, 1, 1]),
    Persona("Oukuninushi", "Emperor", 41, [29, 34, 25, 20, 22], [1, 1, 1, 4, 0, 1, 1]),
    Persona("Thoth", "Emperor", 45, [28, 43, 23, 21, 27], [1, 1, 1, 3, 0, 4, 0]),
    Persona("Pabilsag", "Emperor", 51, [38, 29, 30, 33, 30], [1, 3, 0, 1, 1, 0, 4]),
    Persona("Barong", "Emperor", 65, [48, 44, 40, 36, 34], [1, 1, 1, 3, 0, 1, 1]),
    Persona("Odin", "Emperor", 74, [48, 60, 42, 39, 43], [1, 0, 1, 3, 5, 1, 1], max_sl_req=True)
]

Hierophant = [  # Great vegetables!
    Persona("Omoikane", "Hierophant", 7, [5, 8, 5, 4, 6], [1, 1, 0, 2, 1, 1, 1]),
    Persona("Anzu", "Hierophant", 15, [9, 11, 10, 13, 9], [1, 0, 1, 2, 3, 1, 1]),
    Persona("Shiisaa", "Hierophant", 21, [18, 18, 9, 14, 11], [1, 0, 2, 3, 1, 1, 0]),
    Persona("Unicorn", "Hierophant", 29, [17, 22, 19, 22, 14], [1, 1, 3, 1, 0, 1, 0]),
    Persona("Flauros", "Hierophant", 36, [30, 20, 24, 20, 21], [1, 3, 0, 1, 2, 1, 1]),
    Persona("Hokuto Seikun", "Hierophant", 45, [29, 34, 31, 26, 22], [1, 0, 1, 4, 1, 1, 1]),
    Persona("Cerberus", "Hierophant", 52, [37, 30, 32, 35, 29], [1, 4, 0, 1, 1, 1, 1]),
    Persona("Daisoujou", "Hierophant", 60, [34, 45, 40, 30, 41], [1, 3, 1, 1, 1, 3, 0]),
    Persona("Hachiman", "Hierophant", 70, [33, 60, 39, 38, 47], [1, 1, 3, 3, 1, 1, 0]),
    Persona("Kohryu", "Hierophant", 76, [50, 53, 54, 40, 38], [1, 1, 1, 4, 1, 3, 1], max_sl_req=True,
            special_fusion=["Genbu", "Seiryu", "Suzaku", "Byakko"])
]

Lovers = [
    Persona("Queen Mab", "Lovers", 25, [17, 19, 15, 17, 14], [1, 1, 1, 3, 0, 1, 1]),
    Persona("Undine", "Lovers", 33, [21, 27, 13, 26, 19], [1, 0, 5, 1, 1, 1, 1]),
    Persona("Leanan Sidhe", "Lovers", 42, [1, 0, 3, 1, 2, 1, 1], [1, 0, 3, 1, 2, 1, 1]),
    Persona("Raphael", "Lovers", 53, [32, 38, 24, 33, 39], [1, 1, 4, 1, 1, 3, 0]),
    Persona("Cybele", "Lovers", 64, [41, 47, 37, 39, 35], [1, 2, 3, 0, 1, 1, 1]),
    Persona("Ishtar", "Lovers", 71, [46, 44, 33, 48, 49], [1, 1, 1, 3, 0, 1, 1], max_sl_req=True),
]

Chariot = [
    Persona("Slime", "Chariot", 2, [3, 2, 3, 2, 3], [2, 0, 1, 1, 1, 1, 1]),
    Persona("Nata Taishi", "Chariot", 6, [6, 2, 6, 7, 4], [1, 2, 1, 0, 1, 1, 1]),
    Persona("Eligor", "Chariot", 12, [11, 6, 13, 8, 5], [2, 1, 1, 1, 1, 0, 2]),
    Persona("Ara Mitama", "Chariot", 18, [11, 11, 11, 11, 11], [2, 1, 1, 0, 1, 1, 1]),
    Persona("Ares", "Chariot", 25, [18, 15, 20, 15, 14], [2, 1, 1, 1, 0, 3, 1]),
    Persona("Triglav", "Chariot", 43, [33, 23, 27, 32, 21], [2, 1, 1, 0, 1, 1, 1]),
    Persona("Kin-Ki", "Chariot", 54, [41, 25, 53, 23, 27], [3, 1, 1, 1, 1, 1, 1]),
    Persona("Thor", "Chariot", 65, [43, 39, 53, 32, 25], [2, 1, 1, 5, 0, 1, 1]),
    Persona("Atavaka", "Chariot", 72, [50, 41, 43, 41, 48], [3, 1, 0, 1, 1, 3, 1]),
    Persona("Futsunushi", "Chariot", 80, [59, 38, 61, 44, 45], [3, 1, 1, 1, 1, 1, 0], max_sl_req=True,
            special_fusion=["Ares", "Triglav", "Kin-Ki", "Atavaka", "Neko Shogun"])
]

Justice = [
    Persona("Angel", "Justice", 4, [4, 5, 2, 8, 5], [1, 1, 1, 1, 2, 2, 0]),
    Persona("Archangel", "Justice", 11, [8, 9, 7, 7, 9], [1, 1, 1, 1, 1, 3, 0]),
    Persona("Principality", "Justice", 19, [11, 15, 10, 18, 10], [1, 1, 1, 1, 1, 3, 0]),
    Persona("Power", "Justice", 27, [21, 20, 11, 17, 19], [1, 2, 1, 0, 3, 1, 0]),
    Persona("Virtue", "Justice", 33, [22, 29, 21, 19, 15], [1, 1, 0, 3, 1, 3, 0]),
    Persona("Dominion", "Justice", 38, [22, 32, 25, 24, 18], [1, 1, 1, 3, 0, 4, 0]),
    Persona("Throne", "Justice", 49, [37, 30, 24, 37, 26], [1, 5, 1, 1, 1, 3, 0]),
    Persona("Uriel", "Justice", 58, [35, 42, 37, 36, 31], [1, 4, 1, 1, 1, 3, 0]),
    Persona("Melchizedek", "Justice", 66, [51, 46, 46, 34, 28], [1, 1, 1, 1, 1, 3, 0]),     # This name is awful!
    Persona("Sraosha", "Justice", 74, [57, 36, 44, 62, 33], [1, 1, 1, 5, 1, 4, 0], max_sl_req=True)
]

Hermit = [
    Persona("Forneus", "Hermit", 6, [4, 5, 7, 9, 5], [1, 1, 2, 0, 1, 1, 3]),
    Persona("Ippon-Datara", "Hermit", 17, [15, 6, 14, 13, 10], [1, 2, 1, 1, 1, 0, 3]),
    Persona("Lamia", "Hermit", 26, [16, 23, 12, 20, 14], [1, 2, 1, 2, 1, 1, 3]),
    Persona("Mothman", "Hermit", 33, [20, 23, 17, 28, 18], [1, 2, 0, 4, 1, 1, 1]),
    Persona("Hitoko-Nushi", "Hermit", 41, [28, 33, 20, 20, 19], [1, 0, 3, 1, 3, 1, 1]),
    Persona("Kurama Tengu", "Hermit", 48, [30, 34, 28, 38, 21], [1, 2, 1, 0, 5, 1, 1]),
    Persona("Niddhoggr", "Hermit", 55, [23, 41, 35, 31, 42], [1, 1, 3, 1, 1, 0, 3]),
    Persona("Nebiros", "Hermit", 63, [38, 47, 39, 40, 32], [1, 4, 1, 0, 2, 0, 3]),
    Persona("Arahabaki", "Hermit", 73, [50, 55, 62, 37, 25], [4, 0, 0, 1, 1, 3, 3]),
    Persona("Ongyo-Ki", "Hermit", 82, [59, 64, 59, 47, 24], [1, 1, 1, 3, 5, 0, 3], max_sl_req=True,
            special_fusion=["Oni", "Fuu-Ki", "Kin-Ki", "Sui-Ki"])
]

Fortune = [
    Persona("Fortuna", "Fortune", 35, [19, 23, 22, 26, 22], [1, 3, 1, 0, 3, 1, 1]),
    Persona("Clotho", "Fortune", 44, [22, 31, 28, 26, 32], [1, 1, 1, 1, 4, 1, 1]),
    Persona("Lachesis", "Fortune", 51, [31, 29, 25, 34, 31], [1, 1, 2, 0, 3, 1, 1]),
    Persona("Ananta", "Fortune", 58, [43, 42, 45, 28, 23], [2, 1, 5, 0, 1, 1, 1]),
    Persona("Atropos", "Fortune", 65, [36, 48, 36, 37, 45], [1, 0, 1, 1, 3, 1, 1]),
    Persona("Norn", "Fortune", 72, [42, 53, 31, 48, 46], [1, 1, 2, 0, 5, 1, 3], max_sl_req=True,
            special_fusion=["Atropos", "Lachesis", "Clotho"])
]

Strength = [
    Persona("Sandman", "Strength", 5, [4, 5, 6, 4, 3], [1, 1, 1, 0, 2, 1, 1]),
    Persona("Valkyrie", "Strength", 8, [7, 6, 6, 7, 5], [1, 1, 2, 1, 0, 1, 1]),
    Persona("Titan", "Strength", 14, [11, 12, 10, 10, 6], [1, 1, 0, 2, 1, 1, 1]),
    Persona("Rakshasa", "Strength", 23, [19, 12, 18, 14, 12], [2, 1, 0, 1, 1, 1, 1]),
    Persona("Kusi Mitama", "Strength", 28, [18, 21, 12, 19, 21], [1, 1, 1, 0, 3, 1, 1]),
    Persona("Oni", "Strength", 30, [25, 12, 26, 18, 16], [2, 3, 1, 1, 1, 1, 1]),
    Persona("Hanuman", "Strength", 42, [31, 25, 31, 21, 25], [2, 1, 3, 0, 1, 1, 1]),
    Persona("Kali", "Strength", 50, [37, 25, 36, 35, 27], [1, 1, 3, 0, 1, 1, 0]),
    Persona("Siegfried", "Strength", 63, [48, 36, 41, 38, 33], [3, 1, 2, 1, 0, 1, 1]),
    Persona("Zaou-Gongen", "Strength", 90, [61, 48, 71, 47, 50], [1, 4, 1, 0, 1, 1, 1], max_sl_req=True)
]

Hanged = [
    Persona("Berith", "Hanged Man", 15, [12, 10, 9, 12, 9], [1, 3, 1, 1, 0, 1, 1]),
    Persona("Yomotsu-Ikusa", "Hanged Man", 22, [17, 16, 18, 12, 10], [1, 0, 2, 1, 1, 1, 3]),
    Persona("Makami", "Hanged Man", 27, [16, 21, 12, 22, 16], [1, 3, 0, 1, 2, 0, 3]),
    Persona("Orthrus", "Hanged Man", 39, [34, 21, 28, 23, 18], [1, 3, 0, 1, 1, 1, 1]),
    Persona("Yatsufusa", "Hanged Man", 49, [32, 33, 27, 36, 26], [1, 5, 1, 1, 4, 3, 0],
            special_fusion=["Makami", "Orthrus", "Mothman", "Thoth", "Narasimha"]),
    Persona("Taowu", "Hanged Man", 56, [40, 37, 31, 38, 29], [1, 0, 1, 1, 3, 0, 3]),
    Persona("Hell Biker", "Hanged Man", 66, [49, 40, 40, 48, 28], [1, 4, 1, 1, 1, 0, 1]),
    Persona("Vasuki", "Hanged Man", 71, [48, 47, 50, 40, 35], [1, 1, 2, 3, 1, 1, 0]),
    Persona("Attis", "Hanged Man", 82, [51, 56, 56, 50, 40], [1, 3, 1, 1, 4, 1, 0], max_sl_req=True)
]

Death = [
    Persona("Ghoul", "Death", 9, [8, 7, 9, 5, 5], [1, 0, 3, 1, 1, 0, 1]),
    Persona("Mokoi", "Death", 14, [13, 7, 9, 11, 9], [1, 0, 3, 1, 1, 1, 1]),
    Persona("Matador", "Death", 24, [17, 10, 16, 25, 11], [1, 0, 1, 1, 1, 1, 4]),
    Persona("Samael", "Death", 36, [24, 29, 25, 19, 18], [1, 1, 2, 3, 0, 1, 3]),
    Persona("Mot", "Death", 46, [32, 38, 30, 24, 21], [1, 1, 1, 3, 0, 1, 4]),
    Persona("White Rider", "Death", 58, [49, 31, 37, 40, 24], [1, 3, 0, 1, 1, 3, 4]),
    Persona("Alice", "Death", 72, [39, 56, 33, 45, 44], [1, 1, 1, 1, 1, 0, 4],
            special_fusion=["Nebiros", "Belial"]),
    Persona("Mahakala", "Death", 78, [58, 38, 57, 49, 39], [1, 5, 1, 4, 1, 1, 3], max_sl_req=True,
            special_fusion=["Matador", "White Rider", "Mother Harlot", "Daisoujou", "Hell Biker", "Trumpeter"])
]

Temperance = [
    Persona("Apsaras", "Temperance", 4, [3, 5, 3, 5, 3], [1, 0, 1, 1, 1, 1, 1]),
    Persona("Sylph", "Temperance", 11, [8, 10, 5, 10, 7], [1, 1, 1, 0, 2, 1, 1]),
    Persona("Xiezhai", "Temperance", 16, [14, 12, 9, 13, 7], [1, 1, 1, 2, 0, 1, 1]),
    Persona("Nigi Mitama", "Temperance", 23, [15, 16, 14, 15, 16], [1, 1, 1, 0, 3, 1, 1]),
    Persona("Mithra", "Temperance", 31, [22, 26, 21, 16, 15], [1, 1, 3, 0, 1, 3, 1]),
    Persona("Genbu", "Temperance", 40, [28, 27, 39, 12, 21], [1, 1, 3, 0, 1, 1, 1]),
    Persona("Seiryu", "Temperance", 47, [30, 31, 33, 28, 26], [1, 0, 1, 1, 3, 1, 1]),
    Persona("Suzaku", "Temperance", 54, [30, 36, 31, 42, 30], [1, 4, 0, 1, 1, 1, 1]),
    Persona("Byakko", "Temperance", 62, [47, 32, 35, 49, 30], [1, 0, 5, 3, 1, 3, 1]),
    Persona("Yurlungur", "Temperance", 69, [41, 50, 45, 43, 35], [1, 0, 5, 1, 2, 1, 1]),
    Persona("Vishnu", "Temperance", 73, [46, 52, 34, 54, 43], [1, 0, 3, 1, 1, 3, 1], max_sl_req=True)
]

Devil = [
    Persona("Ukobach", "Devil", 3, [3, 4, 3, 4, 2], [1, 2, 0, 1, 1, 1, 1]),
    Persona("Lilim", "Devil", 10, [4, 11, 5, 9, 8], [1, 1, 1, 1, 1, 0, 2]),
    Persona("Vetala", "Devil", 19, [17, 10, 14, 12, 11], [1, 0, 1, 1, 2, 1, 2]),
    Persona("Incubus", "Devil", 28, [17, 22, 16, 19, 17], [1, 3, 1, 1, 1, 0, 3]),
    Persona("Pazuzu", "Devil", 37, [27, 15, 28, 29, 19], [1, 1, 2, 1, 1, 0, 1]),
    Persona("Succubus", "Devil", 44, [22, 33, 28, 32, 27], [1, 2, 1, 1, 1, 0, 3]),
    Persona("Lilith", "Devil", 53, [30, 43, 30, 36, 27], [1, 1, 1, 2, 1, 0, 3]),
    Persona("Belphegor", "Devil", 61, [40, 48, 42, 39, 21], [1, 1, 1, 5, 1, 0, 4]),
    Persona("Belial", "Devil", 68, [51, 31, 48, 40, 41], [1, 1, 1, 1, 1, 1, 4]),
    Persona("Beelzebub", "Devil", 81, [51, 57, 48, 50, 44], [1, 5, 3, 4, 1, 0, 4], max_sl_req=True,
            special_fusion=["Pazuzu", "Belphegor", "Belial", "Mot", "Seth", "Baal Zebul"])
]

Tower = [
    Persona("Taotie", "Tower", 35, [20, 27, 30, 22, 13], [1, 1, 1, 1, 1, 1, 4]),
    Persona("Cu Chulainn", "Tower", 46, [40, 32, 28, 25, 20], [2, 1, 0, 1, 4, 1, 1]),
    Persona("Abbadon", "Tower", 55, [43, 27, 50, 23, 29], [1, 3, 2, 1, 1, 0, 4]),
    Persona("Mara", "Tower", 62, [44, 35, 48, 36, 30], [1, 5, 1, 1, 2, 0, 4]),
    Persona("Masakado", "Tower", 69, [51, 32, 45, 46, 40], [3, 3, 1, 0, 1, 1, 0]),
    Persona("Yoshitsune", "Tower", 75, [52, 39, 49, 61, 34], [3, 2, 1, 4, 1, 4, 1],
            special_fusion=["Masakado", "Shiki-Ouji", "Oukuninushi", "Hachima", "Hitokoto-Nushi"]),
    Persona("Shiva", "Tower", 80, [59, 48, 44, 54, 42], [1, 1, 5, 4, 1, 1, 1], max_sl_req=True,
            special_fusion=["Rangda", "Barong"])
]

Star = [
    Persona("Kaiwan", "Star", 24, [16, 23, 14, 15, 11], [0, 1, 1, 1, 1, 1, 3]),
    Persona("Neko Shogun", "Star", 32, [26, 20, 19, 23, 15], [2, 1, 1, 4, 0, 3, 3],
            special_fusion=["Saki Mitama", "Ara Mitama", "Kusi Mitama", "Nigi Mitama"]),
    Persona("Fuu-Ki", "Star", 43, [25, 32, 34, 27, 18], [1, 0, 1, 1, 1, 1, 1]),
    Persona("Ganesha", "Star", 50, [38, 29, 31, 27, 32], [1, 1, 1, 0, 3, 1, 1]),
    Persona("Garuda", "Star", 57, [39, 33, 28, 47, 31], [1, 1, 1, 0, 4, 4, 0]),
    Persona("Kartikeya", "Star", 67, [47, 39, 40, 44, 38], [1, 1, 1, 4, 1, 1, 1]),
    Persona("Saturnus", "Star", 75, [50, 57, 36, 43, 49], [1, 5, 0, 1, 3, 1, 1]),
    Persona("Helel", "Star", 87, [56, 57, 56, 49, 50], [2, 3, 1, 1, 0, 3, 3], max_sl_req=True)
]

Moon = [
    Persona("Andras", "Moon", 20, [14, 16, 13, 12, 12], [1, 1, 1, 3, 0, 1, 1]),
    Persona("Nozuchi", "Moon", 27, [26, 13, 19, 15, 15], [1, 1, 0, 4, 1, 1, 1]),
    Persona("Yamata-no-Orochi", "Moon", 34, [29, 21, 26, 18, 15], [1, 0, 3, 3, 0, 1, 1]),
    Persona("Alraune", "Moon", 41, [17, 35, 21, 29, 28], [1, 2, 2, 1, 0, 1, 3]),
    Persona("Girimehkala", "Moon", 48, [36, 35, 23, 30, 27], [4, 1, 1, 1, 1, 0, 0]),
    Persona("Sui-Ki", "Moon", 57, [42, 49, 43, 33, 17], [1, 0, 5, 4, 1, 1, 1]),
    Persona("Seth", "Moon", 68, [46, 51, 40, 39, 35], [1, 1, 4, 0, 1, 1, 1]),
    Persona("Baal Zebul", "Moon", 77, [48, 60, 49, 40, 41], [1, 0, 5, 1, 1, 1, 3]),
    Persona("Sandalphon", "Moon", 84, [56, 61, 46, 47, 49], [1, 1, 1, 1, 3, 4, 0], max_sl_req=True)
]

Sun = [
    Persona("Cu Sith", "Sun", 10, [10, 5, 6, 9, 7], [1, 0, 1, 1, 2, 1, 1]),
    Persona("Phoenix", "Sun", 20, [9, 15, 9, 20, 14], [1, 1, 0, 3, 1, 1, 1]),
    Persona("Gdon", "Sun", 31, [27, 10, 23, 22, 18], [1, 5, 0, 1, 1, 1, 1]),
    Persona("Yatagarasu", "Sun", 40, [28, 27, 22, 31, 19], [1, 1, 0, 1, 2, 3, 1]),
    Persona("Narasimha", "Sun", 47, [29, 27, 30, 35, 27], [2, 0, 1, 1, 1, 3, 1]),
    Persona("Tam Lin", "Sun", 53, [45, 31, 34, 39, 25], [2, 2, 1, 1, 1, 3, 1],
            special_fusion=["Phoenix", "Gdon", "Yatagarasu", "Narasimha"]),
    Persona("Jatayu", "Sun", 61, [38, 33, 35, 48, 25], [1, 1, 1, 0, 5, 1, 1]),
    Persona("Horus", "Sun", 68, [45, 48, 35, 45, 38], [1, 0, 1, 3, 1, 4, 1]),   # Heresy!
    Persona("Suparna", "Sun", 77, [48, 52, 45, 55, 38], [1, 1, 1, 0, 3, 1, 1]),
    Persona("Asura", "Sun", 86, [59, 57, 51, 50, 48], [1, 3, 2, 1, 0, 3, 1], max_sl_req=True)
]

Judgement = [
    Persona("Anubis", "Judgement", 59, [38, 41, 37, 37, 31], [1, 1, 1, 1, 1, 3, 1]),
    Persona("Trumpeter", "Judgement", 67, [40, 47, 39, 45, 37], [1, 1, 5, 4, 1, 4, 3],
            special_fusion=["Matador", "White Rider", "Daisoujou", "Taotie", "Pabilsag", "Taowu"]),
    Persona("Michael", "Judgement", 72, [45, 42, 43, 48, 45], [2, 1, 1, 1, 0, 3, 1]),
    Persona("Satan", "Judgement", 76, [45, 60, 47, 40, 43], [1, 4, 1, 1, 0, 1, 4]),
    Persona("Metatron", "Judgement", 83, [54, 55, 53, 46, 48], [1, 3, 1, 1, 1, 3, 0]),
    Persona("Ardha", "Judgement", 90, [62, 52, 64, 41, 58], [2, 1, 3, 3, 1, 1, 1],
            special_fusion=["Parvati", "Shiva"]),
    Persona("Lucifer", "Judgement", 93, [62, 69, 61, 52, 51], [2, 1, 1, 1, 1, 0, 3], max_sl_req=True,
            special_fusion=["Ananta", "Anubis", "Trumpeter", "Michael", "Satan", "Metatron"])
]

Aeon = [
    Persona("Ame-no-Uzume", "Aeon", 18, [9, 15, 12, 10, 15], [1, 1, 1, 0, 3, 3, 1]),
    Persona("Narcissus", "Aeon", 24, [13, 18, 11, 16, 21], [0, 1, 2, 2, 2, 1, 1]),
    Persona("Sati", "Aeon", 31, [19, 27, 20, 17, 17], [1, 3, 0, 1, 1, 1, 1]),
    Persona("Raja Naga", "Aeon", 37, [25, 26, 24, 22, 21], [2, 0, 1, 3, 1, 1, 1]),
    Persona("Kushinada-Hime", "Aeon", 44, [25, 32, 27, 24, 31], [1, 1, 1, 1, 1, 3, 0]),
    Persona("Quetzalcoatl", "Aeon", 51, [30, 31, 31, 35, 33], [1, 1, 1, 1, 2, 3, 0]),
    Persona("Kingu", "Aeon", 58, [38, 44, 38, 30, 31], [1, 0, 1, 2, 1, 1, 2]),
    Persona("Lakshimi", "Aeon", 65, [36, 50, 37, 38, 41], [1, 0, 3, 1, 1, 3, 1]),
    Persona("Kaguya", "Aeon", 74, [37, 65, 36, 44, 47], [1, 0, 1, 1, 2, 3, 3], max_sl_req=True)
]

Jester = [
    Persona("Gurr", "Jester", 20, [16, 11, 14, 15, 11], [1, 1, 1, 1, 2, 0, 2]),
    Persona("Take-Minakata", "Jester", 27, [20, 20, 22, 14, 12], [2, 1, 1, 2, 1, 0, 0]),
    Persona("Pale Rider", "Jester", 34, [25, 24, 21, 24, 15], [1, 1, 1, 1, 2, 0, 3]),
    Persona("Loa", "Jester", 40, [25, 30, 28, 23, 21], [1, 1, 1, 1, 2, 0, 2]),
    Persona("Baphomet", "Jester", 47, [25, 35, 35, 36, 37], [1, 1, 1, 1, 1, 0, 3]),
    Persona("Kumbhanda", "Jester", 55, [37, 36, 35, 44, 20], [1, 5, 1, 1, 0, 1, 1]),
    Persona("Chernobog", "Jester", 62, [46, 47, 32, 35, 33], [2, 1, 1, 1, 0, 1, 3]),
    Persona("Seiten Taisei", "Jester", 68, [47, 34, 40, 48, 42], [2, 0, 1, 1, 2, 1, 1]),
    Persona("Magatsu-Izanagi", "Jester", 77, [60, 58, 55, 50, 20], [1, 1, 1, 1, 1, 3, 3], max_sl_req=True)
]

World = [
    Persona("Izanagi-no-Okami", "World", 91, [80, 80, 80, 80, 80], [2, 2, 2, 2, 2, 1, 1],
            special_fusion=["Izanagi", "Sandman", "Nata Taishi", "Girimehkala", "Norn",
                            "Oukuninushi", "Orthrus", "Kartikeya", "Mithra", "Tzitzimitl",
                            "Cu Chulainn", "Legion"], is_kami=True)
]

# All of that was in preparation for this array, organized in such a way that each index only contains
# Personas of a single Arcana, in the same order as they are listed on the fusion chart.
Personas = [Fool, Magician, Priestess, Empress, Emperor, Hierophant, Lovers, Chariot, Justice, Hermit, Fortune,
            Strength, Hanged, Death, Temperance, Devil, Tower, Star, Moon, Sun, Judgement, Jester, Aeon, World]
