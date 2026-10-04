import streamlit as st
import math

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 25px;
}

.calculator {
    max-width: 650px;
    margin: auto;
    padding: 25px;
    border-radius: 25px;
    background: rgba(15, 23, 42, 0.95);
    box-shadow: 0px 15px 50px rgba(0,0,0,0.45);
}

.result-box {
    background: #020617;
    border: 1px solid #334155;
    border-radius: 15px;
    padding: 20px;
    text-align: right;
    margin-bottom: 20px;
}

.result-label {
    color: #64748b;
    font-size: 14px;
}

.result-value {
    color: #f8fafc;
    font-size: 36px;
    font-weight: bold;
    word-wrap: break-word;
}

div.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 600;
    border: 1px solid #334155;
    background: #1e293b;
    color: white;
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #38bdf8;
    color: #38bdf8;
}

.section-title {
    color: #38bdf8;
    font-size: 18px;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 8px;
}

.history-item {
    background: #1e293b;
    padding: 8px 12px;
    border-radius: 8px;
    margin-bottom: 5px;
    color: #cbd5e1;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "display" not in st.session_state:
    st.session_state.display = "0"

if "memory" not in st.session_state:
    st.session_state.memory = 0

if "history" not in st.session_state:
    st.session_state.history = []

if "angle_mode" not in st.session_state:
    st.session_state.angle_mode = "DEG"

# -------------------------------------------------
# FUNCTIONS
# -------------------------------------------------
def add_to_display(value):

    if st.session_state.display == "0":
        st.session_state.display = value
    else:
        st.session_state.display += value


def clear_display():
    st.session_state.display = "0"


def delete_last():
    if len(st.session_state.display) > 1:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = "0"


def calculate_expression():

    expression = st.session_state.display

    try:

        # Replace calculator symbols with Python symbols
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))

        # Allowed characters only
        allowed = "0123456789+-*/(). "

        if not all(char in allowed or char in "." for char in expression):
            raise ValueError("Invalid expression")

        result = eval(expression, {"__builtins__": {}}, {})

        if not math.isfinite(float(result)):
            raise ValueError("Invalid result")

        result = round(result, 12)

        st.session_state.history.insert(
            0,
            f"{st.session_state.display} = {result}"
        )

        st.session_state.history = st.session_state.history[:10]

        st.session_state.display = str(result)

    except Exception:
        st.session_state.display = "Error"


def scientific_function(function):

    try:

        x = float(st.session_state.display)

        # -------------------------
        # TRIG FUNCTIONS
        # -------------------------

        if function == "sin":

            value = math.radians(x) if st.session_state.angle_mode == "DEG" else x
            result = math.sin(value)

        elif function == "cos":

            value = math.radians(x) if st.session_state.angle_mode == "DEG" else x
            result = math.cos(value)

        elif function == "tan":

            value = math.radians(x) if st.session_state.angle_mode == "DEG" else x

            if abs(math.cos(value)) < 1e-12:
                raise ValueError

            result = math.tan(value)

        # -------------------------
        # INVERSE TRIG
        # -------------------------

        elif function == "asin":

            if x < -1 or x > 1:
                raise ValueError

            result = math.asin(x)

            if st.session_state.angle_mode == "DEG":
                result = math.degrees(result)

        elif function == "acos":

            if x < -1 or x > 1:
                raise ValueError

            result = math.acos(x)

            if st.session_state.angle_mode == "DEG":
                result = math.degrees(result)

        elif function == "atan":

            result = math.atan(x)

            if st.session_state.angle_mode == "DEG":
                result = math.degrees(result)

        # -------------------------
        # LOG FUNCTIONS
        # -------------------------

        elif function == "log":

            if x <= 0:
                raise ValueError

            result = math.log10(x)

        elif function == "ln":

            if x <= 0:
                raise ValueError

            result = math.log(x)

        # -------------------------
        # POWERS
        # -------------------------

        elif function == "square":

            result = x ** 2

        elif function == "cube":

            result = x ** 3

        elif function == "sqrt":

            if x < 0:
                raise ValueError

            result = math.sqrt(x)

        elif function == "cbrt":

            result = math.copysign(abs(x) ** (1 / 3), x)

        # -------------------------
        # OTHER
        # -------------------------

        elif function == "factorial":

            if x < 0 or not x.is_integer():
                raise ValueError

            result = math.factorial(int(x))

        elif function == "reciprocal":

            if x == 0:
                raise ValueError

            result = 1 / x

        elif function == "absolute":

            result = abs(x)

        elif function == "percent":

            result = x / 100

        else:
            return

        result = round(result, 12)

        st.session_state.history.insert(
            0,
            f"{function}({x}) = {result}"
        )

        st.session_state.history = st.session_state.history[:10]

        st.session_state.display = str(result)

    except Exception:

        st.session_state.display = "Error"


# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown(
    '<div class="main-title">🧮 Scientific Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Powerful • Fast • Easy to Use</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# CALCULATOR CONTAINER
# -------------------------------------------------
st.markdown('<div class="calculator">', unsafe_allow_html=True)

