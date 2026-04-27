greeting = """
Vielen Dank, dass Sie sich für die Teilnahme an dieser Studie entschieden haben!<br>
+ Ihre Aufgabe wird darin bestehen, die Leistung von zwei Tochtergesellschaften eines auf Damenkleidung spezialisierten Unternehmens zu bewerten.
+ Die Bearbeitungszeit beträgt ca. <b>25 Minuten</b>.
+ Am Ende der Studie erhalten Sie <b>Feedback</b> zu Ihrer persönlichen Schätzleistung.
+ Die Teilnahme an dieser Studie wird für Studierende mit <b>0,5 Versuchspersonenstunden</b> vergütet. 
+ Zusätzlich werden im Rahmen dieser Studie <b>10 x 20€</b> und <b>10 x 10€</b> unter allen Teilnehmer*innen verlost.<br>
"""

greeting_acc = """
Vielen Dank, dass Sie sich für die Teilnahme an dieser Studie entschieden haben!<br>
+ Ihre Aufgabe wird darin bestehen, die Leistung von zwei Tochtergesellschaften eines auf Damenkleidung spezialisierten Unternehmens zu bewerten.
+ Die Bearbeitungszeit beträgt ca. <b>25 Minuten</b>.
+ Am Ende der Studie erhalten Sie <b>Feedback</b> zu Ihrer persönlichen Schätzleistung.
+ Die Teilnahme an dieser Studie wird mit <b>0,5</b> Versuchspersonenstunden vergütet. 
+ Zusätzlich werden im Rahmen dieser Studie <b>5 x 20€</b> und <b>20 x 10€</b> unter allen Teilnehmenden verlost.<br>

"""

screening_page_content = dict(
    title="Teilnahmeregistrierung",
    button_text="Registrieren",
    screening_info=(
        "Bevor Sie an dieser Studie teilnehmen können, müssen wir sicher gehen, dass "
        "Sie nicht bereits an dieser oder einer ähnlichen Studie teilgenommen haben. "
        "Dazu möchten wir Sie bitten, Ihre E-Mail-Adresse einzutragen. Dies dient "
        "gleichzeitig der Dokumentation Ihrer Teilnahme."
    ),
    email_instruction="Ihre E-Mailadresse:",
    email_pattern=r"[^@]+@[^@]+\.[^@]+",
    email_match_hint="Bitte geben Sie eine gültige E-Mailadresse ein",
    data_protection_info=(
        "Ihre hier eingegebene E-Mail-Adresse wird getrennt von Ihrem "
        "Experimentaldatensatz und in einer kodierten Form, die keine Nutzung für "
        "andere Zwecke als den Abgleich mit E-Mail-Adressen von anderen Teilnehmenden "
        "ermöglicht, gespeichert."
    ),
    exclusion_title="Teilnahme nicht möglich",
    exclusion_icon="times-circle",
    exclusion_message="Leider können Sie an diesem Experiment nicht teilnehmen, da Sie "
                      "bereits and dieser oder einer sehr ähnlichen Studie teilgenommen"
                      "haben.<br><br>"
                      "Bei Fragen können Sie sich gerne an folgende E-Mail-Adresse wenden: "
                      "felix.schabasian@stud.uni-goettingen.de",
)

informed_consent_content = dict(
    experimenter_in_charge="Abdul Schamel",
    experimenter_in_charge_email="abdul.schamel@stud.uni-goettingen.de",
    privacy_officer="Herr Prof. Dr. Wiebe",
    privacy_officer_email="datenschutzvorfall@uni-goettingen.de",
    study_email="abdul.schamel@stud.uni-goettingen.de",
    consent_accept_label="Akzeptieren",
    consent_reject_label="Ablehnen",
    # language=HTML
    title="Einverständniserklärung",
    statustext="",
    # language=HTML
    introduction="""<span style="font-size: large; "><b>Allgemeine Informationen 
    zum Datenschutz</b></span>""",
    # language=HTML
    experiment_info="""Bei der Durchführung von Experimenten werden durch die dabei zu 
    treffenden Entscheidungen der Teilnehmenden Daten generiert. Diese Daten werden 
    wissenschaftlich durch die Abteilung für Wirtschafts- und Sozialpsychologie des 
    Georg-Elias-Müller-Institutes für Psychologie ausgewertet. Dabei werden alle Forschungsdaten 
    grundsätzlich <b>getrennt</b> von personenbezogenen Daten gespeichert, die eine direkte 
    Identifizierung von einzelnen Teilnehmenden erlauben würden.""",
    # language=HTML
    anonymity_info="""<b>Eine nachträgliche Verknüpfung von Forschungsdaten mit Merkmalen, 
    die einen direkten Rückschluss auf Ihre Person zulassen, ist im vorliegenden Versuch 
    nicht möglich!</b>""",
    # language=HTML
    personal_data_info="""Auf der nächsten Seite dieses Versuchs werden wir Ihre E-Mail-Adresse abfragen, 
    um Ihre Teilnahme zu dokumentieren.
     Zusätzlich werden wir am Ende dieser Studie Ihren Vornamen, Nachnamen und nochmals Ihre 
    E-Mail-Adresse sowie ggf. Ihre Matrikelnummer abfragen, diese personenbezogenen Daten dienen dazu, 
    um Ihnen Ihre Versuchspersonenstunden auszustellen bzw. Sie im Fall eines Gewinnes bei der Verlosung zu
     kontaktieren. <br>
""",
    # language=HTML
    data_disclaimer="""Die <b>anonymen</b> Forschungsdaten werden für die Erstellung von 
    wissenschaftlichen Forschungsarbeiten und Vorträgen genutzt. Diese Arbeiten werden 
    veröffentlicht. In den Veröffentlichungen ist die Zuordnung von Forschungsdaten zu einzelnen 
    Personen ausgeschlossen. Anonymisierte Daten können ebenfalls im Sinne einer transparenten und 
    offenen Wissenschaft Dritten zur Verfügung gestellt werden. Personenbezogene Daten werden 
    grundsätzlich nicht an Dritte weitergegeben.""",
    # language=HTML
    consent="""<span style="font-size: large; "><b>Einwilligungserklärung zur Datenerhebung und Datenverarbeitung</b></span>
    <br><br>
    Ich erkläre mich damit einverstanden, dass im Rahmen dieser Studie mich betreffende 
    personenbezogene Daten/Angaben durch die Versuchsleitung erhoben und verarbeitet werden. 
    Mir ist bekannt, dass die erhobenen personenbezogenen Daten gelöscht werden, sobald dies 
    nach dem Forschungs- oder Statistikzweck möglich ist. Von dieser Löschung nicht betroffen 
    sind anonymisierte Daten, die keinen Rückschluss auf meine Person zulassen. <br>
    Ich bin auch damit einverstanden, dass die Studienergebnisse in anonymer Form 
    veröffentlicht werden. Mir ist bekannt, dass ich jederzeit mein Einverständnis ohne Angabe 
    von Gründen und ohne nachteilige Folgen für mich zurückziehen und eine Löschung der von 
    mir erhobenen Daten verlangen kann. Mir ist jedoch klar, dass eine Löschung bereits 
    anonymisierter Daten nicht mehr möglich sein wird. Mir ist bekannt, dass meine Angaben in 
    Übereinstimmung mit §4 BDSG behandelt werden.
    <br><br>
    Der Verantwortliche für diese Studie und die Datenerhebung ist:
    <br>
    {experimenter_in_charge} ({experimenter_in_charge_email}).
    <br><br>
    Der für diese Studie verantwortliche Datenschutzbeauftragte ist der Datenschutzbeauftragte 
    der Georg-August-Universität Göttingen, {privacy_officer}. <br>
    Datenschutzverstöße und -probleme kann ich jederzeit unter folgender E-Mail-Adresse melden:
    {privacy_officer_email}
    <br><br>
    Mir ist bekannt, dass ich bezogen auf die Verarbeitung meiner personenbezogenen Daten ein 
    Beschwerderecht bei einer Datenschutz-Aufsichtsbehörde (Landesbeauftragte für den 
    Datenschutz Niedersachsen, Prinzenstraße 5, 30159 Hannover) habe. Mir ist zudem bekannt, 
    dass ich ein Recht auf Auskunft über meine verarbeiteten personenbezogenen Daten habe, 
    einschließlich einer unentgeltlichen Kopie dieser Daten. Dieses Auskunftsrecht besteht 
    gegenüber dem genannten Verantwortlichen. Weiterhin ist mir bekannt, dass ich ein Recht 
    auf Berichtigung sowie auf Löschung meiner verarbeiteten personenbezogenen Daten habe. 
    Ich willige ein, dass meine Angaben in Übereinstimmung mit Art. 6 DSGVO behandelt werden.
    <br> <br>
    Ich habe diesbezüglich keine weiteren Fragen mehr und willige hiermit in die dargestellte 
    Untersuchung ein. Alle mich interessierenden Fragen wurden ausreichend geklärt.
    <br><br>
    <b>Notiz:</b> Wenn Sie auf 'Akzeptieren' klicken, wird das Experiment sofort starten. Klicken 
    Sie auf 'Ablehnen', um das Experiment zu beenden, ohne dass Ihre persönlichen Daten 
    aufgezeichnet werden.""",
    consent_reject_title="Consent: Rejected",
    consent_reject_icon="times-circle",
    # The following text needs a {study_email} placeholder!
    # language=HTML
    consent_reject_message="""Sie haben das Experiment abgebrochen.
    <br><br>
    Sie können diese Seite jetzt schließen.
    <br><br>
    Wenn Sie Fragen haben, schreiben Sie uns bitte eine Mail an 
    <span style="color: blue; ">{study_email}</span>""",
)

