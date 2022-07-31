from tkinter import *
from BasicFusionCalculator import *
from FusionSearch import *
# ================== Colors ==========================
bg1 = "purple4"
bg2 = "grey20"
bg3 = "black"
fg1 = "gold"
fg2 = "white"
lbl_font = ("Arial", 14)
bt_font = ("Arial", 12)


def checkmax(bar, var):
    # Called after the intvar is changed
    def _check():
        # print(bar.numpicks, var.get())
        if var.get():   # checked
            if bar.numpicks < bar.maxpicks:
                bar.numpicks += 1
            else:
                var.set(0)
        else:           # unchecked
            bar.numpicks -= 1
    return _check


class ArcanaMenu(Frame):

    def __init__(self, parent, picks=arcanas, maxpicks=1):
        Frame.__init__(self, parent, bg=bg1)
        self.maxpicks = maxpicks
        self.numpicks = 0
        self.vars = []
        r = 0
        col = 0
        for i in range(len(picks)):
            var = IntVar()
            chk = Checkbutton(self, text=picks[i], variable=var, command=checkmax(self, var), bg=bg2, fg=fg2,
                              activebackground=bg2, activeforeground=fg2, font=bt_font, indicatoron=False,
                              selectcolor="black")
            chk.grid(row=r, column=col, sticky="nsew")
            col += 1
            self.vars.append(var)
            if col > 3:
                col = 0
                r += 1

    def selection(self):
        state = list(map((lambda var: var.get()), self.vars))
        selection = []
        for i in range(len(state)):
            if state[i] == 1:
                selection.append(arcanas[i])
        return selection


class PersonaEntry(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg=bg1)
        self.personas = []
        r = 0
        col = 0
        for i in range(12):
            entry = Entry(self, bg=bg3, fg=fg2, font=bt_font)
            entry.grid(row=r, column=col, sticky="nsew")
            col += 1
            self.personas.append(entry)
            if col > 5:
                col = 0
                r += 1

    def get_names(self):
        names = []
        for name in self.personas:
            if len(name.get()) > 0:
                names.append(name.get())
        return names


class VelvetRoomPortable(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)

        self.configure(bg=bg1)
        self.geometry("1280x720")
        self.title("The Velvet Room Portable")

        icon = PhotoImage(file="igor.png")
        self.iconphoto(True, icon)

        container = Frame(self, bg=bg1)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, ADFC, ATFC, PDFC, PTFC, RestrictedFusionSearch, FusionSearch, PersonaSearch, PersonaCompendium):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, controller):

        frame = self.frames[controller]
        frame.tkraise()


class Home(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)
        af_label = Label(self, text="Arcana Fusion Calculators", font=lbl_font, bg=bg1, fg=fg1)
        af_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        adf_bt = Button(self, text="Double Fusion", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(ADFC))
        adf_bt.grid(row=1, column=0, sticky="ew")

        atf_bt = Button(self, text="Triple Fusion", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(ATFC))
        atf_bt.grid(row=1, column=1, sticky="ew")

        pf_label = Label(self, text="Persona Fusion Calculators", font=lbl_font, bg=bg1, fg=fg1)
        pf_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        pdf_bt = Button(self, text="Double Fusion", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(PDFC))
        pdf_bt.grid(row=3, column=0, sticky="ew")

        ptf_bt = Button(self, text="Triple Fusion", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(PTFC))
        ptf_bt.grid(row=3, column=1, sticky="ew")

        fs_label = Label(self, text="Fusion Search", font=lbl_font, bg=bg1, fg=fg1)
        fs_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        fs_bt = Button(self, text="Full", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(FusionSearch))
        fs_bt.grid(row=5, column=0, sticky="ew")

        rfs_bt = Button(self, text="Restricted", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(RestrictedFusionSearch))
        rfs_bt.grid(row=5, column=1, sticky="ew")

        ps_label = Label(self, text="Persona Search", font=lbl_font, bg=bg1, fg=fg1)
        ps_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        ps_bt = Button(self, text="Get a Persona's Info!", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaSearch))
        ps_bt.grid(row=7, column=0, columnspan=2, sticky="ew")

        pc_bt = Button(self, text="Persona Compendium", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaCompendium))
        pc_bt.grid(row=8, column=0, columnspan=2, sticky="ew")


