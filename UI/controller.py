import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        pass

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def fillDDYear(self):
        years = self._model.getYears()
        yearsDD = list(map(lambda x: ft.dropdown.Option(x), years))
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def readDDTeams(self, e):
        if e.control.data is None:
            self.selectedTeam = None
        else:
            self.selectedTeam = e.control.data
        #print(self.selectedTeam)
    def handleYearDDSelection(self, e):
        self.allTeams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.clean()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Ho trovato {len(teams)} squadre che hanno giocato nell'anno {self._view._ddAnno.value}"))
        for t in self.allTeams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data = t,
                                                                     text = t.teamCode,
                                                                     on_click=self.readDDTeams))
        self._view.update_page()

