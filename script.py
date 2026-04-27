# -*- coding: utf-8 -*-
import time
import re
import datetime
import alfred3 as al
from thesmuggler import smuggle
import random
import pprint
import csv
import statistics
from matplotlib.figure import Figure

# TODO: Pagetype?

content = smuggle("files/content.py")
screening = smuggle("files/exp_screening.py")
registration = smuggle("files/exp_registration.py")
informed_consent = smuggle("files/informed_consent.py")

exp = al.Experiment()

# Introduction
@exp.setup
def setup(exp):
    # Yoking
    exp.session_timeout = 3600

    exp.exclusion_list = list(exp.read_csv_tolist("files/exclusion_list.csv"))

    position1 = [6, 7]
    exp.first = random.choice(position1)


@exp.member
class ExpSection(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = True
    allow_jumpto = True


@exp.member(of_section="ExpSection")
class LandingPage(al.Page):
    name = "landingpage"
    title = "Herzlich Willkommen zur Studie"

    def on_exp_access(self):
        self += al.Text(text=content.greeting_acc, position="center")


@exp.member(of_section="ExpSection")
class InformedConsentPage(informed_consent.InformedConsent):
    content = content.informed_consent_content


@exp.member(of_section="ExpSection")
class Screening(screening.ScreeningPage):
    email_screening = True
    register_on_hiding = True
    mortimer_url = "https://alfredo3.psych.bio.uni-goettingen.de/mortimer3"
    content = content.screening_page_content
    part_check_filter = {
         "Acc_MC_online": {"exp_id": "61e57f9d9abdfbc62aa4cbac"},
         "Acc_MC_lab": {"exp_id": "6288b36f28b2a3ca2d7ce73e"},
         "Acc_SchFel": {"exp_id": "675ab734b673ce5cc83edc04"}
     }

    def on_first_hide(self):
        self.log.info("Screening Page closed")


@exp.member(of_section="ExpSection")
class RandomizationPage1(al.AutoForwardPage):
    name = "Condition_assignement"
    title = ""
    timeout = "0s"

    def on_exp_access(self):
        self += al.HideNavigation()

    def on_first_hide(self):
        randomizer = al.ListRandomizer(
            ("control", 80), ("process_accountability", 80), ("outcome_accountability", 80),
            exp=self.exp, inclusive=False,
            respect_version=True
        )

        self.exp.condition = randomizer.get_condition()
        self.exp.log.info(self.exp.condition)


class InstructionPage1(al.Page):
    name = "instruction1"
    title = "Erläuterung der Schätzaufgabe"

    def on_exp_access(self):
        self += al.Text(content.instruction)


class InitialVasStressPage(al.Page):
    name = "initial_VASstress"
    title = "Bevor es los geht"

    def on_exp_access(self):
        self += al.Text(text="Bitte geben Sie an, wie Sie sich jetzt, d.h. in diesem Moment fühlen.")

        self += al.Text("Ich fühle mich:", align="rigth")

        self += al.RangeInput(
                    name="insecure",
                    force_input=True,
                    min=0,
                    max=100,
                    step=1,
                    rightlab="sehr unsicher",
                    leftlab="nicht unsicher",
                    display_locale="de-DE",
                    display_suffix=" ",
                    display_input=False
                )

        self += al.RangeInput(
            name="stressed",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr gestresst",
            leftlab="nicht gestresst",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
                    name="anxious",
                    force_input=True,
                    min=0,
                    max=100,
                    step=1,
                    rightlab="sehr ängstlich",
                    leftlab="nicht ängstlich",
                    display_locale="de-DE",
                    display_suffix=" ",
                    display_input=False
                )

        self += al.RangeInput(
                    name="nervous",
                    force_input=True,
                    min=0,
                    max=100,
                    step=1,
                    rightlab="sehr aufgeregt",
                    leftlab="nicht aufgeregt",
                    display_locale="de-DE",
                    display_suffix=" ",
                    display_input=False
                )


class PostManiVasStressPage(al.Page):
    name = "postmani_VASstress"
    title = "Noch ein paar kurze Fragen"

    def on_exp_access(self):
        self += al.Text(text="Bitte geben Sie an, wie Sie sich jetzt, d.h. in diesem Moment fühlen.")

        self += al.Text("Ich fühle mich:", align="rigth")

        self += al.RangeInput(
            name="insecure_post",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr unsicher",
            leftlab="nicht unsicher",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
            name="stressed_post",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr gestresst",
            leftlab="nicht gestresst",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
            name="anxious_post",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr ängstlich",
            leftlab="nicht ängstlich",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
            name="nervous_post",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr aufgeregt",
            leftlab="nicht aufgeregt",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )


class InitialStressPage(al.Page):
    name = "initial"
    title = "Bevor es los geht"

    def on_exp_access(self):
        self += al.Text(content.instruction_STAI, align="center")
        STAI_items = [
            ("STAI_S_01", "Ich bin ruhig."),
            ("STAI_S_02", "Ich fühle mich geborgen."),
            ("STAI_S_03", "Ich fühle mich angespannt."),
            ("STAI_S_04", "Ich bin bekümmert."),
            ("STAI_S_05", "Ich fühle mich ungezwungen."),
            ("STAI_S_06", "Ich bin aufgeregt."),
            ("STAI_S_07", "Ich bin besorgt, dass etwas schiefgehen könnte."),
            ("STAI_S_08", "Ich fühle mich ausgeruht."),
            ("STAI_S_09", "Ich bin beunruhigt."),
            ("STAI_S_10", "Ich fühle mich wohl."),
            ("STAI_S_11", "Ich fühle mich selbstsicher."),
            ("STAI_S_12", "Ich bin nervös."),
            ("STAI_S_13", "Ich bin zappelig."),
            ("STAI_S_14", "Ich bin verkrampft."),
            ("STAI_S_15", "Ich bin entspannt."),
            ("STAI_S_16", "Ich bin zufrieden."),
            ("STAI_S_17", "Ich bin besorgt."),
            ("STAI_S_18", "Ich bin überreizt."),
            ("STAI_S_19", "Ich bin froh."),
            ("STAI_S_20", "Ich bin vergnügt.")
        ]

        for item in STAI_items:
            # Text element to display the item text
            # item_text = al.Text(item[1], width="full")

            # SingleChoiceBar for user input
            item_choice = al.SingleChoiceBar(
                "überhaupt nicht <br> 1", "ein wenig <br> 2", "ziemlich <br> 3", "sehr <br> 4",
                name=f"initial{item[0]}", leftlab=item[1], force_input=True)

            # Important: We use a Row element to arrange text and input horizontally
            self += al.Hline()
            self += item_choice

# @exp.member(of_section="ExpSection")
# class InstructionPage2(al.Page):
#    name = "instruction2"
#    title = "Einleitung Teil 2"
#
#    def on_exp_access(self):
#        self += al.Text(content.instruction)
#
#        if self.exp.condition == "process_accountability":
#            self += al.Text(content.process_accountability)
#
#        elif self.exp.condition == "outcome_accountability":
#            self += al.Text(content.outcome_accountability)
#
#        elif self.exp.condition == "control":
#            pass


class ManiCheckPrePage(al.Page):
    name = "mani_check_pre"
    title = "Ein paar Fragen"

    def on_first_show(self):
        self += al.Text(
            text="Bitte beantworten Sie noch die folgenden Fragen, bevor Sie mit den Beurteilungsaufgaben beginnen ",
            align="center")
        self += al.Hline()
        self += al.SingleChoiceBar(
                "mein Vorgehen <br> 1", "2", "3", "4", "5", "6", "mein Ergebnis <br> 7",
                name=f"acc_pre", leftlab=content.acc_pre, force_input=True)
        self += al.Hline()
        self += al.SingleChoiceBar(
                "überhaupt nicht <br> 1", "2", "3", "4", "5", "6", " sehr <br> 7",
                name=f"justify", leftlab=content.justify_instr, force_input=True)
        if self.exp.condition == "outcome_accountability":
            self += al.Hline()
            self += al.SingleChoice(
                "mein Vorgehen", "mein Ergebnis", "beides gleichermaßen",
                name=f"interview_pre", leftlab=content.interview_pre_OA, force_input=True)
        elif self.exp.condition == "process_accountability":
            self += al.Hline()
            self += al.SingleChoice(
                "mein Vorgehen", "mein Ergebnis", "beides gleichermaßen",
                name=f"interview_pre", leftlab=content.interview_pre_PA, force_input=True)
        else:
            pass


class McStartPage(al.Page):
    name = "mc_start_page"
    title = "Bevor es losgeht!"
    def on_exp_access(self):
        self += al.Text(content.mc_begin, align="center")


class MCQuestionnairePre2(al.Page):
    name = "epistemic_motivation"
    title = "Ein paar weitere Fragen"

    def on_exp_access(self):
        self += al.Text(content.epi_motiv_instr, align="center")
        self += al.Hline()
        choice_labels = [
            "trifft überhaupt nicht zu <br>1",
            "2",
            "3",
            "4",
            "trifft absolut zu <br> 5",
        ]
        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv1,
            name="epistemic_motivation1",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv2,
            name="epistemic_motivation2",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv3,
            name="epistemic_motivation3",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv4,
            name="epistemic_motivation4",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv5,
            name="epistemic_motivation5",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv6,
            name="epistemic_motivation6",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.AC_01,
            name="ac1",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv7,
            name="epistemic_motivation7",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv8,
            name="epistemic_motivation8",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv9,
            name="epistemic_motivation9",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.epi_motiv10,
            name="epistemic_motivation10",
            force_input=True,
            align="center",
        )


