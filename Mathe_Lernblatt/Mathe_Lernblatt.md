<style>
    body {
        background: #ffffffff;
        color: #000000ff;
    }

    h1{
        font-weight: bold;
        text-decoration: underline;
    }

    h2{
        font-weight: bold;
        text-decoration: underline;
    }

    <style>
  table {
    border-collapse: collapse; /* Verhindert doppelte Rahmenlinien */
    width: 100%;
  }

  table, th, td {
    border: 1px solid black; /* Setzt einen schwarzen, ein Pixel breiten Rahmen */
  }

  th, td {
    padding: 8px; /* Fügt etwas Luft zwischen Text und Rahmen ein */
    text-align: center;
  }

  .ÜSchrift{
    font-weight: bold;
    text-decoration: underline
  }

  details {
    border: 1px black solid;
    padding: 5px
  }

  code {
    background: #eaeaeaff;
    color: #7778b8ff;
    padding:3px
  }
</style>

<h1>Normalenformen</h1>

<h2> Was ist eine Normalform ?</h2>

* `allgemeine Form` = $ax^2 + 2bxy + cy^2 + dx + ey + f = 0$
* Durch __Drehung d. Koordinate__ wird  d. __Term xy eliminiert__ $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{Normalform sieht dann so aus}}\ \ \ \ }$ $\lambda_1 u^2 + \lambda_2 v^2 + g = 0$
    * $\lambda_1$ & $\lambda_2$ = Eigenwerte d. Matrix $\underrightarrow{\ \ \ \ \textcolor{#83b7ea}{\text{repräsentiert}}\ \ \ \ }$  quadratischen Teil d. Gleichung

<details>
    <summary class="ÜSchrift">Wie Normalform bestimmen ?</summary>

* <u>__3 Schritte__</u>
    1) Matrix aufstellen

        $\begin{pmatrix}
        a & b \\
        b & c
        \end{pmatrix}$
        
    1) Eigenwerte bestimmen
    1) Einsetzten in d. Normalform
</details>


<table>
  <thead>
    <tr>
      <th>&lambda;<sub>1</sub></th>
      <th>&lambda;<sub>2</sub></th>
      <th>h</th>
      <th>Typ</th>
      <th>Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>leere Menge</td>
      <td>u² + v² + 1 = 0</td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>0</td>
      <td>Punkt</td>
      <td>u² + v² = 0</td>
    </tr>
    <tr>
      <td>+</td>
      <td>+</td>
      <td>-</td>
      <td>Ellipse</td>
      <td>u² + v² = 1</td>
    </tr>
    <tr>
      <td>+</td>
      <td>0</td>
      <td>+</td>
      <td>leere Menge</td>
      <td>u² + 1 = 0</td>
    </tr>
    <tr>
      <td>+</td>
      <td>0</td>
      <td>0</td>
      <td>Gerade (Doppelgerade)</td>
      <td>u² = 0</td>
    </tr>
    <tr>
      <td>+</td>
      <td>0</td>
      <td>-</td>
      <td>zwei parallele Geraden</td>
      <td>u² - 1 = 0</td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>+</td>
      <td>Hyperbel</td>
      <td>u² - v² = -1</td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>0</td>
      <td>zwei sich schneidende Geraden</td>
      <td>u² - v² = 0</td>
    </tr>
    <tr>
      <td>+</td>
      <td>-</td>
      <td>-</td>
      <td>Hyperbel</td>
      <td>u² - v² = 1</td>
    </tr>
  </tbody>
</table>
















































































































































































































































































































































































































































































































































































































































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