instruction = """
<p>
In diesem Experiment geht es darum, wie gut Personen in der Lage sind, die wirtschaftliche Situation zweier 
Tochtergesellschaften eines Bekleidungsunternehmens zu beurteilen.
Dabei sollen anhand geeigneter Kennzahlen und qualitativer Kriterien die Stärken und Schwächen der einzelnen 
Tochtergesellschaften bewertet werden.
</p>
<p> 
Hierfür werden zentrale Finanz- und Leistungsindikatoren (z. B. Umsatz, Gewinn, Rentabilität) bereitgestellt und 
miteinander in Beziehung gesetzt.
</p>
<p> 
Die Aufgabe besteht aus zwei Runden. In jeder Runde erhalten Sie die Kennzahlen einer Tochtergesellschaft und geben 
eine Bewertung auf einer Skala von 0 bis 100 ab.
</p>
<p> 
Bitte bearbeiten Sie die Aufgaben <b>gewissenhaft und sorgfältig</b>, um eine hohe Datenqualität zu gewährleisten.
</p>

"""

case_background = """

Women’s Clothing Store, Inc. ist ein Unternehmen, das sich auf den Einzelhandel mit Damenbekleidung spezialisiert hat. 
WCS besitzt fünf Tochtergesellschaften, die jeweils Bekleidung für bestimmte Nischen im Damenbekleidungsmarkt anbieten. 
WCS ist in ganz Nordamerika tätig und erwägt derzeit einen Vorstoß in die europäischen Märkte.
<br> <br>
Die beiden größten Tochtergesellschaften von WCS sind __RadWear__ und __WorkWear__. __RadWear__ betreibt Einzelhandelsgeschäfte, die
 sich auf Bekleidung für jugendliche Mädchen  spezialisieren. __WorkWear__ ist auf Uniformen für Frauen spezialisiert – 
 insbesondere für Krankenhausmitarbeiterinnen, Reinigungskräfte und Kellnerinnen. WCS führt seine Tochtergesellschaften
  in einer weitgehend dezentralen Weise. Jede verfügt über einen Abteilungsleiter, der für die Leistung der Abteilung 
  sowie für die Kommunikation zwischen der zentralen Verwaltung von WCS und seiner  Abteilung verantwortlich ist.
<br> <br>
Pat Jenks ist der Finanzvorstand (CFO) von WCS Inc. Im Jahr 2018 nahm Pat an einem Symposium der Harvard Business School
 teil. Der Professor Robert Kaplan von Harvard stellte den Symposiumsteilnehmern ein Management-Tool namens Balanced 
 Scorecard vor. Die Balanced Scorecard enthält laut Kaplan eine Reihe von Leistungskennzahlen, die sorgfältig ausgewählt
  wurden, um wichtige Aspekte einer Geschäftseinheit in den vier Bereichen wirtschaftlicher Erfolg, Kundenbeziehungen, 
  interne Geschäftsprozesse sowie Lernen und Wachstum abzubilden. Diese Kennzahlen sollten die Erfolgsfaktoren der 
  Einheit sein und mit ihrer Strategie und Mission verknüpft werden. 
<br> <br>
Eine kurze Beschreibung jeder Art von Kennzahl folgt unten:
<br> <br>
>__Finanzielle Kennzahlen__ zeigen, wie gut eine Geschäftseinheit ihre Rentabilitäts- und andere wirtschaftliche Ziele 
erreicht. 
><br> <br>
>__Kundenbezogene Kennzahlen__ zeigen den Erfolg einer Geschäftseinheit bei der Gewinnung und Bindung der Kunden.
><br>  
>__Interne Geschäftsprozesskennzahlen__ zeigen die Leistung einer Geschäftseinheit bei Aktivitäten, die entscheidend 
sind, um die Kunden- und Finanzziele zu erreichen.  
><br>
>__Lern- und Wachstumskennzahlen__ zeigen den Erfolg einer Geschäftseinheit bei der Entwicklung des Personals und der 
Systeme, die für langfristiges Wachstum und Verbesserungen erforderlich sind.
<br> 
Das Jahr 2018 war für WCS eher enttäuschend, und Pat entschied sich Anfang 2019, das Konzept der Balanced Scorecard 
auszuprobieren. Dabei waren mehrere Schritte erforderlich. Zunächst traf sich Pat mit dem Top-Management-Team von WCS, 
um die übergeordnete Unternehmensmission zu erläutern. Dieses Team stellte fest, dass die folgende Unternehmensmission 
inspirierend und passend die Unternehmensziele widerspiegelt:
<br>

>_"Wir werden ein herausragender Bekleidungslieferant in jeder der von WCS bedienten Spezialnischen sein."_

<br>
Das Top-Management-Team traf sich anschließend mit jeder Abteilungsleitung, um die unternehmensweite Mission zu 
vermitteln und die Rolle der jeweiligen Leitung bei der Entwicklung einer Balanced Scorecard für ihre Division zu 
besprechen.
Nachdem die divisionalen Scorecards entwickelt worden waren, traf sich jede Abteilungsleitung erneut mit dem 
Top-Management, um die Scorecard der eigenen Division zu erläutern, Fragen zu beantworten und gegebenenfalls notwendige
 Anpassungen vorzunehmen, die vom Top-Management gefordert wurden.
Die Scorecards wurden rechtzeitig für den experimentellen Einsatz im letzten Quartal des Jahres 2019  entwickelt. 
Basierend auf den Erfahrungen von WCS in diesem Quartal wurden die Scorecards für den Einsatz im Jahr 2020 angepasst.
Nachfolgend folgt eine Beschreibung der Erfahrungen jeder Division bei der Entwicklung und Nutzung der Balanced 
Scorecard.

<br> <br>

_RadWear_ 
<br>
Als das Konzept der Balanced Scorecard Chris Peters, der Leitung der RadWear-Division, erklärt wurde, war Chris 
begeistert von der Möglichkeit, die Leistungstreiber der Division genau zu bestimmen. RadWear ist ein relativ neues 
Mitglied der WCS-Nischenfamilie und wurde erst 2015 gegründet. Chris denkt, dass das Balanced-Scorecard-Konzept das 
Potenzial hat, sowohl WCS als auch RadWear zu einer erheblich besseren Leistung beizutragen. 
<br> <br>
Um eine Balanced Scorecard für RadWear zu entwickeln, traf sich Chris zunächst mit dem Management-Team der Division. 
Dieses Team umfasst einen Divisions-Controller, einen Marketing-Manager, einen Einkaufsleiter, einen Personalmanager 
und einen Betriebsleiter der Filialen. 
<br> <br>
Zunächst definierte das Team die Kundschaft von RadWear und analysierte dann die Faktoren, die diese Kundinnen dazu 
bringen, bei RadWear einzukaufen, wiederzukommen und den Anteil ihrer Kleidungseinkäufe bei RadWear zu steigern.
<br> <br>
Das Management von RadWear stellte fest, dass das Wachstum des Unternehmens durch eine aggressive Strategie der 
Eröffnung neuer Filialen erfolgen muss. Zudem wurde erkannt, dass die Anzahl der angebotenen Marken erhöht werden muss,
 um die Aufmerksamkeit der jugendlichen Kundinnen zu gewinnen und ihren Modebedarf bei RadWear zu decken.
 <br> <br>
 RadWear kam zu dem Schluss, dass sein Wettbewerbskreis relativ klein ist, da Jugendliche  nur eine begrenzte Mobilität 
 haben. Diese Strategien und Kundenmerkmale dienten als Grundlage für die Entwicklung der Messgrößen und Zielvorgaben 
 von RadWear’s Scorecard.
 <br> <br>
 Obwohl das Top-Management von WCS einige kleinere Anpassungen forderte, war das Team begeistert von der daraus 
 resultierenden Scorecard und motiviert, dieses neue Management-Tool im Jahr 2020 einzusetzen. Die Zielvorgaben von 
 RadWear’s Scorecard sind in __Anlage 1__ dargestellt.
<br> 

_WorkWear_ <br>
Taylor Graham wurde 2014 Manager der WorkWear-Abteilung. WorkWear ist eine der älteren Abteilungen von WCS und hat 
ihren Betrieb 2009 aufgenommen. Taylor interessierte sich für Pat Jenks‘ Idee der Balanced Scorecard, insbesondere 
weil WorkWear einige neue Geschäftsstrategien in Betracht zog.
<br> <br>
Die Führungskräfte von WorkWear trafen sich, um ihre Kunden  zu definieren und die Faktoren zu bestimmen, die den 
Umsatz bei diesen Kunden steigern könnten. WorkWear verkauft seine Produkte durch direkten Verkaufskontakt mit 
Geschäftskunden. Die Kunden von WorkWear sind daher Geschäftsleiter (oft Personalverantwortliche), die über den 
Lieferanten der Firmenuniformen entscheiden. Diese Manager sind viel beschäftigte Fachleute mit zahlreichen 
Verantwortlichkeiten. Sie möchten in der Regel nur wenig Zeit für die Auswahl und den Kauf von Uniformen aufwenden, 
stellen jedoch hohe Anforderungen an die Haltbarkeit und Reinigungsfähigkeit. Wenn sich die Belegschaft dieser 
Unternehmen verändert, benötigen sie oft in kurzer Zeit neue Uniformen. Die WorkWear-Geschäftsleitung berücksichtigte 
diese Kundenmerkmale bei der Entwicklung ihrer Geschäftsstrategien.
<br> <br>
Obwohl WCS sich historisch auf Damenbekleidung konzentriert hat, entschied sich die WorkWear-Geschäftsleitung, ihren 
Umsatz durch die Aufnahme einiger grundlegender Uniformen für Männer zu steigern. Es wird erwartet, dass dies WorkWear
 als Lieferanten für Unternehmen attraktiver macht, die ihre Uniformen von einem einzigen Anbieter beziehen möchten. 
 Außerdem beschloss WorkWear, einen Katalog zu drucken, damit Kunden einige Bestellungen auch ohne direkten 
 Verkaufsbesuch aufgeben können, insbesondere bei Nachbestellungen oder Ersatzkäufen. Dies sollte dazu beitragen, 
 einige Verkäufe zu halten, die sonst aus Zeitgründen verloren gehen könnten. Diese Strategien und Kundenmerkmale 
 wurden zur Entwicklung der Messgrößen und Zielvorgaben in WorkWears Scorecard herangezogen, die anschließend von der 
 WCS-Geschäftsleitung geringfügig angepasst wurde. Die resultierende Scorecard ist in Anlage 2 dargestellt. Die 
 WorkWear-Mitarbeiter waren mit diesem neuen Werkzeug zufrieden.
<br> <br>
Viele der WorkWear-Messgrößen ähneln denen, die auch bei RadWear verwendet werden. Natürlich unterscheiden sich die 
Kunden von WorkWear und RadWear sowie deren Verkaufsmethoden. Daher sind die gewählten Messgrößen zwar in vielen 
Aspekten ähnlich, aber nicht identisch, ebenso wenig wie die Zielvorgaben. Dies ist angemessen und wurde von der 
WCS-Geschäftsleitung genehmigt.

"""