class McQuestionnairePre3(al.Page):
    name = "systematic_information_processing"
    title = "Noch ein paar Fragen"

    def on_exp_access(self):
        self += al.Text(text="Auf dieser Seite finden Sie einige Aussagen, die sich auf Ihre geplante Vorgehensweise bei der "
                             "gleich folgenden Schätzaufgabe beziehen. Wählen Sie dazu die auf Sie passende Antwort durch"
                             " Anklicken aus. Es gibt keine richtigen oder falschen Antworten. Überlegen Sie bitte "
                             "nicht lange und entscheiden Sie dann, wie stark Sie denken, dass das jeweils beschriebene Vorgehen "
                             "bei Ihrer eigenen Arbeitsweise vorhanden sein wird.", align="center")
        self += al.Hline()
        choice_labels = [
            "gar nicht <br> 1",
            "2",
            "3",
            "4",
            "sehr häufig <br> 5"
        ]
        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.systematic_information_processing1,
            name="systematic_information_processing1",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        choice_labels = [
            "stimme absolut nicht zu <br> 1",
            "2",
            "3",
            "4",
            "stimme absolut zu <br> 5"
        ]
        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.systematic_information_processing2,
            name="systematic_information_processing2",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        choice_labels = [
            "nie <br> 1",
            "2",
            "3",
            "4",
            "immer <br> 5"
        ]
        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.systematic_information_processing3,
            name="systematic_information_processing3",
            force_input=True,
            align="center",
        )


