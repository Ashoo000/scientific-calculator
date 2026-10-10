import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Scientific Calculator - Ayesha khaliq",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {
        background: #0b1120;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    .block-container {
        padding-top: 1rem;
        max-width: 700px;
    }
</style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    padding: 12px;
    background: #0b1120;
    color: #f1f5f9;
    font-family: Arial, sans-serif;
}

.calculator {
    max-width: 540px;
    margin: 0 auto;
    padding: 24px;
    border: 1px solid #273449;
    border-radius: 24px;
    background: #111b2e;
    box-shadow: 0 20px 50px #0005;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.title {
    font-size: 21px;
    font-weight: 700;
}

.subtitle {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 6px;
}

.mode {
    background: #23334c;
    color: #cbd5e1;
    border: 0;
    border-radius: 9px;
    padding: 10px 14px;
    cursor: pointer;
    font-weight: bold;
}

.display {
    background: #091321;
    border: 1px solid #26374e;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 16px;
    min-height: 125px;
}

.previous {
    color: #94a3b8;
    text-align: right;
    font-size: 13px;
    min-height: 20px;
    overflow-wrap: anywhere;
}

#screen {
    width: 100%;
    background: transparent;
    border: none;
    outline: none;
    color: #f8fafc;
    font-size: 30px;
    text-align: right;
    margin-top: 15px;
    font-family: inherit;
    caret-color: #38bdf8;
}

#screen::placeholder { color: #64748b; }

.grid {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 9px;
}

button {
    border: 1px solid #293950;
    border-radius: 11px;
    padding: 14px 2px;
    min-height: 48px;
    color: #e2e8f0;
    background: #1d2a40;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: background .15s, transform .1s;
}

