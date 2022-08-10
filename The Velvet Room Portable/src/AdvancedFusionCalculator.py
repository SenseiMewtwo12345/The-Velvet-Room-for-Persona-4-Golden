from tkinter import messagebox
from PersonaSearch import *
import math


def special_fusion_checker(name_list):
    """
    Checks if a given list of names contains the fusion requirements for a Persona that requires a Special Fusion.

    :param name_list: List of strings
    :return: 2D List where each element contains a list with element 0 being a Persona object, and element 1 being the
            length of the list of ingredients for the special fusion, which can be checked by other functions, i.e.
            if a triple fusion is performed but the function finds a Special double fusion among the Personas being
            fused. I want to display the Special fusion and also the result of the triple fusion in that case.
            If no special fusions are found, this list will be empty. It may also contain more than one possible
            special fusion, especially if run in the Fusion Search or Constant Persona Search functions, which can
            contain 12-13 Personas.
    """
    successes = []
    for arcana in Personas:  # First, detect if the Personas entered are a valid Special Fusion
        for persona in arcana:
            if persona.special_fusion is not None:
                sp_fusion = persona.special_fusion
                sp_fusion_check = all(item in name_list for item in sp_fusion)
                if sp_fusion_check:
                    successes.append([persona, len(sp_fusion)])
    return successes


def persona_double_fusion(name1, name2):
    """
    Performs a double fusion using the Persona 4 Golden fusion chart from https://i.imgur.com/mzlJptZ.jpeg

    :param name1: string - Name of the first Persona in the fusion
    :param name2: string - Name of the second Persona in the fusion

    :return: Persona object - The result of the fusion
    """

    names = [name1, name2]

    check = special_fusion_checker(names)
    if len(check) != 0:     # Check if a special fusion was successfully found
        return check[0][0]  # Not going to inquire any further as this fusion is the only possible result.

    persona1 = persona_search(name1)    # Find Persona objects associated with names
    persona2 = persona_search(name2)    # Returns None if name is invalid

    # Check to make sure valid Persona names were entered
    if persona1 is None:
        messagebox.showerror(title="Error: Invalid Name", message="\nError: " + name1 + " is not a valid name for a "
                                   "Persona.\nMost likely, you mispelled it or didn't capitalize the name!")
        if persona2 is None:
            messagebox.showerror(title="Error: Invalid Name", message="\nError: " + name2 + " is also not a valid name "
                                       "for a Persona.\nMost likely, you mispelled it or didn't capitalize the name!")
        return None
    if persona2 is None:
        messagebox.showerror(title="Error: Invalid Name", message="\nError: " + name2 + " is not a valid name for a "
                             "Persona.\nMost likely, you mispelled it or didn't capitalize the name!")
        return None

    if persona1.arcana == persona2.arcana:
        same_arcana = arcanas.index(persona1.arcana)
        if persona1.base_lv > persona2.base_lv:
            higher_lv = persona1
            lower_lv = persona2
        elif persona2.base_lv > persona1.base_lv:
            higher_lv = persona2
            lower_lv = persona1
        else:
            messagebox.showerror(title="Error: Duplicate Personas",
                                 message="It's impossible to have two of the same Persona at once!")
            return None

        # Fusing the two lowest level Personas of the same Arcana is impossible, so we need to check for that.
        if Personas[same_arcana][1].special_fusion is None or Personas[same_arcana][1].name == higher_lv.name:
            if lower_lv.name == Personas[same_arcana][0].name:
                messagebox.showerror(title="Error: Same Arcana Levels Too Low",
                                     message="The levels of your Personas are too low to result in a valid fusion!")
                return None
        else:
            if lower_lv.name == Personas[same_arcana][0].name and higher_lv.name == Personas[same_arcana][2].name:
                messagebox.showerror(title="Error: Same Arcana Levels Too Low",
                                     message="You can't fuse the two lowest level Personas of the same Arcana!")
                return None

        reverse_personas = []
        for persona in Personas[same_arcana]:
            reverse_personas.append(persona)
        reverse_personas.reverse()  # We need to work backwards down this list until we find the correct Persona
        for persona in range(len(reverse_personas)):
            try_persona = reverse_personas[persona].base_lv
            # Can't return one of the Personas involved in the fusion.
            # We don't want to return a Persona that requires a Special Fusion either.
            if higher_lv.base_lv > try_persona != lower_lv.base_lv and reverse_personas[persona].special_fusion is None:
                return reverse_personas[persona]

    try:    # If the user enters Izanagi-no-Okami, we need to return an error.
        arcana_list = [arcanas.index(persona1.arcana), arcanas.index(persona2.arcana)]
        arcana_list.sort()  # This restricts the coordinates to Double Fusion
        arcana_result = fusion_chart[arcana_list[0]][arcana_list[1]]

        if arcana_result == "Invalid":  # Sometimes, two arcanas cannot fuse, and we need to return an error.
            messagebox.showerror(title="Error: Invalid Fusion",
                                 message=persona1.arcana + " and " + persona2.arcana + " cannot fuse.")
        else:
            arcana_index = arcanas.index(arcana_result)
            level_calc = ((persona1.base_lv + persona2.base_lv) / 2.) + 1
            level_calc = math.floor(level_calc)

            for persona in Personas[arcana_index]:
                if persona.base_lv >= level_calc and persona.special_fusion is None:  # Skip if special fusion.
                    return persona
    except IndexError:
        messagebox.showerror(title="Error: Is Kami!", message="Izanagi-no-Okami cannot be used in fusion!")


