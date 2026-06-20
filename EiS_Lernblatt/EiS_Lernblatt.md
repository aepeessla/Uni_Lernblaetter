# Meine Gedankengänge f. d. neue Übungsblatt. 

> Da es zu warm ist & ich nicht all meine Sachen n. unten tragen möchte (es ist schon unordentlich genug) mache ich es hier:

## <u>Aufgabe 1)</u>

![alt text](image.png)
* so soll mein Code aussehen !

### <u>Gleichheit</u>
* <u>Wann gelten 2 tabellen als gleich ?</u>
  * Records gleich
  * Records in derselben Reihenfolge vorkommen
  * die Reihenfolge der Attribute innerhalb des Schemas oder der Records die Gleichheit nicht beeinflusst

* <u>Wie sieht eine Tabelle aus ?</u>
  ```scala
  val table1 = new Table(
    Seq(
        "studentID": Int -> ...,
        "grade": Double -> ...,
        "bonus": Double -> ...
    )
  )
  ```

>* <u>Vorlesung</u>
![alt text](IMG_2854.jpeg)
![alt text](IMG_2856.jpeg)

---

```scala
override def equals(other: Any): Boolean = other match {
  case thatTable: Table =>
    //Vgl. Zeilenanzahl
    this.numRecords == thatTable.numRecords &&
    //Vgl. Schema
    this.schema == thatTable.schema &&
    (0 until numRecords).forall { i =>
    this.records(i) == thatTable.records(i)
    }
  case _ => false
}
```
* Hier wird bei Tabelle A & Tabelle B jeweils d. Einträge geöffnet (Zeilen) & zeilenweise durchiteriert.

* Da wir `numRecords` verw. ist es garantiert, dass wir \lnot <span style="color: #81B9DB">out of range</span> sind.  
  * Wir müssen \lnot `this.numRange` & `that.numRange` bestimmen, weil wir bereits in d. ersten Kontrolle d. Längen vergleichen haben.
  * Damit wir bei `this.records(i)` ankommen können, muss ja d. erste Bedingung schon stimmen, weil wir d. Bedingungen mit `&&` verbunden haben.
* Diese würden dann $\lnot$ mehr gleich sein, weshalb wir den <code style="color: #D281DB">hashCode</code> verw. können. In der Aufgabenstellung wurde gesagt, dass d. Reihenfolge im inneren d. Tabellen egal ist, wobei d. Werte stimmen sollten. D. Schema haben wir bereits ein Schritt davor kontrolliert. Deswegen können wie das `def hashCode` überschreiben & unser eigenen hashCode def.

```scala
override def hashCode(): Int = {
  //Mein hashCode soll aus den Werten die Summe ausrechnen
  (schema, records).hashCode
}
```
* <code style="color: #d35843ff">(schema, records).hashCode</code>: Wenn ich `(a,b).hashCode` aufrufe dann wird autom. zunächst `a.hashCode` aufgerufen, dann `b.hashCode`
* Scala nutzt f. Tupel eine ausgeklügelte Formel, d. d. Werte miteinander vermischt & multip., damit d. genaue Position wichtig bleibt. So haben `(5, 10)` & `(10, 5)` garantiert unterschiedl. Codes!


* Beim <span style="color: #8CD4C2">hashCode</span> geht es nur darum, dass wir ein "Ober-Index" verw. d. quazi d. Index einer "Ober-Klasse" ist, d. dann mehrere Tabellen in sich hat (`HashSet[Table[Records[Schema[String, Int|Double]]]]`)

---

* `0 until 4` = Exklusiv $\implies$ `0123`
* `0 to 4` = Inklusiv $\implies$ `01234`

<details>
  <summary style="text-size:20px"><b><u>Wie kann man mit `.foreach` eine Schleife v. a bis b erstellen ?</b></u></summary>
  
  ```scala
  (0 until upTo).forall(i => tableA(i) <= tableB(i))
  ```

  D. ist identisch zu:
  ```python
  for i in range(a,b):
    if False:
      break
  ```

  Mit `(0 until upTo).forall(i => ...)`. Somit erstellen wir eine Variabel `i`, d. d. Werte v. 0 bis upTo einnimmt.
</details>










# <u><b>Aufgabe 2</u></b>


<details><div style="border: black 1px solid">
  <summary>Aufgabe:</summary>
  Arbeiten Sie in:

  - `src/main/scala/dbms/v2/indexing/HashIndex.scala`
  - `src/main/scala/dbms/v2/indexing/TreeIndex.scala`
  - `src/main/scala/dbms/v2/indexing/MapBasedIndex.scala`

  Das Template enthält `toString`-Implementierungen für `HashIndex` und `TreeIndex`, diese sind aber nicht ganz
  korrekt.

  Gefordertes Verhalten:

  - Finden und beheben Sie das Problem.
  - Ändern Sie den Code so, dass es nur noch eine gemeinsame `toString`-Methode für `HashIndex` und `TreeIndex`
    gibt.

  Relevante Testsuite:

  ```bash
  sbt "testOnly dbms.v2.ScoredIndexRepresentationSuite"
  ```
</div></details>












# <u><b>Aufgabe 4</u></b>

```scala
/** Joins two tables sharing exactly one attribute. */
def naturalJoin(other: Table): Table = {
???
}
```
* <u>Ist Attribut enthalten ?</u>
  * Attribute vgl.
    * <span style="color: #a9a9a9ff">D. Attribute sind in den Schemas gespeichert, also kann ich gucken, ob d. gesuchte Attribut enthalten ist </span>
  * `TableRecord.attributes: Map[String, Variant]`("grade" -> 1.0): Wir können hier d. beiden Strings vgl.
    * Gleich $\implies$ füge d. `Record` in das neue Table mit `.appendRecord`
    * $\lnot$ Gleich $\implies$ mache weiter
  
<details>
<summary><u>Brauche ich ein Index?</u></summary>

* Weil wir mehrere Tables kontrollieren
</details>













<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>