button:hover { background: #31435d; }
button:active { transform: scale(.96); }

.science { color: #7dd3fc; background: #172b42; }
.operator { color: #93c5fd; background: #203654; }
.clear { color: #fca5a5; background: #47232e; }
.equal {
    color: white;
    background: #0284c7;
    border-color: #0284c7;
}
.equal:hover { background: #0369a1; }

.history {
    margin-top: 20px;
    padding-top: 14px;
    border-top: 1px solid #293950;
    color: #94a3b8;
    font-size: 13px;
}

.history-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.history button {
    min-height: auto;
    padding: 5px 10px;
    font-size: 12px;
}

#historyList {
    max-height: 100px;
    overflow-y: auto;
    line-height: 1.9;
    overflow-wrap: anywhere;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 11px;
    margin-top: 18px;
}

@media(max-width: 420px) {
    .calculator { padding: 14px; }
    .grid { gap: 6px; }
    button { font-size: 13px; min-height: 44px; }
    #screen { font-size: 24px; }
}
</style>
</head>

<body>
<div class="calculator">

    <div class="header">
        <div>
            <div class="title">Scientific Calculator</div>
            <div class="subtitle">By Ayesha khaliq • Precision • Performance</div>
        </div>
        <button class="mode" id="mode" onclick="toggleMode()">
            DEG
        </button>
    </div>

    <div class="display">
        <div class="previous" id="previous">Ready to calculate</div>
        <input id="screen" type="text"
            placeholder="0"
            autocomplete="off"
            spellcheck="false"
            aria-label="Calculator display">
    </div>

    <div class="grid">
        <button class="clear" onclick="clearAll()">AC</button>
        <button class="operator" onclick="backspace()">⌫</button>
        <button class="operator" onclick="append('(')">(</button>
        <button class="operator" onclick="append(')')">)</button>
        <button class="operator" onclick="append('/')">÷</button>

        <button class="science" onclick="fn('sin')">sin</button>
        <button class="science" onclick="fn('cos')">cos</button>
        <button class="science" onclick="fn('tan')">tan</button>
        <button class="science" onclick="append('sqrt(')">√</button>
        <button class="operator" onclick="append('*')">×</button>

        <button class="science" onclick="fn('asin')">sin⁻¹</button>
        <button class="science" onclick="fn('acos')">cos⁻¹</button>
        <button class="science" onclick="fn('atan')">tan⁻¹</button>
        <button class="science" onclick="append('^2')">x²</button>
        <button class="operator" onclick="append('-')">−</button>

        <button class="science" onclick="fn('log')">log</button>
        <button class="science" onclick="fn('ln')">ln</button>
        <button class="science" onclick="append('^')">xʸ</button>
        <button class="science" onclick="append('!')">n!</button>
        <button class="operator" onclick="append('+')">+</button>

        <button onclick="append('7')">7</button>
        <button onclick="append('8')">8</button>
        <button onclick="append('9')">9</button>
        <button class="science" onclick="append('π')">π</button>
        <button class="science" onclick="append('%')">%</button>

        <button onclick="append('4')">4</button>
        <button onclick="append('5')">5</button>
        <button onclick="append('6')">6</button>
        <button class="science" onclick="append('e')">e</button>
        <button class="science" onclick="append('Ans')">Ans</button>

        <button onclick="append('1')">1</button>
        <button onclick="append('2')">2</button>
        <button onclick="append('3')">3</button>
        <button onclick="append('.')">.</button>
        <button class="equal" onclick="calculate()">=</button>

        <button onclick="append('0')">0</button>
        <button onclick="append('00')">00</button>
        <button class="science" onclick="append('π*')">π×</button>
        <button class="operator" onclick="append('-')">−</button>
        <button class="operator" onclick="append('/')">÷</button>
    </div>

    <div class="history">
        <div class="history-head">
            <strong>Calculation History</strong>
            <button onclick="clearHistory()">Clear</button>
        </div>
        <div id="historyList">Your calculations will appear here.</div>
    </div>

    <div class="footer">
        Developed by Ayesha khaliq · Use your keyboard or click buttons · Enter to calculate
    </div>
</div>

<script>
const screen = document.getElementById("screen");
const previous = document.getElementById("previous");
const historyList = document.getElementById("historyList");
const modeButton = document.getElementById("mode");

let angleMode = "DEG";
let lastAnswer = 0;
let history = [];

function toggleMode() {
    angleMode = angleMode === "DEG" ? "RAD" : "DEG";
    modeButton.textContent = angleMode;
    screen.focus();
}

function append(value) {
    if (screen.dataset.done === "true" && /^[0-9.]$/.test(value)) {
        screen.value = "";
    }
    screen.dataset.done = "false";

    const start = screen.selectionStart ?? screen.value.length;
    const end = screen.selectionEnd ?? start;
    const text = screen.value;

    screen.value = text.slice(0, start) + value + text.slice(end);
    const position = start + value.length;
    screen.focus();
    screen.setSelectionRange(position, position);
}

function fn(name) {
    const start = screen.selectionStart ?? screen.value.length;
    const end = screen.selectionEnd ?? start;
    const text = screen.value;
    const selected = text.slice(start, end);
    let insertion = selected ? name + "(" + selected + ")" : name + "(";

    screen.value = text.slice(0, start) + insertion + text.slice(end);
    const position = start + insertion.length;
    screen.focus();
    screen.setSelectionRange(position, position);
    screen.dataset.done = "false";
}

function clearAll() {
    screen.value = "";
    previous.textContent = "Ready to calculate";
    screen.dataset.done = "false";
    screen.focus();
}

function backspace() {
    const start = screen.selectionStart ?? screen.value.length;
    const end = screen.selectionEnd ?? start;

    if (start !== end) {
        screen.value = screen.value.slice(0, start) + screen.value.slice(end);
        screen.setSelectionRange(start, start);
    } else if (start > 0) {
        screen.value = screen.value.slice(0, start - 1) + screen.value.slice(end);
        screen.setSelectionRange(start - 1, start - 1);
    }
    screen.focus();
    screen.dataset.done = "false";
}

function clearHistory() {
    history = [];
    historyList.textContent = "Your calculations will appear here.";
}

function factorial(n) {
    if (!Number.isInteger(n) || n < 0 || n > 170) {
        throw new Error("Factorial requires integer 0 to 170");
    }
    let result = 1;
    for (let i = 2; i <= n; i++) result *= i;
    return result;
}

function prepareExpression(raw) {
    let s = raw.trim();
    if (!s) throw new Error("Please enter an expression");

    let balance = 0;
    for (const char of s) {
        if (char === "(") balance++;
        if (char === ")") balance--;
        if (balance < 0) throw new Error("Check your brackets");
    }
    s += ")".repeat(balance);

    s = s.replace(/×/g, "*").replace(/÷/g, "/");
    s = s.replace(/π/g, "Math.PI");
    s = s.replace(/\bAns\b/g, "(" + lastAnswer + ")");
    s = s.replace(/\be\b/g, "Math.E");
    s = s.replace(/√/g, "sqrt");

    // Factorial
    s = s.replace(/(\d+(?:\.\d+)?|\))!/g, "factorial($1)");

    // Exponent and percentage
    s = s.replace(/\^/g, "**");
    s = s.replace(/(\d+(?:\.\d+)?|\))%/g, "($1/100)");

    // Implicit multiplications
    s = s.replace(/(\d)(Math\.PI|Math\.E|\()/g, "$1*$2");
    s = s.replace(/(\))(Math\.PI|Math\.E|\d|\()/g, "$1*$2");

    return s;
}

function calculate() {
    try {
        const original = screen.value;
        let expression = prepareExpression(original);

        const evaluator = new Function(
            "factorial", "sin", "cos", "tan", "asin", "acos", "atan", "log", "ln", "sqrt",
            '"use strict"; return (' + expression + ');'
        );

        const sinFn = angleMode === "DEG" ? x => Math.sin(x * Math.PI / 180) : Math.sin;
        const cosFn = angleMode === "DEG" ? x => Math.cos(x * Math.PI / 180) : Math.cos;
        const tanFn = angleMode === "DEG" ? x => Math.tan(x * Math.PI / 180) : Math.tan;

        const asinFn = angleMode === "DEG" ? x => Math.asin(x) * 180 / Math.PI : Math.asin;
        const acosFn = angleMode === "DEG" ? x => Math.acos(x) * 180 / Math.PI : Math.acos;
        const atanFn = angleMode === "DEG" ? x => Math.atan(x) * 180 / Math.PI : Math.atan;

        const result = evaluator(
            factorial,
            sinFn,
            cosFn,
            tanFn,
            asinFn,
            acosFn,
            atanFn,
            x => Math.log10(x),
            Math.log,
            Math.sqrt
        );

        if (typeof result !== "number" || !Number.isFinite(result)) {
            throw new Error("Result is undefined or out of range");
        }

        lastAnswer = result;
        const formatted = Number(result.toPrecision(12)).toString();

        previous.textContent = original + " =";
        screen.value = formatted;
        screen.dataset.done = "true";

        history.unshift(original + " = " + formatted);
        history = history.slice(0, 10);
        historyList.innerHTML = "";
        history.forEach(item => {
            const row = document.createElement("div");
            row.textContent = item;
            historyList.appendChild(row);
        });

    } catch (error) {
        previous.textContent = "Error: Invalid expression";
    }
}

// Keyboard support
screen.addEventListener("keydown", function(event) {
    if (event.key === "Enter" || event.key === "=") {
        event.preventDefault();
        calculate();
    } else if (event.key === "Escape") {
        event.preventDefault();
        clearAll();
    }
});

document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") clearAll();
});
</script>
</body>
</html>
"""

components.html(html_code, height=880, scrolling=True)