rad_wear_perform = """
| Kennzahl  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| Ziel für 2020  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
|:-------- | :-------:    |
| _Finanziell:_  |   |  |  |
| 1.  Umsatzrendite (divisionaler NI / divisionaler Umsatz) | 24%   | 
| 2.  Umsatz aus neuen Filialen (% des Umsatzes aus Filialen, die 2020 eröffnet wurden) | 30%    | 
| 3.  Umsatzwachstum ([Umsatz 2020 – Umsatz 2019] / Umsatz 2019)  | 35%    | |
| 4.  Marktanteil bezogen auf Verkaufsfläche (Umsatz / gesamte Verkaufsfläche für Jugendmode im Umkreis von 5 Meilen um die Filialen) | $80     | 
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Kundenbezogen:_  |   |  |  |
| 1.  Bewertung durch Mystery Shopper (siehe Hinweis 1 unten) |85    | 
| 2.  Wiederholungskäufe (% des Umsatzes durch Stammkunden) | 30%     |
| 3.  Rückgaben von Kunden als % des Umsatzes | 12%   | 
| 4.  Kundenzufriedenheitsbewertung (aus einer Kundenumfrage) | 92%     | 
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
|_Interne Geschäftsprozesse:_ |   |  |  |
| 1.  % der Rückgaben an Lieferanten wegen Qualitätsproblemen | 6%    | 
| 2.  Durchschnittliche Anzahl großer Marken pro Filiale  | 32     | 
| 3.  Durchschnittliche Preisnachlässe (Rabatte), um Lagerware zu verkaufen  | 16%    | 
| 4.  % des Umsatzes aus neuen Artikeln, die vom Chefeinkäufer als Marktführer eingestuft wurden  | 25%     | 
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Lernen und Wachstum:_ |   |  |  |
| 1.  Durchschnittliche Betriebszugehörigkeit des Verkaufspersonals (in Jahren) | 1.4    | 
| 2.  # Schulungsstunden pro Mitarbeiter  | 15     | 
| 3.  % der Filialen, die Schlüsselfunktionen laut Geschäftsleitung digitalisiert haben  | 85%   | 
| 4.  # Verbesserungsvorschläge pro Mitarbeiter | 3.3     |

"""

