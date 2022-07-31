arcanas = ["Fool", "Magician", "Priestess", "Empress", "Emperor", "Hierophant", "Lovers", "Chariot", "Justice",
           "Hermit", "Fortune", "Strength", "Hanged Man", "Death", "Temperance", "Devil", "Tower", "Star", "Moon",
           "Sun", "Judgement", "Jester", "Aeon", "World"]
# This list will be used to index the next 2D list later

fusion_chart = [      # This 2D list uses the following image as a reference: https://i.imgur.com/mzlJptZ.jpeg
    [   # Row 1: Fool Arcana
        "Fool", "Temperance", "Death", "Moon", "Death", "Chariot", "Empress", "Sun", "Magician", "Strength", "Magician",
        "Magician", "Strength", "Hermit", "Hierophant", "Temperance", "Star", "Empress", "Emperor", "Devil",
        "Hanged Man", "Priestess", "Death"
    ],
    [   # Row 2: Magician Arcana
        "Fortune", "Magician", "Moon", "Justice", "Strength", "Devil", "Death", "Temperance", "Strength", "Empress",
        "Lovers", "Justice", "Sun", "Emperor", "Strength", "Sun", "Hanged Man", "Invalid", "Star", "Chariot", "Lovers",
        "Hierophant", "Emperor"
    ],
    [   # Row 3: Priestess Arcana
        "Lovers", "Fortune", "Priestess", "Hermit", "Empress", "Sun", "Emperor", "Hierophant", "Hermit", "Death",
        "Hanged Man", "Justice", "Moon", "Magician", "Hierophant", "Justice", "Magician", "Emperor", "Star", "Devil",
        "Sun", "Devil", "Sun"
    ],
    [   # Row 4: Empress Arcana
        "Judgement", "Sun", "Temperance", "Empress", "Moon", "Death", "Justice", "Justice", "Magician", "Magician",
        "Star", "Hierophant", "Temperance", "Chariot", "Devil", "Priestess", "Hermit", "Chariot", "Temperance",
        "Priestess", "Strength", "Temperance"
    ],
    [   # Row 5: Emperor Arcana
        "Hermit", "Death", "Justice", "Fool", "Emperor", "Empress", "Justice", "Temperance", "Devil", "Priestess",
        "Lovers", "Hermit", "Empress", "Moon", "Sun", "Moon", "Star", "Death", "Magician", "Chariot", "Lovers",
        "Justice", "Hanged Man"
    ],
    [   # Row 6: Hierophant Arcana - Great Vegetables!
        "Tower", "Jester", "Empress", "Priestess", "Chariot", "Hierophant", "Death", "Sun", "Temperance", "Justice",
        "Priestess", "Sun", "Death", "Devil", "Magician", "Emperor", "Hanged Man", "Moon", "Empress", "Strength",
        "Chariot", "Magician", "Moon"
    ],
    [   # Row 7: Lovers Arcana
        "Devil", "Temperance", "Hanged Man", "Fool", "Devil", "Hanged Man", "Lovers", "Hierophant", "Priestess",
        "Magician", "Star", "Emperor", "Moon", "Star", "Hierophant", "Hierophant", "Star", "Hermit", "Hanged Man",
        "Devil", "Strength", "Sun", "Justice"
    ],
    [   # Row 8: Chariot Arcana
        "Lovers", "Emperor", "Magician", "Emperor", "Tower", "Judgement", "Hierophant", "Chariot", "Temperance",
        "Justice", "Devil", "Magician", "Death", "Hermit", "Magician", "Moon", "Hanged Man", "Hierophant", "Sun",
        "Strength", "Temperance", "Chariot", "Strength"
    ],
    [   # Row 9: Justice Arcana
        "Chariot", "Chariot", "Hermit", "Death", "Jester", "Magician", "Aeon", "Temperance", "Justice", "Strength",
        "Lovers", "Temperance", "Priestess", "Strength", "Hermit", "Magician", "Lovers", "Moon", "Strength",
        "Temperance", "Lovers", "Emperor", "Lovers"
    ],
    [   # Row 10: Hermit Arcana
        "Strength", "Empress", "Magician", "Fool", "Moon", "Lovers", "Hierophant", "Priestess", "Emperor", "Hermit",
        "Empress", "Hierophant", "Moon", "Sun", "Magician", "Justice", "Death", "Justice", "Empress", "Temperance",
        "Star", "Moon", "Magician"
    ],
    [   # Row 11: Fortune Arcana
        "Judgement", "Strength", "Aeon", "Strength", "Priestess", "Hanged Man", "Hanged Man", "Temperance", "Priestess",
        "Judgement", "Fortune", "Star", "Death", "Hermit", "Devil", "Emperor", "Chariot", "Star", "Lovers", "Priestess",
        "Hanged Man", "Devil", "Priestess"
    ],
    [   # Row 12: Strength Arcana
        "Empress", "Tower", "Empress", "Jester", "Hermit", "Moon", "Fool", "Aeon", "Priestess", "Justice", "Priestess",
        "Strength", "Hierophant", "Hanged Man", "Sun", "Hermit", "Hanged Man", "Emperor", "Justice", "Temperance",
        "Invalid", "Empress", "Chariot"
    ],
    [   # Row 13: Hanged Man Arcana
        "Star", "Fortune", "Chariot", "Sun", "Hierophant", "Star", "Justice", "Devil", "Star", "Strength", "Fool",
        "Star", "Hanged Man", "Priestess", "Death", "Justice", "Hermit", "Empress", "Priestess", "Devil", "Empress",
        "Priestess", "Death"
    ],
    [   # Row 14: Death Arcana
        "Star", "Fool", "Chariot", "Hierophant", "Strength", "Magician", "Hanged Man", "Devil", "Devil", "Magician",
        "Moon", "Empress", "Devil", "Death", "Chariot", "Star", "Lovers", "Lovers", "Priestess", "Empress", "Invalid",
        "Temperance", "Hanged Man"
    ],
    [   # Row 15: Temperance Arcana
        "Justice", "Sun", "Lovers", "Aeon", "Devil", "Emperor", "Fortune", "Moon", "Magician", "Devil", "Tower",
        "Emperor", "Justice", "Jester", "Temperance", "Hermit", "Star", "Hierophant", "Hanged Man", "Hermit", "Invalid",
        "Death", "Empress"
    ],
    [   # Row 16: Devil Arcana
        "Lovers", "Chariot", "Hermit", "Fool", "Death", "Moon", "Tower", "Emperor", "Priestess", "Death", "Tower",
        "Lovers", "Justice", "Lovers", "Justice", "Devil", "Emperor", "Emperor", "Empress", "Hierophant", "Invalid",
        "Chariot", "Magician"
    ],
    [   # Row 17: Tower Arcana
        "Fortune", "Emperor", "Moon", "Judgement", "Priestess", "Emperor", "Judgement", "Hierophant", "Chariot",
        "Jester", "Magician", "Devil", "Fortune", "Justice", "Judgement", "Star", "Tower", "Hanged Man", "Priestess",
        "Chariot", "Invalid", "Hermit", "Emperor"
    ],
    [   # Row 18: Star Arcana
        "Hermit", "Hierophant", "Empress", "Jester", "Sun", "Lovers", "Hierophant", "Aeon", "Sun", "Death", "Magician",
        "Devil", "Sun", "Fortune", "Hierophant", "Fortune", "Hermit", "Star", "Emperor", "Moon", "Strength", "Invalid",
        "Empress", "Chariot"
    ],
    [   # Row 19: Moon Arcana
        "Empress", "Sun", "Empress", "Moon", "Strength", "Aeon", "Hanged Man", "Fool", "Star", "Jester", "Strength",
        "Hierophant", "Magician", "Hanged Man", "Hanged Man", "Death", "Hanged Man", "Death", "Moon", "Strength",
        "Invalid", "Hermit", "Hierophant"
    ],
    [   # Row 20: Sun Arcana
        "Empress", "Fortune", "Aeon", "Lovers", "Devil", "Magician", "Jester", "Priestess", "Judgement", "Tower",
        "Chariot", "Tower", "Empress", "Empress", "Fortune", "Lovers", "Death", "Chariot", "Death", "Sun", "Invalid",
        "Lovers", "Priestess"
    ],
    [   # Row 21: Judgement Arcana
        "Temperance", "Sun", "Temperance", "Star", "Hanged Man", "Fool", "Emperor", "Tower", "Sun", "Temperance",
        "Fool", "Temperance", "Fool", "Strength", "Chariot", "Death", "Aeon", "Lovers", "Hermit", "Chariot",
        "Judgement", "Chariot", "Hanged Man"
    ],
    [   # Row 22: Jester Arcana
        "Priestess", "Star", "Moon", "Devil", "Chariot", "Fortune", "Tower", "Strength", "Hermit", "Aeon", "Emperor",
        "Magician", "Moon", "Fortune", "Priestess", "Aeon", "Judgement", "Death", "Hanged Man", "Lovers", "Death",
        "Jester", "Devil"
    ],
    [   # Row 23: Aeon Arcana
        "Jester", "Empress", "Fool", "Star", "Sun", "Sun", "Judgement", "Justice", "Temperance", "Moon", "Fool",
        "Hermit", "Jester", "Strength", "Judgement", "Lovers", "Fortune", "Tower", "Tower", "Hierophant", "Sun",
        "Judgement", "Aeon"
    ]
]
# That didn't totally destroy my sanity at all!
