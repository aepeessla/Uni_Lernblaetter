<!-- Style:  -->
<style>
  /* 1. Ebene: Punkt */
  ul { list-style-type: disc; } 

  /* 2. Ebene: Pfeil rechts */
  ul ul { list-style-type: "→ "; }

  /* 3. Ebene: Pfeil rechts (identisch zur 2. Ebene) */
  ul ul ul { list-style-type: "→ "; }
</style>
<!-- Image -->
<style>
  img {
    width: 400px;  /* Alle Bilder werden 300px breit */
    height: auto;  /* Die Höhe passt sich automatisch an (keine Verzerrung) */
  }
</style>
<!-- Textgröße -->
<style>
  body {
    font-size: 13px; /* Verkleinert die Standardschrift von 16px auf 14px */
  }
</style>
<!-- Tabelle -->
<style>
  table {
    width: 100%;
    border-collapse: collapse; /* Verbindet die Ränder zu sauberen Linien */
    font-size: 13px;           /* Schrift verkleinern */
  }

  /* Linien nur an den Seiten der Zellen (Spaltentrennung) */
  th, td {
    border: 1px solid #000;    /* Schwarze Linie um jede Zelle */
    padding: 10px;
    text-align: left;
  }

  /* Bilder skalieren ohne zu schneiden */
  td img {
    width: 120px;
    height: auto;
    object-fit: contain;       /* Skaliert proportional im Rahmen */
    display: block;
  }
</style>
<!-- Lückentext -->
<style>
  .luecke {
    border-bottom: 2px solid #000; /* Der Unterstrich */
    color: transparent;           /* Text am Anfang unsichtbar */
    cursor: pointer;
    padding: 0 5px;
    transition: color 0.3s;       /* Schöner Einblend-Effekt */
  }

  .luecke.offen {
    color: black;                 /* Text wird sichtbar */
    border-bottom: 1px solid #ccc;
  }
</style>




1) [Mehrdimensionale Grenzwerte](#Mehrdimensionale_Grenzwerte)



<hr>



<a id="Mehrdimensionale_Grenzwerte"></a>

# **Mehrdimensionale Grenzwerte**

## **Grenzwert bestimmen**

### <u>1) Einf. einsetzten</u>
* Versuchen d. Werte einzusetzen $\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{wenn } \frac{0}{0}}\ \ \ \ }$ d. 3 Fälle

<hr style="border-color: #d8d8d8ff"></hr>

### 2) <u>Achsen</u>

**1) Fall: Achsen**: 

Wir setzen quazi $x=0/y=0$ & setzen dann den $y,x$-Wert des $\lim$ ein
  * $y=0, x \to \dots$
  * $x=0, y \to \dots$

**2) Fall: Ursprungsgeraden**: 

<b><span style="color: #fc0303;">D. ist keine fertige Lösung, d. zeigt nur, dass wir kein Grenzwert haben. D.h., wenn hier alle Ergebnisse gleich sind, dann muss ich dennoch die anderen Beweise rechnen (Sandwitch-Lemma, Polarkoordinaten)</span></b>

* $y = mx \ \lor x = my$

**3) Fall: Kurven**: 
* wenn **Zähler Pot./Nenner Pot.** sehr unterschliedl.

* $y = x^2 \ \lor x = y^2$

### 2) <u>Abschätzen</u>

<u>Polarkoordinaten</u>

* nur f. **($\mathbf{\lim \to 0,0}$)**

* Wir ersetzten $x$ & $y$
  * $x = r \cdot \cos(\varphi)$
  * $y = r \cdot \sin(\varphi)$
    * d. bedeutet einf. nur, dass $r \to 0$, wobei $\varphi$ variabel bleibt
* <u>Nutzen</u>: $\cos^2(\varphi) + \sin^2(\varphi) = 1$
* <span style="color: #fc0303;">WICHTIG !!! D. Ergebnis am Ende darf </span>$\color{red}\lnot$ <span style="color: #fc0303;">mehr vom Winkel abhängen</span>