class ADFC(Frame):  # Arcana Double Fusion Calculator

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)
        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=2, sticky="ew")

        tf_bt = Button(self, text="To Triple Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(ATFC))
        tf_bt.grid(row=0, column=2, columnspan=2, sticky="ew")

        header = Label(self, text="Select Arcanas", bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=1, column=0, columnspan=4)

        arcana_container = Frame(self, bg=bg1)
        arcana_container.grid(row=2, column=0, columnspan=4)

        instructions = "Select two Arcanas to fuse them,\nOr select one Arcana to fuse two of the same.\n" \
                       "Click an Arcana again to deselect it!"
        instructions_lbl = Label(self, text=instructions, bg=bg1, fg=fg1, font=lbl_font)
        instructions_lbl.grid(row=2, column=5, columnspan=4)

        df_menu = ArcanaMenu(arcana_container, maxpicks=2)
        df_menu.grid(row=0, column=0, columnspan=4)

        def submit():
            if len(df_menu.selection()) == 1:
                selection = [df_menu.selection()[0], df_menu.selection()[0]]
            else:
                selection = df_menu.selection()

            try:
                result.configure(text="Result = " + basic_double_fusion(selection[0], selection[1]))
            except TypeError:
                result.configure(text="Fusion failed")

        df_submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                           activeforeground=fg2, font=bt_font,
                           command=submit)
        df_submit.grid(row=3, column=0, columnspan=4)

        result = Label(self, bg=bg1, fg=fg1, font=lbl_font)
        result.grid(row=4, column=0, columnspan=4)


class ATFC(Frame):  # Arcana Triple Fusion Calculator

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)
        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=2, sticky="ew")

        df_bt = Button(self, text="To Double Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(ADFC))
        df_bt.grid(row=0, column=2, columnspan=2, sticky="ew")

        header = Label(self, text="Select highest level Arcana", bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=1, column=0, columnspan=4)

        arcana_container1 = Frame(self, bg=bg1)
        arcana_container1.grid(row=2, column=0, columnspan=4)

        instructions = "Select the Arcana of the highest level Persona first.\nThen select the other two Arcanas,\n" \
                       "or one if the lower level Personas are the same Arcana. \n" \
                       "Click an Arcana again to deselect it!"
        instructions_lbl = Label(self, text=instructions, bg=bg1, fg=fg1, font=lbl_font)
        instructions_lbl.grid(row=2, column=5, columnspan=4)

        tf_menu = ArcanaMenu(arcana_container1, maxpicks=1)
        tf_menu.grid(row=0, column=0, columnspan=4)

        df_header = Label(self, text="Select Arcanas", bg=bg1, fg=fg1, font=lbl_font)
        df_header.grid(row=3, column=0, columnspan=4)

        arcana_container = Frame(self, bg=bg1)
        arcana_container.grid(row=4, column=0, columnspan=4)

        df_menu = ArcanaMenu(arcana_container, maxpicks=2)
        df_menu.grid(row=0, column=0, columnspan=4)

        def submit():
            selection1 = tf_menu.selection()[0]

            if len(df_menu.selection()) == 1:
                selection2 = [df_menu.selection()[0], df_menu.selection()[0]]
            else:
                selection2 = df_menu.selection()

            try:
                result.configure(text="Result = " + basic_triple_fusion(selection2[0], selection2[1], selection1))
            except TypeError:
                result.configure(text="Fusion failed")

        tf_submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                           activeforeground=fg2, font=bt_font,
                           command=submit)
        tf_submit.grid(row=5, column=0, columnspan=4)

        result = Label(self, bg=bg1, fg=fg1, font=lbl_font)
        result.grid(row=6, column=0, columnspan=4)


