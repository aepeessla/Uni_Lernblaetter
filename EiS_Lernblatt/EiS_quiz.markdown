<style>
  code {
    background-color: #e9e9e9ff;
    color: #999999ff;
    padding: 2px 6px;          /* Ein bisschen Abstand, damit es gut aussieht */
    border-radius: 3px;  
  }

  details {
    border: #e4e3e3ff 1px solid;
    padding: 8px
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

* `.getOrElse()` entpackt autom.
</details>





<details>
<summary><u><b>Wie macht man aus einer Liste eine String-Repräsentation ?</b></u></summary>

* `<list>.mkString(<Was soll am Angfang stehen>, <Wie sollen die Elemente getrennt werden>, <was soll am Ende stehen>)`
</details>




<details>
<summary><u><b>Wie funktioniert <code>override def equals(obj: any): Boolean = ???</code> ?</b></u></summary>

* Wir vgl. unser aktuelle Objekt(`this`) mit einem anderen(`obj`)

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

    * Das __verw. eines Objekts__, dass <span style="color: red">unveränderl.</span> ist
    </details>
</details>



<h1>Object</h1>

<details>
<summary><u><b>Wie wird ein Object noch genannt ?</b></u></summary>

* Singleton



  <details>
  <summary><u><b>Was ist die Eigenschaft eines Singletons ?</b></u></summary>

  * _Während d. Laufzeit_ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{Erstellung einer einizigen}}\ \ \ \ }$ <span style="color: red">__Instanz__</span>

    <details>
    <summary><u><b>Wann genau wird eine Instanz für dieses Object erstellt ?</b></u></summary>

    * Wenn es _im Code_ __zum ersten Mal aufgerufen__ wird
    </details>


    <details>
    <summary><u><b>Was schreiben wir in ein <code>object</code> & wie verwenden wir eine <code>class</code> mit dem object ?</b></u></summary>

    * <span class="sub">Was schreiben wir in einem object ?</span>
      * Variabeln oder Methoden, d. f. \forall Objekte des gleichen Typs gelten sollen
      * wenn wir aber mehrere Objekte erstellen wollen, dann def. wir ein `class` mit dem __gleichen Namen__ wie das `object`
    

    <details>
    <summary><u><b>Welche Eigenschaften haben diese "best friends" ?</b></u></summary>

    * gegenseitiger Zugriff auf <code style="color: #ff6a00ff">private</code> Felder

      <details>
      <summary><u><b>Mit was kann ich "Fabrik-Methoden" erstellen, die bequem Objekte erstellt ohne die Verwendung von <code>new</code> ?</b></u></summary>

      * <code style="color: rgb(83, 201, 67)">apply</code>
      </details>
    </details>
    </details>
  </details> 

  * <span class="sub">Beispiel: </span>
    * ```scala
      // 1. Die Klasse für die individuellen Personen
      class Person(val name: String)

      // 2. Das Companion Object für die "allgemeinen" Dinge
      object Person {
        // Eine Konstante, die für alle gilt
        val spezies = "Mensch"
        
        // Eine Hilfsmethode, die nicht an einer speziellen Person klebt
        def printSpezies(): Unit = println(s"Alle Personen sind vom Typ $spezies")
        
        // Die "Fabrik"-Methode (apply)
        def apply(name: String): Person = new Person(name)
      }

      // Benutzung im Code:
      @main def main(): Unit = {
        // Individuelle Personen (Instanzen)
        val p1 = Person("Efe") 
        val p2 = Person("Sude")
        
        // Aufruf von globaler Logik aus dem Companion Object
        Person.printSpezies() 
      }
      ```
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