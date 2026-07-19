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

* Das Problem ist, dass die Parameter der Klasse Seat die Datentypen <code style="color: rgb(76, 215, 58)">Int</code> haben müssen, welches eine ganze Zahl repräsentiert. Die ü.geb. Parameter jedoch haben den Datentyp <code style="color: rgb(76, 215, 58)">String</code>. Gleichzeitig wurden die Parameter `row` & `number` mit <code style="color: rgb(112, 132, 231)">val</code> deklariert, welches bedeutet, dass es eine <span style="color: red">unveränderliche Variabel</span> ist. Somit muss der ü.geb. Datentyp __IMMER__ ein  <code style="color: rgb(76, 215, 58)">Int</code> sein !

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

Das Probelm hiebei ist, dass bei der Kontrolle nicht auf den Seat selbst zugegriffen wird, sondern auf seinen Value. D.h., dass bei Seat(2,8) garnicht auf das Seat-Objekt selbst geschaut wird, sondern auf seinen Wert "Jonas", welches nicht als key enthalten ist. 

* <span class="a1">Lösung</span>:
    ```scala
    val wanted = Seat(2,8)
    println(Reservations.contains(wanted))
    ```





















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