class PDFC(Frame):  # Persona Double Fusion Calculator

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)
        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=3, sticky="ew")

        tf_bt = Button(self, text="To Triple Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PTFC))
        tf_bt.grid(row=0, column=3, columnspan=3, sticky="ew")

        header = Label(self, text="Enter the names of the Personas you wish to fuse: Make sure to capitalize "
                                  "and spell correctly!", bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=1, column=0, columnspan=6)

        persona1 = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona1.grid(row=2, column=0, columnspan=3, sticky="ew", padx=50)

        persona2 = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona2.grid(row=2, column=3, columnspan=3, sticky="ew", padx=50)

        def submit():
            try:
                results = persona_double_fusion(persona1.get(), persona2.get()).info()
                if results is not None:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, results)
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
                else:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, "Error")
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
            except AttributeError:
                show_results.configure(state=NORMAL)
                show_results.delete("1.0", END)
                show_results.insert(END, "Error")
                show_results.configure(state=DISABLED)
                v.config(command=show_results.yview)

        submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                        activeforeground=fg2, font=bt_font,
                        command=submit)
        submit.grid(row=3, column=0, columnspan=6)

        results_frame = Frame(self, width=300, height=400, bg=bg3)
        results_frame.grid(row=4, column=0, columnspan=6)

        v = Scrollbar(results_frame, orient="vertical")
        v.pack(side=RIGHT, fill="y")

        show_results = Text(results_frame, bg=bg3, fg=fg1, font=lbl_font, width=110, height=20, state=DISABLED,
                            yscrollcommand=v.set)
        v.config(command=show_results.yview)
        show_results.pack()

        ps_bt = Button(self, text="Get a Persona's Info!", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaSearch))
        ps_bt.grid(row=5, column=0, columnspan=6)


class PTFC(Frame):  # Persona Double Fusion Calculator

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)

        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=2, sticky="ew")

        df_bt = Button(self, text="To Double Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PDFC))
        df_bt.grid(row=0, column=2, columnspan=2, sticky="ew")

        header = Label(self, text="Enter the names of the Personas you wish to fuse:", bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=1, column=0, columnspan=4)

        persona1 = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona1.grid(row=2, column=0, columnspan=2, sticky="ew", padx=0)

        persona2 = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona2.grid(row=2, column=2, columnspan=2, sticky="ew", padx=0)

        persona3 = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona3.grid(row=2, column=4, columnspan=2, sticky="ew", padx=0)

        def submit():
            try:
                results = persona_triple_fusion(persona1.get(), persona2.get(), persona3.get())
                msg = ""
                if len(results) > 1:
                    msg += "\nA Special Double Fusion was found among the Personas you entered!\n"
                    for persona in results:
                        msg += persona.info() + "\n\n"
                    if msg is not None:
                        show_results.configure(state=NORMAL)
                        show_results.delete("1.0", END)
                        show_results.insert(END, msg)
                        show_results.configure(state=DISABLED)
                        v.config(command=show_results.yview)
                else:
                    msg += results[0].info() + "\n\n"
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, msg)
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
            except TypeError:
                show_results.configure(state=NORMAL)
                show_results.delete("1.0", END)
                show_results.insert(END, "Error")
                show_results.configure(state=DISABLED)
                v.config(command=show_results.yview)

        submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                        activeforeground=fg2, font=bt_font,
                        command=submit)
        submit.grid(row=3, column=0, columnspan=6)

        results_frame = Frame(self, width=300, height=400, bg=bg3)
        results_frame.grid(row=4, column=0, columnspan=6)

        v = Scrollbar(results_frame, orient="vertical")
        v.pack(side=RIGHT, fill="y")

        show_results = Text(results_frame, bg=bg3, fg=fg1, font=lbl_font, width=110, height=20, state=DISABLED,
                            yscrollcommand=v.set)
        v.config(command=show_results.yview)
        show_results.pack()

        ps_bt = Button(self, text="Get a Persona's Info!", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaSearch))
        ps_bt.grid(row=5, column=0, columnspan=6)


