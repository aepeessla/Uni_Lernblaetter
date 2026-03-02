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

## Grenzwert bestimmen

### <u>1) Einf. einsetzten</u>
* Versuchen d. Werte einzusetzen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{wenn } \frac{0}{0}}\ \ \ \ }$ d. 3 Fälle

### 1) <u>Achsen</u>

**1) Fall: Achsen**: 

Wir setzen quazi $x=0/y=0$ & setzen dann den $y,x$-Wert des $\lim$ ein
  * $y=0, x \to \dots$
  * $x=0, y \to \dots$

**2) Fall: Ursprungsgeraden**: 


* $y = mx \ \lor x = my$

**3) Fall: Kurven**: 
* wenn **Zähler Pot./Nenner Pot.** sehr unterschliedl.

* $y = x^2 \ \lor x = y^2$

* man kann auch `Sandwitch-Lemma` anw. 











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