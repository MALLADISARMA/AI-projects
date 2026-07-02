import streamlit as st
from grader import grade_prompt

st.set_page_config(
    page_title="AI Prompt Grader",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Prompt Grader")

st.write("Evaluate the quality of your prompt using Gemini.")

prompt = st.text_area(
    "Enter your Prompt",
    height=250,
    placeholder="Example:\nExplain Machine Learning to a beginner in 300 words using simple language."
)

if st.button("Grade Prompt", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
        st.stop()

    with st.spinner("Evaluating..."):

        try:

            result = grade_prompt(prompt)

            st.success("Evaluation Completed")

            st.metric(
                "Overall Score",
                f"{result['overall_score']}/10"
            )

            st.divider()

            c1, c2 = st.columns(2)

            with c1:

                st.subheader("Scores")

                st.progress(result["clarity"] / 2)
                st.write(f"Clarity : {result['clarity']}/2")

                st.progress(result["context"] / 2)
                st.write(f"Context : {result['context']}/2")

                st.progress(result["specificity"] / 2)
                st.write(f"Specificity : {result['specificity']}/2")

            with c2:

                st.subheader("Scores")

                st.progress(result["constraints"] / 2)
                st.write(f"Constraints : {result['constraints']}/2")

                st.progress(result["output_format"] / 2)
                st.write(f"Output Format : {result['output_format']}/2")

            st.divider()

            st.subheader("✅ Strengths")

            for item in result["strengths"]:
                st.success(item)

            st.subheader("❌ Weaknesses")

            for item in result["weaknesses"]:
                st.error(item)

            st.subheader("💡 Suggestions")

            for item in result["suggestions"]:
                st.info(item)

        except Exception as e:

            st.error("Error while evaluating prompt.")
            st.exception(e)