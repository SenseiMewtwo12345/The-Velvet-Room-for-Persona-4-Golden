from AdvancedFusionCalculator import *


def sort_by_arcana(fusion_list):
    return arcanas.index(fusion_list[1].arcana)


def sort_by_base_lv(fusion_list):
    return fusion_list[1].base_lv


def fusion_sorter(fusion_formulas, fusion_results, sort_type="Arcana"):
    fusion_list = []
    for i in range(len(fusion_formulas)):
        fusion_list.append([fusion_formulas[i], fusion_results[i]])

    if sort_type == "Arcana":
        fusion_list.sort(key=sort_by_arcana)

    if sort_type == "Level":
        fusion_list.sort(reverse=True, key=sort_by_base_lv)

    return fusion_list


def restricted_fusion_search(name1, names, player_level=99, sort_type="Arcana"):
    """
    Find out all the possible fusions you can perform with one Persona and all the rest in your
    roster. For example, if you wanted to find out all the possible ways to fuse Kaiwan with your other
    Personas.

    :param name1: string - A name of the Persona to be held constant
    :param names: List of strings - All the other Personas in the roster
    :param player_level: Int - The level of the main character. 99 by default.
    :param sort_type: Denotes how you want the results to be sorted. Valid values are "Arcana" and "Level".
                "Arcana" by default.
    :return: string - All the possible results, or None if an error occurs
    """

    # First, let's check to make sure all the Personas given are unique and that Kami isn't one of them.
    if name1 in names or len(set(names)) < len(names):
        messagebox.showerror(title="Error: Duplicate Personas",
                             message="It's impossible to have two of the same Persona at once!")
        return None
    if name1 == "Izanagi-no-Okami" or "Izanagi-no-Okami" in names:
        messagebox.showerror(title="Error: Is Kami!", message="Izanagi-no-Okami cannot be used in fusion!")
        return None

    # Now, let's make sure all the names are valid!
    error_message = "Error: One or more invalid names for a Persona!\n"
    error = False
    if persona_search(name1) is None:
        error = True
        error_message += name1 + " | "
    for i in range(len(names)):
        if persona_search(names[i]) is None:
            error = True
            error_message += names[i] + " | "
    if error:
        messagebox.showerror(title="Error: Invalid names",
                             message=error_message + "are not valid names.\n"
                                                     "You probably mispelled or didn't capitalize them!")
        return None

    special_formulas = []
    special_results = []

    # Now, let's check for Special Fusions. I want to inform the user of them regardless if the constant Persona is
    # involved or not.
    sp_check_names = [name1]
    for name in names:
        sp_check_names.append(name)
    check = special_fusion_checker(sp_check_names)
    message = ""
    if len(check) > 0:
        message += "\nOne or more possible Special Fusions were found!\n\n"

        for fusion in check:
            if fusion[0].base_lv <= player_level:
                formula = ""
                formula += fusion[0].name + " (Lv. " + str(fusion[0].base_lv) + " " + fusion[0].arcana + ") = "
                for persona in range(len(fusion[0].special_fusion)):

                    if persona < len(fusion[0].special_fusion) - 1:
                        formula += fusion[0].special_fusion[persona] + " + "
                    else:
                        formula += fusion[0].special_fusion[persona] + "\n"

                special_formulas.append(formula)
                special_results.append(fusion[0])

        if len(special_formulas) > 0:
            special_sorted_list = fusion_sorter(special_formulas, special_results, sort_type=sort_type)

            for i in special_sorted_list:
                message += i[0]
        else:
            message += "But the the main character's level isn't high enough to perform them!"

        message += "\n\n"

    results = []
    formulas = []

    # Now, let's check all the possible double fusions that can be performed with name1
    for name in names:
        try:
            result = persona_double_fusion_noerr(name1, name)
            if result.base_lv <= player_level:
                formula = result.name + " (Lv. " + str(result.base_lv) + " " + result.arcana + ") = " + name1 + " + " \
                          + name + "\n"
                results.append(result)
                formulas.append(formula)
        except AttributeError:
            do_nothing = True

    # Now, let's check all the possible triple fusions that can be performed with name1

    # First, we need to make sure that we aren't carrying out any duplicate fusions.

    triple_fusions_list = []  # Let's do that by creating a list of lists containing 3 Persona names

    for i in range(len(names)):
        for j in range(len(names)):
            if i != j:  # We can't have two of the same Persona in each list.
                triple_fusion = [name1, names[i], names[j]]
                triple_fusion.sort()  # Ensures that elements containing the same set of Personas are duplicates.
                triple_fusion_tuple = (triple_fusion[0], triple_fusion[1], triple_fusion[2])
                triple_fusions_list.append(triple_fusion_tuple)
    triple_fusions_set = set(triple_fusions_list)  # This will remove any non-unique fusions.

    for fusion in triple_fusions_set:
        try:
            result = persona_triple_fusion_noerr(fusion[0], fusion[1], fusion[2])
            if len(result) > 1:
                if result[1].base_lv <= player_level:
                    results.append(result[1])
                    formula = result[1].name + " (Lv. " + str(result[1].base_lv) + " " + result[1].arcana + ") = " + \
                              fusion[0] + " + " + fusion[1] + " + " + fusion[2] + "\n"
                    formulas.append(formula)
            else:
                if result[0].base_lv <= player_level:
                    results.append(result[0])
                    formula = result[0].name + " (Lv. " + str(result[0].base_lv) + " " + result[0].arcana + ") = " + \
                              fusion[0] + " + " + fusion[1] + " + " + fusion[2] + "\n"
                    formulas.append(formula)
        except TypeError:
            do_nothing = True

    sorted_list = fusion_sorter(formulas, results, sort_type=sort_type)

    for i in sorted_list:
        message += i[0]

    return message


