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


# Allgemein

## Gaußsche Summenformel:

<details>
<summary class="n"><u><b>Wie lautet d. Gaußsche Summenformel ?</b></u></summary>

  * $\boxed{\binom{n+1}{k} \text{ oder} \approx \binom{n}{k}}$
    
    * __Genauer__:
      * $\binom{n}{k} = \frac{n!}{k! \cdot (n - k)!}$
  

    <details>
    <summary class="n"><u><b>Was ist ein Binom ?</b></u></summary>
      
    * $\binom{n}{k}$
      * n = Gesamtzahl d. Elem.
      * k = Paarung
    </details>
</details>
  





# Asymptotik (O-Notation)

<details>
<summary class="n"><u><b>Was sind die Schritte zur Ordnung von asymptotischen Wachstums ?</b></u></summary>

  1) __<u>$\forall$ Funk. vereinf.</u>__
  2) Jede Funktion in eine feinere Klasse einordnen(Tabelle)

  <table>
  <thead>
    <tr>
      <th align="left">Klasse</th>
      <th align="left">Funktionen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>konstant</td>
      <td>?</td>
    </tr>
    <tr>
      <td>log n</td>
      <td>?</td>
    </tr>
    <tr>
      <td>n<sup>1</sup></td>
      <td>?</td>
    </tr>
    <tr>
      <td>n<sup>1</sup> &middot; log n</td>
      <td>?</td>
    </tr>
    <tr>
      <td>n<sup>3/2</sup></td>
      <td>?</td>
    </tr>
    <tr>
      <td>c<sup>n</sup></td>
      <td>?</td>
    </tr>
  </tbody>
</table>

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