class MCQuestionnairePre4(al.Page):
    name = "MC_accountability"
    title = "Ein paar letzte Fragen noch, bevor es losgeht."

    def on_exp_access(self):
        self += al.Text(text="Auf dieser Seite finden Sie einige Aussagen die sich auf den von Ihnen geplanten Fokus während der "
                             "nachfolgenden Aufgabe beziehen. Wählen Sie dazu die auf Sie passende Antwort durch "
                             "anklicken aus. Es gibt keine richtigen oder falschen Antworten. Überlegen Sie bitte nicht"
                             " lange und entscheiden Sie dann, wie stark die Aussagen jeweils für Sie persönlich"
                             " zutreffen.", align="center")
        self += al.Hline()
        choice_labels = [
            "stimme überhaupt nicht zu <br> 1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "stimme vollkommen zu <br> 7"
        ]
        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.MC_PA1,
            name="MC_PA_1",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            # *choice,
            # toplab=top_labels,
            leftlab=content.MC_OA1,
            name="MC_OA_1",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.MC_PA2,
            name="MC_PA_2",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            # *choice,
            # toplab=top_labels,
            leftlab=content.MC_OA2,
            name="MC_OA_2",
            force_input=True,
            align="center",
        )
        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.AC_02,
            name="ac2",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.MC_PA3,
            name="MC_PA_3",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            # *choice,
            # toplab=top_labels,
            leftlab=content.MC_OA3,
            name="MC_OA_3",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            leftlab=content.MC_PA4,
            name="MC_PA_4",
            force_input=True,
            align="center",
        )

        self += al.Hline()

        self += al.SingleChoiceBar(
            *choice_labels,
            # *choice,
            # toplab=top_labels,
            leftlab=content.MC_OA4,
            name="MC_OA_4",
            force_input=True,
            align="center",
        )


class Background(al.Page):
    title = "Hintergrund"
    def on_first_show(self):

        self += al.Text(content.case_background,
                        align="left",
                        width="wide"
                        )


class TargetRadWear(al.Page):
    title = "Anlage 1"
    def on_first_show(self):

        self += al.Text("<i>Abteilung: RadWear</i> <br><i>Balanced Scorecard</i> <br><i>Kennzahlen und Zielwerte für das Geschäftsjahr zum 31.Dezember , 2020</i> <br>",
                        align="center",
                        width="medium"
                        )
        self += al.Text(content.rad_wear_perform,
                        align="center",
                        width="wide"
                        )

        self += al.Alert(text=
             "Hinweis 1:  NI bedeutet Nettogewinn; # steht für Anzahl; % steht für Prozent.",
                          category="dark", width="wide")


class TargetWorkWear(al.Page):
    title = "Anlage 2 "

    def on_first_show(self):
        self += al.Text("<i>Abteilung: WorkWear</i> <br><i>Balanced Scorecard</i> <br><i>Kennzahlen und Zielwerte für das Geschäftsjahr zum 31.Dezember , 2020</i> <br>",
                        align="center",
                        width="medium"
                        )
        self += al.Text(content.work_wear_perform,
                        align="center",
                        width="wide"
                        )

        self += al.Alert(text=
             "Hinweis 1:  Das Mystery-Buyer-Programm schickt anonyme Prüfer in die Filialen. Diese Prüfer treten als "
             "normale Kunden auf und führen verschiedene „Tests“ des Geschäfts und des Personals durch. Die Prüfer "
             "bewerten die Filialen anhand von zehn Kriterien; bei perfekter Bewertung in allen Kategorien ergibt sich "
             "eine Gesamtpunktzahl von 100 Punkten. Zu den Kriterien gehören unter anderem das Erscheinungsbild des "
             "Geschäfts und des Personals, das Auftreten der Mitarbeiter sowie die Effizienz und Effektivität des "
             "Kassensystems.",
             category="dark", width="wide")

        self += al.Alert(text=
             "Hinweis 2:  NI bedeutet Nettogewinn; # steht für Anzahl; % steht für Prozent.",
             category="dark", width="wide")