<u><b>Sandwich-Lemma</b></u>

* $|\sin(\dots)| \leq 1$ & $|\cos(\dots)| \leq 1$.
* Nenner verkleinern macht den Bruch größer: Da $x^2 \geq 0$ ist, gilt z.B. $x^2 + y^2 \geq y^2$.
* Teilbrüche sind kleiner oder gleich $1$: $\frac{x^2}{x^2+y^2} \leq 1$.

<p>
  <button popovertarget="mehrdimensionale Grenzwerte" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Aufgaben
  </button> 
</p>

<div id="mehrdimensionale Grenzwerte" popover style="padding: 15px; border-radius: 15px; border: 1px solid #ff016fff; max-width: 300px; background-color: #edededff">
  <u>Übung 8</u>
  <p>

  Nr. 3a)
  <img src="image-15.png" alt="Übung 8, Nr. 3a" width="300">
  Nr. 3b)
  <img src="image-17.png" alt="Übung 8, Nr. 3a" width="300">
  Nr. 3c)
  <img src="image-19.png" alt="Übung 8, Nr. 3a" width="300">
  Nr. 3d)
  <img src="image-20.png" alt="Übung 8, Nr. 3a" width="300">
</div>

## **Unstelligkeitswerte finden bei mehreren Veränderlichen**:

* Wir haben eine Schnittstelle & wir müssen den $\lim$ einfach dort hinschichen

<u><b>Wann weiß ich, dass es direkt unstetig ist ?</b>></u>
* Wenn eine Konstate steht 

<p>
  <button popovertarget="Unstelligkeitswerte finden bei mehreren Veränderlichen" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Aufgaben
  </button> 
</p>

<div id="Unstelligkeitswerte finden bei mehreren Veränderlichen" popover style="padding: 15px; border-radius: 15px; border: 1px solid #ff016fff; max-width: 300px; background-color: #edededff">
  <u><b>Übung 8</b></u>
  <p>

  <b>Nr. 4a)</b>
  <img src="image-21.png" alt="Übung 8, Nr. 3a" width="300">
  <b>Nr. 4b)</b>
  <img src="image-22.png" alt="Übung 8, Nr. 3a" width="300">
  <b>Nr. 4c)</b>
  <img src="image-23.png" alt="Übung 8, Nr. 3a" width="300">
  Mein Ergebnis x_0 = $\pm$ 3. Deswegen ist es nicht stetig, weil nur hier bei (3,3), (-3,-3) das ausgeschnitte Stück 9 reinpasst & bei den anderen nicht !

  <b>Nr. 4d)</b>
  <img src="image-24.png" alt="Übung 8, Nr. 3a" width="300">
</div>

## **Bestimmung der Höhenlinien & Definitionsbereich**

## **Was ist eine Höhenlinie?**:
* Funktion mit mehreren Var. ($f(x,y)$)
  * $\forall$ Werte haben d. gleiche Höhe: $f(x,y)= c$


<p>
  <button popovertarget="Bestimmung der Höhenlinien & Definitionsbereich" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Aufgaben
  </button> 
</p>

<div id="Bestimmung der Höhenlinien & Definitionsbereich" popover style="padding: 15px; border-radius: 15px; border: 1px solid #ff016fff; max-width: 300px; background-color: #edededff">
  <u><b>Übung 8</b></u>
  <p>

  <b>Nr. 5a)</b>
  <img src="image-25.png" alt="Übung 8, Nr. 3a" width="300">
  <b>Nr. 5b)</b>
  <img src="image-26.png" alt="Übung 8, Nr. 3a" width="300">
  <b>Nr. 5b)</b>
  <img src="image-27.png" alt="Übung 8, Nr. 3a" width="300">
</div>

## **Die Norm**

* $||x||_{\infty} = max(|x_1|, |x_2|, \dots)$

