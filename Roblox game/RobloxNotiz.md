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

# Skript

## print
* wenn ich einf. in `workspace` einen **Script** hinzufüge & dann `Play` drücke, dann wird d. Code ausgeführt & ausgeggeben 

```luau
print("Hello World")
```
![alt text](image.png)

<span class="a1">Ausgabe<span>:

![alt text](image-1.png)
* wenn man auf`Hello world:1` drauf klickt, dann geht man zu dem Script, wo man es geschrieben hat !


# RemoteEvent

## Client $\to$ Server
You can use a `LocalScript` to Trigger an event on the <span style="color: blue">server</span> by calling the `FireServer()` method on a `RemoteEvent`. If you pass arguments to `FireServer()`, they pass to  the event handler on the server with certain <span style="color: blue">limitations</span>.
* the first parameter of the event handler on the server is always the `Player` object of the client that calls it, and additional parameters follow.

| Client | `RemoteEvent:FireServer(args)` |
| --- | --- |
| __Server__ | `RemoteEvent.OnServerEvent:Connect(function(player, args))` |

## Server $\to$ Client

You can use a `Script` to trigger an event on a <span style="color: blue">client</span> by calling the `FireServer()` method on a `RemoteEvent`. The first argument fpr `FireServer()` is the `Player` object of the client that you wan to respond to the event, and additional arguments pass to the client with certain <span style="color: blue">limitations</span>.
* The event handler doesn't need to include the `Player`object as its first argument because you can determine the player on the client with `Players.LocalPlayer`.

| Server | `RemoteEvent:FireClient(player, args)`|
|--|--|
|__Client__| `RemtoteEvent.OnClickEvent:Connect(function(args))`|






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