class ManiInstr(al.Page):
    title = "Leistung im Jahr 2020"
    def on_first_show(self):

        if self.exp.condition == "process_accountability":
            self += al.Text(content.wcs_performance_pacc,
                 align="left",
                 width="wide"
             )
        elif self.exp.condition == "outcome_accountability":
            self += al.Text(content.wcs_performance_oacc,
                            align="left",
                            width="wide"
                            )
        elif self.exp.condition == "control":
            self += al.Text(content.wcs_performance_noacc,
                            align="left",
                            width="wide"
                            )


class BSCRadWear(al.Page):
    title = "Anlage 3 "

    def on_first_show(self):

        self += al.Text("<i>Abteilung: RadWear</i> <br><i>Audited Balanced Scorecard</i> <br><i>Kennzahlen und Zielwerte für das Geschäftsjahr zum 31.Dezember , 2020</i> <br>",
                        align="center",
                        width="medium"
                        )
        self += al.Text(content.rad_wear_balanced_scorecard,
            align="center",
            width="wide"
        )


class BSCWorkWear(al.Page):
    title = "Anlage 4 "

    def on_first_show(self):
        self += al.Text("<br><i>Abteilung: WorkWear</i> <br><i>Audited Balanced Scorecard</i> <br><i>Kennzahlen und Zielwerte für das Geschäftsjahr zum 31.Dezember , 2020</i> <br>",
                        align="center",
                        width="medium"
                        )
        self += al.Text(content.work_wear_balanced_scorecard,
            align="center",
            width="wide"
        )


class RadWearEval(al.Page):
    title = "WCS Inc. <br>Formular für Erstbewertung"

    def on_first_show(self):
        self += al.Text("Jahr: 2020 <br> Manager: Chris Peters <br> Abteilung: RadWear",
                        align="left",
                        width="wide"
                        )
        self += al.Text(content.rad_wear_balanced_scorecard,
            align="center",
            width="wide"
        )

        self += al.Hline()
        self += al.VerticalSpace()

        self += al.Text(
            "1.  Geben Sie Ihre anfängliche Leistungsbewertung für diese Führungskraft an, indem Sie auf der "
            "nachstehenden Skala den Marker platzieren.  Die Bedeutung der einzelnen Skalenpunkte finden Sie unten. ",
            align="left"

        )
        self += al.VerticalSpace()

        self += al.RangeInput(
            name="rad_eval",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="Exzellent",
            leftlab="Neuzuweiseung",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False)
        self += al.VerticalSpace()
        self += al.Text(
            "Exzellent: Manager übertrifft die Erwartungen  <br>"
            "Neuzuweisung: ausreichende Verbesserung unwahrscheinlich <br>",
            align="left",
            width="medium"
        )
        self += al.VerticalSpace()
        self += al.Hline()
        self += al.Text(
            "2.  Geben Sie an, wie stark Sie von dieser Einschätzung überzeugt sind (wie stark Sie die oben "
            "angegebene Meinung vertreten), indem Sie auf der nachstehenden Skala den Marker platzieren:",
            align="left"
        )

        self += al.RangeInput(
            name="rad_conf",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr stark",
            leftlab="sehr schwach",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False)

        self += al.Hline()
        self += al.VerticalSpace()
        if self.exp.condition == "process_accountability":
            self += al.Text(
                "3.  Bitte erläutern und begründen Sie, wie Sie zu Ihrer Entscheidung über die Leistungsbewertung "
                "von Chris Peters gekommen sind.",
                align="left"
            )

            self += al.VerticalSpace()

            self += al.TextArea(
                name="justification_rad",
                force_input=True,
            )


