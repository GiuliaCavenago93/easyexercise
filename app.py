import streamlit as st
import pandas as pd
from datetime import datetime

# Load questions from Excel
questions_df = pd.read_excel("questions.xlsx")

st.title("🌱 Plant Operator Data Collection Form")

responses = {}

# Group questions by section
sections = questions_df['section'].unique()

with st.form("data_form"):
    for section in sections:
        st.header(section)
        section_questions = questions_df[questions_df['section'] == section]

      # Special help for "waste composition"
            if q_key.strip().lower() == "waste composition":
                responses[q_key] = st.text_area(q_key, help="Example: 30% organic, 20% glass, 50% paper")
            else:
                if input_type == 'dropdown':
                    responses[q_key] = st.selectbox(q_key, options)
                elif input_type == 'number':
                    responses[q_key] = st.number_input(q_key, step=1.0)
                elif input_type == 'text':
                    responses[q_key] = st.text_input(q_key)
                else:
                    # fallback in case other input types appear
                    responses[q_key] = st.text_input(q_key)
            
            # Ask for unit if required
            if unit_required:
                unit_key = f"{q_key} (unit)"
                responses[unit_key] = st.text_input(unit_key, placeholder="e.g. kg/year, m³/year")

    submitted = st.form_submit_button("Submit")

# Save data to Excel
if submitted:
    output_df = pd.DataFrame([responses])
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"response_{timestamp}.xlsx"
    output_df.to_excel(output_file, index=False)
    st.success(f"✅ Responses saved to {output_file}")