work_wear_perform= """
| Kennzahl  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| Ziel für 2020  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
|:-------- | :-------:    | 
| _Finanziell:_  |   |  |  |
| 1.  Umsatzrendite (divisionaler NI/divisionaler Umsatz) | 24%   | 
| 2.  Umsatz pro Vertriebsbesuch   |$400     |
| 3.  Umsatzwachstum ([Umsatz 2020 – Umsatz 2019] / Umsatz 2019) | 34%    | 
| 4.  Kataloggewinne (% des NI durch Katalogbestellungen) | 6%     |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Kundenbezogen:_  |   |  |  |
| 1.  „Gebundene Kunden“ (% der Kunden, bei denen wir Alleinlieferant sind) |20%    | 
| 2.  Wiederholungskäufe (% des Umsatzes durch Stammkunden) | 25%     | 
| 3.  Empfehlungen (% der Neukunden, die durch Geschäftspartner auf uns aufmerksam wurden)  | 50%   | 
| 4.  Kundenzufriedenheitsbewertung (aus einer Kundenumfrage) | 84%     |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
|_Interne Geschäftsprozesse:_ |   |  |  |
| 1.  % der Rückgaben an Lieferanten wegen Qualitätsproblemen   | 8%    |
| 2.  % der Bestellungen, die innerhalb einer Woche ausgeliefert wurden  | 85%    | 
| 3.  Durchschnittliche Preisnachlässe (Rabatte), um Lagerware zu verkaufen   | 20%    | 
| 4.  Katalogbestellungen mit Fehlern (% der Katalogbestellungen, die falsch ausgeführt wurden)  | 5%     |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Learning and Growth:_ |   |  |  |
| 1.  MBA-Anteil (% der regionalen Vertriebsleiter mit MBA-Abschluss) | 12%    | 
| 2.  # Schulungsstunden pro Mitarbeiter | 12     | 
| 3.  Zertifizierungen (% der Auftragsbearbeiter mit Zertifizierung in Datenbank-Management-Tools) |20%   |
| 4.  # Verbesserungsvorschläge pro Mitarbeiter | 3.1      | 

"""


wcs_performance_noacc = """

Die Gesamtleistung von WCS im Jahr 2020 war gut.  Die Leistung der einzelnen Geschäftsbereiche war jedoch etwas 
uneinheitlich. Die geprüften Scorecards für RadWear und WorkWear, einschließlich der Zielvorgaben und tatsächlichen 
Werte für das Jahr zum 31. Dezember 2020, sind in den Anhängen 4 und 5 dargestellt.
<br>
<br>
Pat Jenks steht nun vor der schwierigen Aufgabe, die Leistung der Abteilungsleiter für das Jahr 2020 zu bewerten. Da 
Chris Peters und Taylor Graham die beiden größten Abteilungen leiten, wird ihnen die meiste Aufmerksamkeit gewidmet. 
Die Ergebnisse der Jahresendbewertungen werden von WCS in mehreren Bereichen genutzt. Sie dienen zur Festlegung von 
Gehaltserhöhungen und Jahresendprämien. Zudem spielen sie eine Rolle bei Entscheidungen über Beförderungen oder 
Versetzungen innerhalb oder aus dem Unternehmen. Darüber hinaus dienen die Leistungsbewertungen als Methode zur 
Rückmeldung und Orientierung für die Abteilungsleiter in Bezug auf ihre Leistungen und zukünftigen Maßnahmen.
<br>
Obwohl Pat eine erste Bewertung vornehmen wird, wird die endgültige schriftliche Beurteilung die Gespräche mit den 
einzelnen Abteilungsleitern berücksichtigen. Daher kann die anfängliche Bewertung aufgrund zusätzlicher Informationen, 
die die Bewerteten liefern, noch angepasst werden. Pat hält es jedoch für wichtig, vor den Gesprächen eine erste 
Bewertung vorzunehmen, um Objektivität und hohe Standards zu wahren. Spätere Anpassungen sollen sicherstellen, dass 
die Bewertungen die spezifischen Umstände der einzelnen Abteilungen fair widerspiegeln.
<br> 
<br>
_Ihre Aufgabe_ 
<br>
Bitte übernehmen Sie die Rolle von Pat Jenks bei der Bewertung der Leistung von Chris Peters und Taylor Graham, den 
Managern von RadWear bzw. WorkWear. Das von WCS verwendete Bewertungsformular ist beigefügt. Denken Sie daran, dass 
dies eine erste Bewertung ist, die nach Verfügbarkeit weiterer Informationen für Jenks angepasst wird. Für jeden der 
Manager sollten Sie eine Gesamtleistungsbewertung angeben.


"""

wcs_performance_pacc = """

Die Gesamtleistung von WCS im Jahr 2020 war gut.  Die Leistung der einzelnen Geschäftsbereiche war jedoch etwas 
uneinheitlich. Die geprüften Scorecards für RadWear und WorkWear, einschließlich der Zielvorgaben und tatsächlichen 
Werte für das Jahr zum 31. Dezember 2020, sind in den Anhängen 4 und 5 dargestellt.
<br>
<br>
Pat Jenks steht nun vor der schwierigen Aufgabe, die Leistung der Abteilungsleiter für das Jahr 2020 zu bewerten. Da 
Chris Peters und Taylor Graham die beiden größten Abteilungen leiten, wird ihnen die meiste Aufmerksamkeit gewidmet. 
Die Ergebnisse der Jahresendbewertungen werden von WCS in mehreren Bereichen genutzt. Sie dienen zur Festlegung von 
Gehaltserhöhungen und Jahresendprämien. Zudem spielen sie eine Rolle bei Entscheidungen über Beförderungen oder 
Versetzungen innerhalb oder aus dem Unternehmen. Darüber hinaus dienen die Leistungsbewertungen als Methode zur 
Rückmeldung und Orientierung für die Abteilungsleiter in Bezug auf ihre Leistungen und zukünftigen Maßnahmen.
<br>
Obwohl Pat eine erste Bewertung vornehmen wird, wird die endgültige schriftliche Beurteilung die Gespräche mit den 
einzelnen Abteilungsleitern berücksichtigen. Daher kann die anfängliche Bewertung aufgrund zusätzlicher Informationen, 
die die Bewerteten liefern, noch angepasst werden. Pat hält es jedoch für wichtig, vor den Gesprächen eine erste 
Bewertung vorzunehmen, um Objektivität und hohe Standards zu wahren. Spätere Anpassungen sollen sicherstellen, dass 
die Bewertungen die spezifischen Umstände der einzelnen Abteilungen fair widerspiegeln.
<br> 
<br>
_Ihre Aufgabe_ 
<br>
Bitte nehmen Sie die Rolle von Pat Jenks bei der Bewertung der Leistung von Chris Peters und Taylor Graham, den 
Managern von RadWear bzw. WorkWear, ein.  Der von WCS verwendete Bewertungsbogen ist beigefügt.  Denken Sie daran, 
dass es sich um eine erste Bewertung handelt, die angepasst wird, sobald Jenks weitere Informationen zur Verfügung 
stehen. Für jeden der Manager sollten Sie eine Gesamtbewertung der Leistung abgeben. Beim Ausfüllen jeder 
Leistungsbewertung werden Sie gebeten, schriftlich zu erklären und zu begründen, wie Sie zu Ihrer Entscheidung gekommen
 sind. Dies ist ein Standardverfahren bei WCS, das dazu dient, Belege für den Leistungsbewertungsprozess zu liefern. Der
  Präsident von WCS wird die ersten Bewertungen der Leistung der Führungskräfte überprüfen, daher ist es wichtig, dass 
  Sie die Bewertungen sorgfältig und präzise ausfüllen.

 

"""

