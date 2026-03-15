<style>
    h1 {
        text-decoration: underline;
        background-color: #bbc3eeff
    }
    h2 {
        text-decoration: underline;
        background-color: #d5d9edff
    }
    .wi1 {
        color: #ff0051ff
    }
    .wi2 {
        color: #bd4269ff
    }
    .subtitle {
      text-decoration: underline;
      font-weight: bold
    }


</style>

<h1>Mathe Lernblatt</h1>

<h2>Themensammlung</h2>

* Bernoulli-Formel
* Prozentrechnung/Bruchrechnung
* Bedingte/ Unbedingte Wahrscheinlichkeit
* Binomialverteilung
* 4-Fälderrafel
* Baumdiagramm

<h2>Bernoulli-Formel</h2>

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

* $n$ : Anzahl d. Versuche
* $k$ : Anzahl d. Treffer (Wie viele Erfolge ?)
* $p$ : Wie <span class="wi1">hoch</span> ist d. Wahrscheinlichkeit auf einen Erfolg
* $(1-p)$: Das ist quazi $(100 \% - \text{mein Erfolg})$ $\to$ automatisch d. Rest
* $\binom{n}{k}$: Wie viele Möglichkeiten gibt es 

<h2>Wie berechnet man den Binomialkoeffizienten ?</h2>

* <span class="subtitle">Aussehen</span>:
  * $\binom{n}{k}$

* <span class="subtitle">Berechnung</span>:
  *  $\frac{n!}{k! \cdot (n-k)!}$

* <span class="subtitle">Wichtig</span>:
  * <span class="wi1">kürzen</span>















<script>
  MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    svg: {
      fontCache: 'global'
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
