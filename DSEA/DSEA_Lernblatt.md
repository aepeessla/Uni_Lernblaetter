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

# Notationen

<details>
<summary class="n"><u><b>Welche 3 Notationen gibt es ?</b></u></summary>

* $O$ => worst case
* $\Omega$ => best case
* $\theta$ => avarage case
</details>


# Monogame

<details>
<summary class="n"><u><b>Was sind Monogame ?</b></u></summary>

* Ehe f. $\forall$
* es gibt eine gerade Anzahl an Personen
  * wir wollen $n$ Paare
  * _jede Person_ hat eine __Präferenz__ ($p_1: p_3 \lt p_4 \lt p_2$)
</details>

<details>
<summary class="n"><u><b>

* $p_1$: $p_4 < p_2 < p_3$
* $p_2$: $p_4 < p_3 < p_1$ 
* $p_3$: $p_4 < p_1 < p_2$ 
* $p_4$: $p_3 < p_1 < p_2$
</b></u></summary>

* Bei $n$ Paaren $\to n - 1$ Möglichkeiten
* <span class="a1">Instabilität prüfen</span>:
  * <details>
    <summary class="n"><u><b>Wie finde ich die Paare heraus ?</b></u></summary>

    * <span class="a1">Eliminations-Tabelle</span>:
      <table>
      <thead>
        <tr>
          <th>Person</th>
          <th>1.Wahl</th>
          <th>2.Wahl</th>
          <th>3.Wahl</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>$p_1$</td>
          <td>$p_2$</td>
          <td>$p_3$</td>
          <td>$p_4$</td>
        </tr>
        <tr>
          <td>$p_3$</td>
          <td>$p_1$</td>
          <td>$p_2$</td>
          <td>$p_2$</td>
        </tr>
        <tr>
          <td>$p_2$</td>
          <td>$p_3$</td>
          <td>$p_1$</td>
          <td>$p_1$</td>
        </tr>
        <tr>
          <td>$p_4$</td>
          <td>$p_4$</td>
          <td>$p_4$</td>
          <td>$p_3$</td>
        </tr>
      </tbody>
    </table>

    </details>

    1) <span class="a1">Heiratsantrag</span>:
    * Jede Person macht ihrer aktuell höchsten Wahl einen Antrag
      * $p_1 \to p_3$
      * $p_2 \to p_1$
      * $p_3 \to p_2$
      * $p_4 \to p_2$
      
    2) <span class="a1">Kandidat halten/ablehnen</span>:
    * $p_1$ bekommt nur den Antrag v. $p_2$ $\implies$ hält $p_2$.
    * $p_3$ bekommt nur den Antrag v. $p_1$ $\implies$ hält $p_1$
    * $p_2$ bekommt Anträge v. $p_3$ & $p_4$. Da $p_2$ d. Person $p_3$ lieber mag als $p_4$, hält $p_2$ d. Person $p_3$ & lehnt $p_4$ ab

    3) <span class="a1">Symmetrisch streichen</span>:
    * Wenn $x$ von $y$ abgelehnt wird (oder $x$ jemand Schlechteres als seine aktuelle Zusage verfällt), streichst du d. Verbindung $x \leftrightarrow y$ bei beiden Personen durch
      * Da $p_2$ d. Person $p_4$ ablehnt, streichst du $p_4$ in d. Zeile v. $p_2$ & $p_2$ in d. Zeile v. $p_4$.
</details>










































































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