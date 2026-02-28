<!-- Style:  -->
<style>
  /* 1. Ebene: Punkt */
  ul { list-style-type: disc; } 

  /* 2. Ebene: Pfeil rechts */
  ul ul { list-style-type: "→ "; }

  /* 3. Ebene: Pfeil rechts (identisch zur 2. Ebene) */
  ul ul ul { list-style-type: "→ "; }
</style>
<!-- Image -->
<style>
  img {
    width: 400px;  /* Alle Bilder werden 300px breit */
    height: auto;  /* Die Höhe passt sich automatisch an (keine Verzerrung) */
  }
</style>
<!-- Textgröße -->
<style>
  body {
    font-size: 13px; /* Verkleinert die Standardschrift von 16px auf 14px */
  }
</style>
<!-- Tabelle -->
<style>
  table {
    width: 100%;
    border-collapse: collapse; /* Verbindet die Ränder zu sauberen Linien */
    font-size: 13px;           /* Schrift verkleinern */
  }

  /* Linien nur an den Seiten der Zellen (Spaltentrennung) */
  th, td {
    border: 1px solid #000;    /* Schwarze Linie um jede Zelle */
    padding: 10px;
    text-align: left;
  }

  /* Bilder skalieren ohne zu schneiden */
  td img {
    width: 120px;
    height: auto;
    object-fit: contain;       /* Skaliert proportional im Rahmen */
    display: block;
  }
</style>
<!-- Lückentext -->
<style>
  .luecke {
    border-bottom: 2px solid #000; /* Der Unterstrich */
    color: transparent;           /* Text am Anfang unsichtbar */
    cursor: pointer;
    padding: 0 5px;
    transition: color 0.3s;       /* Schöner Einblend-Effekt */
  }

  .luecke.offen {
    color: black;                 /* Text wird sichtbar */
    border-bottom: 1px solid #ccc;
  }
</style>



<div id="info-einstein" popover style="padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 0.9em;">
  Einstein war ein theoretischer Physiker und Nobelpreisträger.
</div>



<!-- Der richtige Lerninhalt -->
<table>
  <tr>
    <th></th>
    <th>Eukaryoten</th>
    <th>Prokaryoten</th>
  </tr>
  <tr>
    <td><b>len(Okazaki Fragment)</b></td>
    <td>100 bis 200 Nt</td>
    <td>1000 bis 2000 Nt</td>
  </tr>
  <tr>
    <td><b>len(Primer)</b></td>
    <td>8 bis 11 Nt</td>
    <td>11 bis 12 Nt</td>
  </tr>
  <tr>
    <td><b>Replikationsgeschwindigkeit</b></td>
    <td>2500 Nt/min.</td>
    <td>50.000 Nt/min.</td>
  </tr>
  <tr>
    <td><b>Anzahl pro Replikon</b></td>
    <td>25.000(Maus)</td>
    <td>1</td>
  </tr>
  <tr>
    <td><b>len(Replikons)</b></td>
    <td>150 kb(Maus)</td>
    <td>4.700 (E.Coli.)</td>
  </tr>
</table>



# **DNA POL bei Eukaryoten**

![alt text](image-43.png)

# **Eukaryotische Replikationsgabel**

![alt text](image-44.png)

* Helikase = Reißverschluss öffner
* <span style="background-color: #e6e216; color: #8f8d1a; padding: 0px 5px; border-radius: 2px;">RPA</span>
(Replication Protein A) = d. sind d. einzelstrangbindenden Proteine (**ssb-Protein** (Single-Strand Binding Protein)), d. d. Replikationsgabel aufhalten
* Pol $\epsilon$: $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{synthetisiert}}\ \ \ \ }$ Leitstrang
* Pol $\delta$: $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{synthetisiert}}\ \ \ \ }$ Folgestrang
* <span style="background-color: #e6e216; color: #8f8d1a; padding: 0px 5px; border-radius: 2px;">PCNA</span>(Proliferating Cell Nuclear Antigen) $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{gibt Polymeasen}}\ \ \ \ }$ halt

    * <u><b>Warum so wichtig ?</b></u>
        * nur in aktiven ***teilenden*** Zellen vorhanden
        * kaum in ruhenden
            * <span style="color-background: #7abd2d ; color: #7abd2d">Marker f. Tumorenwachstum </span>
    * <u><b>Was macht es genau ?</b></u>    
        * ❗sorgt dafür, dass d. Polymerase nicht weg fliegt ❗

    <img src="image-53.png" alt="Girl" style="width: 150px;">

    
