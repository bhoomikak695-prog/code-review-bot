import streamlit as st
from reviewer import review_code

st.set_page_config(page_title="Code Review Bot", layout="wide")

# ---------- HEADER ----------
st.markdown("## 🧑‍💻 Code Review Bot")
st.caption("Upload a code file or paste your code to get instant AI-powered feedback")

col1, col2 = st.columns([1, 1])

# ---------- LEFT PANEL ----------
with col1:
    st.markdown("### 📂 Code Input")

    language = st.selectbox("Language", ["Python", "JavaScript", "Java", "C++"])

    ext_map = {
        "Python": "py",
        "JavaScript": "js",
        "Java": "java",
        "C++": "cpp"
    }
    ext = ext_map[language]

    uploaded_file = st.file_uploader(
        f"Upload {language} file",
        type=[ext]
    )

    code = ""

    if uploaded_file is not None:
        raw = uploaded_file.read()
        decoded = False

        for encoding in ["utf-8", "utf-16", "latin-1", "cp1252"]:
            try:
                code = raw.decode(encoding)
                decoded = True
                break
            except UnicodeDecodeError:
                continue

        if not decoded:
            st.error("❌ Could not read file. Ensure it's a valid code file.")
            code = ""
        elif code.startswith("PK"):
            st.error("❌ This looks like a ZIP/Office file.")
            code = ""
        else:
            st.success(f"✅ Loaded: {uploaded_file.name}")
            st.code(code, language=language.lower())

    if not code:
        code = st.text_area(
            "Or paste your code here",
            height=300,
            placeholder="Paste your code here..."
        )

    submitted = st.button("🚀 Review my code", type="primary")

# ---------- RIGHT PANEL ----------
with col2:
    st.markdown("### 📊 Review Dashboard")

    if submitted and code.strip():
        with st.spinner("Analysing your code... ⏳"):
            result = review_code(code, language)
            lines = [l for l in result.split("\n") if l.strip()]

            # ---------- SUMMARY ----------
            issue_count = len(lines)
            score = max(0, 10 - issue_count)

            colA, colB, colC = st.columns(3)

            with colA:
                st.metric("Score", f"{score}/10")

            with colB:
                st.metric("Issues", issue_count)

            with colC:
                st.metric("Language", language)

            st.progress(score / 10)
            st.divider()

            # ---------- AI REVIEW ----------
            st.markdown("### 🤖 AI Feedback")

            if issue_count == 0:
                st.success("✅ No issues found! Your code looks clean.")
            else:
                for line in lines:
                    low = line.lower()

                    if any(word in low for word in ["error", "bug", "bare", "none", "global"]):
                        st.error(f"🔴 {line}")
                    elif any(word in low for word in ["long", "print", "logging", "avoid"]):
                        st.warning(f"🟡 {line}")
                    else:
                        st.info(f"🔵 {line}")

    elif submitted:
        st.warning("⚠️ Please upload a file or paste some code first.")
    else:
        st.info("ℹ️ Submit your code on the left to see the review here.")