def persona_double_fusion_noerr(name1, name2):
    """
    Same as persona_double_fusion but doesn't show error messages.

    :param name1: string - Name of the first Persona in the fusion
    :param name2: string - Name of the second Persona in the fusion

    :return: Persona object - The result of the fusion
    """

    names = [name1, name2]

    check = special_fusion_checker(names)
    if len(check) != 0:     # Check if a special fusion was successfully found
        return check[0][0]  # Not going to inquire any further as this fusion is the only possible result.

    persona1 = persona_search(name1)    # Find Persona objects associated with names
    persona2 = persona_search(name2)    # Returns None if name is invalid

    # Check to make sure valid Persona names were entered
    if persona1 is None or persona2 is None:
        return None

    if persona1.arcana == persona2.arcana:
        same_arcana = arcanas.index(persona1.arcana)
        if persona1.base_lv > persona2.base_lv:
            higher_lv = persona1
            lower_lv = persona2
        elif persona2.base_lv > persona1.base_lv:
            higher_lv = persona2
            lower_lv = persona1
        else:
            return None

        # Fusing the two lowest level Personas of the same Arcana is impossible, so we need to check for that.
        if Personas[same_arcana][1].special_fusion is None or Personas[same_arcana][1].name == higher_lv.name:
            if lower_lv.name == Personas[same_arcana][0].name:
                return None
        else:
            if lower_lv.name == Personas[same_arcana][0].name and higher_lv.name == Personas[same_arcana][2].name:
                return None

        reverse_personas = []
        for persona in Personas[same_arcana]:
            reverse_personas.append(persona)
        reverse_personas.reverse()  # We need to work backwards down this list until we find the correct Persona
        for persona in range(len(reverse_personas)):
            try_persona = reverse_personas[persona].base_lv
            # Can't return one of the Personas involved in the fusion.
            # We don't want to return a Persona that requires a Special Fusion either.
            if higher_lv.base_lv > try_persona != lower_lv.base_lv and reverse_personas[persona].special_fusion is None:
                return reverse_personas[persona]

    try:    # If the user enters Izanagi-no-Okami, we need to return an error.
        arcana_list = [arcanas.index(persona1.arcana), arcanas.index(persona2.arcana)]
        arcana_list.sort()  # This restricts the coordinates to Double Fusion
        arcana_result = fusion_chart[arcana_list[0]][arcana_list[1]]

        if arcana_result == "Invalid":  # Sometimes, two arcanas cannot fuse, and we need to return an error.
            return None
        else:
            arcana_index = arcanas.index(arcana_result)
            level_calc = ((persona1.base_lv + persona2.base_lv) / 2.) + 1
            level_calc = math.floor(level_calc)

            for persona in Personas[arcana_index]:
                if persona.base_lv >= level_calc and persona.special_fusion is None:  # Skip if special fusion.
                    return persona
    except IndexError:
        return None