* POL $\alpha$-Primase $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{setzt}}\ \ \ \ }$ Primer
* <span style="background-color: #e6e216; color: #8f8d1a; padding: 0px 5px; border-radius: 2px;">FEN1</span> (Flap Endonuclease) $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{schneidet}}\ \ \ \ }$ Primer am Ende weg
* DNA-Ligase $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{versiegelt}}\ \ \ \ }$ DNA-Strang

# **Wann weiß d. Zelle, dass d. Replikation zu Ende ist? (Termination)**

* Wenn 2 Teams aufeinanderstoßen
* Vorteil $\to$ kein besonderen Signale notw.

# **Was sind Histonen-Oktamere ?**

* D. ist das fertige Produkt aus einzelnen Histonen 
* besteht aus $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{jeweils einer Kopie}}\ \ \ \ }$ v. 4 Proterinen
    * $H2A$, $H2B$, $H3$ und $H4$.

![alt text](image-45.png)

# **Was kann geschehen, wenn d. nicht so läuft wie geplant ?**

**<u>Progerie</u>**
* <u>Was macht es ?</u>
    * Kinder $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{altern}}\ \ \ \ }$ schneller
* <u>Grund ?</u>
    * Helikase-Defekt
* <u>Was geschieht ?</u>
    * Replikationsgabel $\lnot$ sauber $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{entstehung}}\ \ \ \ }$ DNA-Brüche
    * man benötigt Helikase $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{entwirren}}\ \ \ \ }$ Telomere
        * wenn Helikase $\lnot$ richtig funktioniert $\implies$ Telomere verkürzen schneller als normal $=$ schnellere Alterung

**<u>Ophtalmoplegia</u>**
* <u>Was macht es ?</u>
    * Augenmuskelatur $\implies$ gelähmt $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Grund}}\ \ \ \ }$ Mitochondrien funk. $\lnot$ richtig $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{weil}}\ \ \ \ }$ DNA Pol $\gamma$-Defekt
* <u>Warum ausgerechnet d. Augenmuskelatur ?</u>
    * manche Gewebe = Energie-Junkie(benötign viel ATP) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{führt zu}}\ \ \ \ }$ ATP-/Energie-Mangel $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Augenmuskeln}}\ \ \ \ }$ schalten ab $\implies$ Lähmung

<u>**Was genau wird mit Krebs assoziiert ?**</u>
* DNA Pol $\gamma$ mut.
* erhöhte Expression v. DNA $\beta$

# **Wrm. werden Telomere immer kürzer ?**

* Primerentf.  $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{verkürzt}}\ \ \ \ }$ Chromosomen $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{pro}}\ \ \ \ }$ Replikation

![alt text](image-46.png)

# **Wie verhindert d. Zelle dieses Problem ?**

* an den Enden $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{hinzugef.}}\ \ \ \ }$ Telomere $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{durch}}\ \ \ \ }$ Telomerasen $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{Grund}}\ \ \ \ }$ Verlustvermeidung

* Telomere $\underrightarrow{\ \ \ \ \textcolor{#d6b315}{\text{bestehen}}\ \ \ \ }$ <span style="color: #6c6ee0;">simplen, tandem-repetitiven Seq.</span>
    * Bsp. bei Mensch: $\color{red}(TTAGGG)_{n = ca. 2000}$

![alt text](image-47.png)


# **Telomerase**

## **<u>Das End-Replikationsproblem</u>**
<u>Was ist das grundlegende Problem bei der Replikation linearer Chromosomen?</u>

* lineare Chromosomen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Problem}}\ \ \ \ }$ Primerentf. am Folgestrang $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Folge}}\ \ \ \ }$ Chromosomen verkürzen sich bei jeder Replikation