class WorkWearEval(al.Page):
    title = "WCS Inc. <br>Formular für Erstbewertung"

    def on_first_show(self):
        self += al.Text("Jahr: 2020 <br> Manager: Taylor Graham <br> Abteilung: WorkWear",
                    align="left",
                    width="wide"
                    )

        self += al.Text(content.work_wear_balanced_scorecard,
            align="center",
            width="wide"
        )

        self += al.Hline()
        self += al.VerticalSpace()

        self += al.Text(
            "1. Geben Sie Ihre anfängliche Leistungsbewertung für diese Führungskraft an, indem Sie auf der "
            "nachstehenden Skala den Marker platzieren.  Die Bedeutung der einzelnen Skalenpunkte finden Sie unten.",
            align="left"
        )

        self += al.VerticalSpace()

        self += al.RangeInput(
            name="work_eval",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="Exzellent",
            leftlab="Neuzuweiseung",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False)

        self += al.VerticalSpace()

        self += al.Text(
            "Exzellent = Der Manager übertrifft die Erwartungen  <br>"
            "Neuzuweisung = eine ausreichende Verbesserung des Mangers ist unwahrscheinlich <br>",
            align="left",
            width="medium"
        )

        self += al.Hline()
        self += al.VerticalSpace()

        self += al.Text(
            "2.  Geben Sie an, wie stark Sie von dieser Einschätzung überzeugt sind (wie stark Sie die oben "
            "angegebene Meinung vertreten), indem Sie auf der nachstehenden Skala den Marker platzieren:",
            align="left"
        )

        self += al.VerticalSpace()

        self += al.RangeInput(
            name="work_conf",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr stark",
            leftlab="sehr schwach",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False)

        self += al.Hline()
        self += al.VerticalSpace()
        if self.exp.condition == "process_accountability":
            self += al.Text(
                "3.  Bitte erläutern und begründen Sie, wie Sie zu Ihrer Entscheidung über die Leistungsbewertung "
                "von Taylor Graham gekommen sind.",
                align="left"
            )

            self += al.VerticalSpace()

            self += al.TextArea(
                name="justification_work",
                force_input=True,
            )


class OutcomeJustificationPage(al.Page):
    def on_each_show(self):

        eval_diff = self.exp.values["work_eval"] - self.exp.values["rad_eval"]
        self += al.Value(eval_diff, name=f"evalution_difference")

        if eval_diff > 0:
            self +=al.Text(f"Sie haben den Work Wear Manager (Taylor Graham) um {eval_diff} Punkte besser bewertet"
                           "als den Rad Wear Manager (Chris Peters). Die Evaluation des Präsidenten von WCS legt nahe, "
                           "dass die beiden Manager gleich gut gearbeitet haben und dementsprechend gleich gut hätten "
                           "bewertet werden müssen. Bitte erläutern Sie weshalb Ihre Evalution der beiden Manger, von"
                           "dieser objektiven Evalution der Leistungen abweicht.",
                            align="left",
                            width="wide" )

        elif eval_diff < 0:
            self += al.Text(
                f"Sie haben den Rad Wear Manager (Chris Peters) um {eval_diff} Punkte besser bewertet"
                "als den Work Wear Manager (Taylor Graham). Die Evaluation des Präsidenten von WCS legt nahe, "
                "dass die beiden Manager gleich gut gearbeitet haben und dementsprechend gleich gut hätten "
                "bewertet werden müssen. Bitte erläutern Sie weshalb Ihre Evalution der beiden Manger, von"
                "dieser objektiven Evalution der Leistungen abweicht.",
                align="left",
                width="wide")

        else:
            self += al.Text(
                f"Sie haben den Rad Wear Manager (Chris Peters) und den Work Wear Manager (Taylor Graham) gleich"
                "gut bewertet. Die Evaluation des Präsidenten von WCS deckt sich mit Ihrer Einschätzung, dass die beiden "
                "Manager gleich gut gearbeitet haben und dementsprechend gleich gut zu bewerten waren."
                " Bitte erläutern Sie weshalb Ihre Evalution der beiden Manger, dieser objektiven Evalution der"
                " Leistungen entspricht.",
                align="left",
                width="wide")

        self += al.VerticalSpace()

        self += al.TextArea(
            name="justification_outcome",
            force_input=True,
            )


class FinalStressPage(al.Page):
    name = "final_stai"
    title = "Ein paar letzte Fragen noch, bevor es losgeht."

    def on_exp_access(self):
        self += al.Text(content.instruction_STAI, align="center")

        STAI_items = [
            ("STAI_S_01", "Ich bin ruhig."),
            ("STAI_S_02", "Ich fühle mich geborgen."),
            ("STAI_S_03", "Ich fühle mich angespannt."),
            ("STAI_S_04", "Ich bin bekümmert."),
            ("STAI_S_05", "Ich fühle mich ungezwungen."),
            ("STAI_S_06", "Ich bin aufgeregt."),
            ("STAI_S_07", "Ich bin besorgt, dass etwas schiefgehen könnte."),
            ("STAI_S_08", "Ich fühle mich ausgeruht."),
            ("STAI_S_09", "Ich bin beunruhigt."),
            ("STAI_S_10", "Ich fühle mich wohl."),
            ("STAI_S_11", "Ich fühle mich selbstsicher."),
            ("STAI_S_12", "Ich bin nervös."),
            ("STAI_S_13", "Ich bin zappelig."),
            ("STAI_S_14", "Ich bin verkrampft."),
            ("STAI_S_15", "Ich bin entspannt."),
            ("STAI_S_16", "Ich bin zufrieden."),
            ("STAI_S_17", "Ich bin besorgt."),
            ("STAI_S_18", "Ich bin überreizt."),
            ("STAI_S_19", "Ich bin froh."),
            ("STAI_S_20", "Ich bin vergnügt.")
        ]

        for item in STAI_items:
            # Text element to display the item text
            # item_text = al.Text(item[1], width="full")

            # SingleChoiceBar for user input
            item_choice = al.SingleChoiceBar(
                "überhaupt nicht <br> 1", "ein wenig <br> 2", "ziemlich <br> 3", "sehr <br> 4",
                name=f"final{item[0]}", leftlab=item[1], force_input=True)

            # Important: We use a Row element to arrange text and input horizontally
            self += al.Hline()
            self += item_choice