wcs_performance_oacc = """

Die Gesamtleistung von WCS im Jahr 2020 war gut.  Die Leistung der einzelnen Geschäftsbereiche war jedoch etwas 
uneinheitlich. Die geprüften Scorecards für RadWear und WorkWear, einschließlich der Zielvorgaben und tatsächlichen 
Werte für das Jahr zum 31. Dezember 2020, sind in den Anhängen 4 und 5 dargestellt.
<br>
<br>
Pat Jenks steht nun vor der schwierigen Aufgabe, die Leistung der Abteilungsleiter für das Jahr 2020 zu bewerten. Da 
Chris Peters und Taylor Graham die beiden größten Abteilungen leiten, wird ihnen die meiste Aufmerksamkeit gewidmet. 
Die Ergebnisse der Jahresendbewertungen werden von WCS in mehreren Bereichen genutzt. Sie dienen zur Festlegung von 
Gehaltserhöhungen und Jahresendprämien. Zudem spielen sie eine Rolle bei Entscheidungen über Beförderungen oder 
Versetzungen innerhalb oder aus dem Unternehmen. Darüber hinaus dienen die Leistungsbewertungen als Methode zur 
Rückmeldung und Orientierung für die Abteilungsleiter in Bezug auf ihre Leistungen und zukünftigen Maßnahmen.
<br>
Obwohl Pat eine erste Bewertung vornehmen wird, wird die endgültige schriftliche Beurteilung die Gespräche mit den 
einzelnen Abteilungsleitern berücksichtigen. Daher kann die anfängliche Bewertung aufgrund zusätzlicher Informationen, 
die die Bewerteten liefern, noch angepasst werden. Pat hält es jedoch für wichtig, vor den Gesprächen eine erste 
Bewertung vorzunehmen, um Objektivität und hohe Standards zu wahren. Spätere Anpassungen sollen sicherstellen, dass 
die Bewertungen die spezifischen Umstände der einzelnen Abteilungen fair widerspiegeln.
<br> 
<br>
_Ihre Aufgabe_ 
<br>
Bitte nehmen Sie die Rolle von Pat Jenks bei der Bewertung der Leistung von Chris Peters und Taylor Graham, den 
Managern von RadWear bzw. WorkWear, ein.  Der von WCS verwendete Bewertungsbogen ist beigefügt.  Denken Sie daran, 
dass es sich um eine erste Bewertung handelt, die angepasst wird, sobald Jenks weitere Informationen zur Verfügung 
stehen. Für jeden der Manager sollten Sie eine Gesamtbewertung der Leistung abgeben. Nachdem ausfüllen beider
Leistungsbewertungen erhalten Sie ein Feedback und werden gebeten, schriftlich die Qualität Ihrer Bewertungen zu 
erklären und zu begründen. Dies ist ein Standardverfahren bei WCS, das dazu dient, Belege für den 
Leistungsbewertungsprozess zu liefern. 


"""

rad_wear_balanced_scorecard = """
| Kennzahl &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| Ziel  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Tatsächlich  &nbsp; &nbsp; | % besser als Zielvorgabe  |
|:-------- | :-------:    |  :-------: |  :-------: |
| _Finanziell:_  |   |  |  |
| 1.  Umsatzrendite | 24%   | 26%   | 8.33%|
| 2.  Verkäufe in neuen Filialen | 30%    | 31.2%    | 4.00% |
| 3.  Umsatzwachstum  | 35%    | 38%   | 8.57% |
| 4.  Markanteil im Verhältnis zu Einzelhandelsfläche  | $80     | $84.70    | 5.88%|
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Kundenbezogen:_  |   |  |  |
| 1.  Bewertung des Mystery-Shopper Programms    |85    | 91.8   |8.00% |
| 2.  Wiederholte Verkäufe   | 30%     | 34%   | 13.33%|
| 3.  Umtäusche von Kunden in % der Verkäufe   | 12%   | 11.7%   | 2.50% |
| 4.  Bewertung der Kundenzufriedenheit   | 92%     | 95%   | 3.26% |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
|_Interne Geschäftsprozesse:_ |   |  |  |
| 1.  Rücksendung an Lieferanten      | 6%    | 5%   | 16.67% |
| 2.  Durchschnittliche Anzahl großer Marken pro Filiale  | 32     | 36   | 12.50% |
| 3.  Durchschnittliche Preisnachlässe   | 16%    | 13.5%    |15.63% |
| 4.  Verkäufe durch neue Marktführer | 25%     | 27%   | 8.00% |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Lernen und Wachstum:_ |   |  |  |
| 1.  Durchschnittliche Dauer der Betriebszugehörigkeit des Verkaufspersonals  | 1.4    | 1.5  | 7.14% |
| 2.  Schulungsstunden pro Mitarbeiter  | 15     | 17 | 13.33% |
| 3.  Digitalisierung der Filialen  | 85%   | 87.7   | 3.18% |
| 4.  Verbesserungsvorschläge pro Mitarbeiter | 3.3     | 3.5    | 6.06% |

"""

work_wear_balanced_scorecard = """
| Kennzahl  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| Ziel  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Tatsächlich  &nbsp; &nbsp; |  % besser als Zielvorgabe  |
|:-------- | :-------:    |  :-------: |  :-------: |
| _Finanziell:_  |   |  |  |
| 1.  Umsatzrendite | 24%   | 25%   | 4.17%|
| 2.  Einnahmen pro Verkaufsbesuch  |$400     | $433     | 8.25% |
| 3.  Umsatzwachstum  | 34%    | 36%  | 5.88% |
| 4.  Kataloggewinne  | 6%     | 6.5%     | 8.33% |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Kundenbezogen:_  |   |  |  |
| 1.  Gebundene Kunden   |20%    | 22.7%    | 13.50% |
| 2.  Wiederholungskäufe  | 25%     | 27%   | 8.00%|
| 3.  Empfehlungen       | 50%   | 51.6%    | 3.20% |
| 4.  Bewertung der Kundenzufriedenheit  | 84%     | 86%   | 2.38% |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
|_Interne Geschäftsprozesse:_ |   |  |  |
| 1.  Rücksendungen an Lieferanten      | 8%    | 7%  | 12.50% |
| 2.  Bestellungen innerhalb einer Woche bearbeitet   | 85%    | 99%   | 16.47% |
| 3.  Durchschnittliche Preisnachlässe   | 20%    | 18.5%   |7.50% |
| 4.  Katalogbestellungen mit Fehlern  | 5%     | 4.2%    | 16.00% |
| &nbsp;  | &nbsp;  | &nbsp; | &nbsp; |
| _Learning and Growth:_ |   |  |  |
| 1.  Masterabschlüsse in der Betriebswissenschaft   | 12%    | 13.6%  | 13.33% |
| 2.  Schulungsstunden pro Mitarbeiter  | 12     | 13 | 8.33% |
| 3.  Zertifizierungen  |20%   | 21.2%   | 6.00% |
| 4.  Verbesserungsvorschläge pro Mitarbeiter  | 3.1      | 3.2    | 3.22% |

"""

