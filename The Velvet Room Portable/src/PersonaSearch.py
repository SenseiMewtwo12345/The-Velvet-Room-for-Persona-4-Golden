from P4G_Personas import *
from fusion_chart import *


def persona_search(name):
    """
    Locates a persona in the Personas array by name

    :param name: String - Name of desired Persona
    :return: Persona object - The desired Persona - None if no Persona is found
    """
    for arcana in Personas:
        for persona in arcana:
            if persona.name == name:
                return persona


def compendium(arcana=None):
    """
    Compiles a compendium of the names, arcanas, and levels of every Persona and returns it as a string.

    :param arcana: string - This can be used to restrict what Arcana of Personas will appear. Optional.
    :return: string - The compendium of Personas, ready to be printed.
    """
    compendium_msg = ""
    if arcana in arcanas:
        compendium_msg += "\n\n" + arcana + "\n"
        for persona in Personas[arcanas.index(arcana)]:
            compendium_msg += persona.name + " (Lv. " + str(persona.base_lv) + " " + persona.arcana + ")\n"
        return compendium_msg
    else:
        for arcana in range(len(Personas)):
            compendium_msg += "\n\n" + arcanas[arcana] + "\n"
            for persona in Personas[arcana]:
                compendium_msg += persona.name + " (Lv. " + str(persona.base_lv) + " " + persona.arcana + ")\n"
        return compendium_msg
