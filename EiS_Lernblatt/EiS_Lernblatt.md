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
override def equals(that: Any): Boolean = {
        that match {
            // Sind beide Elemete gleich, sind die 
            case thatTable: Table => 
                this.project.numRecords == thatTable.project.numRecords && this.records.forall(table: Table => )
            case _ => False
        }
    }
```







<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>