class PostManiVasStressPage(al.Page):
    name = "postmani_VASstress"
    title = "Ein paar letzte Fragen noch, bevor es losgeht."

    def on_exp_access(self):
        self += al.Text(text="Bitte geben Sie an wie Sie sich jetzt, d.h. in diesem Moment fühlen.")

        self += al.Text("Ich fühle mich:", align="rigth")

        self += al.RangeInput(
            name="insecure_posttask",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr unsicher",
            leftlab="nicht unsicher",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
            name="stressed_posttask",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr gestresst",
            leftlab="nicht gestresst",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
            name="anxious_posttask",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr ängstlich",
            leftlab="nicht ängstlich",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )

        self += al.RangeInput(
            name="nervous_posttask",
            force_input=True,
            min=0,
            max=100,
            step=1,
            rightlab="sehr aufgeregt",
            leftlab="nicht aufgeregt",
            display_locale="de-DE",
            display_suffix=" ",
            display_input=False
        )



@exp.member(of_section="ExpSection")
class InstructionSection(al.Section):
    allow_forward = True
    allow_backward = True
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass
    def on_exp_access(self):
        self += InitialStressPage()
        self += InitialVasStressPage()

    def on_enter(self):
        if self.exp.condition == "process_accountability":
            self += InstructionPage1()
            self += Background(name="background")
            self += TargetRadWear(name="target_rad_wear")
            self += TargetWorkWear(name="target_work_wear")
            self += ManiInstr(name="mani_instr")

        elif self.exp.condition == "outcome_accountability":
            self += InstructionPage1()
            self += Background(name="background")
            self += TargetRadWear(name="target_rad_wear")
            self += TargetWorkWear(name="target_work_wear")
            self += ManiInstr(name="mani_instr")

        else:
            self += InstructionPage1()
            self += Background(name="background")
            self += TargetRadWear(name="target_rad_wear")
            self += TargetWorkWear(name="target_work_wear")
            self += ManiInstr(name="mani_instr")



@exp.member(of_section="ExpSection")
class ManiCheckSection(al.Section):
    allow_forward = True
    allow_backward = True
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass

    def on_exp_access(self):
        self += al.AutoForwardPage(name = "mc_start_up",
            title = "",
            timeout = "0s")

    def on_enter(self):
        if self.exp.condition == "process_accountability":

            self += McStartPage()
            self += ManiCheckPrePage()
            self += MCQuestionnairePre2()
            self += McQuestionnairePre3()
            self += MCQuestionnairePre4()
            self += FinalStressPage()
            self += PostManiVasStressPage()

        elif self.exp.condition == "outcome_accountability":

            self += McStartPage()
            self += ManiCheckPrePage()
            self += MCQuestionnairePre2()
            self += McQuestionnairePre3()
            self += MCQuestionnairePre4()
            self += FinalStressPage()
            self += PostManiVasStressPage()

        else:

            self += McStartPage()
            self += ManiCheckPrePage()
            self += MCQuestionnairePre2()
            self += McQuestionnairePre3()
            self += MCQuestionnairePre4()
            self += FinalStressPage()
            self += PostManiVasStressPage()


@exp.member(of_section="ExpSection")
class TaskSection(al.Section):
    allow_forward = True
    allow_backward = True
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass

    def on_exp_access(self):
        self += al.AutoForwardPage(name = "task_start_up",
            title = "",
            timeout = "0s")

    def on_enter(self):
        if self.exp.condition == "process_accountability":

            self += BSCRadWear(name="bsc_rad_wear")
            self += BSCWorkWear(name="bsc_work_wear")
            self += RadWearEval(name="eval_rad_wear")
            self += WorkWearEval(name="eval_work_wear")

        elif self.exp.condition == "outcome_accountability":

            self += BSCRadWear(name="bsc_rad_wear")
            self += BSCWorkWear(name="bsc_work_wear")
            self += RadWearEval(name="eval_rad_wear")
            self += WorkWearEval(name="eval_work_wear")
            self += OutcomeJustificationPage(name="just_outcome")

        else:

            self += BSCRadWear(name="bsc_rad_wear")
            self += BSCWorkWear(name="bsc_work_wear")
            self += RadWearEval(name="eval_rad_wear")
            self += WorkWearEval(name="eval_work_wear")