<u>1. Positive Definitheit</u>:
* Eine Länge kann $\lnot \lt 0$

<u>2. Homogenität</u>:
* wenn ich eine Pfeil doppolt so lange ziehe ($\lambda = 2$), dann ist d. Länge v. meinem Pfeil auch 2 $\times$ so lang. Auch wenn ich d. in d. andere Seite ziehe, wie ($\lambda = -3$), dann ist sie immer noch $3 \times$ so lang, also $|\lambda|$

<u>3. Dreiecksungleichung</u>:
* wenn ich v. $\overset{\to}{AB}$, dann $\nu(x+y)$

<u>Wo ist dies Regel f. mich relevant ?</u>:
* Sandwich-Lemma: D. Dreieckungleichung hilft und die beiden Grenzen zu bestimmen !
*Wenn man n. unten abschätzen müssen oder voneinander abziehen müssen: $|\overset{\text{direkte Weg}}{\nu(x) - \nu(y)}| \le \overset{\text{mit Umweg}}{\nu(x - y)}$
* **NORME SIND IMMER STETIG**
  * wenn ich einmal bewiesen habe, dass etw. eine Norm ist, dann brauche ich kein $\epsilon$-$\delta$-Beweise oder Limes-Rechnungen


# **Kurvendiskussion mit mehreren Veränderlichen**

## **Kritischer Punkt**:
$$\text{I) } f_x(x,y) = 0$$
$$\text{II) }f_y(x,y) = 0$$
* $\text{I}$ oder $\text{II}\underrightarrow{\ \ \ \ \textcolor{#7abd2d}{\text{eins.}}\ \ \ \ }$ in d. andere eins & umstellen !

## **KP charakterisieren**:
* $H_f = \begin{pmatrix} f_{xx} & f_{yx} \\ f_{xy} & f_{yx} \end{pmatrix}$ bilden

* $\det(H_f)$
  * $\det(H_f) \gt 0$: echter Extremum(Max.,Min.)
  * $\det(H_f) = 0$: Keine Aussage
  * $\det(H_f) \lt 0$: Sattelpunkt


<p>
  <button popovertarget="Kurvendiskussion mit mehreren Veränderlichen" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Aufgaben
  </button> 
</p>

<div id="Kurvendiskussion mit mehreren Veränderlichen" popover style="padding: 15px; border-radius: 15px; border: 1px solid #ff016fff; max-width: 300px; background-color: #edededff">
  <u><b>Übung 9</b></u>
  <p>

  <b>Nr. 3a)</b>
  <img src="image-28.png" width="500">
  <b>Nr. 3b)</b>
  <img src="image-29.png" width="500">
  <b>Nr. 3c)</b>
  <img src="image-30.png" width="500">
</div>

# **Kurvendiskussion mit mehreren Veränderlichen & einer Nebenbedingung**

![alt text](image-31.png)

## **Lagrange-Funktion**:
### <u>**Allgem. Schritte**</u>:

1. <u>Nebenbedingung</u>:
* $\forall$ auf eine Seite bringen, sodass auf einer Seite = 0 steht
2. <u>Lagrange-Funktion</u>
* $L(x,y,\lambda) = f(x,y) + \lambda \cdot (\text{Nebenbedingung})$
3. <u>1.Ableitung</u>
4. <u>KP</u>
5. <u>2.Ableitungen</u>
6. <u>geränderte Matrix</u>

# **Implizierte Ableitung**
<b><span style="color: #fc0303;">Wichtig ist, dass bei F(x,y) am Ende = 0 steht!</span></b>

## **Normale Gleichung**:
Formel: $\boxed{-\frac{F_x}{F_y}}$

