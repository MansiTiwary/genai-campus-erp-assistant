import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Campus ERP — AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root variables ── */
:root {
    --navy:    #0f1b2d;
    --navy-2:  #162035;
    --navy-3:  #1e2d48;
    --gold:    #c9a84c;
    --gold-lt: #e8c870;
    --teal:    #2dd4bf;
    --red:     #e05c5c;
    --green:   #4caf7d;
    --text:    #d4dce8;
    --muted:   #7b8fa6;
    --card-bg: #162035;
    --border:  rgba(201,168,76,0.18);
}

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--navy) !important;
    color: var(--text) !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; max-width: 1100px !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--navy-2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: var(--gold) !important; }
[data-testid="stSidebar"] .stRadio label { color: var(--text) !important; }

/* ── Header banner ── */
.erp-header {
    background: linear-gradient(135deg, var(--navy-3) 0%, #0f2744 100%);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    position: relative;
    overflow: hidden;
}
.erp-header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 160px; height: 160px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(201,168,76,0.12) 0%, transparent 70%);
}
.erp-header .icon { font-size: 2.4rem; line-height: 1; }
.erp-header h1 {
    font-family: 'Playfair Display', serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: var(--gold-lt) !important;
    margin: 0 !important;
    line-height: 1.2;
}
.erp-header p {
    color: var(--muted);
    font-size: 0.85rem;
    margin: 0.25rem 0 0 !important;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* ── Section heading ── */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    font-weight: 600;
    color: var(--gold) !important;
    border-left: 3px solid var(--gold);
    padding-left: 0.75rem;
    margin-bottom: 1.2rem !important;
}

/* ── Metric cards ── */
.metric-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
.metric-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.1rem 1.2rem;
    text-align: center;
}
.metric-card .label { font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }
.metric-card .value { font-size: 1.8rem; font-weight: 700; color: var(--gold-lt); line-height: 1.2; }
.metric-card .sub   { font-size: 0.8rem; color: var(--teal); margin-top: 0.2rem; }

/* ── AI response box ── */
.ai-box {
    background: linear-gradient(135deg, var(--navy-3) 0%, #0f2744 100%);
    border: 1px solid var(--border);
    border-left: 3px solid var(--teal);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-top: 1rem;
    line-height: 1.7;
    font-size: 0.95rem;
}
.ai-box .ai-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--teal);
    font-weight: 600;
    margin-bottom: 0.6rem;
}

/* ── Placement badge ── */
.company-badge {
    display: inline-block;
    background: rgba(201,168,76,0.15);
    border: 1px solid rgba(201,168,76,0.35);
    color: var(--gold-lt);
    border-radius: 20px;
    padding: 0.3rem 0.9rem;
    font-size: 0.82rem;
    margin: 0.25rem;
    font-weight: 500;
}
.no-company {
    color: var(--muted);
    font-style: italic;
    font-size: 0.9rem;
}