@exp.member(of_section="ExpSection")
class JustSection(al.Section):
    allow_forward = True
    allow_backward = False
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass

    def on_exp_access(self):
        self += al.AutoForwardPage(name = "just_start_up",
            title = "",
            timeout = "0s")

    def on_enter(self):
        if self.exp.condition == "outcome_accountability":
            self += OutcomeJustificationPage(name="just_outcome")
        else:
            pass

@exp.member(of_section="ExpSection")
class FQSection(al.Section):
    allow_forward = True
    allow_backward = True
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass


@exp.member(of_section="FQSection")
class TaskCompletedPage(al.Page):
    name = "task_completed_page"
    title = "Fast geschafft!"
    def on_exp_access(self):
        self += al.Text(content.task_complet)


# @exp.member(of_section="FQSection")
# class FinalStressPage(al.Page):
#     name = "final_stress"
#     title = "Abschlussfragen 1"
#
#     def on_exp_access(self):
#         self += al.Text(content.instruction_STAI, align="center")
#
#         STAI_items = [
#             ("STAI_S_01", "Ich bin ruhig."),
#             ("STAI_S_02", "Ich fühle mich geborgen."),
#             ("STAI_S_03", "Ich fühle mich angespannt."),
#             ("STAI_S_04", "Ich bin bekümmert."),
#             ("STAI_S_05", "Ich fühle mich ungezwungen."),
#             ("STAI_S_06", "Ich bin aufgeregt."),
#             ("STAI_S_07", "Ich bin besorgt, dass etwas schiefgehen könnte."),
#             ("STAI_S_08", "Ich fühle mich ausgeruht."),
#             ("STAI_S_09", "Ich bin beunruhigt."),
#             ("STAI_S_10", "Ich fühle mich wohl."),
#             ("STAI_S_11", "Ich fühle mich selbstsicher."),
#             ("STAI_S_12", "Ich bin nervös."),
#             ("STAI_S_13", "Ich bin zappelig."),
#             ("STAI_S_14", "Ich bin verkrampft."),
#             ("STAI_S_15", "Ich bin entspannt."),
#             ("STAI_S_16", "Ich bin zufrieden."),
#             ("STAI_S_17", "Ich bin besorgt."),
#             ("STAI_S_18", "Ich bin überreizt."),
#             ("STAI_S_19", "Ich bin froh."),
#             ("STAI_S_20", "Ich bin vergnügt.")
#         ]
#
#         for item in STAI_items:
#             # Text element to display the item text
#             # item_text = al.Text(item[1], width="full")
#
#             # SingleChoiceBar for user input
#             item_choice = al.SingleChoiceBar(
#                 "überhaupt nicht <br> 1", "ein wenig <br> 2", "ziemlich <br> 3", "sehr <br> 4",
#                 name=f"final{item[0]}", leftlab=item[1], force_input=True)
#
#             # Important: We use a Row element to arrange text and input horizontally
#             self += al.Hline()
#             self += item_choice
#
#
# @exp.member(of_section="FQSection")
# class PostTaskVasStressPage(al.Page):
#     name = "posttask_VASstress"
#     title = "Abschlussfragen 2"
#
#     def on_exp_access(self):
#         self += al.Text(text="Bitte geben Sie an wie Sie sich jetzt, d.h. in diesem Moment fühlen.")
#
#         self += al.Text("Ich fühle mich:", align="rigth")
#
#         self += al.RangeInput(
#             name="insecure_posttask",
#             force_input=True,
#             min=0,
#             max=100,
#             step=1,
#             rightlab="sehr unsicher",
#             leftlab="nicht unsicher",
#             display_locale="de-DE",
#             display_suffix=" ",
#             display_input=False
#         )
#
#         self += al.RangeInput(
#             name="stressed_posttask",
#             force_input=True,
#             min=0,
#             max=100,
#             step=1,
#             rightlab="sehr gestresst",
#             leftlab="nicht gestresst",
#             display_locale="de-DE",
#             display_suffix=" ",
#             display_input=False
#         )
#
#         self += al.RangeInput(
#             name="anxious_posttask",
#             force_input=True,
#             min=0,
#             max=100,
#             step=1,
#             rightlab="sehr ängstlich",
#             leftlab="nicht ängstlich",
#             display_locale="de-DE",
#             display_suffix=" ",
#             display_input=False
#         )
#
#         self += al.RangeInput(
#             name="nervous_posttask",
#             force_input=True,
#             min=0,
#             max=100,
#             step=1,
#             rightlab="sehr aufgeregt",
#             leftlab="nicht aufgeregt",
#             display_locale="de-DE",
#             display_suffix=" ",
#             display_input=False
#         )