## <u>**Was ist d. Lösung ?**</u>

* Chromosomenenden $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{besitzen}}\ \ \ \ }$ Telomere (z.B. $TTAGGG_n$) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{verlängert durch}}\ \ \ \ }$ Telomerase $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Ergebnis}}\ \ \ \ }$ Kompensation des DNA-Verlusts

## <u>**Was ist die Telomerase & wie funktioniert sie biochemisch?**</u>

* Telomerase $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{ist ein}}\ \ \ \ }$  <span style="color: #fc0303;">Ribonukleoprotein</span> $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{besteht aus}}\ \ \ \ }$  Protein ($\colorbox{red}{TERT}$) + RNA-Anteil ($\colorbox{red}{TERC}$)
* $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{nutzt}}\ \ \ \ }$  eigene RNA ($TERC$) als Matrize f. DNA-Synthese
* Arbeitsweise: Telomerase $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{verlängert aktiv}}\ \ \ \ }$  den 3'-Überhang (Matrizenstrang) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{danach}}\ \ \ \ }$  Primase & DNA-Polymerase füllen den Folgestrang auf

<span style="font-size: 8px;">TERT= Telomerase Reverse Transcriptase; TERC = Telomerase RNA Component</span>

## <u>**Wie schützt die Zelle ihre offenen DNA-Enden vor dem Abbau oder falscher Reparatur?**</u>

* Telomer-DNA $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{bildet}}\ \ \ \ }$  `T-Loop` (Schleife) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Funktion}}\ \ \ \ }$  versteckt das offene Ende & reguliert Telomerase-Aktivität
* `SHELTERIN-Komplex` (z.B. $TRF1/TRF2$) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{bindet an}}\ \ \ \ }$  `T-Loop` $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Funktion}}\ \ \ \ }$  versiegelt das Ende & schützt vor unbeabsichtigter DNA-Reparatur

* `TRF1` = reguliert len(Telomere)
* `TRF2` = Stabilität
    * hilft T-loop zu bilden

<span style="font-size: 8px">TRF = Telomere Repeat binding Factor, SHELTERIN-KOMPLEX bei Eukaryoten</span>

![alt text](image-50.png)

## <u>**Was würde ohne T-loop geschehen & was ist mit unbeabsichtigter DNA-Reparatur gemeint?**</u>

* Reperaturenzyme versuchen d. Enden mit einem anderen Ende zu verkleben $\implies$ Chromosomen würden verschmelzen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{bildet}}\ \ \ \ }$  `T-Loop` (Schleife) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{nächste Zellteilung}}\ \ \ \ }$ Zerstörung des Erbguts
* Zelle könnte v. Außen n. Innen anfangen, d. DNA abzubauen


## <u>**Wie erkennen Telomerase-Enzyme, wann sie abbrechen müssen?**</u>

* Telomere $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{prod. gleichzeitig}}\ \ \ \ }$  **long non-coding RNA** (<p>
  <button popovertarget="TERRA" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Terra
  </button> 
</p>

<div id="TERRA" popover style="padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 0.9em;">
  Also ist TERRA wie der Manometer bei der Heizung. TERRA wird immer prod., wenn Telomerase aktiv ist. TERRA wird v. einem RNA-Polymerase synthetisiert. Wenn Telomer so kurz ist, dass sich dann auch TERRA verändert, weiß d. Zelle, dass d. Zeit gekommen ist zu sterben.
</div>)

1) **Embryonalphase**:
* Zelle teilt sich rasant $\to$ Telomerase hochaktiv $\implies$ End-Replikations-Problem sofort behoben
2) **Geburt**:
* Zelle wandelt sich um zu einer somatischen Zelle \to Gen f. Telomerase wird abgeschaltet $\implies$ Telomerase verschwindet aus d. Zelle
3) **Erwachsenenleben**:
* regelmäßige Zellteilung $\to$ jede Replikation = Verust des Endes $\implies$ Telomer immer kürzer
4) **Das Hayflick-Limit wird erreicht (Kritische Telomerkürze)**:
* n. 50 bis 70 zellteilungen Limit erreicht $\implies$ Telomer zu kurz, um T-loop zu bilde; SHELTERIN-Komplax verlieren halt
5) **Zellulär Alarm(TERRA greift ein)**:
* Zelle = Panik $\to$ fährt TERRA-Prod. drastisch hoch $\to$ nackte Chromosomenende v. Zelle als lebensbedrohlichen DNA-Doppelbruch intepretiert $\to$ DNA-Schaden-Kontrollpunkt wird aktiviert
6) **Endstsadium**:
* Seneszenz
* Apoptose

