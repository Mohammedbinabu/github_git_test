import streamlit as st

# Title
st.title("Compare Base Model vs Fine-Tuned Model")

# Text input for prompt
prompt = st.text_area("Enter your prompt:", height=150)

# Layout: two columns
col1, col2 = st.columns(2)

# Run models when button clicked
if st.button("Generate Responses"):
    with st.spinner("Generating responses..."):

        # Simulate getting responses (replace with real model inference)
        import time
        time.sleep(1)  # Simulate loading

        # Replace these with actual model inference
        base_response = f"[Base Model Response to]: {prompt}"
        fine_tuned_response = f"[Fine-tuned Model Response to]: {prompt}"

        # Display side-by-side
        with col1:
            st.subheader("Base Model")
            st.write(base_response)

        with col2:
            st.subheader("Fine-Tuned Model")
            st.write(fine_tuned_response)