# Display
st.markdown(
    f"""
    <div class="result-box">
        <div class="result-label">DISPLAY</div>
        <div class="result-value">{st.session_state.display}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# DEG / RAD
# -------------------------------------------------
col1, col2, col3 = st.columns([1, 1, 2])

with col1:

    if st.button(
        "DEG" if st.session_state.angle_mode == "DEG" else "deg",
        use_container_width=True
    ):
        st.session_state.angle_mode = "DEG"
        st.rerun()

with col2:

    if st.button(
        "RAD" if st.session_state.angle_mode == "RAD" else "rad",
        use_container_width=True
    ):
        st.session_state.angle_mode = "RAD"
        st.rerun()

with col3:

    st.caption(
        f"Angle Mode: **{st.session_state.angle_mode}**"
    )

# -------------------------------------------------
# MEMORY BUTTONS
# -------------------------------------------------
st.markdown(
    '<div class="section-title">Memory</div>',
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4)

with m1:

    if st.button("MC", use_container_width=True):
        st.session_state.memory = 0
        st.rerun()

with m2:

    if st.button("MR", use_container_width=True):
        st.session_state.display = str(st.session_state.memory)
        st.rerun()

with m3:

    if st.button("M+", use_container_width=True):

        try:
            st.session_state.memory += float(
                st.session_state.display
            )
        except:
            pass

        st.rerun()

with m4:

    if st.button("M-", use_container_width=True):

        try:
            st.session_state.memory -= float(
                st.session_state.display
            )
        except:
            pass

        st.rerun()

# -------------------------------------------------
# SCIENTIFIC FUNCTIONS
# -------------------------------------------------
st.markdown(
    '<div class="section-title">Scientific Functions</div>',
    unsafe_allow_html=True
)

row1 = st.columns(5)

scientific_buttons = [
    ("sin", "sin"),
    ("cos", "cos"),
    ("tan", "tan"),
    ("asin", "asin"),
    ("acos", "acos")
]

for col, (label, function) in zip(row1, scientific_buttons):

    with col:

        if st.button(label, use_container_width=True):
            scientific_function(function)
            st.rerun()


row2 = st.columns(5)

scientific_buttons = [
    ("atan", "atan"),
    ("log", "log"),
    ("ln", "ln"),
    ("√", "sqrt"),
    ("x²", "square")
]

for col, (label, function) in zip(row2, scientific_buttons):

    with col:

        if st.button(label, use_container_width=True):
            scientific_function(function)
            st.rerun()


row3 = st.columns(5)

scientific_buttons = [
    ("x³", "cube"),
    ("∛x", "cbrt"),
    ("x!", "factorial"),
    ("1/x", "reciprocal"),
    ("|x|", "absolute")
]

for col, (label, function) in zip(row3, scientific_buttons):

    with col:

        if st.button(label, use_container_width=True):
            scientific_function(function)
            st.rerun()

# -------------------------------------------------
# CONSTANTS
# -------------------------------------------------
st.markdown(
    '<div class="section-title">Constants</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("π", use_container_width=True):
        add_to_display("π")
        st.rerun()

with c2:

    if st.button("e", use_container_width=True):
        add_to_display("e")
        st.rerun()

with c3:

    if st.button("%", use_container_width=True):
        scientific_function("percent")
        st.rerun()

# -------------------------------------------------
# MAIN CALCULATOR BUTTONS
# -------------------------------------------------
st.markdown(
    '<div class="section-title">Calculator</div>',
    unsafe_allow_html=True
)

# Row 1
cols = st.columns(4)

buttons = ["C", "⌫", "(", ")"]

for col, button in zip(cols, buttons):

    with col:

        if st.button(button, use_container_width=True):

            if button == "C":
                clear_display()

            elif button == "⌫":
                delete_last()

            else:
                add_to_display(button)

            st.rerun()

# Row 2
cols = st.columns(4)

buttons = ["7", "8", "9", "÷"]

for col, button in zip(cols, buttons):

    with col:

        if st.button(button, use_container_width=True):

            add_to_display(button)
            st.rerun()

# Row 3
cols = st.columns(4)

buttons = ["4", "5", "6", "×"]

for col, button in zip(cols, buttons):

    with col:

        if st.button(button, use_container_width=True):

            add_to_display(button)
            st.rerun()

# Row 4
cols = st.columns(4)

buttons = ["1", "2", "3", "-"]

for col, button in zip(cols, buttons):

    with col:

        if st.button(button, use_container_width=True):

            add_to_display(button)
            st.rerun()

# Row 5
cols = st.columns(4)

buttons = ["0", ".", "^", "+"]

for col, button in zip(cols, buttons):

    with col:

        if st.button(button, use_container_width=True):

            add_to_display(button)
            st.rerun()

# Equal button
if st.button("=", use_container_width=True):

    calculate_expression()
    st.rerun()

# -------------------------------------------------
# CLOSE CALCULATOR
# -------------------------------------------------
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# HISTORY
# -------------------------------------------------
st.markdown("---")

st.subheader("📜 Calculation History")

if st.session_state.history:

    for item in st.session_state.history:

        st.markdown(
            f'<div class="history-item">{item}</div>',
            unsafe_allow_html=True
        )

    if st.button("Clear History"):

        st.session_state.history = []
        st.rerun()

else:

    st.info("No calculations yet.")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")

st.caption(
    "🧮 Scientific Calculator • Built with Python & Streamlit"
)