@exp.member(of_section="FQSection")
class ManiCheckPostPage(al.Page):
    name = "mani_check_post"
    title = "Abschlussfragen 1"

    def on_first_show(self):
        self += al.Text(text="Bitte beantworten Sie die folgenden Fragen", align="center")
        self += al.Hline()

        self += al.SingleChoiceBar(
                "mein Vorgehen <br> 1", "2", "3", "4", "5", "6", "mein Ergebnis <br> 7",
                name=f"acc_post", leftlab=content.acc_post, force_input=True)
        if self.exp.condition == "outcome_accountability":
            self += al.Hline()
            self += al.SingleChoice(
                "mein Vorgehen", "mein Ergebnis", "beides gleichermaßen",
                name=f"interview_post", leftlab=content.interview_post_OA, force_input=True)
        elif self.exp.condition == "process_accountability":
            self += al.Hline()
            self += al.SingleChoice(
                "mein Vorgehen", "mein Ergebnis", "beides gleichermaßen",
                name=f"interview_post", leftlab=content.interview_post_PA, force_input=True)
        else:
            pass


@exp.member(of_section="FQSection")
class SusCheckPage(al.Page):
    name = "suspicion_check"
    title = "Abschlussfragen 2"

    def on_exp_access(self):
        self += al.TextArea(
                toplab=content.suspicion_check,
                name="suspicion",
                force_input=True,
            )

        self += al.Hline()

        self += al.TextArea(
            toplab=content.comments,
            name="comments",
            force_input=False,
        )

        self += al.Hline()

        self += al.TextArea(
            toplab=content.AC_03,
            name="ac3",
            force_input=False,
        )


# TODO: add instruction text!
@exp.member(of_section="FQSection")
class FinalQuestionnaire5(al.Page):
    name = "demographics"
    title = "Demographische Angaben"

    def on_exp_access(self):
        self += al.Text(text="Zum Abschluss haben wir noch einige Fragen zu Ihren demographischen Daten", align="center")

        self += al.Hline()

        choice_list = ["noch nicht ausgewählt", "weiblich", "männlich", "divers"]

        self += al.SingleChoiceList(
            leftlab="Bitte wählen Sie das Geschlecht aus, zu dem Sie sich zugehörig fühlen.",
            *choice_list,
            name="gender",
            force_input=True,
        )

        self += al.Hline()

        self += al.NumberEntry(
            leftlab="Bitte geben Sie Ihr Alter an.",
            suffix="Jahre",
            name="age",
            force_input=True,
        )

        self += al.Hline()

        self += al.TextEntry(
            leftlab="Bitte tragen Sie Ihren Studiengang oder Ihre Beschäftigung ein.",
            force_input=True,
            name="occupation",
        )


class SelectionPage(registration.SelectionPage):
    content = content.registration_selection_content

    pass


# TODO: Check which information we need.
class RegistrationPage(registration.RegistrationPage):
    content = content.registration_page_content


@exp.member(of_section="ExpSection")
class SelRegSection(al.Section):
    allow_forward = True
    allow_backward = True
    allow_jumpfrom = False
    allow_jumpto = False

    def validate_on_backward(self):
        pass

    def on_exp_access(self):
        self += SelectionPage()
        self += RegistrationPage()


@exp.member
class ExperimentFinish(al.ForwardOnlySection):
    def on_exp_access(self):
        srsi_page = al.Page(
            name="srsi",
            title="Abschlussfrage zur Verwendung Ihrer Daten"
        )

        srsi_page += al.Text(
            text=content.srsi,
            width="wide",
            align="center",
        )

        srsi_page += al.Text(
            text=content.srsi_question,
            width="wide",
            align="center",
        )

        srsi_page += al.SingleChoiceButtons(
            "Starke Ablehnung",
            "Ablehnung",
            "Eher Ablehnung",
            "Weder noch",
            "Eher Zustimmung",
            "Zustimmung",
            "Starke Zustimmung",
            name="srsi",
            force_input=True,
            align="center",
            vertical=True,
            width="narrow",
            description='Participant quality of data rating. Self-reported single item '
                        '(SRSI) indicator from Meade and Craig (2012) and Ward and '
                        'Pond (2015): Sollten wir Ihrer ehrlichen Meinung nach Ihre '
                        'Daten in unseren Analysen dieser Studie verwenden?'
        )

        self += srsi_page

        debriefing = al.Page(
            name="debriefing_page",
            title="Abschließende Informationen zum Versuch"
        )

        debriefing += al.Text(
            content.debriefing_text,
            width="wide"
        )

        self += debriefing


if __name__ == "__main__":
    exp.run()
