<style>
  code {
    background-color: #e9e9e9ff;
    color: #999999ff;
    padding: 2px 6px;          /* Ein bisschen Abstand, damit es gut aussieht */
    border-radius: 3px;  
       }
  details {
    border: #e4e3e3ff 1px solid;
  }

  h1 {
    text-decoration: underline;
    font-weight: bold;
  }

  h2 {
    text-decoration: underline;
    font-weight: bold;
  }

  h3 {
    text-decoration: underline;
    font-weight: bold;
  }

  body{
    background: #ffffff;
    color: black;
  }

  .sub {
    font-weight: bold;
    text-decoration: underline
  }



  .richtig { color: green; font-weight: bold; }
  .falsch { color: red; font-weight: bold; }
</style>


<details>
<summary><u><b>Was muss ich verwenden, wenn ich eine Liste für Key-Value-Parre verwenden möchte ? </b></u></summary>

* `Map`
    <details>
    <summary><u><b>Wie mache ich sie veränderlich ?</b></u></summary>

    * <input type="text" id="eingabe" placeholder="Wort eingeben...">
      <div id="ergebnis"></div>

      <script>
          const musterloesung = "scala.collection.mutable.Map"; // Hier das Zielwort definieren
          const inputFeld = document.getElementById("eingabe");
          const ergebnisDiv = document.getElementById("ergebnis");

          inputFeld.addEventListener("keypress", function(event) {
              if (event.key === "Enter") {
                  const nutzerEingabe = inputFeld.value;
                  
                  if (nutzerEingabe === musterloesung) {
                      ergebnisDiv.innerHTML = `<span class="richtig">Richtig!</span>`;
                  } else {
                      ergebnisDiv.innerHTML = `<span class="falsch">Falsch!</span> Das Wort war nicht "${nutzerEingabe}".`;
                  }
              }
          });
      </script>

    </details>
</details>

<details>
<summary><u><b>Du hast eine Liste: <code>scala.collection.mutable.Map[A]</code> & möchtest den Wert bekommen, wenn es nicht vorhanden ist, dann soll (0: Long) zurückgegeben werden, wann es vorhanden ist, dann soll der Wert zurückgegeben werden.</b></u></summary>

* `val current_count = <list>.getOrElse(key, 0L)`
</details>

<details>
<summary><u><b>Entpackt .getOrElse() automatisch oder muss muss ich es mit .head extrahieren ?</b></u></summary>

* Ja, d- Elem. wird als "nacktes" Elem. extrahiert
</details>

<details>
<summary><u><b>Wie macht man aus einer Liste eine String-Repräsentation ?</b></u></summary>

* `<list>.mkString(<Was soll am Angfang stehen>, <Wie sollen die Elemente getrennt werden>, <was soll am Ende stehen>)`
</details>

<details>
<summary><u><b>Wie funktioniert <code>override def equals(obj: any): Boolean = ???</code> ?</b></u></summary>

* Wir vgl. unser aktuelle Objekt(`this`) mit einer anderen(`obj`)
  <details>
  <summary><u><b>Wie wird `equals` aufgerufen ?</b></u></summary>

  ```scala
  <obj1>.equals(<obj2>)
  ```
  </details>

  <details>
  <summary><u><b>Wie guckt man, ob das ü.geb. Objekt den gleichen Typ hat ?</b></u></summary>
  
  * <span class="sub">Bsp.</span>: wir haben eine `class Counter(inhalt: Iterable[A])`
    * wir haben also eine Objekt mit dem Typen Counter
  * <span class="sub">Kontrolle</span>:
    ```scala
    obj match {
      case other: Counter[_] => <tatsächl. Vgl.>
      case _ => false
    }
    ```
  </details>
</details>


<details>
<summary><u><b>Wie erstelle ich meinen eigenen <code>hashCode</code> ?</b></u></summary>

* wir packen d. __einzelnen Parameter__ d. Klasse oder jegliches <span style="color: red">in einen Tupel</span> & fügen am Ende `.##` hinzu
  
  * <span class="sub">Bsp.</span>:
    ```scala
    class Person(val vorname: String, val nachname: String, val alter: Int) {
      override def equals(obj: Any): Boolean = {
          obj match {
              case p: Person => vorname == p.vorname && nachname == p.nachname && alter == p.alter
              case _         => false
          }
      }
      // TODO: Implementiere hashCode
      override def hashCode: Int = (vorname, nachname, alter).##
    }
    ```
    <details>
    <summary><u><b>Worauf muss ich achten, wenn ich Parameter für den hashCode verwenden möchte ?</b></u></summary>
    
    * $parameterEquals \equiv parameterHashCode$ 
    </details>

    <details>
    <summary><u><b>Was währe empfehlenswert, wenn wir etwas f. den hashCode verwenden möchten ?</b></u></summary>

    * Das verw. eines Objekts, dass unveränderl. ist
    </details>
</details>









































<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$']]
    }
  };
</script>
<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>