justify_instr = """ Für wie wahrscheinlich halten Sie es, dass Sie Ihre Beurteilungen rechtfertigen müssen?"""

interview_pre_OA = """In dem Bericht, den ich schreiben werde, wird es vorrangig um ... gehen."""

interview_pre_PA = """In den Berichten, die ich schreiben werde, wird es vorrangig um ... gehen."""

interview_post_OA = """In dem Bericht, den ich geschrieben habe, ging es vorrangig um ..."""

interview_post_PA = """In den Berichten, die ich geschrieben habe, ging es vorrangig um ..."""

acc_pre = "Währenden der Aufgabe werde ich mich eher konzentrieren auf..."

task_begin = """ 
Auf der nächsten Seite beginnen die Beurteilungen der beiden Abteilungen."""

mc_begin = """ 
Bevor mit den Beurteilungen der beiden Abteilungen beginnen, haben wir auf den nächsten Seiten noch ein paar Fragen an Sie."""

task_complet = """ 
Sie haben nun die Abteilungen bewertet. Die Studie ist damit beinahe abgeschlossen. <br><br> 
Auf den folgenden Seiten haben wir noch einige Fragen zu Ihrem Fokus bei der 
Aufgabenbearbeitung."""

acc_post = """ Wofür haben Sie sich während der Aufgabenbearbeitung verantwortlich gefühlt?"""

interview_post = """ In dem kommenden Interview wird es vorrangig um ... gehen. """

systematic_information_processing1 = """
Ich werde versuchen, alle möglichen Perspektiven bei den Beurteilungen der Abteilungen einzunehmen.
"""

systematic_information_processing2 = """
Ich werde versuchen, meine Beurteilungen so gründlich wie möglich zu treffen.
"""

systematic_information_processing3 = """
Ich werde mir ausführliche Gedanken machen, bevor ich eine Beurteilung abgebe.
"""

epi_motiv_instr = """
Auf dieser Seite finden Sie einige Aussagen, die sich auf Ihre geplante Vorgehensweise bei der folgenden Aufgabe beziehen.
Wählen Sie dazu die auf Sie passende Antwort durch Anklicken aus. Es gibt keine richtigen oder falschen
  Antworten. Überlegen Sie bitte nicht lange und entscheiden Sie dann, wie stark Sie denken, dass das jeweils beschriebene Vorgehen 
   bei Ihrer eigenen Arbeitsweise vorhanden sein wird.
"""

epi_motiv1 = """
Ich werde mich darum bemühen, alles sorgfältig zu durchdenken.
"""

epi_motiv2 = """
Ich werde diese Aufgabe systematisch angehen.
"""

epi_motiv3 = """
Ich werde versuchen, den logischen Zusammenhang zwischen den Kennzahlen und der Gesamtleistung der Abteilung herauszufinden.
"""

epi_motiv4 = """
Ich werde die Aufgabe analytisch angehen.
"""

epi_motiv5 = """
Ich werde mich sehr auf die einzelnen Schritte konzentrieren, die zur Bewältigung dieser Aufgabe nötig sind.
"""

epi_motiv6 = """
Ich werde versuchen, Regeln herauszufinden, auf die ich meine Beurteilungen gründen kann.
"""

epi_motiv7 = """
Ich werde mich sehr darauf konzentrieren, was ich tue, um eine Antwort auf die Schätzaufgabe zu finden.
"""

epi_motiv8 = """
Ich werde mir meines Denkprozesses sehr bewusst sein.
"""

epi_motiv9 = """
Ich werde Beurteilungen treffen, indem ich sorgfältig alle Informationen analysiere, die mir zur Verfügung stehen.
"""

epi_motiv10 = """
Ich werde klare Regeln verwenden.
"""

## Manipulationskontrolle nach Zhang & Mittal (2005)
MC_PA1 = """
Während ich meine Beurteilungen abgebe, werde ich mich hauptsächlich auf den Prozess meiner Entscheidungsfindung konzentrieren.
"""

MC_OA1 = """
Während ich meine Beurteilungen abgebe, werde ich mich hauptsächlich auf das Ergebnis meiner Entscheidungen konzentrieren.
"""

MC_PA2 = """
Ich werde meinen Entscheidungsprozess rechtfertigen müssen.
"""

MC_OA2 = """
Ich werde die Ergebnisse meiner Beurteilungen rechtfertigen müssen.
"""

MC_PA3 = """
Ich werde mich bemühen, eine gute Strategie für meine Beurteilungen zu finden und nicht darum, möglichst gute Beurteilungen abzugeben.
"""

MC_OA3 = """
Ich werde mich bemühen, möglichst gute Beurteilungen abzugeben und nicht darum, eine möglichst gute Strategie für die Beurteilungen zu verfolgen.
"""

MC_PA4 = """
Ich werde hauptsächlich auf eine möglichst gute Strategie für meine Beurteilungen achten.
"""

MC_OA4 = """
Ich werde hauptsächlich auf das Abgeben möglichst guter Beurteilungen achten.
"""

instruction_STAI ="""
Auf dieser Seite finden Sie einige Gefühlsbeschreibungen, bitte geben Sie an, wie sehr diese <b>im Moment </b> 
auf Sie zutreffen? Wählen Sie dazu die auf Sie passende Antwort durch Anklicken aus. Es gibt keine richtigen oder 
falschen Antworten. Überlegen Sie bitte nicht lange und entscheiden Sie dann, wie stark das betreffende Gefühl im Moment
 bei Ihnen vorhanden ist.
"""

STAI_S1 = """
Ich bin ruhig.
"""

STAI_S2 = """
Ich fühle mich geborgen.
"""

STAI_S3 = """
Ich fühle mich angespannt.
"""

STAI_S4 = """
Ich bin bekümmert.
"""

STAI_S5 = """
Ich fühle mich ungezwungen.
"""

STAI_S6 = """
Ich fühle mich ungezwungen.
"""

STAI_S7 = """
Ich bin besorgt, dass etwas schiefgehen könnte.
"""

STAI_S8 = """
Ich fühle mich ausgeruht.
"""

STAI_S9 = """
Ich bin beunruhigt.
"""

STAI_S10 = """
Ich fühle mich wohl.
"""

STAI_S11 = """
Ich fühle mich selbstsicher.
"""

STAI_S12 = """
Ich bin nervös.
"""

STAI_S13 = """
Ich bin zappelig.
"""

STAI_S14 = """
Ich bin verkrampft.
"""

STAI_S15 = """
Ich bin entspannt.
"""

STAI_S16 = """
Ich bin zufrieden.
"""

STAI_S17 = """
Ich bin besorgt.
"""

STAI_S18 = """
Ich bin überreizt.
"""

STAI_S19 = """
Ich bin froh.
"""

STAI_S20 = """
Ich bin vergnügt.
"""