class RestrictedFusionSearch(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)

        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=3, sticky="ew")

        fs_bt = Button(self, text="To Full Fusion Search", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(FusionSearch))
        fs_bt.grid(row=0, column=3, columnspan=3, sticky="ew")

        pl_lbl = Label(self, text="Player Level:", bg=bg1, fg=fg1, font=lbl_font)
        pl_lbl.grid(row=1, column=1, columnspan=1)

        player_level = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        player_level.insert(END, "99")
        player_level.grid(row=1, column=2, columnspan=1)

        sort_lbl = Label(self, text="Sort by:", bg=bg1, fg=fg1, font=lbl_font)
        sort_lbl.grid(row=1, column=3, columnspan=1)

        sort_option = StringVar()
        arcana = Radiobutton(self, text="Arcana", bg=bg2, fg=fg2, activebackground=bg2, activeforeground=fg2,
                             font=bt_font, indicatoron=True, selectcolor="black", variable=sort_option, value="Arcana")
        arcana.grid(row=1, column=4, columnspan=1, sticky="ew")

        level = Radiobutton(self, text="Level", bg=bg2, fg=fg2, activebackground=bg2, activeforeground=fg2,
                            font=bt_font, indicatoron=True, selectcolor="black", variable=sort_option, value="Level")
        level.grid(row=1, column=5, columnspan=1, sticky="ew")

        sort_option.set("Arcana")

        header1 = Label(self, text="Enter the name of the Persona you want to experiment with:", bg=bg1, fg=fg1,
                        font=lbl_font)
        header1.grid(row=2, column=0, columnspan=3)

        persona = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona.grid(row=2, column=3, columnspan=1)

        header2 = Label(self, text="Enter the names of your other Personas: "
                                   "Leave fields blank if you can't fill them all.", bg=bg1, fg=fg1, font=lbl_font)
        header2.grid(row=3, column=0, columnspan=6)

        personas = PersonaEntry(self)
        personas.grid(row=4, column=0, columnspan=6)

        def submit():
            try:
                results = restricted_fusion_search(persona.get(), personas.get_names(),
                                                   player_level=int(player_level.get()), sort_type=sort_option.get())
                if results is not None:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, results)
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
                else:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, "Error")
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
            except AttributeError:
                show_results.configure(state=NORMAL)
                show_results.delete("1.0", END)
                show_results.insert(END, "Error")
                show_results.configure(state=DISABLED)
                v.config(command=show_results.yview)

        submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                        activeforeground=fg2, font=bt_font,
                        command=submit)
        submit.grid(row=5, column=0, columnspan=6)

        results_frame = Frame(self, width=300, height=400, bg=bg3)
        results_frame.grid(row=6, column=0, columnspan=6)

        v = Scrollbar(results_frame, orient="vertical")
        v.pack(side=RIGHT, fill="y")

        show_results = Text(results_frame, bg=bg3, fg=fg1, font=lbl_font, width=110, height=20, state=DISABLED,
                            yscrollcommand=v.set)
        v.config(command=show_results.yview)
        show_results.pack()

        ps_bt = Button(self, text="Get a Persona's Info!", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaSearch))
        ps_bt.grid(row=7, column=0, columnspan=6)