## **Parametische GLeichung**:
* **Formel**: $\boxed{y'(x) = \frac{\dot{y}(t)}{\dot{x}(t)}}$

## **Normale Gleichung mit mehreren Veränderlichen**:
* **Formel**: $\boxed{-\frac{F_x}{{\underset{d. was gesucht ist}{F_y}}}}$

# **Taylor Polynom**:

## $\mathbb{R}$:

* Formel: $\boxed{T_f^{\text{n}}(x, x_0) = \sum_{k = 0}^n \frac{f(x)^{(k)}}{k}(x-x_0)^k}$ 

## $\mathbb{R^n}$:

* Formel: $\boxed{T_f^{\text{n}}(\overset{x,y,z,\dots}{M}) = \sum_{k = 0}^n \frac{\nabla^k_f}{k}(x,y,z,\dots)^T}$ 
  * <span style="color: #fc0303;">Hier haben wir kein $()^k$ bei $(x-x_0)$</span>



# **Flächen**:
## Tangentialebene:

Wenn ich Normalenvektor habe: $\nabla(x,y,z) = \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}$ 

$$\boxed{F_x \cdot (x - x_0) + F_y \cdot (y - y_0) + F_z \cdot (z - z_0) = 0}$$
  * $x_0, y_0, z_0$ sind d. Punkte, d. geg. sind

## Normalverktor:

$$\boxed{\vec{n} = \nabla F(x,y,z) = \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}}$$

* <span style="color: #fc0303;">Man muss es nicht in den Bruch packen, sondern kann es einfach in $\nabla$ einfügen</span>

$$\boxed{\vec{n}_{normiert} = \frac{1}{\sqrt{(F_x)^2 + (F_y)^2 + (F_z)^2}} \cdot \begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}}$$

## Tangentialvektoren:
* $u = const$, $v = const$

* $\Phi_u, \Phi_v$ berechnen (einf. d. inneren Sachen n. d. Var. ableiten)

### <u>Normalverktor</u>:
* Kreuzprodukt berechnen: $\Phi_u \times \Phi_v$
![alt text](image-33.png)

<p>
  <button popovertarget="Normalverktor" style="border:none; background:none; color:blue; text-decoration:underline; cursor:pointer;">
    Aufgaben
  </button> 
</p>

<div id="Normalverktor" popover style="padding: 15px; border-radius: 15px; border: 1px solid #ff016fff; max-width: 300px; background-color: #edededff">
  <u><b>Übung 10</b></u>
  <p>

  <b>Nr.10.5a)</b>
  <img src="image-32.png" width="500">
</div>























































































































































































































# **Trigonometrie/Identitäten**

<!-- Der richtige Lerninhalt -->
<table>
  <thead>
    <tr>
      <th>Winkel (Grad)</th>
      <th>0°</th>
      <th>30°</th>
      <th>45°</th>
      <th>60°</th>
      <th>90°</th>
    </tr>
    <tr>
      <th>Winkel (Bogenmaß)</th>
      <td>$0$</td>
      <td>$\frac{\pi}{6}$</td>
      <td>$\frac{\pi}{4}$</td>
      <td>$\frac{\pi}{3}$</td>
      <td>$\frac{\pi}{2}$</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Sinus</b></td>
      <td>$\frac{\sqrt{0}}{2} = 0$</td>
      <td>$\frac{\sqrt{1}}{2} = \frac{1}{2}$</td>
      <td>$\frac{\sqrt{2}}{2}$</td>
      <td>$\frac{\sqrt{3}}{2}$</td>
      <td>$\frac{\sqrt{4}}{2} = 1$</td>
    </tr>
    <tr>
      <td><b>Cosinus</b></td>
      <td>$\frac{\sqrt{4}}{2} = 1$</td>
      <td>$\frac{\sqrt{3}}{2}$</td>
      <td>$\frac{\sqrt{2}}{2}$</td>
      <td>$\frac{\sqrt{1}}{2} = \frac{1}{2}$</td>
      <td>$\frac{\sqrt{0}}{2} = 0$</td>
    </tr>
  </tbody>
</table>































































































































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