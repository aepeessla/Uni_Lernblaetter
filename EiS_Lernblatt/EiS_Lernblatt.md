<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>

# Allgemeine Informationen zu Scala
* statisch typitisiert
<html lang="de">
<head>
    <meta charset="UTF-8">
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        th {
            background-color: #4A90E2;
            color: white;
            text-align: left;
            padding: 12px;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
            vertical-align: top;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
        .feature {
            font-weight: bold;
            color: #333;
            width: 25%;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
    </style>
</head>


<table>
    <thead>
        <tr>
            <th>Merkmal</th>
            <th>Statische Typisierung (Scala)</th>
            <th>Dynamische Typisierung (Python)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="feature">Zeitpunkt der Prüfung</td>
            <td><b>Kompilierzeit:</b> Der Typ wird geprüft, bevor das Programm startet.</td>
            <td><b>Laufzeit:</b> Der Typ wird geprüft, während das Programm ausgeführt wird.</td>
        </tr>
        <tr>
            <td class="feature">Variablen-Bindung</td>
            <td>Fest an einen Typ gebunden. Ein <code>Int</code> bleibt ein <code>Int</code>.</td>
            <td>Flexibel. Eine Variable kann nacheinander verschiedene Typen halten.</td>
        </tr>
        <tr>
            <td class="feature">Fehlererkennung</td>
            <td><b>Früh:</b> IDE (VS Code) und Compiler zeigen Fehler sofort an.</td>
            <td><b>Spät:</b> Fehler tauchen oft erst auf, wenn die entsprechende Zeile ausgeführt wird.</td>
        </tr>
        <tr>
            <td class="feature">Performance</td>
            <td>Tendenziell <b>schneller</b>, da die JVM nicht erst prüfen muss, was in der Variable steckt.</td>
            <td>Tendenziell <b>langsamer</b> durch den "Overhead" der Typprüfung während der Ausführung.</td>
        </tr>
        <tr>
            <td class="feature">Code-Beispiel</td>
            <td><code>val x: Int = 5</code><br><code>x = "Hallo"</code> <span style="color:red;">(Fehler!)</span></td>
            <td><code>x = 5</code><br><code>x = "Hallo"</code> <span style="color:green;">(Erlaubt)</span></td>
        </tr>
    </tbody>
</table>

