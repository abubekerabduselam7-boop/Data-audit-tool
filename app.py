import streamlit as st
import pandas as pd
from datetime import datetime, time

# Page Configuration & Branding
st.set_page_config(
    page_title="Wright Dental Clinic | Kansanga",
    page_icon="🦷",
    layout="wide"
)

# Custom Infographic CSS Styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.04);
    }
    .metric-title { font-size: 12px; color: #64748b; font-weight: 700; text-transform: uppercase; }
    .metric-value { font-size: 22px; color: #0f172a; font-weight: bold; margin: 4px 0; }
    .metric-sub { font-size: 12px; color: #2563eb; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# Title Header & Banner
st.title("🦷 Wright Dental Clinic — Kansanga")
st.caption("📍 336C Lukuli Road, Kansanga, Kampala | 24/7 Care | Wheelchair Accessible | Cards & NFC Accepted")

# Facility Header Image
try:
    st.image("clinic_photo.jpg", caption="Wright Dental Clinic — 336C Lukuli Road Facility", use_container_width=True)
except Exception:
    st.image("https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&q=80&w=1200", caption="Wright Dental Clinic — Kansanga Facility", use_container_width=True)

st.divider()

# Executive Metric Cards Row
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="metric-card"><div class="metric-title">Google Rating</div><div class="metric-value">⭐ 4.6 / 5.0</div><div class="metric-sub">41 Verified Reviews</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-card"><div class="metric-title">Operating Hours</div><div class="metric-value">🕒 24 / 7</div><div class="metric-sub">Monday – Sunday</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-card"><div class="metric-title">Facility Standard</div><div class="metric-value">♿ Accessible</div><div class="metric-sub">Wheelchair & Card Ready</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="metric-card"><div class="metric-title">Emergency Unit</div><div class="metric-value">🚨 On-Demand</div><div class="metric-sub">Lukuli Road Desk</div></div>', unsafe_allow_html=True)

st.write("")

# Main Interface Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📅 Patient Intake & Booking", 
    "💰 Treatment Cost Estimator", 
    "📊 Operational Analytics", 
    "🚨 24/7 Emergency Triage"
])

# Tab 1: Patient Booking Form
with tab1:
    st.subheader("Patient Booking & Registration")
    with st.form("booking_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            name = st.text_input("Full Name*")
            phone = st.text_input("Phone Number (+256...)*")
            age_group = st.selectbox("Patient Age Category", ["Pediatric (Children)", "Adult Care", "Senior Care"])
        with col_b:
            service = st.selectbox("Primary Service Required", [
                "General Checkup & Cleaning",
                "Professional Teeth Whitening",
                "Tooth Extraction / Surgery",
                "Root Canal Treatment",
                "Emergency Relief"
            ])
            date = st.date_input("Preferred Date", min_value=datetime.today())
            preferred_time = st.time_input("Preferred Time Slot", value=time(9, 0))

        notes = st.text_area("Additional Symptoms or Notes")
        submit = st.form_submit_button("Submit Registration")

        if submit:
            if name and phone:
                st.success(f"✅ Booking registered for **{name}** on **{date} at {preferred_time}**. Our Kansanga desk will call **{phone}** to confirm.")
            else:
                st.error("Please provide both a Name and Phone Number.")

# Tab 2: Interactive Treatment Cost Estimator
with tab2:
    st.subheader("Interactive Cost Estimator (UGX)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Select Procedures:**")
        checkup = st.checkbox("General Consultation & X-Ray", value=True)
        scaling = st.checkbox("Full Mouth Scaling & Polishing")
        whitening = st.checkbox("In-Clinic Teeth Whitening")
        fillings = st.slider("Composite Fillings Count", 0, 5, 0)
        extractions = st.slider("Tooth Extractions Count", 0, 4, 0)
        after_hours = st.checkbox("Apply After-Hours / Emergency Surcharge")

    with col2:
        st.markdown("**Estimated Fee Summary:**")
        total = 0
        items = []

        if checkup:
            total += 50000
            items.append({"Service": "Consultation & X-Ray", "Cost (UGX)": "50,000"})
        if scaling:
            total += 120000
            items.append({"Service": "Scaling & Polishing", "Cost (UGX)": "120,000"})
        if whitening:
            total += 500000
            items.append({"Service": "Teeth Whitening", "Cost (UGX)": "500,000"})
        if fillings > 0:
            cost = fillings * 80000
            total += cost
            items.append({"Service": f"Fillings (x{fillings})", "Cost (UGX)": f"{cost:,}"})
        if extractions > 0:
            cost = extractions * 100000
            total += cost
            items.append({"Service": f"Extractions (x{extractions})", "Cost (UGX)": f"{cost:,}"})
        if after_hours:
            total += 50000
            items.append({"Service": "24/7 Emergency Surcharge", "Cost (UGX)": "50,000"})

        if items:
            st.table(pd.DataFrame(items))
            st.metric("Total Estimate", f"UGX {total:,}")
        else:
            st.info("Select options on the left to display cost calculation.")

# Tab 3: Native Streamlit Analytics Chart
with tab3:
    st.subheader("Monthly Patient Volume Analytics")
    analytics_df = pd.DataFrame({
        "Monthly Volume": [180, 110, 95, 60, 85]
    }, index=["Routine Cleaning", "Pediatric Care", "Teeth Whitening", "Extractions", "Emergency Pain"])
    
    st.bar_chart(analytics_df)

# Tab 4: Emergency Protocols
with tab4:
    st.warning("🚨 **Emergency Response Desk:** 336C Lukuli Road, Kansanga (Open 24/7)")
    st.markdown("""
    * **Knocked-out Tooth:** Keep tooth in milk/saline solution and visit within 60 minutes.
    * **Severe Pain or Swelling:** Visit our 24/7 reception immediately for triage and pain relief.
    * **Contactless Payments:** Card, Mobile Money, and NFC accepted at arrival.
    """)