AC_01 ="""Ich werde diese Studie weiter aufmerksam bearbeiten. Um zu zeigen, dass Sie aufmerksam lesen,
antworten Sie hier bitte mit einem Wert von zwei."""

AC_02 ="""Ich bearbeite diese Studie aufmerksam. Um zu zeigen, dass Sie aufmerksam lesen,
antworten Sie hier bitte mit einem Wert von drei."""

AC_03 ="""Falls Sie weiterhin aufmerksam an der Studie arbeiten, geben Sie hier bitte "999" ein."""


suspicion_check = """
Was glauben Sie, war das Ziel dieser Studie?
"""

comments = """
Haben Sie noch weitere Anmerkungen?
"""

# Self-reported single item (SRSI) indicator Meade and Craig (2012) and Ward and Pond (2015)
srsi = """
Für diese Studie ist es von entscheidender Bedeutung, dass wir nur Antworten von 
Personen einbeziehen, die ihre volle Aufmerksamkeit dieser Studie gewidmet haben.
Andernfalls könnten jahrelange Bemühungen (die der Forschenden und die der anderen 
Teilnehmendenen) zunichtegemacht werden. Ihre Angabe wirkt sich nicht auf Ihre Teilnahme an 
der Verlosung oder Ihre Gewinnchancen aus. 
"""


srsi_question = """
<b>Sollten wir Ihrer ehrlichen Meinung nach Ihre Daten in unseren Analysen dieser Studie 
verwenden?</b><br>
"""


graphic_feedback = """
Diese Grafik zeigt Ihnen, wie akkurat Sie im Vergleich zu den bisherigen Teilnehmenden 
die Beliebtheit der EasyPhones geschätzt haben. Die <b>Mean Absolute 
Deviation (MAD)</b> gibt hier konkret an, wie stark die geschätzten Beliebtheitswerte von den wahren (=tatsächlichen) 
Beliebtheitswerten durchschnittlich abweichen. Sie gibt dabei die Abweichung vom wahren Wert in denselben 
Maßeinheiten in denen die Fragen beantwortet wurden an. In diesem Fall also in Beliebheitswerten von 1 bis 8.
Bei perfekter Übereinstimmung mit den wahren Beliebheitswerten beträgt die MAD 0, umso stärker die Schätzungen von den
wahren Beliebtheitswerten abweichen, desto größer wird die MAD bis zu einem maximalen Wert von 8.<br>. 
Es gilt also: Je kleiner der MAD, desto akkurater sind Ihre Schätzungen im Schnitt gewesen.
"""

feedback_text = """
Sie erhalten nun eine Rückmeldung zu Ihrer Schätzleistung. Hierzu haben wir die 
durchschnittliche Genauigkeit Ihrer finalen Schätzungen im zweiten Versuchsabschnitt
berechnet. Die Angabe erfolgt dabei als mittlere absolute Abweichung (engl.: Mean 
absolute deviation). Ihre finalen Schätzungen wiesen durchschnittlich folgende
Abweichung auf:

<div style="text-align: center;"><b>{mad_self}</b></div>
<br>
Zur besseren Einschätzung dieser Rückmeldung zeigen wir Ihnen nun noch die mittlere
 Abweichung aller bisherigen Teilnehmenden in dieser Studie:
<br><br>
<div style="text-align: center;"><b>{mad_others}</b></div>

"""

registration_selection_content = dict(
    title="Vergütung",
    statustext="Klicken Sie auf 'Weiter', wenn Sie eine Auswahl getroffen haben.",
    instr_selection="<b>Folgende Vergütungsoptionen stehen zur Auswahl:</b>",
    instr_choice="Bitte entscheiden Sie sich für eine Vergütungsoption",
    # The following option needs to be set to the number of options
    # in this dictionary. There can be more options in the dictionary
    # than are shown on the page. You can add configuration blocks for
    # more options and update the available_options setting, whenever
    # necessary
    available_options=5,
    show_option_1=True,
    option_1_instruction="<u>Verlosung: </u><br>"
                         "Wenn sie an der Geldverlosung teilnehmen wollen benötigen wir von Ihnen auf der "
                         " nächsten Seite die Eingabe persönlicher Informationen (Name, Vorname, E-Mail-Adresse). "
                         "Die von Ihnen angegebenen Informationen werden vertraulich behandelt und dienen "
                         "ausschließlich dazu, Sie im Fall eines Gewinnes kontaktieren zu können.",
    option_1_label="Verlosung",
    option_1_register_name=True,
    option_1_register_birth_date=False,
    option_1_register_email=True,
    option_1_register_phone=False,
    option_1_register_iban=False,
    option_1_register_address=False,
    option_1_register_various=False,
    option_1_register_payout=False,

    show_option_2=True,
    option_2_instruction="<u>Versuchspersonenstunden: </u><br>"
                         "Zusätzlich zur Teilnahme an der Geldverlosung haben Sie als "
                         "Göttinger Psychologie-Student*in die Möglichkeit, sich die "
                         "Teilnahme mit 0,5 Versuchspersonenstunden vergüten zu lassen."
                         " Sofern Sie sich für diese Vergütungsoption entscheiden, "
                         "benötigen wir auf der nächsten Seite die Eingabe persönlicher"
                         " Informationen (Matrikelnummer, Name, Vorname, "
                         "E-Mail-Adresse). Die von Ihnen angegebenen Informationen "
                         "werden vertraulich behandelt und dienen ausschließlich der "
                         "Ausstellung ihrer Versuchspersonenstunden.",
    option_2_label="VP-Stunden & Verlosung",
    option_2_register_name=True,
    option_2_register_birth_date=False,
    option_2_register_email=True,
    option_2_register_phone=False,
    option_2_register_iban=False,
    option_2_register_address=False,
    option_2_register_various=True,
    option_2_register_payout=False,

    show_option_3=True,
    option_3_instruction="<u>Keine Verlosungs-Teilnahme</u><br>"
                         "Sie können die Teilnahme an der Verlosung auch ablehnen. In "
                         "diesem Fall werden keine weiteren persönlichen Informationen "
                         "erfragt.",
    option_3_label="Keine Verlosungs-Teilnahme",
    option_3_register_name=False,
    option_3_register_birth_date=False,
    option_3_register_email=False,
    option_3_register_phone=False,
    option_3_register_iban=False,
    option_3_register_address=False,
    option_3_register_various=False,
    option_3_register_payout=False,

    show_option_4=False,
    option_4_instruction="<b>4. Spende: </b>"
                         "Bei der Auswahl dieser Vergütungsoption, werden keinerlei persönliche"
                         "Angaben benötigt. Ein Pauschalbetrag von X € wird an Y pro Auswahl dieser"
                         "Option gespendet.",
    option_4_label="4. Spende",
    option_4_register_name=True,
    option_4_register_birth_date=False,
    option_4_register_email=True,
    option_4_register_phone=False,
    option_4_register_iban=False,
    option_4_register_address=False,
    option_4_register_various=False,
    option_4_register_payout=False,

    show_option_5=False,
    option_5_instruction="This is the instruction for option 5.",
    option_5_label="Itemlabel Option 5",
    option_5_register_name=True,
    option_5_register_birth_date=False,
    option_5_register_email=True,
    option_5_register_phone=False,
    option_5_register_iban=False,
    option_5_register_address=False,
    option_5_register_various=False,
    option_5_register_payout=False,
)

