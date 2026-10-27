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
  * $\boxed{\binom{n+1}{2} \text{ oder} \approx \binom{n}{2}}$
  
  * Beispiel:
    * $\binom{n}{2} = \frac{n(n-1)}{2}$
      * $\mathcal{O}(n^2)$

  <details>
  <summary class="n"><u><b>Was ist ein Binom ?</b></u></summary>
    
  * $\binom{n}{k}$
    * n = Gesamtzahl d. Elem.
    * k = Paarung
  </details>





# Asymptotik (O-Notation)

<details>
<summary class="n"><u><b>Was bedeutet $f \in \mathcal{O}(g)$ ?</b></u></summary>

* $f$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{wächst höchstens so schnell wie}}\ \ \ \ }$ $g$ $\quad (\approx \le)$

  <details>
  <summary class="n"><u><b>Wie lautet die formale Definition ?</b></u></summary>

  * $\exists c > 0, n_0 : \ f(n) \le c \cdot g(n) \quad \forall n \ge n_0$
  </details>

  <details>
  <summary class="n"><u><b>Warum sind konstante Faktoren egal ?</b></u></summary>

  * $c$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{schluckt}}\ \ \ \ }$ jeden Faktor $\implies$ $\pi \cdot n \in \Theta(n)$
  </details>
</details>



<details>
<summary class="n"><u><b>Was bedeuten $\Omega$, $\Theta$ und $o$ ?</b></u></summary>

* $\Omega(g)$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{mindestens}}\ \ \ \ }$ $(\approx \ge)$
* $\Theta(g)$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{genauso}}\ \ \ \ }$ $(\approx =)$
  * $\Theta(g) = \mathcal{O}(g) \cap \Omega(g)$
* $o(g)$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{echt langsamer}}\ \ \ \ }$ $(\approx \lt)$ $\implies$ Schreibweise: <span style="color: red">$f \prec g$</span>
</details>



<details>
<summary class="n"><u><b>Wie sieht die Wachstums-Hierarchie aus ?</b></u></summary>

* $\boxed{1 \prec \log\log n \prec \log n \prec (\log n)^k \prec \sqrt{n} \prec n \prec n \log n \prec n^2 \prec n^k \prec 2^n \prec 3^n \prec n! \prec n^n}$

  <details>
  <summary class="n"><u><b>Was schlägt was ?</b></u></summary>

  * __Potenz__ $n^\varepsilon$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{schlägt}}\ \ \ \ }$ jeden __Logarithmus__
  * __Exponentialfkt.__ $c^n$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{schlägt}}\ \ \ \ }$ jede __Potenz__
  </details>

  <details>
  <summary class="n"><u><b>Ist die Basis egal ?</b></u></summary>

  * __Log__: <code style="color: rgb(91, 218, 120)">Ja</code> $\implies$ $\log_2 n \in \Theta(\ln n)$
  * __Exp.__: <span style="color: red">__Nein__</span> $\implies$ $2^n \prec 3^n$
  </details>
</details>



<details>
<summary class="n"><u><b>Wie prüfe ich, welche von zwei Funktionen schneller wächst ?</b></u></summary>

* $\lim\limits_{n \to \infty} \frac{f(n)}{g(n)}$
  * $= 0$ $\implies$ $f \prec g$
  * $= c$ $\ (0 \lt c \lt \infty)$ $\implies$ $f \in \Theta(g)$
  * $= \infty$ $\implies$ $g \prec f$

  <details>
  <summary class="n"><u><b>Was mache ich, wenn $\frac{\infty}{\infty}$ oder $\frac{0}{0}$ rauskommt ?</b></u></summary>

  * <code style="color: rgb(77, 152, 195)">L'Hôpital</code>: $\lim \frac{f(n)}{g(n)} = \lim \frac{f'(n)}{g'(n)}$

    <details>
    <summary><u><b>Welche Ableitungen brauche ich oft ?</b></u></summary>

    * $(\ln n)' = \frac{1}{n}$
    * $(\sqrt{n})' = \frac{1}{2\sqrt{n}}$
    * $(2^n)' = 2^n \cdot \ln 2$
    </details>
  </details>
</details>



<details>
<summary class="n"><u><b>Wie vereinfache ich $\log(n \log n)$ ?</b></u></summary>

* $\log(a \cdot b) = \log a + \log b$ $\implies$ $\log n + \log\log n$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{dominiert}}\ \ \ \ }$ $\Theta(\log n)$
* <span style="color: red">__nicht__</span> $\Theta(n \log n)$ !
</details>



<details>
<summary class="n"><u><b>Wie vereinfache ich $\sqrt{n^3}$ und $\log(n^k)$ ?</b></u></summary>

* $\sqrt{n^3} = n^{3/2}$
* $\log(n^k) = k \cdot \log n \in \Theta(\log n)$
</details>



<details>
<summary class="n"><u><b>Wogegen geht $10^{1/n}$ ?</b></u></summary>

* $\frac{1}{n} \to 0$ $\implies$ $10^{1/n} \to 10^0 = 1$ $\implies$ $\Theta(1)$
* wird <span style="color: red">__kleiner__</span>, nicht größer !
</details>



<details>
<summary class="n"><u><b>Wie ordne ich Funktionen nach ihrem Wachstum ?</b></u></summary>

1) __vereinfachen__ (Konstanten weg) $\to$ 2) __Klasse__ aus Hierarchie zuordnen $\to$ 3) grob __sortieren__ $\to$ 4) __Nachbarn__ per $\lim \frac{f}{g}$ prüfen

  <details>
  <summary class="n"><u><b>Was mache ich bei Exponenten wie $n^{\log n}$ vs. $2^{\sqrt{n}}$ ?</b></u></summary>

  * $\log$ v. __beiden__ vergleichen: $\log^2 n$ vs. $\sqrt{n}$ $\implies$ $n^{\log n} \prec 2^{\sqrt{n}}$

    <details>
    <summary class="n"><u><b>Worauf muss ich dabei achten ?</b></u></summary>

    * $\log f \in \Theta(\log g)$ $\overset{!}{\not\Rightarrow}$ $f \in \Theta(g)$
      * <span class="a1">Bsp.</span>: $\log(n^2) = 2 \log n$, aber $n \prec n^2$
    </details>
  </details>
</details>



<details>
<summary class="n"><u><b>Ordne: $f_1 = \pi n$, $f_2 = 10^{1/n}$, $f_3 = 2^n$, $f_4 = n \ln n$, $f_5 = \log(n \log n)$, $f_6 = \sqrt{n^3}$ (Präsenzblatt 1, Aufg. 2)</b></u></summary>

* $\boxed{f_2 \prec f_5 \prec f_1 \prec f_4 \prec f_6 \prec f_3}$
  * $\Theta(1) \prec \Theta(\log n) \prec \Theta(n) \prec \Theta(n \log n) \prec \Theta(n^{3/2}) \prec 2^n$

  <details>
  <summary class="n"><u><b>Warum ist $f_4 \prec f_6$ ?</b></u></summary>

  * $\frac{n \ln n}{n^{3/2}} = \frac{\ln n}{\sqrt{n}}$ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{L'Hôpital}}\ \ \ \ }$ $\frac{1/n}{1/(2\sqrt{n})} = \frac{2}{\sqrt{n}} \to 0$
  </details>

  <details>
  <summary class="n"><u><b>Was ändert sich, wenn $f_1 = \pi^n$ wäre ?</b></u></summary>

  * $\frac{\pi^n}{2^n} = (\frac{\pi}{2})^n \to \infty$ $\implies$ $f_3 \prec f_1$ $\implies$ $f_1$ ganz nach oben
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