/* ── Attendance bar ── */
.att-bar-wrap { background: var(--navy-3); border-radius: 6px; height: 10px; overflow: hidden; margin-top: 0.5rem; }
.att-bar { height: 100%; border-radius: 6px; transition: width 0.6s ease; }
.att-good   { background: linear-gradient(90deg, var(--green), #6ee7b7); }
.att-warn   { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
.att-danger { background: linear-gradient(90deg, var(--red), #f87171); }

/* ── Chat area ── */
.chat-bubble-user {
    background: var(--navy-3);
    border: 1px solid var(--border);
    border-radius: 12px 12px 2px 12px;
    padding: 0.85rem 1.1rem;
    margin-bottom: 0.75rem;
    font-size: 0.95rem;
    max-width: 80%;
    margin-left: auto;
    color: var(--text);
}
.chat-bubble-ai {
    background: linear-gradient(135deg, #132040 0%, #0d1e38 100%);
    border: 1px solid var(--border);
    border-left: 3px solid var(--teal);
    border-radius: 2px 12px 12px 12px;
    padding: 0.85rem 1.1rem;
    margin-bottom: 1.25rem;
    font-size: 0.95rem;
    max-width: 85%;
    line-height: 1.7;
    color: var(--text);
}
.chat-bubble-ai .who { font-size: 0.7rem; color: var(--teal); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; margin-bottom: 0.4rem; }

/* ── Fee status pill ── */
.status-pill {
    display: inline-block;
    border-radius: 20px;
    padding: 0.25rem 1rem;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.status-paid { background: rgba(76,175,125,0.2); color: var(--green); border: 1px solid rgba(76,175,125,0.4); }
.status-pending { background: rgba(224,92,92,0.2); color: var(--red); border: 1px solid rgba(224,92,92,0.4); }
.status-partial { background: rgba(245,158,11,0.2); color: #f59e0b; border: 1px solid rgba(245,158,11,0.4); }

/* ── Streamlit overrides ── */
div[data-testid="stSelectbox"] > div { background: var(--navy-3) !important; border-color: var(--border) !important; }
div[data-testid="stNumberInput"] input { background: var(--navy-3) !important; border-color: var(--border) !important; color: var(--text) !important; }
.stTextArea textarea { background: var(--navy-3) !important; border-color: var(--border) !important; color: var(--text) !important; font-family: 'DM Sans', sans-serif !important; }
.stButton > button {
    background: linear-gradient(135deg, #b8922a, var(--gold)) !important;
    color: #0f1b2d !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.6rem !important;
    font-family: 'DM Sans', sans-serif !important;
    letter-spacing: 0.03em !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }
div[data-testid="stAlert"] { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)


# ─── Helpers ─────────────────────────────────────────────────────────────────

def api_get(path: str, params: dict = None):
    try:
        r = requests.get(f"{API_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Cannot connect to backend. Make sure the FastAPI server is running (`uvicorn app:app --reload`)."
    except Exception as e:
        return None, str(e)


def api_post(path: str, body: dict):
    try:
        r = requests.post(f"{API_URL}{path}", json=body, timeout=60)
        r.raise_for_status()
        return r.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Cannot connect to backend."
    except Exception as e:
        return None, str(e)


def ai_box(text: str):
    st.markdown(f"""
    <div class="ai-box">
        <div class="ai-label">✦ Gemini AI Analysis</div>
        {text}
    </div>""", unsafe_allow_html=True)


def section_title(icon: str, title: str):
    st.markdown(f'<div class="section-title">{icon} {title}</div>', unsafe_allow_html=True)


# ─── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="erp-header">
    <div class="icon">🎓</div>
    <div>
        <h1>GenAI Campus ERP Assistant</h1>
        <p>AI-Powered Student Information &amp; Analytics System</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── Load student list once ───────────────────────────────────────────────────
@st.cache_data(ttl=60)
def load_students():
    data, err = api_get("/student-list")
    return data or [], err


students, student_err = load_students()

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏫 Navigation")
    menu = st.radio(
        "Select Module",
        [
            "📊  CGPA Analysis",
            "💼  Placement Eligibility",
            "📅  Attendance Summary",
            "💰  Fee Status",
            "🤖  AI Assistant",
        ],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown(
        "<div style='font-size:0.75rem;color:#7b8fa6;line-height:1.6;'>"
        "<b style='color:#c9a84c;'>Backend</b><br>"
        f"<code style='color:#2dd4bf;'>FastAPI</code> → <code>localhost:8000</code><br><br>"
        "<b style='color:#c9a84c;'>AI Engine</b><br>"
        "<code style='color:#2dd4bf;'>Gemini 1.5 Flash</code>"
        "</div>",
        unsafe_allow_html=True
    )

    if student_err:
        st.warning(f"⚠ {student_err}", icon=None)

module = menu.split("  ", 1)[1]

# ═══════════════════════════════════════════════════════════════════════════════
# MODULE: CGPA Analysis
# ═══════════════════════════════════════════════════════════════════════════════
if module == "CGPA Analysis":
    section_title("📊", "Student CGPA Analysis")

    if not students:
        st.error("⚠ Could not load student list. Check backend connection.")
    else:
        col_sel, col_btn = st.columns([3, 1])
        with col_sel:
            selected = st.selectbox("Select Student", students)
        with col_btn:
            st.write("")  # vertical align
            st.write("")
            analyze = st.button("Analyze", use_container_width=True)

        if analyze:
            with st.spinner("Fetching data & generating AI analysis…"):
                data, err = api_get("/student-cgpa", {"name": selected})

            if err:
                st.error(f"Error: {err}")
            elif "message" in data:
                st.warning(data["message"])
            else:
                cgpa = float(data["cgpa"])
                # Grade colour
                grade_color = "#4caf7d" if cgpa >= 8 else ("#f59e0b" if cgpa >= 6.5 else "#e05c5c")
                grade_label = "Excellent" if cgpa >= 8.5 else ("Good" if cgpa >= 7 else ("Average" if cgpa >= 5.5 else "Below Average"))

                st.markdown(f"""
                <div class="metric-grid">
                    <div class="metric-card">
                        <div class="label">Student</div>
                        <div class="value" style="font-size:1.3rem">{data['student']}</div>
                    </div>
                    <div class="metric-card">
                        <div class="label">CGPA</div>
                        <div class="value" style="color:{grade_color}">{cgpa:.2f}</div>
                        <div class="sub">{grade_label}</div>
                    </div>
                    <div class="metric-card">
                        <div class="label">Scale</div>
                        <div class="value" style="font-size:1.2rem">/ 10.0</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                ai_box(data.get("ai_response", "—"))


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE: Placement Eligibility
# ═══════════════════════════════════════════════════════════════════════════════
elif module == "Placement Eligibility":
    section_title("💼", "Placement Eligibility Checker")

    col_inp, col_btn = st.columns([2, 1])
    with col_inp:
        student_id = st.number_input("Student ID", min_value=1, step=1, label_visibility="visible")
    with col_btn:
        st.write("")
        st.write("")
        check = st.button("Check Eligibility", use_container_width=True)

    if check:
        with st.spinner("Checking eligibility…"):
            data, err = api_get("/placement-eligibility", {"student_id": int(student_id)})

        if err:
            st.error(f"Error: {err}")
        elif "message" in data:
            st.warning(data["message"])
        else:
            cgpa = float(data["cgpa"])
            companies = data.get("eligible_companies", [])

            st.markdown(f"""
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="label">Student</div>
                    <div class="value" style="font-size:1.2rem">{data['student']}</div>
                </div>
                <div class="metric-card">
                    <div class="label">CGPA</div>
                    <div class="value">{cgpa:.2f}</div>
                </div>
                <div class="metric-card">
                    <div class="label">Eligible Companies</div>
                    <div class="value">{len(companies)}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Eligible Companies**")
            if companies:
                badges = "".join(f'<span class="company-badge">{c}</span>' for c in companies)
                st.markdown(f'<div style="margin-bottom:1rem">{badges}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="no-company">No companies match current CGPA requirements.</p>', unsafe_allow_html=True)

            ai_box(data.get("ai_response", "—"))


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE: Attendance Summary
# ═══════════════════════════════════════════════════════════════════════════════
elif module == "Attendance Summary":
    section_title("📅", "Attendance Summary")

    col_inp, col_btn = st.columns([2, 1])
    with col_inp:
        student_id = st.number_input("Student ID", min_value=1, step=1, key="att_id")
    with col_btn:
        st.write("")
        st.write("")
        view = st.button("View Summary", use_container_width=True)

    if view:
        with st.spinner("Loading attendance data…"):
            data, err = api_get("/attendance-summary", {"student_id": int(student_id)})

        if err:
            st.error(f"Error: {err}")
        elif "message" in data:
            st.warning(data["message"])
        else:
            pct = float(data.get("attendance", 0))
            bar_class = "att-good" if pct >= 75 else ("att-warn" if pct >= 60 else "att-danger")
            status_txt = "✅ Satisfactory" if pct >= 75 else ("⚠ At Risk" if pct >= 60 else "❌ Critical")
            status_col = "#4caf7d" if pct >= 75 else ("#f59e0b" if pct >= 60 else "#e05c5c")

            st.markdown(f"""
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="label">Attendance</div>
                    <div class="value" style="color:{status_col}">{pct:.1f}%</div>
                    <div class="sub">{status_txt}</div>
                </div>
                <div class="metric-card">
                    <div class="label">Minimum Required</div>
                    <div class="value" style="font-size:1.5rem">75%</div>
                </div>
                <div class="metric-card">
                    <div class="label">Shortfall</div>
                    <div class="value" style="font-size:1.5rem;color:{status_col}">{max(0, 75 - pct):.1f}%</div>
                </div>
            </div>
            <div class="att-bar-wrap">
                <div class="att-bar {bar_class}" style="width:{min(pct,100)}%"></div>
            </div>
            <div style="text-align:right;font-size:0.75rem;color:#7b8fa6;margin-top:0.3rem">{pct:.1f}% of 100%</div>
            """, unsafe_allow_html=True)

            ai_box(data.get("ai_response", "—"))


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE: Fee Status
# ═══════════════════════════════════════════════════════════════════════════════
elif module == "Fee Status":
    section_title("💰", "Fee Status Checker")

    col_inp, col_btn = st.columns([2, 1])
    with col_inp:
        student_id = st.number_input("Student ID", min_value=1, step=1, key="fee_id")
    with col_btn:
        st.write("")
        st.write("")
        check_fee = st.button("Check Fee", use_container_width=True)

    if check_fee:
        with st.spinner("Fetching fee record…"):
            data, err = api_get("/fee-status", {"student_id": int(student_id)})

        if err:
            st.error(f"Error: {err}")
        elif "message" in data:
            st.warning(data["message"])
        else:
            status = data.get("status", "").lower()
            pill_class = "status-paid" if "paid" in status else ("status-pending" if "pend" in status else "status-partial")

            st.markdown(f"""
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="label">Pending Fee</div>
                    <div class="value">₹{float(data['pending_fee']):,.0f}</div>
                </div>
                <div class="metric-card">
                    <div class="label">Status</div>
                    <div class="value" style="font-size:1rem;padding-top:0.6rem">
                        <span class="status-pill {pill_class}">{data['status'].upper()}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            ai_box(data.get("ai_response", "—"))


# ═══════════════════════════════════════════════════════════════════════════════
# MODULE: AI Assistant
# ═══════════════════════════════════════════════════════════════════════════════
elif module == "AI Assistant":
    section_title("🤖", "AI Academic Assistant")

    st.markdown(
        "<p style='color:#7b8fa6;font-size:0.9rem;margin-bottom:1.2rem'>"
        "Ask anything about academics, placements, exams, attendance policies, study tips, and more."
        "</p>",
        unsafe_allow_html=True
    )

    # Chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Render chat history
    for entry in st.session_state.chat_history:
        st.markdown(f'<div class="chat-bubble-user">{entry["q"]}</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="chat-bubble-ai"><div class="who">✦ Gemini AI</div>{entry["a"]}</div>',
            unsafe_allow_html=True
        )

    # Input
    question = st.text_area(
        "Your question",
        placeholder="e.g. What CGPA do I need for TCS placement? How can I improve my attendance?",
        height=110,
        label_visibility="collapsed"
    )

    col_ask, col_clear = st.columns([3, 1])
    with col_ask:
        ask_btn = st.button("Ask Gemini ✦", use_container_width=True)
    with col_clear:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    if ask_btn:
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking…"):
                # FIX: use POST to handle long/special-char questions
                data, err = api_post("/ask", {"question": question})

            if err:
                st.error(f"Error: {err}")
            else:
                st.session_state.chat_history.append({
                    "q": question,
                    "a": data.get("answer", "No response")
                })
                st.rerun()



# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000"

# st.set_page_config(
#     page_title="GenAI Campus ERP Assistant",
#     page_icon="🎓",
#     layout="wide"
# )

# st.title("🎓 GenAI Campus ERP Assistant")
# st.markdown("### AI Powered Student Information System")

# # --------------------------------------------------
# # Load Student Names
# # --------------------------------------------------

# students = []

# try:
#     response = requests.get(f"{API_URL}/student-list")
#     if response.status_code == 200:
#         students = response.json()
# except:
#     pass

# # --------------------------------------------------
# # Sidebar
# # --------------------------------------------------

# menu = st.sidebar.selectbox(
#     "Choose Service",
#     [
#         "Student CGPA Analysis",
#         "Placement Eligibility",
#         "Attendance Summary",
#         "Ask AI Assistant"
#     ]
# )

# # --------------------------------------------------
# # CGPA ANALYSIS
# # --------------------------------------------------

# if menu == "Student CGPA Analysis":

#     st.header("📊 Student CGPA Analysis")

#     if students:
#         selected_student = st.selectbox(
#             "Select Student",
#             students
#         )

#         if st.button("Analyze CGPA"):
#             response = requests.get(
#                 f"{API_URL}/student-cgpa?name={selected_student}"
#             )
#             data = response.json()

#             if "student" in data:
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.success(f"Student: {data['student']}")
#                 with col2:
#                     st.metric("CGPA", data["cgpa"])

#                 st.subheader("🤖 AI Performance Analysis")
#                 st.write(data.get("ai_response", ""))
#             else:
#                 st.error("Student not found.")
#     else:
#         st.error("Unable to load student list.")

# # --------------------------------------------------
# # PLACEMENT
# # --------------------------------------------------

# elif menu == "Placement Eligibility":

#     st.header("💼 Placement Eligibility")

#     student_id = st.number_input(
#         "Enter Student ID",
#         min_value=1,
#         step=1
#     )

#     if st.button("Check Eligibility"):
#         response = requests.get(
#             f"{API_URL}/placement-eligibility?student_id={student_id}"
#         )
#         data = response.json()
#         st.json(data)

# # --------------------------------------------------
# # ATTENDANCE
# # --------------------------------------------------

# elif menu == "Attendance Summary":

#     st.header("📅 Attendance Summary")

#     student_id = st.number_input(
#         "Enter Student ID",
#         min_value=1,
#         step=1,
#         key="attendance"
#     )

#     if st.button("View Attendance"):
#         response = requests.get(
#             f"{API_URL}/attendance-summary?student_id={student_id}"
#         )
#         data = response.json()
#         st.json(data)

# # --------------------------------------------------
# # AI CHATBOT
# # --------------------------------------------------

# elif menu == "Ask AI Assistant":

#     st.header("🤖 ERP AI Assistant")

#     question = st.text_area(
#         "Ask any question about academics, placements, attendance, exams, etc."
#     )

#     if st.button("Ask Gemini"):
#         response = requests.get(
#             f"{API_URL}/ask?question={question}"
#         )
#         data = response.json()

#         st.subheader("Answer")
#         st.write(data.get("answer", ""))