registration_page_content = dict(
    title="Registrierung",
    statustext="Um Ihre Registrierung abzuschließen, klicken Sie auf 'Weiter'.",
    instr_no_registration="Wir benötigen keine persönlichen Daten von Ihnen. "
                          "Sie können auf 'Weiter' klicken.",
    instr_registration="Bitte geben Sie die folgenden persönlichen Informationen ein.",
    first_name_instr="Bitte geben Sie Ihren Vornamen ein",
    last_name_instr="Bitte geben Sie Ihren Nachnamen ein",
    birth_date_instr="Bitte geben Sie Ihr Geburtsdatum ein",
    birth_date_pattern=r"^(0[1-9]|[12][0-9]|3[01])[-/.](0[1-9]|1[012])[-/.](19|20)\d\d$",
    birth_date_suffix="TT.MM.JJJJ",
    birth_date_match_hint="Dies ist der Match-Hinweis für das Feld Geburtsdatum.",
    email_instr="Bitte geben Sie Ihre E-Mail-Adresse ein",
    email_pattern=r"[^@]+@[^@]+\.[^@]+",
    email_match_hint="Bitte geben Sie eine gültige E-Mail-Adresse ein.",
    iban_instr="Bitte geben Sie Ihre IBAN ein",
    iban_pattern=r"^[A-Z]{2}[0-9]{2}(?:[ ]?[0-9]{4}){4}(?:[ ]?[0-9]{1,2})?$",
    iban_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    bic_instr="Bitte geben Sie Ihren BIC ein",
    bic_pattern=r"^[a-zA-Z]{6}[0-9a-zA-Z]{2}([0-9a-zA-Z]{3})?$",
    bic_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    tax_office_instr="Bitte geben Sie den Sitz Ihres Finanzamtes an.",
    phone_instr="Bitte geben Sie Ihre Telefonnummer ein",
    phone_pattern=r"^\+?(?:[0-9]\x20?){6,14}[0-9]$",
    phone_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    street_instr="Bitte geben Sie den Straßennamen ein",
    house_number_instr="Bitte geben Sie die Hausnummer ein",
    postal_code_instr="Bitte geben Sie die Postleitzahl ein",
    postal_code_pattern=r"(?i)^[a-z0-9][a-z0-9\- ]{0,10}[a-z0-9]$",
    postal_code_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    city_instr="Bitte geben Sie den Stadtnamen ein",
    country_instr="Bitte geben Sie den Ländernamen ein",
    various_instr="Bitte geben Sie Ihre Matrikelnummer ein",
    various_pattern=r"^..*$",  # Anything but empty
    various_match_hint="Fehler: Bitte überprüfen Sie Ihre Eingabe.",
    privacy_info="This is a dummy text for privacy information",
    repeated_title="Anscheinend haben Sie bereits an dem Experiment teilgenommen",
    repeated_text="This is a dummy text for the repeated participation page",
    repeated_participation_title="Erneute Teilnahme detektiert",
    repeated_participation_icon="times-circle",
    repeated_participation_message="Es tut uns leid, aber eine wiederholte Teilnahme an diesem "
                                   "Experiment ist nicht erlaubt. Ihre persönlichen Daten werden "
                                   "nicht gespeichert",
)

disclaimerregistr = """<b>Hinweis:</b> Die Verlosung erfolgt, sobald die Datenerhebung abgeschlossen ist. Dies kann 
noch ein paar Wochen dauern. Im Gewinnfall benachrichtigen wir Sie per E-Mail. Die Überweisungen und das Ausstellen der
Versuchspersonenstunden finden blockweise statt. Daher kann es auch hierbei zu Wartezeiten von ein bis zwei Wochen 
kommen. Wir senden Ihne die Bescheinigung über das Ableisten der Versuchspersonenstunde per E-Mail. 
Herzlichen Dank für Ihr Verständnis.
"""

debriefing_text = """
<p> Vielen Dank für Ihre Teilnahme an unserer Studie zum Thema "Bewertung der Unternehmensleistung". <br>

<p>Ziel der Studie ist die Untersuchung der Effekte von Prozess- und Ergebnisverantwortlichkeit auf die Urteilsqualität in Beurteilungsaufgaben.
Prozessverantwortlichkeit bezeichnet dabei die Erwartung, sich vor anderen für die Strategie bei der Bearbeitung einer Aufgabe rechtfertigen zu müssen und nicht für das Ergebnis.
Ergebnisverantwortlichkeit konzentriert sich dagegen ausschließlich auf das Ergebnis der Aufgabe und explizit nicht auf den Weg dorthin. </p>

Wir vermuten, dass sich vor allem Prozessverantwortlichkeit positiv auf die Genauigkeit der Beurteilung im Experiment 
auswirkt und dass kognitive Verzerrungen dadurch reduziert werden. Außerdem gehen wir davon aus, dass dieser Effekt 
durch eine Erhöhung der sogenannten epistemischen Motivation vermittelt wird, also darüber wie sehr Menschen motiviert 
sind, sich tiefgehend und systematisch mit der vorliegenden Aufgabe und den präsentierten Informationen
 auseinanderzusetzen.
 
Die Ankündigung eines Berichts mit Fokus entweder auf dem Prozess oder dem Ergebnis der Urteilsfindung dient dazu, die
 jeweilige Art von Verantwortlichkeit bei Personen in den entsprechenden Experimentalgruppen zu erzeugen. Falls Ihnen 
 kein Bericht angekündigt wurde, waren Sie Teil der Kontrollgruppe. Die Einteilung erfolgt zufällig.


<p>Der grundlegende Nachweis über die Wirksamkeit dieser in der Forschung oft verwendeten Manipulation stellt ein weiteres Ziel dieser Erhebung dar.
Dies soll über Fragen direkt zu Gefühlen der Prozess- und Ergebnisverantwortlichkeit, 
aber auch über die Messung damit zusammenhängender Konstrukte wie situativem Stress zu verschiedenen Zeitpunkten in der Studie geschehen.</p>

<p>In der Aufgabe werden zwei Abteilungen bewertet. Beide Abteilungen zeigen objektiv betrachtet eine sehr ähnliche 
Leistung. Allerdings schneidet eine Abteilung bei den gemeinsamen Kennzahlen besser ab, während die andere in den 
spezifischen Kennzahlen überlegen ist. Menschen neigen dazu, die Abteilung mit den besseren gemeinsamen Kennzahlen 
insgesamt höher zu bewerten – ein Phänomen, das als common measures bias bezeichnet wird. In unserer Studie wird daher 
untersucht, ob Prozessverantwortlichkeit zu einer Reduktion dieser kognitiven Verzerrung führt. </p>

<p><b>Da die Datenerhebung noch nicht abgeschlossen ist, möchten wir Sie bitten, diese Informationen nicht mit potenziellen anderen Teilnehmenden zu teilen.</b><br>
Sollten Sie Fragen zur Studie haben oder nach Abschluss über die Ergebnisse informiert werden wollen, 
wenden Sie sich gerne per Mail an abdul.schamel@stud.uni-goettingen.de</p>


<p>Falls Sie über SurveyCircle teilgenommen haben können Sie den folgenden Survey Code unter 
https://www.surveycircle.com einlösen und durch SurveyCircle kostenlos Teilnehmer für Ihre eigene Studie gewinnen: 2XVP-PY5Y-RWC3-71G5
Sie können den Survey Code auch mit einem Klick einlösen:  https://www.surveycircle.com/2XVP-PY5Y-RWC3-71G5/ 



</p>
"""