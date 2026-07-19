<style>
  details {
    margin-bottom: 7px  ;
    border: lightgrey 1px solid;
    padding: 8px
}
  summary {
    font-size: 20px
  }
  img {
    width: auto;
    height: auto;
  }

  code {
    background: #eeeeeeff 2px;
    padding: 2px 2px 2px 2px;
    border-radius: 6px
  }

  body {
    background: #ffffffff;
    color: #000000ff;
  }

  h1 {
    font-weight: bold;
    text-decoration: underline;
  }

  h2 {
    font-weight: bold;
    text-decoration: underline;
  }

  h3 {
    font-weight: bold;
    text-decoration: underline;
  }
  
  /* Zielvorgabe für alle Blockquotes */
  blockquote {
    border-left: 5px solid #7cb459ff; /* Ein farbiger Strich links */
    padding-left: 20px;             /* Abstand zum Text */
    background-color: #edfbeaff;      /* Ein leichter Hintergrund */
    margin-left: 10px;              /* Die eigentliche Einrückung */
    color: #333;                    /* Textfarbe */
  }

  /* Optional: Wenn du das Aussehen der Liste im Blockquote verändern willst */
  blockquote ul {
    list-style-type: square;
  }


  ul li, ol li {
    margin-top: 20px; /* Gewünschten Abstand hier anpassen */
  }

  .a1 {
    font-weight: bold;
    text-decoration: underline;
  }

  .mermaid {
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  }

  .r {
    background: #b7e99bff
  }

  .f {
    background: #e99b9bff
  }
  .n {
    background: #9bb5e9ff
  }
  .w{
    background: #ff0090ff
  }
</style>

# Aufgabe 2

![alt text](image-10.png)

## 1. `val s = Seat("2","8")`

* Das Problem ist, dass die Parameter der Klasse `Seat` die Datentypen <code style="color: rgb(76, 215, 58)">Int</code> haben müssen, welches eine ganze Zahl repräsentiert. Die ü.geb. Parameter jedoch haben den Datentyp <code style="color: rgb(76, 215, 58)">String</code>. Somit muss der ü.geb. Datentyp __IMMER__ ein  <code style="color: rgb(76, 215, 58)">Int</code> sein !

* <span class="a1">Lösung</span>:
    ```scala
    val s = Seat(2,8)
    ```

___
## 2

```scala
def describe(seat: Seat): String = 
    s"row seat.row, seat seat.number"
```
* D. Problem hierbei ist, dass wir `s` autom. `.toString` repräsentiert, wobei es den eingegeben Text zu einem reinen String macht. Das war wir machen müssnen ist, die Platzthalter in ${} schreiben müssen. Somit führt Scala zunächst einmal den Ausdruck in den Klammern und fügt das Ergebnis mit dem String zu einem einzelnen String zusammen.

* <span class="a1">Lösung</span>:
    ```scala
    def describe(seat: Seat): String = {
        s"row ${seat.row},  seat ${seat.number}"
    }
    ```

## <span class="f">3  </span>

* Es handelt sich um eine <span style="color: red">normale Klasse</span>, nicht um eine case class. 
* Scala (und Java) $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{vgl.}}\ \ \ \ }$ __normale Klassen__ $\implies$ __Referenzidentität__ (Speicheradresse)
    * Da `wanted` = <span style="color: red">neu erzeugtes Objekt</span> $\implies$ andere __Speicheradresse__ als das Objekt, das in der Map liegt
        * deshalb liefert `contains` d. Ergebnis <code style="color: rgb(76, 215, 58)">False</code>

* <span class="a1">Lösung</span>: `case class` def. (`case class Seat(row: Int, number: Int)`), da Case Classes autom. strukturelle Gleichheit (equals und hashCode) implementieren


# Aufgabe 3)

![alt text](image-11.png)

## 1

```scala
case class Temperature(celsius: Double) extends Ordered[Temperature] {
    override def compare(that: Temperature): Int =
        if (this.celsius < that.celsius) {
            -1
        } else if (this.celsius > that.celsius) {
            +1
        } else {
            0
        }
}
```
# <span class="f">4  </span>
* `Ordered[Temperature]` = <span style="color: red">Trait von Scala</span>
    * enthält bereits die vollständige, fertige Logik für sämtliche Vergleichsoperatoren (<, <=, >, >=)
        * Diese Operatoren sind dort so def., dass sie intern einfach compare aufrufen & d. Ergebnis auswerten (z. B. ist a < b intern definiert als a.compare(b) < 0). Sobald du also compare implementierst, funktionieren alle anderen Operatoren autom. „out of the box“.

* durch Erben v. `Ordered[Temperature]` (`extends Ordered[...]`) $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{meine Klasse bekommt bereitgestellt}}\ \ \ \ }$ Methode compare

### Eselsbrücke:

>* __Trait__ (Ordered): Das Wort ist ein Eigenschaftswort (Adjektiv)
>    * beschreibt eine Fähigkeit
>    * Wenn eine Klasse Ordered implementiert, bedeutet das einfach nur: „Man kann Objekte dieser Klasse miteinander vergleichen (größer, kleiner, gleich).“
>
>* Die __Datenstruktur__ (z. B. List, Set, Tree): Das sind Hauptwörter (Substantive). Das sind die tatsächlichen Behälter, in denen man ganz viele Temperaturen speichert.

















<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    }
  };
</script>
<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>