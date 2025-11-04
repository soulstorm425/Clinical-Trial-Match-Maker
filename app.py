import streamlit as st

st.title("Clinical Trial Match Maker (Demo)")

st.markdown("""
Answer a few quick questions to see potential trial matches.  
*No personal data collected — this is a PHI-free prototype.*
""")

age = st.number_input("Age", min_value=0, max_value=120, value=55)
diagnosis = st.text_input("Primary cancer type (e.g., ovarian, endometrial, cervical)").strip().lower()
ecog = st.radio("ECOG performance status (0–4)", [0, 1, 2, 3, 4])
prior_chemo = st.checkbox("Received prior systemic chemotherapy?")
disease_status = st.selectbox("Disease status", ["new diagnosis", "recurrent", "metastatic", "maintenance phase"])
creatinine = st.number_input("Creatinine ratio to ULN", min_value=0.0, value=1.0, step=0.1)

if st.button("Check eligibility"):
    eligible_trials = []

    # Example logic (toy data)
    if "ovarian" in diagnosis and age >= 18 and ecog <= 2 and not prior_chemo and creatinine <= 1.5:
        eligible_trials.append("OVARIAN-FRONTLINE-01")
    if "endometrial" in diagnosis and age >= 18 and ecog <= 2 and creatinine <= 1.5:
        eligible_trials.append("ENDOMETRIAL-IO-03")
    if "cervical" in diagnosis and disease_status in ["recurrent", "metastatic"] and ecog <= 1:
        eligible_trials.append("CERVIX-COMBO-04")

    if eligible_trials:
        st.success("✅ Potential matches:")
        for t in eligible_trials:
            st.write(f"- **{t}**")
    else:
        st.warning("⚠️ No matching trials based on these answers.")