def persona_triple_fusion(name1, name2, name3):
    """

    :param name1: string - Name of the first Persona in the fusion
    :param name2: string - Name of the second Persona in the fusion
    :param name3: string - Name of the third Persona in the fusion
    :return: List of Persona objects
    """
    results = []  # Placeholder for a list of results. We will append any fusions we find to this list.
    special = False
    names = [name1, name2, name3]

    # Let's check and make sure that the user entered three unique Persona names.
    if len(set(names)) < 3:
        messagebox.showerror(title="Error: Duplicate Personas",
                             message="It's impossible to have two of the same Persona at once!")
        return None

    check = special_fusion_checker(names)
    if len(check) != 0:
        for i in check:
            results.append(i[0])     # We want to notify the user that there was a possible special double fusion, but
            if i[1] > 2:             # still return a triple fusion result.
                special = True      # However, in the event of a special triple fusion,
    if special:                     # do not perform the rest of this function's tasks.
        return results

    persona_list = []
    for name in names:
        persona_list.append(persona_search(name))   # Get the Personas associated with the names

    # Now we need to make sure the names entered were valid.
    error_message = "Error: One or more invalid names for a Persona! "
    error = False
    for i in range(len(persona_list)):
        if persona_list[i] is None:
            error = True
            error_message += names[i] + " | "
    if error:
        messagebox.showerror(title="Error: Invalid names",
                             message=error_message + "are not valid names.\n"
                                                     "You probably mispelled or didn't capitalize them!")
        return None

    # Now we need to assign them to variables by their level.
    highest_level = []
    for persona in persona_list:
        if persona.base_lv == max([persona_list[0].base_lv, persona_list[1].base_lv, persona_list[2].base_lv]):
            highest_level.append(persona)
    if len(highest_level) > 1:  # If there is a tie in levels, we need to resolve it.
        tied_arcanas = []
        for persona in highest_level:  # Get the arcanas of the tied Personas
            tied_arcanas.append(arcanas.index(persona.arcana))
        tiebreaker_arcana = min(tied_arcanas)  # The Persona with the lowest Arcana wins the tie.
        for persona in highest_level:
            if arcanas.index(persona.arcana) == tiebreaker_arcana:
                persona3 = persona
    else:
        persona3 = highest_level[0]

    lower_level = []
    # And now assign the other two to persona1 and persona2:
    for persona in persona_list:
        if persona.name != persona3.name:
            lower_level.append(persona)
    persona1, persona2 = lower_level

    # First, perform a double fusion using the arcanas of the two lower level Personas.

    try:    # If the user enters Izanagi-no-Okami, we need to return an error.
        arcana_list = [arcanas.index(persona1.arcana), arcanas.index(persona2.arcana)]
        arcana_list.sort()  # This restricts the coordinates to Double Fusion
        arcana4 = fusion_chart[arcana_list[0]][arcana_list[1]]

        if arcana4 == "Invalid":  # Sometimes, two arcanas cannot fuse, and we need to return an error.
            messagebox.showerror(title="Error: Invalid Fusion",
                                 message=persona1.arcana + " and " + persona2.arcana +
                                 " cannot fuse with a Persona higher level than both of them.")
            return None

    except ValueError:
        messagebox.showerror(title="Error: Is Kami!", message="Izanagi-no-Okami cannot be used in fusion!")
        return None

    # And now we fuse Persona3 with the arcana result from the previous fusion, only this time we use the Triple Fusion
    # side of the fusion chart.

    try:    # If the user enters Izanagi-no-Okami, we need to return an error.
        arcana_list = [arcanas.index(persona3.arcana), arcanas.index(arcana4)]
        arcana_list.sort(reverse=True)  # This restricts the coordinates to Triple Fusion
        arcana_result = fusion_chart[arcana_list[0]][arcana_list[1]]

        # This fusion cannot be invalid, so we'll skip that step.
        arcana_index = arcanas.index(arcana_result)
        level_calc = ((persona1.base_lv + persona2.base_lv + persona3.base_lv) / 3.) + 5
        level_calc = math.floor(level_calc)

        for persona in Personas[arcana_index]:
            if persona.base_lv >= level_calc and persona.special_fusion is None:   # Skip if special fusion.
                results.append(persona)
                return results
    except IndexError:
        messagebox.showerror(title="Error: Is Kami!", message="Izanagi-no-Okami cannot be used in fusion!")