class FusionSearch(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)

        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=3, sticky="ew")

        rfs_bt = Button(self, text="To Restricted Fusion Search", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(RestrictedFusionSearch))
        rfs_bt.grid(row=0, column=3, columnspan=3, sticky="ew")

        pl_lbl = Label(self, text="Player Level:", bg=bg1, fg=fg1, font=lbl_font)
        pl_lbl.grid(row=1, column=1, columnspan=1)

        player_level = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        player_level.insert(END, "99")
        player_level.grid(row=1, column=2, columnspan=1)

        sort_lbl = Label(self, text="Sort by:", bg=bg1, fg=fg1, font=lbl_font)
        sort_lbl.grid(row=1, column=3, columnspan=1)

        sort_option = StringVar()
        arcana = Radiobutton(self, text="Arcana", bg=bg2, fg=fg2, activebackground=bg2, activeforeground=fg2,
                             font=bt_font, indicatoron=True, selectcolor="black", variable=sort_option, value="Arcana")
        arcana.grid(row=1, column=4, columnspan=1, sticky="ew")

        level = Radiobutton(self, text="Level", bg=bg2, fg=fg2, activebackground=bg2, activeforeground=fg2,
                            font=bt_font, indicatoron=True, selectcolor="black", variable=sort_option, value="Level")
        level.grid(row=1, column=5, columnspan=1, sticky="ew")

        header = Label(self, text="Enter the names of your Personas: "
                                  "Leave fields blank if you can't fill them all.", bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=2, column=0, columnspan=6)

        personas = PersonaEntry(self)
        personas.grid(row=3, column=0, columnspan=6)

        def submit():
            try:
                results = fusion_search(personas.get_names(), player_level=int(player_level.get()),
                                        sort_type=sort_option.get())
                if results is not None:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, results)
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
                else:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, "Error")
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
            except AttributeError:
                show_results.configure(state=NORMAL)
                show_results.delete("1.0", END)
                show_results.insert(END, "Error")
                show_results.configure(state=DISABLED)
                v.config(command=show_results.yview)

        submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                        activeforeground=fg2, font=bt_font,
                        command=submit)
        submit.grid(row=4, column=0, columnspan=6)

        results_frame = Frame(self, width=300, height=400, bg=bg3)
        results_frame.grid(row=6, column=0, columnspan=6)

        v = Scrollbar(results_frame, orient="vertical")
        v.pack(side=RIGHT, fill="y")

        show_results = Text(results_frame, bg=bg3, fg=fg1, font=lbl_font, width=110, height=20, state=DISABLED,
                            yscrollcommand=v.set)
        v.config(command=show_results.yview)
        show_results.pack()

        ps_bt = Button(self, text="Get a Persona's Info!", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaSearch))
        ps_bt.grid(row=7, column=0, columnspan=6)


class PersonaSearch(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)

        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=3, sticky="ew")

        pc_bt = Button(self, text="Persona Compendium", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaCompendium))
        pc_bt.grid(row=0, column=3, columnspan=3, sticky="ew")

        df_bt = Button(self, text="To Double Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PDFC))
        df_bt.grid(row=1, column=0, columnspan=3, sticky="ew")

        tf_bt = Button(self, text="To Triple Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PTFC))
        tf_bt.grid(row=1, column=3, columnspan=3, sticky="ew")

        fs_bt = Button(self, text="To Full Fusion Search", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(FusionSearch))
        fs_bt.grid(row=2, column=0, columnspan=3, sticky="ew")

        rfs_bt = Button(self, text="To Restricted Fusion Search", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(RestrictedFusionSearch))
        rfs_bt.grid(row=2, column=3, columnspan=3, sticky="ew")

        header = Label(self, text="Enter the name of the Persona you want to see info for: ",
                       bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=3, column=0, columnspan=6)

        persona = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        persona.grid(row=4, column=2, columnspan=1)

        def submit():
            try:
                results = persona_search(persona.get()).info()
                if results is not None:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, results)
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
                else:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, "Error")
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
            except AttributeError:
                show_results.configure(state=NORMAL)
                show_results.delete("1.0", END)
                show_results.insert(END, "Error")
                show_results.configure(state=DISABLED)
                v.config(command=show_results.yview)

        submit = Button(self, text="Submit", bg=bg2, fg=fg2, activebackground=bg2,
                        activeforeground=fg2, font=bt_font,
                        command=submit)
        submit.grid(row=4, column=3, columnspan=1)

        results_frame = Frame(self, width=300, height=400, bg=bg3)
        results_frame.grid(row=6, column=0, columnspan=6)

        v = Scrollbar(results_frame, orient="vertical")
        v.pack(side=RIGHT, fill="y")

        show_results = Text(results_frame, bg=bg3, fg=fg1, font=lbl_font, width=110, height=20, state=DISABLED,
                            yscrollcommand=v.set)
        v.config(command=show_results.yview)
        show_results.pack()


