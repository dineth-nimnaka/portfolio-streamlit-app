import streamlit as st

#  Page Config
st.set_page_config(
    page_title="Dineth Nimnaka",
    page_icon="🐳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}
.block-container {
    padding: 2rem 3rem 4rem 3rem !important;
    max-width: 1400px;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0a0f1e 0%, #0d1b3e 50%, #0a1628 100%);
    border-radius: 20px;
    padding: 3rem 3.5rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(99, 179, 237, 0.15);
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(59,130,246,0.18) 0%, transparent 70%);
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 200px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(99,102,241,0.12) 0%, transparent 70%);
}
.hero-name {
    font-size: 3.2rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -1px;
    margin: 0;
    line-height: 1.1;
}
.hero-name span {
    color: #60a5fa;
}
.hero-role {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1rem;
    color: #93c5fd;
    margin-top: 0.6rem;
    letter-spacing: 0.05em;
}
.hero-role::before { content: '> '; color: #34d399; }
.hero-desc {
    color: #94a3b8;
    font-size: 1rem;
    margin-top: 1rem;
    max-width: 480px;
    line-height: 1.7;
}
.hero-location {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    color: #cbd5e1;
    font-size: 0.82rem;
    padding: 4px 12px;
    border-radius: 20px;
    margin-top: 1rem;
}
.hero-dots {
    position: absolute;
    top: 20px; right: 40px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: rgba(99,179,237,0.3);
    line-height: 1.8;
    text-align: right;
    z-index: 1;
}

/* ── Section Title ── */
.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-title::after {
    content: '';
    flex: 1;
    height: 2px;
    background: linear-gradient(90deg, #3b82f6 0%, transparent 100%);
    border-radius: 2px;
    margin-left: 10px;
}

/* ── Skill Chip ── */
.skill-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 0.5rem;
}
.skill-chip {
    background: #f1f5f9;
    color: #334155;
    padding: 5px 13px;
    border-radius: 6px;
    font-size: 0.82rem;
    font-weight: 600;
    border: 1px solid #e2e8f0;
    font-family: 'JetBrains Mono', monospace;
    transition: all 0.2s;
    display: inline-block;
}
.skill-chip.blue  { background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe; }
.skill-chip.green { background: #f0fdf4; color: #15803d; border-color: #bbf7d0; }
.skill-chip.purple{ background: #faf5ff; color: #7e22ce; border-color: #e9d5ff; }
.skill-chip.orange{ background: #fff7ed; color: #c2410c; border-color: #fed7aa; }

/* ── Stat Card ── */
.stat-card {
    background: linear-gradient(135deg, #0a0f1e, #0d1b3e);
    border-radius: 16px;
    padding: 1.5rem 1.8rem;
    border: 1px solid rgba(99,179,237,0.2);
    position: relative;
    overflow: hidden;
    height: 100%;
}
.stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #3b82f6, #818cf8);
    border-radius: 16px 16px 0 0;
}
.stat-number {
    font-size: 2.2rem;
    font-weight: 700;
    color: #60a5fa;
    font-family: 'JetBrains Mono', monospace;
    line-height: 1;
}
.stat-label {
    color: #f1f5f9;
    font-weight: 600;
    margin-top: 4px;
    font-size: 0.95rem;
}
.stat-sub {
    color: #64748b;
    font-size: 0.78rem;
    margin-top: 4px;
}

/* ── Project Card ── */
.proj-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    border: 1px solid #e2e8f0;
    margin-bottom: 1rem;
    border-left: 4px solid #3b82f6;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    transition: all 0.25s;
}
.proj-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(59,130,246,0.12);
    border-left-color: #2563eb;
}
.proj-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #94a3b8;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.proj-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
    margin: 4px 0;
}
.proj-desc {
    font-size: 0.88rem;
    color: #475569;
    margin: 6px 0 10px 0;
    line-height: 1.6;
}

/* ── Contact Form ── */
.contact-wrap {
    background: #f8fafc;
    border-radius: 16px;
    padding: 1.8rem 2rem;
    border: 1px solid #e2e8f0;
}
.contact-wrap input,
.contact-wrap textarea {
    width: 100%;
    padding: 11px 14px;
    margin-bottom: 10px;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.92rem;
    background: #ffffff;
    color: #1e293b;
    outline: none;
    box-sizing: border-box;
    transition: border-color 0.2s;
}
.contact-wrap input:focus,
.contact-wrap textarea:focus { border-color: #3b82f6; }
.contact-wrap textarea { height: 120px; resize: vertical; }
.contact-wrap button {
    background: linear-gradient(135deg, #1d4ed8, #3b82f6);
    color: white;
    padding: 12px 0;
    width: 100%;
    border: none;
    border-radius: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.02em;
    transition: opacity 0.2s;
}
.contact-wrap button:hover { opacity: 0.88; }

/* ── About Panel ── */
.about-panel {
    background: #ffffff;
    border-radius: 16px;
    padding: 1.6rem;
    border: 1px solid #e2e8f0;
    height: 100%;
}

/* ── Timeline row ── */
.timeline-item {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    padding: 10px 0;
    border-bottom: 1px solid #f1f5f9;
}
.timeline-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    background: #3b82f6;
    margin-top: 5px;
    flex-shrink: 0;
}
.timeline-body { flex: 1; }
.timeline-title { font-weight: 600; color: #1e293b; font-size: 0.92rem; }
.timeline-meta  { color: #94a3b8; font-size: 0.78rem; margin-top: 2px; }

/* ── Social Links ── */
.social-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 1rem;
}
.social-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 16px;
    border-radius: 8px;
    font-size: 0.83rem;
    font-weight: 600;
    text-decoration: none;
    border: 1.5px solid #e2e8f0;
    color: #374151;
    background: #ffffff;
    transition: all 0.2s;
}
.social-btn:hover { border-color: #3b82f6; color: #1d4ed8; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# HERO BANNER
# ══════════════════════════════════════════════════════
st.markdown("""
<div class="hero-banner">
    <div class="hero-dots">
        01 &nbsp;robots.py<br>
        02 &nbsp;timetable.sql<br>
        03 &nbsp;server.java<br>
        04 &nbsp;arena.cpp<br>
        05 &nbsp;portfolio.py ✦
    </div>
    <p class="hero-name">Dineth<br><span>Nimnaka</span></p>
    <p class="hero-role">cs_undergraduate @ SUSL</p>
    <p class="hero-desc" style="max-width: 600px;">
        Dedicated Computer Science undergraduate at Sabaragamuwa University of Sri Lanka, Faculty of Applied Sciences. 
        I bridge the gap between academic research and practical implementation, exploring domains from 
        <b>AI, Robotics (ROS 2), and DevOps</b> to <b>Full-Stack Development</b>. 
        Passionate about mentoring through education and delivering robust, scalable IT solutions.
    </p>
    <span class="hero-location">📍 Sabaragamuwa University of Sri Lanka</span>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# STATS ROW
# ══════════════════════════════════════════════════════
st.markdown('<p class="section-title">🏆 Achievements</p>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4, gap="medium")
with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">#580</div>
        <div class="stat-label">LeetCode Weekly</div>
        <div class="stat-sub">Contest 500 · 27,274 participants</div>
    </div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number" style="color:#34d399;">S5</div>
        <div class="stat-label">SSoC Contributor</div>
        <div class="stat-sub">Social Summer of Code Season 5</div>
    </div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number" style="color:#a78bfa;">ROS2</div>
        <div class="stat-label">Robotics Stack</div>
        <div class="stat-sub">Autonomous system architecture</div>
    </div>""", unsafe_allow_html=True)
with s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number" style="color:#fb923c;">4+</div>
        <div class="stat-label">Live Projects</div>
        <div class="stat-sub">Full-stack & embedded systems</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# MAIN COLUMNS — ABOUT + SKILLS   |   PROJECTS + CONTACT
# ══════════════════════════════════════════════════════
left, right = st.columns([1, 1.6], gap="large")

# ─── LEFT: About + Skills ─────────────────────────────
with left:
    st.markdown('<p class="section-title">👨‍💻 About</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-panel">
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-body">
                <div class="timeline-title">Passionate about autonomous systems</div>
                <div class="timeline-meta">ROS 2 · Robotics architecture · Embedded control</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#34d399;"></div>
            <div class="timeline-body">
                <div class="timeline-title">Competitive programmer</div>
                <div class="timeline-meta">LeetCode · Algorithm design · Problem solving</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#a78bfa;"></div>
            <div class="timeline-body">
                <div class="timeline-title">Backend & full-stack builder</div>
                <div class="timeline-meta">Spring Boot · Firebase · REST APIs</div>
            </div>
        </div>
        <div class="timeline-item" style="border:none;">
            <div class="timeline-dot" style="background:#fb923c;"></div>
            <div class="timeline-body">
                <div class="timeline-title">Open-source contributor</div>
                <div class="timeline-meta">SSoC Season 5 · GitHub collaboration</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-title">🛠️ Skills</p>', unsafe_allow_html=True)

    st.markdown("**Languages**")
    st.markdown("""
    <div class="skill-grid">
        <span class="skill-chip blue">Python</span>
        <span class="skill-chip blue">Java</span>
        <span class="skill-chip blue">C</span>
        <span class="skill-chip blue">JavaScript</span>
        <span class="skill-chip blue">PHP</span>
        <span class="skill-chip blue">SQL</span>
    </div>""", unsafe_allow_html=True)

    st.markdown("**Frameworks & Libraries**")
    st.markdown("""
    <div class="skill-grid">
        <span class="skill-chip green">Streamlit</span>
        <span class="skill-chip green">Spring Boot</span>
        <span class="skill-chip green">ROS 2</span>
    </div>""", unsafe_allow_html=True)

    st.markdown("**Databases**")
    st.markdown("""
    <div class="skill-grid">
        <span class="skill-chip purple">MySQL</span>
        <span class="skill-chip purple">Firebase</span>
        <span class="skill-chip purple">SQLite</span>
    </div>""", unsafe_allow_html=True)

    st.markdown("**Tools**")
    st.markdown("""
    <div class="skill-grid">
        <span class="skill-chip orange">Git</span>
        <span class="skill-chip orange">GitHub</span>
        <span class="skill-chip orange">VS Code</span>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="social-row">
        <a class="social-btn" href="https://github.com/dineth-nimnaka" target="_blank">⬡ GitHub</a>
        <a class="social-btn" href="https://www.linkedin.com/in/dinethnimnaka" target="_blank">in LinkedIn</a>
        <a class="social-btn" href="https://leetcode.com/" target="_blank">⚡ LeetCode</a>
    </div>
    """, unsafe_allow_html=True)


# ─── RIGHT: Projects + Contact ────────────────────────
with right:
    st.markdown('<p class="section-title">💻 Projects</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card">
        <div class="proj-num">Project — 01</div>
        <div class="proj-title">University Lecture Timetable & Events Viewer</div>
        <div class="proj-desc">
            A clean, responsive web application for students and faculty to view schedules
            and live university events. Designed for low-latency reads on a shared MySQL backend.
        </div>
        <div class="skill-grid">
            <span class="skill-chip blue">HTML</span>
            <span class="skill-chip blue">CSS</span>
            <span class="skill-chip blue">JavaScript</span>
            <span class="skill-chip orange">PHP</span>
            <span class="skill-chip purple">MySQL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card" style="border-left-color:#34d399;">
        <div class="proj-num">Project — 02</div>
        <div class="proj-title">Computer Repair Shop Management System</div>
        <div class="proj-desc">
            Real-time ticket and inventory management system for a technical support business,
            powered by Firebase's live database triggers with zero-latency updates across clients.
        </div>
        <div class="skill-grid">
            <span class="skill-chip green">Firebase</span>
            <span class="skill-chip green">Real-time DB</span>
            <span class="skill-chip blue">JavaScript</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card" style="border-left-color:#a78bfa;">
        <div class="proj-num">Project — 03</div>
        <div class="proj-title">Autonomous Robot Navigation (ROS 2)</div>
        <div class="proj-desc">
            Modular ROS 2 architecture for autonomous indoor navigation — sensor fusion,
            path planning nodes, and real-time telemetry logging over a local network.
        </div>
        <div class="skill-grid">
            <span class="skill-chip purple">ROS 2</span>
            <span class="skill-chip blue">Python</span>
            <span class="skill-chip blue">C</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-title">📬 Get In Touch</p>', unsafe_allow_html=True)

    YOUR_EMAIL = "YmDinethnimnaka@outlook.com"
    contact_html = f"""
    <div class="contact-wrap">
        <form action="https://formsubmit.co/{YOUR_EMAIL}" method="POST">
            <input type="hidden" name="_subject" value="New message from your Portfolio!">
            <input type="text"  name="name"    placeholder="Your name"          required>
            <input type="email" name="email"   placeholder="your@email.com"     required>
            <textarea           name="message" placeholder="Your message..."    required></textarea>
            <button type="submit">Send Message →</button>
        </form>
    </div>
    """
    st.markdown(contact_html, unsafe_allow_html=True)


# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<hr style="border:none; border-top:1px solid #e2e8f0; margin:0 0 1rem 0;">
<p style="text-align:center; color:#94a3b8; font-size:0.8rem; font-family:'JetBrains Mono',monospace;">
    © 2026 Dineth Nimnaka &nbsp;·&nbsp; Built with Streamlit &nbsp;·&nbsp; 
    <span style="color:#60a5fa;">dineth.dev</span>
</p>
""", unsafe_allow_html=True)