* verkürzte Telomere $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{nutzen}}\ \ \ \ }$  $TERRA$ $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{lockt an}}\ \ \ \ }$  `Telomerase` $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{verhindert}}\ \ \ \ }$  vorzeitige Seneszenz

* `TERRA` $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{kann hemmen}}\ \ \ \ }$ Telomerase synthetisiert $\lnot \infty$

<span style="font-size: 8px">TERRA = Telomeric Repeat-containing RNA, Seneszenz = Zelle hört auf sich zu teilen, stirbt aber $\lnot$ sofort ab</span>


## <u>**Warum altern unsere Zellen?**</u>
* `Somazellen` $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{schalten ab}}\ \ \ \ }$  `Telomerase` (n. d. Geburt) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Folge}}\ \ \ \ }$  Telomere *verkürzen* sich stetig
* Kritische Verkürzung $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{führt zu}}\ \ \ \ }$  Teilungsstopp (<b><span style="color: #fc0303;">Hayflick-Limit</span></b>, ca. 100 Mitosen) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Ergebnis}}\ \ \ \ }$  Zelluläre Seneszenz

## <u>**Welche Zellen altern nicht und warum?**</u>

* Keimzellen & Krebszellen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{besitzen}}\ \ \ \ }$  aktive Telomerase $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Folge}}\ \ \ \ }$  unbegrenzte Zellteilung (unlimited proliferation)
* Somazellen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Telomere abgestellt}}\ \ \ \ }$  ist eine evolutionäre Strategie $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Zweck}}\ \ \ \ }$  Tumorunterdrückung (da 85% aller Tumore Telomerase+ sind)
 
![alt text](image-48.png)
![alt text](image-49.png)

## <u>**Zusammenfassung**</u>
Also, d. Problem ist eigentlich nur, dass d. codierende Seq. im **Folgestrang** $\lnot$ synthetisiert werden kann, weil d. `Primase` keinen Platz hat eine neuen `Primer` zu setzten, d. dann d. `DNA-Polymerase` ermöglicht, den letzten codierenden Rest zu transkribieren. D. `Telomerase` fügt hierfür d. Telomer im Leitstrang hinzu, damit d. `Primase` mehr Platz hat, um einen Primer hinter d. codierenden Seq. zu setzten und den codierenden Teil zu synthetisieren.

Das Problem ist nur, dass d. `Telomerase` bei `Somazellen` n. d. ***Geburt abgeschaltet*** wird & d. Zeit ab diesem Zeitpunkt anfängt zu schlagen, welches man als Countdown sehen kann, d. bis zum endgültigen Zelltot runterzählt. D. `Telomere` werden quazi bei jeder Zellteilung kürzer, weil keine Telomerasen vorhanden sind, d. d. fehlenden Lücken beheben kann. Grund für ***Alterung***. 

<table>
  <tr>
    <th>Merkmal</th>
    <th>Keimzellen (Spermien/Eizellen)</th>
    <th>Somazellen (Körperzellen)</th>
  </tr>
  <tr>
    <td><b>Telomerase-Aktivität</b></td>
    <td>Hochaktiv</td>
    <td>Inaktiv (abgeschaltet nach der Geburt)</td>
  </tr>
  <tr>
    <td><b>Telomer-Länge</b></td>
    <td>Bleibt über Generationen identisch lang</td>
    <td>Wird bei jeder Zellteilung kürzer</td>
  </tr>
  <tr>
    <td><b>Konsequenz</b></td>
    <td>"Unsterblichkeit": Informationen werden verlustfrei an Kinder weitergegeben</td>
    <td>Begrenzte Lebensdauer: Zellen altern und gehen in Seneszenz</td>
  </tr>