def persona_triple_fusion_noerr(name1, name2, name3):
    """

    :param name1: string - Name of the first Persona in the fusion
    :param name2: string - Name of the second Persona in the fusion
    :param name3: string - Name of the third Persona in the fusion
    :return: List of Persona objects
    """
    results = []  # Placeholder for a list of results. We will append any fusions we find to this list.
    special = False
    names = [name1, name2, name3]

    # Let's check and make sure that the user entered three unique Persona names.
    if len(set(names)) < 3:
        return None

    check = special_fusion_checker(names)
    if len(check) != 0:
        for i in check:
            results.append(i[0])     # We want to notify the user that there was a possible special double fusion, but
            if i[1] > 2:             # still return a triple fusion result.
                special = True      # However, in the event of a special triple fusion,
    if special:                     # do not perform the rest of this function's tasks.
        return results

    persona_list = []
    for name in names:
        persona_list.append(persona_search(name))   # Get the Personas associated with the names

    # Now we need to assign them to variables by their level.
    highest_level = []
    for persona in persona_list:
        if persona.base_lv == max([persona_list[0].base_lv, persona_list[1].base_lv, persona_list[2].base_lv]):
            highest_level.append(persona)
    if len(highest_level) > 1:  # If there is a tie in levels, we need to resolve it.
        tied_arcanas = []
        for persona in highest_level:  # Get the arcanas of the tied Personas
            tied_arcanas.append(arcanas.index(persona.arcana))
        tiebreaker_arcana = min(tied_arcanas)  # The Persona with the lowest Arcana wins the tie.
        for persona in highest_level:
            if arcanas.index(persona.arcana) == tiebreaker_arcana:
                persona3 = persona
    else:
        persona3 = highest_level[0]

    lower_level = []
    # And now assign the other two to persona1 and persona2:
    for persona in persona_list:
        if persona.name != persona3.name:
            lower_level.append(persona)
    persona1, persona2 = lower_level

    # First, perform a double fusion using the arcanas of the two lower level Personas.

    try:    # If the user enters Izanagi-no-Okami, we need to return an error.
        arcana_list = [arcanas.index(persona1.arcana), arcanas.index(persona2.arcana)]
        arcana_list.sort()  # This restricts the coordinates to Double Fusion
        arcana4 = fusion_chart[arcana_list[0]][arcana_list[1]]

        if arcana4 == "Invalid":  # Sometimes, two arcanas cannot fuse, and we need to return an error.
            return None

    except ValueError:
        return None

    # And now we fuse Persona3 with the arcana result from the previous fusion, only this time we use the Triple Fusion
    # side of the fusion chart.

    try:    # If the user enters Izanagi-no-Okami, we need to return an error.
        arcana_list = [arcanas.index(persona3.arcana), arcanas.index(arcana4)]
        arcana_list.sort(reverse=True)  # This restricts the coordinates to Triple Fusion
        arcana_result = fusion_chart[arcana_list[0]][arcana_list[1]]

        # This fusion cannot be invalid, so we'll skip that step.
        arcana_index = arcanas.index(arcana_result)
        level_calc = ((persona1.base_lv + persona2.base_lv + persona3.base_lv) / 3.) + 5
        level_calc = math.floor(level_calc)

        for persona in Personas[arcana_index]:
            if persona.base_lv >= level_calc and persona.special_fusion is None:   # Skip if special fusion.
                results.append(persona)
                return results
    except IndexError:
        return None
