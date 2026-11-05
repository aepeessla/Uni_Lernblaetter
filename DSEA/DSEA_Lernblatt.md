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
  2) __<u>Jede Funktion in eine feinere Klasse einordnen(Tabelle)</u>__

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

  3) __<u>V. oben n- unten lesen = richtige Reihenfolge</u>__
  4) __<u>Nur benachbarte Funktionen per Grenzwert absichern, also $\lim \frac{f}{g}$</u>__
     * <b><span style="color: #5b34eb">Grenzwert-Kriterium</span></b>
     * __Nenner__: D. Funktion, die ich denke, dass langsamer ist
        * Wenn **Ergebnis** $= 0$, dann <span style="color: red">echt langsamer</span>: ≺
</details>


<details>
<summary class="n"><u><b>Wie bestimmt man im Allgemeinen d. Laufzeit eines Codes ?</b></u></summary>

1) __<u>Konstante Operationen/Basisoperationen feststellen ($\mathcal{O}(1)$)</u>__
    * jede Zeile anschauen & zählt elem. Aktionen:
      * **Zuw.** (=)
      * __Rechenop.__ (+, -)
      * __Vgl.__ (<, <=)
2) __<u>Schleifenhierarchie & Durchläufe bestimmen (von innen nach außen)</u>__:
    * __<u>Außerhalb d. Schleifen</u>__:
      * Wie viele Zeilen laufen 1 $\times$ (Bsp.: Startwertw., return)
      * __<u>Innere Schleifen</u>__:
        * Wie oft läuft d. <code style="color: #ff6a00ff">innerste Schleife</code> in Abhängigkeit d. **äußeren Zähler**?
      * __<u>Äußere Schleifen</u>__:
        * Wie oft werden d. Schleifen __insgesamt__ durchlaufen (z.B.: als Summenformel aufgestellt)?
3) __<u>Multiplikation von Durchläufen $\times$ Operationen</u>__:
    * Für jede Ebene rechnet man: $\text{Anzahl d. Schleifendurchläufe} \times \text{Operationen in dieser Ebene}$. 
4) __<u>Man addiert alle Ebenen zusammen.</u>__:
    * Man addiert alle Ebenen zsm.
5) __<u>Fallunterscheidung (Best Case vs. Worst Case)</u>__: 
    * Man prüft, ob bedingte Verzw. (if/else) vorhanden sind, d. d. Anzahl d. Operationen abhängig v. d. Eingabe schwanken lassen
 

</details>

# Landau Symbole

<details>
<summary class="n"><u><b></b></u></summary>

  <details>
  <summary class="n"><u><b>Was sind d, Landau Symbole ?</b></u></summary>

  1) $\mathcal{O}$
     * __<u>Def.</u>__: $\mathcal{O}(T) = \{f: \mathbb{N} \to \mathbb{N} | \exists c, n_0 \in \mathbb{N} \text{ so dass } \color{#ff0037} f(n)  \color{#001eff} \le \color{#ff0037} c \cdot T(n) \color{#000000} \text{ für } \forall n \ge n_0 \}$
       * D. ist d. <span style="color: rgb(255, 0, 0) ">obere Grenze</span> 

  2) $\Omega$
     * __<u>Def.</u>__: $\Omega(T) = \{f: \mathbb{N} \to \mathbb{N} | \exists c, n_0 \in \mathbb{N} \text{ so dass } \color{#ff0037} f(n) \color{#001eff} \ge \color{#ff0037}c \cdot T(n) \color{#000000} \text{ für } \forall n  \le  n_0 \}$
       * D. ist d. <span style="color: rgb(255, 0, 0) ">untere Grenze</span>

  3) $\Theta$
     * $\Theta(n) = \mathcal{O}(n) \cap \Omega(n)$
       * D. ist d. <span style="color: rgb(255, 0, 0) ">Bereich zw.</span> d. obere & d. unteren Grenze
  </details>
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