def fusion_search(names, player_level=99, sort_type="Arcana"):
    """
    Determine every possible fusion result from a list of Persona names.

    :param names: List of strings - All the Personas the player currently owns
    :param player_level: Int - The main character's current level. 99 by default.
    :param sort_type: tring - Determines the sort method. Valid inputs are "Arcana" and "Level". "Arcana" by default.
    :return: string - This string contains a list of all the possible fusions, sorted by the sort method. None, if
                an error occurs or by some miracle there are no results.
    """
    # First, let's check to make sure all the Personas given are unique and that Kami isn't one of them.
    if len(set(names)) < len(names):
        messagebox.showerror(title="Error: Duplicate Personas",
                             message="It's impossible to have two of the same Persona at once!")
        return None
    if "Izanagi-no-Okami" in names:
        messagebox.showerror(title="Error: Is Kami!", message="Izanagi-no-Okami cannot be used in fusion!")
        return None

    # Now, let's make sure all the names are valid!
    error_message = "Error: One or more invalid names for a Persona!\n"
    error = False
    for i in range(len(names)):
        if persona_search(names[i]) is None:
            error = True
            error_message += names[i] + " | "
    if error:
        messagebox.showerror(title="Error: Invalid names",
                             message=error_message + "are not valid names.\n"
                                                     "You probably mispelled or didn't capitalize them!")
        return None

    special_formulas = []
    special_results = []

    # Now, let's check for Special Fusions.
    sp_check_names = []
    for name in names:
        sp_check_names.append(name)
    check = special_fusion_checker(sp_check_names)
    message = ""
    if len(check) > 0:
        message += "\nOne or more possible Special Fusions were found!\n\n"

        for fusion in check:
            if fusion[0].base_lv <= player_level:
                formula = ""
                formula += fusion[0].name + " (Lv. " + str(fusion[0].base_lv) + " " + \
                           fusion[0].arcana + ") = "
                for persona in range(len(fusion[0].special_fusion)):

                    if persona < len(fusion[0].special_fusion) - 1:
                        formula += fusion[0].special_fusion[persona] + " + "
                    else:
                        formula += fusion[0].special_fusion[persona] + "\n"

                special_formulas.append(formula)
                special_results.append(fusion[0])

        if len(special_formulas) > 0:
            special_sorted_list = fusion_sorter(special_formulas, special_results, sort_type=sort_type)

            for i in special_sorted_list:
                message += i[0]
        else:
            message += "But the the main character's level isn't high enough to perform them!"

        message += "\n\n"

    formulas = []
    results = []

    double_fusions_list = []
    # Now, let's check all the possible double fusions that can be performed

    # First, we need to make sure that we aren't carrying out any duplicate fusions.
    for i in range(len(names)):
        for j in range(len(names)):
            if i != j:  # We can't have two of the same Persona in each list.
                double_fusion = [names[i], names[j]]
                double_fusion.sort()    # Ensures that elements containing the same set of Personas are duplicates.
                double_fusion_tuple = (double_fusion[0], double_fusion[1])
                double_fusions_list.append(double_fusion_tuple)
    double_fusions_set = set(double_fusions_list)   # This will remove any non-unique fusions.

    for fusion in double_fusions_set:
        try:
            result = persona_double_fusion_noerr(fusion[0], fusion[1])
            if result.base_lv <= player_level:
                formula = result.name + " (Lv. " + str(result.base_lv) + " " + result.arcana + ") = " + fusion[0] \
                          + " + " + fusion[1] + "\n"
                results.append(result)
                formulas.append(formula)
        except AttributeError:
            do_nothing = True

    # Now, let's check all the possible triple fusions that can be performed

    # First, we need to make sure that we aren't carrying out any duplicate fusions.

    triple_fusions_list = []  # Let's do that by creating a list of lists containing 3 Persona names

    for i in range(len(names)):
        for j in range(len(names)):
            for k in range(len(names)):
                if i != j and i != k and j != k:  # We can't have two of the same Persona in each list.
                    triple_fusion = [names[i], names[j], names[k]]
                    triple_fusion.sort()  # Ensures that elements containing the same set of Personas are duplicates.
                    triple_fusion_tuple = (triple_fusion[0], triple_fusion[1], triple_fusion[2])
                    triple_fusions_list.append(triple_fusion_tuple)
    triple_fusions_set = set(triple_fusions_list)  # This will remove any non-unique fusions.

    for fusion in triple_fusions_set:
        try:
            result = persona_triple_fusion_noerr(fusion[0], fusion[1], fusion[2])
            if len(result) > 1:
                if result[1].base_lv <= player_level:
                    results.append(result[1])
                    formula = result[1].name + " (Lv. " + str(result[1].base_lv) + " " + result[1].arcana + ") = " \
                              + fusion[0] + " + " + fusion[1] + " + " + fusion[2] + "\n"
                    formulas.append(formula)
            else:
                if result[0].base_lv <= player_level:
                    results.append(result[0])
                    formula = result[0].name + " (Lv. " + str(result[0].base_lv) + " " + result[0].arcana + ") = " + \
                              fusion[0] + " + " + fusion[1] + " + " + fusion[2] + "\n"
                    formulas.append(formula)
        except TypeError:
            do_nothing = True

    sorted_list = fusion_sorter(formulas, results, sort_type=sort_type)

    for i in sorted_list:
        message += i[0]

    return message
