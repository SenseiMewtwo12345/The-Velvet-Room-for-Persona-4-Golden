from tkinter import messagebox
from fusion_chart import *


def basic_double_fusion(arcana1, arcana2):
    """
    Performs a double fusion using the Persona 4 Golden fusion chart from https://i.imgur.com/mzlJptZ.jpeg

    :param arcana1: string - The Arcana of the first Persona in the fusion
    :param arcana2: string - The Arcana of the second Persona in the fusion

    :return: string - The Arcana of the result of the fusion
    """
    arcana_list = [arcanas.index(arcana1), arcanas.index(arcana2)]
    arcana_list.sort()
    # This restricts the coordinates in the list to pointing at the Double Fusion part of the chart.
    result = fusion_chart[arcana_list[0]][arcana_list[1]]
    # Sometimes, a fusion between two specific Arcanas can't be performed in game. We want to inform the user when
    # this happens.
    if result == "Invalid":
        messagebox.showerror(title="Error: Invalid fusion.", message=arcana1+" and "+arcana2+" cannot fuse.")
    else:
        return result


def basic_triple_fusion(arcana1, arcana2, arcana3):
    """
        Performs a triple fusion using the Persona 4 Golden fusion chart from https://i.imgur.com/mzlJptZ.jpeg

        :param arcana1: string - The Arcana of the first Persona in the fusion
        :param arcana2: string - The Arcana of the second Persona in the fusion
        :param arcana3: string - The Arcana of the third Persona in the fusion - Must always be the highest base level!

        :return: string - The Arcana of the result of the fusion
        """
    arcana_list = [arcanas.index(basic_double_fusion(arcana1, arcana2)), arcanas.index(arcana3)]
    arcana_list.sort(reverse=True)
    # This restricts the coordinates in the list to pointing
    # at the Triple Fusion part of the chart.
    return fusion_chart[arcana_list[0]][arcana_list[1]]
