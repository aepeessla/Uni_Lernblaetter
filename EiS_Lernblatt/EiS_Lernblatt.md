# **(Un-)Veränderlichkeit**
## <u>Mutuble</u>
* `var`
## <u>Unmutuble</u>
* `val`


# **Typisierung**
* statisch
```scala
@main def start() =
  var a: Int = 42
  println(a)
  println(a.getClass)

// Ausgabe

42
Int
```
* auch wenn ich $\lnot$ den Typ angebe, wird es autom. ü.nommen -> <b><span style="color: #fc0303;">Typinferenz</span></b>
```scala
@main def start() =
    var a = 42
    println(a)
    println(a.getClass)
// Ausgabe
42
int
```
## <u>Typenumwandlung(Casts)</u>


# **Veränderlichkeit & unveränderlichkeit**


* Klasse $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{text}}\ \ \ \ }$ rationale Zahlen
* zähler: Int
* nenner: Int; > 0
* Operation: Addition, Kürzen
* 2 Arten: Objekt darf n. Operationen verändern oder $\lnot$ verändern

```
• Primzahlfaktorzerlegung
• wenn beide d. gleiche Primzahlen haben, dann damit den Nenner und den Zähler teilen

Primzhal oder nicht ?

ist meine Zahl durch eine Zahl durch [2,sqrt(n) teilbar ?, wenn ja keine Primzahl, wenn ja, dann Primzahl]
```














<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>