</table>


# **DNA-Amplifikation**

## <u>**Wie und warum kommt es zur gezielten DNA-Amplifikation in Eukaryoten?**</u>

* Physiologisch $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{nutzt}}\ \ \ \ }$ selektive Über-Replikation definierter Genom-Abschnitte $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Zweck}}\ \ \ \ }$ Erhöhung der Gendosis für starke Proteinproduktion (z.B. rRNA-Gene in Amphibien-Oocyten)
* Pathologisch $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{passiert bei}}\ \ \ \ }$Mutationsereignissen in Krebszellen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Folge}}\ \ \ \ }$ Amplifikation von Onkogenen (sichtbar als HSR oder "Double Minutes")

## <u>**Was sind Onkogene?**</u>
* natürl. Gene, d wachstumsfördernd sind
    * geben Zelle d. Signal zur Teilung

## <u>**Wie stoppen Medikamente wie Acyclovir oder AZT die Virusvermehrung?**</u>

* Medikament $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{besteht aus}}\ \ \ \ }$ `Nukleotidanaloga` (<span style="font-family: script MT">synthetische Arzneistoffe, d. natürl. Bausteinen von DNA/RNA ähneln, aber modifiziert sind</span>) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{eingebaut durch}}\ \ \ \ }$ virale Polymerasen / Reverse Transkriptase (z.B. $AZT$ bei $HIV$) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Folge}}\ \ \ \ }$ Kettenabbruch bei viraler Replikation

## <u>**Wie wird der Übergang zwischen den verschiedenen Zellzyklus-Phasen gesteuert?**</u>

* Zellzyklus $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{kontrolle durch}}\ \ \ \ }$ `CDK-Cyclin-Komplexe`
* Komplex-Aufbau $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{besteht aus}}\ \ \ \ }$ `Cyclin` (regulatorisches Protein) + $CDK$ (cyclinabhängige Kinase)
* Mechanismus $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{aktiver Komplex}}\ \ \ \ }$ phosphoryliert Zielproteine $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Ergebnis}}\ \ \ \ }$ Auslösung des nächsten Zellzyklus-Schritts (z.B. Eintritt in die S-Phase)

## <u>**Wie verhindert der "Wächter des Genoms" (p53) die Replikation von defekter DNA?**</u>

* DNA-Schaden $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{führt zur}}\ \ \ \ }$ Aktivierung von **p53** $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{aktives p35}}\ \ \ \ }$ bindet an Regulationsbereich des **p21-Gens** $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Zelle prod.}}\ \ \ \ }$ **p21** (ein Cdk-Inhibitorprotein) $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{p21 blockiert}}\ \ \ \ }$ den `Cyclin-Cdk-Komplex` der S-Phase $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Ergebnis}}\ \ \ \ }$ Eintritt in S-Phase wird verhindert


* <span style="color: #fc0303; font-family: Courier New">Kinasen aktiviert & Inhibitoren blockieren</span>

## <u>**Zusammenfassung.:**</u>
<p>
  DNA-Amplifikation ist im Grunde die gezielte, massenhafte Kopierung eines DNA-Abschnitts. 
  Das ist wie eine 
  <span class="luecke" onclick="this.classList.toggle('offen')">Polysom</span>, 
  bei der DNA-Polymerasen den Zielabschnitt exponentiell vervielfältigen.
</p>

![alt text](image-55.png)

# Gentechnologie

## <u>**Was ist klassische Genetik ?**</u>

* Herstellung neu rekombinierter DNA-Moleküle aus derselben Art oder unterschiedl. Arten.
* <span style="color: #dfcb1b">Transfergene</span>
    * rekombinierte DNA $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{geg.}}\ \ \ \ }$ Organismen

## <u>**Wrm. ist Gentechnik mögl.?**</u>
* $\forall$ Organismen = DNA $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Speicher}}\ \ \ \ }$ f. Erbinfo.

## <u>**Klassisches Züchten**</u>
Mutter Pferd ($2n = 64$) + Vater Esel ($2n = 62$) = Maultier

