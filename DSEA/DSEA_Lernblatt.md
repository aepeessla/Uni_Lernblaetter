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

# Divide-&-Conquer-Algorithmus

* <span class="a1">Übersicht</span>:
  * Merge-Sort f. Sortierung
  * Karatsuba-Multiplikation
  * Diskrete Fouriertransformation
  * Master-THeorem


## Merge-Sort

<details>
<summary class="n"><u><b>Wie funktioniert das Merge-Sort ?

`[5,6,3,4,9,1,2,7]`</b></u></summary>

1. Teil = Rokusiv aufteilen
  * `[5,6,3,4,9,1,2,7]`
  * `[5,6,3,4]`, `[9,1,2,7]`
  * `[5,6]`, `[3,4]`, `[9,1]`,`[2,7]`
  * `[5]`, `[6]`, `[3]`, `[4]`, `[9]`,`[1]`,`[2]`,`[7]`
2. Teil = Merge
  * `[5,6]`, `[3,4]`, `[1,9]`,`[2,7]`
  * `[3,4,5,6]`, `[1,2,7,9]`
  * `[1,2,3,4,5,6,7,9]`
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