class PersonaCompendium(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg1)

        home_button = Button(self, text="Home", bg=bg2, fg=fg2, font=bt_font,
                             activebackground=bg2, activeforeground=fg2,
                             command=lambda: controller.show_frame(Home))
        home_button.grid(row=0, column=0, columnspan=3, sticky="ew")

        ps_bt = Button(self, text="Get a Persona's Info", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PersonaSearch))
        ps_bt.grid(row=0, column=3, columnspan=3, sticky="ew")

        df_bt = Button(self, text="To Double Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PDFC))
        df_bt.grid(row=1, column=0, columnspan=3, sticky="ew")

        tf_bt = Button(self, text="To Triple Fusion", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(PTFC))
        tf_bt.grid(row=1, column=3, columnspan=3, sticky="ew")

        fs_bt = Button(self, text="To Full Fusion Search", bg=bg2, fg=fg2, font=bt_font,
                       activebackground=bg2, activeforeground=fg2,
                       command=lambda: controller.show_frame(FusionSearch))
        fs_bt.grid(row=2, column=0, columnspan=3, sticky="ew")

        rfs_bt = Button(self, text="To Restricted Fusion Search", bg=bg2, fg=fg2, font=bt_font,
                        activebackground=bg2, activeforeground=fg2,
                        command=lambda: controller.show_frame(RestrictedFusionSearch))
        rfs_bt.grid(row=2, column=3, columnspan=3, sticky="ew")

        header = Label(self, text="Enter an Arcana to see only that Arcana or leave blank: ",
                       bg=bg1, fg=fg1, font=lbl_font)
        header.grid(row=3, column=0, columnspan=6)

        arcana = Entry(self, bg=bg3, fg=fg2, font=bt_font)
        arcana.grid(row=4, column=2, columnspan=1)

        def compendium_button():
            try:
                results = compendium(arcana=arcana.get())
                if results is not None:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, results)
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
                else:
                    show_results.configure(state=NORMAL)
                    show_results.delete("1.0", END)
                    show_results.insert(END, "Error")
                    show_results.configure(state=DISABLED)
                    v.config(command=show_results.yview)
            except AttributeError:
                show_results.configure(state=NORMAL)
                show_results.delete("1.0", END)
                show_results.insert(END, "Error")
                show_results.configure(state=DISABLED)
                v.config(command=show_results.yview)

        compendium_bt = Button(self, text="Open Compendium", bg=bg2, fg=fg2, activebackground=bg2,
                               activeforeground=fg2, font=bt_font,
                               command=compendium_button)
        compendium_bt.grid(row=4, column=3, columnspan=1)

        def sp_fu_button():
            results = ""
            for arc in Personas:
                for persona in arc:
                    if persona.special_fusion is not None:
                        results += persona.name + " = "
                        for i in range(len(persona.special_fusion)):
                            if i != len(persona.special_fusion) - 1:
                                results += persona.special_fusion[i] + " + "
                            else:
                                results += persona.special_fusion[i]
                        results += "\n\n"

            show_results.configure(state=NORMAL)
            show_results.delete("1.0", END)
            show_results.insert(END, results)
            show_results.configure(state=DISABLED)
            v.config(command=show_results.yview)

        sp_fu_bt = Button(self, text="Look up Special Fusions", bg=bg2, fg=fg2, activebackground=bg2,
                          activeforeground=fg2, font=bt_font,
                          command=sp_fu_button)
        sp_fu_bt.grid(row=4, column=4, columnspan=1)

        results_frame = Frame(self, width=300, height=400, bg=bg3)
        results_frame.grid(row=6, column=0, columnspan=6)

        v = Scrollbar(results_frame, orient="vertical")
        v.pack(side=RIGHT, fill="y")

        show_results = Text(results_frame, bg=bg3, fg=fg1, font=lbl_font, width=110, height=20, state=DISABLED,
                            yscrollcommand=v.set)
        v.config(command=show_results.yview)
        show_results.pack()


root = VelvetRoomPortable()
root.mainloop()