## <u>**Mutationen**</u>
* <u>Mensch</u>:
    * ~ $60$ Neumut. beim Baby
* <u>Weizen</u>:
    * $\gt$ $100$ Neumut. bei Pflanze
 
## <u>**Mut. Züchtung**</u>
Man erhöht künstl. d. Mut.rate durch radioaktive Strahlen $\implies$ ca. $1000 \times$
* $\gt$ 3400 Sorten im Markt
* DNA-Transfer/Neu/-Rekombination finden bereits auch in d. Natur statt
* **konventionelle Züchtung**:
    * Individuen mit gewünschten Eigenschaften (z. B. besonders große Früchte) miteinander gekreuzt $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Problem}}\ \ \ \ }$ Durch d. Kreuzung werden ungezielt Tausende unterschiedl. Gene neu kombiniert. Man weiß also nicht genau, welche Gene man am Ende erhält, und muss hoffen, dass d. beste Kombination dabei ist
* **Mutagenese**:
    * d. künstl. Erhöhung d. Mutationsrate durch Radiation, um neue eigenschaften zu erzeugen

![alt text](image-56.png)

# **Restriktionsenzyme**

![alt text](image-57.png)

## <u>**Was machen Restriktionsnukleasen ?**</u>
* schneiden eindringende fremde DNA in Bakterien
* Methylierung dient auch hier als Schutz oder Stempel

## <u>**Wie schneiden Restriktionnukleasen d. DNA ?**</u>
* <span style="color:red">sequenzspezifisch</span> 
    * $GAATTC$ = palindromisch
    * hier sind es <span style="color:red">sticky ends</span>
        * es gibt auch glatte Enden = <span style="color:red">blunt ends</span>
![alt text](image-58.png)

## <u>**Wann sind 2 Restiktionsenzyme kompartible ?**</u>
* wenn sie id. ü.hänge hinterlassen

## <u>**Was genau bedeutet hier palindromisch  ?**</u>
* Seq. auf Leitstrang muss id. auf dem Folgestrang sein $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{gelesen}}\ \ \ \ }$ $5' \to 3'$

# **DNA-Ligase**
![alt text](image-59.png)
## <u>**Mehrere Mögl. d. Ligase**</u>:

![alt text](image-60.png)

## <u>**Wie findet man d. jenige Bakterien, d. rekombinante Moleküle aufgebnommen haben ?**</u>:
1) <u>Selektion</u>:
    * Resistenzgen wird auf alle Bakterien gestrichen $\implies$ nur Bakterien, d. Plasmid aufgenoommen haben ü.leben
1) <u>Screening</u>:
    * Reportergene ($lacZ$)
    * Blau-Weiß-Screening:
        * Gen f. Enzym $\beta-Galaktosidase$ ($lacZ$) liegt genau an d. Stelle, wo man den Gen einf. möchte
            * wenn blau $\implies$ $lacZ$ intakt $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{sapltet Farbstoff}}\ \ \ \ }$ Kolonie wird blau
            * wenn weiß $\implies$ wunschgen erfolgr. eingebaut, weil lacZ-Gen unterbrochen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{Kein Enzym, um Farbstoff zu spalten}}\ \ \ \ }$ Kolonie bleibt weiß
    * <u>Fluoreszenz (GFP)</u>: 
        * Ein anderer Reporter = Grün-fluoreszierende Protein"
            * Bakterien $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{leuchten unter UV-Licht}}\ \ \ \ }$ grün

## <u>**Was sind Vektoren ?**</u>:

![alt text](image-61.png)
![alt text](image-64.png)
![alt text](image-65.png)
![alt text](image-66.png)
![alt text](image-67.png)
![alt text](image-68.png)
![alt text](image-69.png)
![alt text](image-70.png)
![alt text](image-71.png)
![alt text](image-72.png)
![alt text](image-73.png)
![alt text](image-74.png)
![alt text](image-75.png)
![alt text](image-76.png)
![alt text](image-77.png)
![alt text](image-78.png)






































































<script>
  MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    svg: {
      fontCache: 'global'
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>