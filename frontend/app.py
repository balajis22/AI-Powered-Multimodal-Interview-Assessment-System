import streamlit as st
import sys
from pathlib import Path

# --------------------------------------------------
# Import backend
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from backend.services.interview_service import InterviewService


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Interview Assessment",
    page_icon="🎤",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🎤 AI Interview Assessment System")

st.caption(
    "AI-powered interview evaluation using "
    "Computer Vision, Speech Analysis and Semantic AI"
)

st.divider()


# --------------------------------------------------
# Candidate Details
# --------------------------------------------------

left, right = st.columns([1, 1])


with left:

    st.subheader("👤 Candidate Details")

    name = st.text_input(
        "Candidate Name",
        placeholder="Enter candidate name"
    )

    role = st.selectbox(
        "Job Role",
        [
            "Software Engineer",
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Analyst",
            "HR Interview"
        ]
    )

    duration = st.slider(
        "Answer Duration (seconds)",
        10,
        60,
        20
    )

    start = st.button(
        "▶ Start Interview",
        use_container_width=True
    )


# --------------------------------------------------
# Status
# --------------------------------------------------

with right:

    st.subheader("📡 Interview Status")

    status = st.empty()

    camera = st.empty()

    microphone = st.empty()

    status.success("🟢 Ready")

    camera.info("📷 Camera : Waiting")

    microphone.info("🎤 Microphone : Waiting")


# --------------------------------------------------
# Question Area
# --------------------------------------------------

st.divider()

st.subheader("❓ Interview Question")

question_box = st.empty()

question_box.info(
    "Your interview question will appear here "
    "when the interview starts."
)


# --------------------------------------------------
# Results
# --------------------------------------------------

st.divider()

st.subheader("📊 Interview Results")

c1, c2, c3, c4 = st.columns(4)

emotion = c1.empty()
eye = c2.empty()
speech = c3.empty()
overall = c4.empty()

emotion.metric(
    "😊 Emotion",
    "--"
)

eye.metric(
    "👀 Eye Contact",
    "--"
)

speech.metric(
    "🎤 Speech",
    "--"
)

overall.metric(
    "⭐ Overall",
    "--"
)

# Answer-specific scores

a1, a2, a3 = st.columns(3)

semantic = a1.empty()
concept = a2.empty()
answer_score = a3.empty()

semantic.metric(
    "🧠 Semantic Relevance",
    "--"
)

concept.metric(
    "📚 Concept Coverage",
    "--"
)

answer_score.metric(
    "📝 Answer Score",
    "--"
)


# --------------------------------------------------
# Recommendations
# --------------------------------------------------

recommendations = st.empty()


# --------------------------------------------------
# Transcript
# --------------------------------------------------

st.divider()

st.subheader("📝 Candidate Transcript")

transcript_box = st.empty()

transcript_box.info(
    "Transcript will appear after the interview."
)


# --------------------------------------------------
# Additional Speech Information
# --------------------------------------------------

st.divider()

st.subheader("🎤 Speech Analysis")

s1, s2, s3 = st.columns(3)

wpm_box = s1.empty()
fillers_box = s2.empty()
background_box = s3.empty()

wpm_box.metric(
    "Words Per Minute",
    "--"
)

fillers_box.metric(
    "Filler Words",
    "--"
)

background_box.metric(
    "Background Sound",
    "--"
)


# --------------------------------------------------
# Start Interview
# --------------------------------------------------

if start:

    if not name.strip():

        st.warning(
            "Please enter the candidate name before "
            "starting the interview."
        )

        st.stop()


    # --------------------------------------------------
    # Create service
    # --------------------------------------------------

    service = InterviewService()


    # --------------------------------------------------
    # Display Question
    # --------------------------------------------------

    # We use question number 1 for now.
    question_number = 1

    question_data = None

    try:

        from backend.ai.question_bank import get_question

        question_data = get_question(
            role,
            question_number
        )

        question = question_data["question"]

    except Exception as e:

        st.error(
            f"Could not load interview question: {e}"
        )

        st.stop()


    question_box.warning(
        f"### ❓ Question\n\n{question}"
    )


    # --------------------------------------------------
    # Interview Status
    # --------------------------------------------------

    status.warning(
        "🟡 Interview Running"
    )

    camera.success(
        "📷 Camera Active"
    )

    microphone.success(
        "🎤 Recording Audio"
    )


    st.info(
        f"🎯 {role} interview for {name}"
    )


    # --------------------------------------------------
    # Run Interview
    # --------------------------------------------------

    try:

        result = service.run(
            duration=duration,
            role=role,
            question_number=question_number
        )

    except Exception as e:

        status.error(
            "❌ Interview failed"
        )

        camera.error(
            "📷 Camera Error"
        )

        microphone.error(
            "🎤 Recording Error"
        )

        st.exception(e)

        st.stop()


    # --------------------------------------------------
    # Interview Completed
    # --------------------------------------------------

    status.success(
        "✅ Interview Completed"
    )

    camera.info(
        "📷 Camera Stopped"
    )

    microphone.info(
        "🎤 Recording Saved"
    )


    # --------------------------------------------------
    # Display Question
    # --------------------------------------------------

    question_box.success(
        f"### ❓ Question\n\n{result['question']}"
    )


    # --------------------------------------------------
    # Main Results
    # --------------------------------------------------

    emotion.metric(
        "😊 Emotion",
        result["emotion"]
    )

    eye.metric(
        "👀 Eye Contact",
        result["eye_contact"]
    )

    speech.metric(
        "🎤 Speech",
        f'{result["speech_score"]}/100'
    )

    overall.metric(
        "⭐ Overall",
        f'{result["overall_score"]}/100'
    )


    # --------------------------------------------------
    # Answer Evaluation Results
    # --------------------------------------------------

    semantic.metric(
        "🧠 Semantic Relevance",
        f'{result["semantic_score"]}/100'
    )

    concept.metric(
        "📚 Concept Coverage",
        f'{result["concept_coverage"]}/100'
    )

    answer_score.metric(
        "📝 Answer Score",
        f'{result["answer_score"]}/100'
    )


    # --------------------------------------------------
    # Transcript
    # --------------------------------------------------

    transcript_box.success(
        result["transcript"]
    )


    # --------------------------------------------------
    # Answer Feedback
    # --------------------------------------------------

    st.subheader(
        "🧠 Answer Evaluation Feedback"
    )

    st.write(
        result["answer_feedback"]
    )


    # --------------------------------------------------
    # Concept Scores
    # --------------------------------------------------

    st.subheader(
        "📚 Concept Coverage Details"
    )

    for concept_name, score in result[
        "concept_scores"
    ].items():

        st.write(
            f"**{concept_name}** : {score}/100"
        )


    # --------------------------------------------------
    # Recommendations
    # --------------------------------------------------

    recommendations.success(
        "### 📋 AI Recommendations\n\n"
        + "\n".join(
            f"• {r}"
            for r in result["recommendations"]
        )
    )


    # --------------------------------------------------
    # Speech Details
    # --------------------------------------------------

    wpm_box.metric(
        "Words Per Minute",
        result["wpm"]
    )

    fillers_box.metric(
        "Filler Words",
        result["fillers"]
    )

    background_box.metric(
        "Background Sound",
        result["background"]
    )