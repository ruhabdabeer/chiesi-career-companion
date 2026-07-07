from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

user_state = {
    "stage": "intro",
    "last_intent": None
}

def detect_intent(msg):
    msg = msg.lower()

    if any(x in msg for x in ["not sure", "help me choose", "confused", "career", "path", "direction"]):
        return "pathways"

    if any(x in msg for x in ["skills", "strength", "good at"]):
        return "skills"

    if any(x in msg for x in ["about", "chiesi", "company"]):
        return "about"

    if any(x in msg for x in ["department", "teams", "roles"]):
        return "departments"

    return None


# ---------------- CHATBOT ----------------
def get_response(msg):

    global user_state

    msg = msg.lower().strip()

    user_state["last_intent"] = msg

    intent = detect_intent(msg)

    if intent:
        user_state["stage"] = intent


    # =========================
    # STEP 4 (context reactions)
    # =========================

    if user_state["stage"] == "pathways" and "confused" in msg:
        return "Let’s guide you through Pathways first."


    # =========================
    # STEP 5 (coach responses)
    # =========================

    if user_state["stage"] == "skills" and "good at" in msg:
        return """
        That’s useful insight.

        <button class="btn" onclick="window.location='/skills'">
        Start Skills Assessment
        </button>
        """


    # =========================
    # YOUR NORMAL MENU LOGIC BELOW
    # =========================

    # ---------------- YOUR EXISTING LOGIC CONTINUES BELOW ----------------

    # ---------------- FIRST INTRO ----------------
    if msg in ["hi", "hello", "hey", "start", "menu"]:

        return """
        Hello! 👋 I'm Chiesi Career Companion.<br><br>

        I help you explore careers, skills and pathways at Chiesi.<br><br>

        Whenever you're ready please click YES to continue.<br><br>

        <button class="btn" onclick="sendMessage('yes')">YES</button>
        """

    # ---------------- YES MENU ----------------
    if msg == "yes":

        return """
        <div class="bot-block">

        <div class="bot-text">
        Select an option below or type numbers 1 to 4.
        </div>

        <div class="btn-group">

        <button class="btn" onclick="sendMessage('1')">
        1)📍 Pathways Assessment<br>
        <small>Find your career direction at Chiesi</small>
        </button>

        <button class="btn" onclick="sendMessage('2')">
        2)💡 Skills Assessment<br>
        <small>Discover your strengths and working style</small>
        </button>

        <button class="btn" onclick="sendMessage('3')">
        3) 🏢 About Chiesi<br>
        <small>Learn who we are and what we do</small>
        </button>

        <button class="btn" onclick="sendMessage('4')">
        4) 💼 Departments<br>
        <small>Explore all career areas</small>
        </button>

        </div>
        </div>
        """

    # ---------------- PATHWAYS ----------------
    if msg in ["1", "pathways"]:

        return """
        📍 Pathways Assessment<br><br>

        This helps you discover which career direction at Chiesi
        best matches your interests and personality.<br><br>

        <button class="btn" onclick="window.location='/path'">
        Start Pathways Quiz
        </button>

        <button class="btn" onclick="replaceLastBot('yes')">
        Back to Menu
        </button>
        """

    # ---------------- SKILLS ----------------
    if msg in ["2", "skills"]:

        return """
        💡 Skills Assessment<br><br>

        This quiz identifies your strengths and helps match you
        to roles where you’ll naturally perform best.<br><br>

        <button class="btn" onclick="window.location='/skills'">
        Start Skills Quiz
        </button>

        <button class="btn" onclick="replaceLastBot('yes')">
        Back to Menu
        </button>
        """

    # ---------------- ABOUT ----------------
    if msg in ["3", "about"]:

        return """
        🏢 About Chiesi<br><br>

        Chiesi is a global biopharmaceutical company focused on
        respiratory health, rare diseases, and specialty care.<br><br>

        <button class="btn" onclick="window.open('https://www.chiesi.uk.com/about-us')">About Us</button>
        <button class="btn" onclick="window.open('https://www.chiesi.uk.com/about-us/mission-and-values')">Mission & Values</button>
        <button class="btn" onclick="window.open('https://www.chiesi.uk.com/about-us/our-history')">Our History</button>
        <button class="btn" onclick="window.open('https://www.chiesi.uk.com/about-us/ethics-and-transparency')">Ethics & Transparency</button>

        <button class="btn" onclick="replaceLastBot('yes')">
        Back to Menu
        </button>
        """

    # ---------------- DEPARTMENTS ----------------
    if msg in ["4", "departments"]:

        return """
        💼 Departments at Chiesi<br><br>

        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/R%26D%2C-Pharmacovigilance-%26-Regulatory-Affairs_uk/8618402/')">R&D</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Marketing%2C-Market-Access-%26-Business-Excellence-%26-Medical-Affairs_uk/8618702/')">Marketing</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Sales_uk/8618802/')">Sales</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Information-Technology_uk/8619402/')">IT</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Human-Resources_uk/8619102/')">HR</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/AccountingFinance-&-Control_uk/8619002/')">Finance</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Quality_uk/8618602/')">Quality</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Supply-ChainLogistics-&-Procurement_uk/8619302/')">Supply Chain</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Industrial-Operations-&-HSE_uk/8618502/')">Operations</button>
        <button class="btn" onclick="window.open('https://careers.chiesi.com/go/Business-Development-&-Strategic-planning_uk/8619202/')">Strategy</button>

        <button class="btn" onclick="replaceLastBot('yes')">
        Back to Menu
        </button>
        """

    # ---------------- DEFAULT ----------------
    return """
    If you're unsure about anything, please just click or press below to go through the options.<br><br>

    <button class="btn" onclick="sendMessage('yes')">Click or Press Here</button>
    """


# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/path")
def path():
    return render_template("path.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/get", methods=["POST"])
def chatbot():
    msg = request.json["message"]
    return jsonify({"response": get_response(msg)})


if __name__ == "__main__":
    print("Chiesi Career Companion running...")
    app.run(debug=True)