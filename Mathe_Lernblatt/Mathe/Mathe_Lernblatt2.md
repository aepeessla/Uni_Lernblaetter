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




1) [Mehrdimensionale Grenzwerte](#Mehrdimensionale_Grenzwerte)



<hr>



<a id="Mehrdimensionale_Grenzwerte"></a>

# **Mehrdimensionale Grenzwerte**

## **Grenzwert bestimmen**

### <u>1) Einf. einsetzten</u>
* Versuchen d. Werte einzusetzen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{wenn } \frac{0}{0}}\ \ \ \ }$ d. 3 Fälle

<hr style="border-color: #d8d8d8ff"></hr>

### 2) <u>Achsen</u>

**1) Fall: Achsen**: 

Wir setzen quazi $x=0/y=0$ & setzen dann den $y,x$-Wert des $\lim$ ein
  * $y=0, x \to \dots$
  * $x=0, y \to \dots$

**2) Fall: Ursprungsgeraden**: 

<b><span style="color: #fc0303;">D. ist keine fertige Lösung, d. zeigt nur, dass wir kein Grenzwert haben. D.h., wenn hier alle Ergebnisse gleich sind, dann muss ich dennoch die anderen Beweise rechnen (Sandwitch-Lemma, Polarkoordinaten)</span></b>

* $y = mx \ \lor x = my$

**3) Fall: Kurven**: 
* wenn **Zähler Pot./Nenner Pot.** sehr unterschliedl.

* $y = x^2 \ \lor x = y^2$

### 2) <u>Abschätzen</u>

<u>Polarkoordinaten</u>

* nur f. **($\mathbf{\lim \to 0,0}$)**

* Wir ersetzten $x$ & $y$
  * $x = r \cdot \cos(\varphi)$
  * $y = r \cdot \sin(\varphi)$
    * d. bedeutet einf. nur, dass $r \to 0$, wobei $\varphi$ variabel bleibt
* <u>Nutzen</u>: $\cos^2(\varphi) + \sin^2(\varphi) = 1$
* <span style="color: #fc0303;">WICHTIG !!! D. Ergebnis am Ende darf </span>$\color{red}\lnot$ <span style="color: #fc0303;">mehr vom Winkel abhängen</span>

<u><b>Sandwich-Lemma</b></u>

* $|\sin(\dots)| \leq 1$ & $|\cos(\dots)| \leq 1$.
* Nenner verkleinern macht den Bruch größer: Da $x^2 \geq 0$ ist, gilt z.B. $x^2 + y^2 \geq y^2$.
* Teilbrüche sind kleiner oder gleich $1$: $\frac{x^2}{x^2+y^2} \leq 1$.

<p>
  <button popovertarget="mehrdimensionale Grenzwerte" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Aufgaben
  </button> 
</p>

<div id="mehrdimensionale Grenzwerte" popover style="padding: 15px; border-radius: 15px; border: 1px solid #ff016fff; max-width: 300px; background-color: #edededff">
  <strong>
  <u>Übung 8</u>
  <p>

  Nr. 3a)
  <img src="image-15.png" alt="Übung 8, Nr. 3a" width="300">
  Nr. 3b)
  <img src="image-17.png" alt="Übung 8, Nr. 3a" width="300">
  Nr. 3c)
  <img src="image-19.png" alt="Übung 8, Nr. 3a" width="300">
</div>





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