
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Module VI | Applied Mathematics",
    page_icon="📊",
    layout="wide"
)

# ---------------- RESPONSIVE PROJECT NAVIGATION ----------------

PROJECT_OPTIONS = [
    "Home",
    "Bayesian Intrusion Detection",
    "Network Latency Analysis"
]

# Keep the desktop sidebar and the always-visible page navigation in sync.
if "sidebar_project" not in st.session_state:
    st.session_state["sidebar_project"] = "Home"
if "main_project" not in st.session_state:
    st.session_state["main_project"] = "Home"


def _sync_from_sidebar():
    st.session_state["main_project"] = st.session_state["sidebar_project"]


def _sync_from_main():
    st.session_state["sidebar_project"] = st.session_state["main_project"]


# ---------------- PROFESSIONAL DASHBOARD THEME ----------------

st.markdown("""
<style>
/* Main application background */
.stApp {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(59, 130, 246, 0.10),
            transparent 35%
        ),
        #0B1120;
    color: #E5E7EB;
}

/* Main content width and spacing */
.block-container {
    max-width: 1450px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

/* Main headings */
h1 {
    color: #F8FAFC !important;
    font-weight: 800 !important;
    letter-spacing: -0.8px;
}

h2 {
    color: #E2E8F0 !important;
    font-weight: 700 !important;
}

h3 {
    color: #93C5FD !important;
    font-weight: 650 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263449;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #F8FAFC !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #17243A, #111B2D);
    border: 1px solid #2B3B55;
    padding: 20px 22px;
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.15);
}

[data-testid="stMetricLabel"] {
    color: #A5B4CC !important;
}

[data-testid="stMetricValue"] {
    color: #60A5FA !important;
    font-weight: 750 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #2563EB, #4F46E5);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.1rem;
    font-weight: 650;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1D4ED8, #4338CA);
    color: white;
    border: none;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);
}

/* Input fields */
[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: #111827;
    color: #F8FAFC;
    border-radius: 8px;
}

/* Data tables */
[data-testid="stDataFrame"] {
    border: 1px solid #29384E;
    border-radius: 12px;
    overflow: hidden;
}

/* Information, success and warning messages */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Horizontal separators */
hr {
    border-color: #29384E;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

/* Caption text */
[data-testid="stCaptionContainer"] {
    color: #94A3B8;
}

/* Responsive spacing on small screens */
/* Keep the in-page navigation comfortable to tap on phones */
div[role="radiogroup"] {
    gap: 0.5rem;
}

div[role="radiogroup"] label {
    min-height: 2.75rem;
    align-items: center;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    div[role="radiogroup"] {
        flex-wrap: wrap;
    }
}
</style>
""", unsafe_allow_html=True)


st.title("📊 Applied Mathematics-I")
st.subheader("Module VI: Probability, Skewness & Kurtosis")
st.caption(
    "Second Year Engineering | Information Technology | "
    "Interactive Mini Project"
)

# This navigation stays in the main page, so mobile users do not need
# to discover or open Streamlit's collapsed sidebar to change sections.
st.radio(
    "Navigate to a section",
    PROJECT_OPTIONS,
    key="main_project",
    horizontal=True,
    on_change=_sync_from_main
)

project = st.session_state["main_project"]

st.markdown("""
This application demonstrates Bayesian probability and statistical
moment analysis using network security and network latency examples.
""")



st.sidebar.title("Project Navigation")

st.sidebar.radio(
    "Choose a mini-project",
    PROJECT_OPTIONS,
    key="sidebar_project",
    on_change=_sync_from_sidebar
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Academic project based on Applied Mathematics-I, Module VI."
)

# ---------------- HOME PAGE ----------------


if project == "Home":

    st.header("Welcome to the Module VI Project")

    st.write(
        "An interactive workspace for probability and "
        "statistical analysis of network data."
    )

    # Dashboard summary cards
    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric("Mini Projects", "02", "Ready to explore")

    with metric2:
        st.metric("Mathematical Methods", "Bayes + Moments")

    with metric3:
        st.metric("Interactive Charts", "Enabled")

    st.markdown("---")

    col1, col2 = st.columns(2)


    with col1:
        st.subheader("1. Bayesian Intrusion Detection")
        st.write(
            "Calculate the probability of malware interception "
            "and identify the likely source server using Bayes' theorem."
        )
        st.latex(
            r"P(S_i\mid M)="
            r"\frac{P(M\mid S_i)P(S_i)}{P(M)}"
        )

    with col2:
        st.subheader("2. Network Latency Analysis")
        st.write(
            "Calculate central moments, skewness and kurtosis "
            "to study packet-delay distributions."
        )
        st.latex(r"\mu_r=\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^r")

    st.markdown("---")
    st.subheader("How to use this website")

    st.markdown("""
    1. Select a project from the left sidebar.
    2. Enter or modify the input values.
    3. Click the calculation button.
    4. Read the mathematical results and interpretation.
    5. Explore the tables and interactive graphs.
    """)

# ---------------- PROJECT 1 ----------------

elif project == "Bayesian Intrusion Detection":

    st.header("Bayesian Spam & Intrusion Detection")
    st.write(
        "Estimate the probability of malware interception across "
        "three servers and determine the probability that a detected "
        "malware packet originated from Server S3."
    )

    st.subheader("Step 1: Configure server traffic proportions")

    c1, c2, c3 = st.columns(3)

    with c1:
        p1 = st.number_input(
            "Traffic proportion: S1",
            min_value=0.0,
            max_value=1.0,
            value=0.40,
            step=0.05,
            format="%.2f"
        )

    with c2:
        p2 = st.number_input(
            "Traffic proportion: S2",
            min_value=0.0,
            max_value=1.0,
            value=0.35,
            step=0.05,
            format="%.2f"
        )

    with c3:
        p3 = st.number_input(
            "Traffic proportion: S3",
            min_value=0.0,
            max_value=1.0,
            value=0.25,
            step=0.05,
            format="%.2f"
        )

    st.caption(f"Total traffic proportion: {p1 + p2 + p3:.4f}")

    st.subheader("Step 2: Enter malware probabilities")

    c1, c2, c3 = st.columns(3)

    with c1:
        m1 = st.number_input(
            "P(Malware | S1)",
            min_value=0.0,
            max_value=1.0,
            value=0.01,
            step=0.01,
            format="%.3f"
        )

    with c2:
        m2 = st.number_input(
            "P(Malware | S2)",
            min_value=0.0,
            max_value=1.0,
            value=0.02,
            step=0.01,
            format="%.3f"
        )

    with c3:
        m3 = st.number_input(
            "P(Malware | S3)",
            min_value=0.0,
            max_value=1.0,
            value=0.04,
            step=0.01,
            format="%.3f"
        )

    if st.button("Calculate Bayesian Probabilities", type="primary"):

        proportions = np.array([p1, p2, p3])
        malware_rates = np.array([m1, m2, m3])

        if not np.isclose(proportions.sum(), 1.0):
            st.error(
                "The traffic proportions must add up to 1 "
                "(or 100%). Please correct the inputs."
            )

        else:
            # Total probability theorem
            total_malware = float(
                np.sum(proportions * malware_rates)
            )

            st.markdown("---")
            st.subheader("Results")

            r1, r2 = st.columns(2)

            with r1:
                st.metric(
                    "Total malware probability",
                    f"{total_malware * 100:.4f}%"
                )

            with r2:
                if total_malware > 0:
                    posterior_s3 = p3 * m3 / total_malware
                    st.metric(
                        "P(S3 | Malware)",
                        f"{posterior_s3 * 100:.4f}%"
                    )
                else:
                    posterior_s3 = None
                    st.metric("P(S3 | Malware)", "Undefined")

            st.subheader("Calculation 1: Total Probability Theorem")

            st.latex(
                r"P(M)=P(M\mid S_1)P(S_1)"
                r"+P(M\mid S_2)P(S_2)"
                r"+P(M\mid S_3)P(S_3)"
            )

            st.code(
                f"P(M) = ({m1:.4f} x {p1:.2f})"
                f" + ({m2:.4f} x {p2:.2f})"
                f" + ({m3:.4f} x {p3:.2f})\n"
                f"P(M) = {total_malware:.6f}\n"
                f"P(M) = {total_malware * 100:.4f}%"
            )

            st.subheader("Calculation 2: Bayes' Theorem")

            st.latex(
                r"P(S_3\mid M)="
                r"\frac{P(M\mid S_3)P(S_3)}{P(M)}"
            )

            if posterior_s3 is not None:
                st.code(
                    f"P(S3 | M) = ({m3:.4f} x {p3:.2f})"
                    f" / {total_malware:.6f}\n"
                    f"P(S3 | M) = {posterior_s3:.6f}\n"
                    f"P(S3 | M) = {posterior_s3 * 100:.4f}%"
                )

            else:
                st.warning(
                    "Bayes' posterior is undefined because "
                    "the total malware probability is zero."
                )

            results = pd.DataFrame({
                "Server": ["S1", "S2", "S3"],
                "Traffic proportion (%)": proportions * 100,
                "Malware probability (%)": malware_rates * 100,
                "Joint probability (%)":
                    proportions * malware_rates * 100
            })

            st.subheader("Server comparison")
            st.dataframe(results, use_container_width=True)

           
            fig = px.bar(
                results,
                x="Server",
                y="Joint probability (%)",
                color="Server",
                title="Contribution of Each Server to Malware Probability"
            )

            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="#E5E7EB",
                margin=dict(l=20, r=20, t=60, b=20)
            )

            st.plotly_chart(fig, use_container_width=True)

            st.success(
                "Calculation completed successfully."
            )

    st.info(
    "Default example: traffic proportions of 40%, 35%, and 25%, "
    "with malware probabilities of 1%, 2%, and 4% for S1, S2, "
    "and S3 respectively. Change the inputs to explore other scenarios."
)

# ---------------- PROJECT 2 ----------------

elif project == "Network Latency Analysis":

    st.header("Skewness & Kurtosis of Network Latency")

    st.write(
        "Analyze packet delays in milliseconds using the first four "
        "central moments, skewness and kurtosis."
    )

    default_data = "10, 12, 15, 12, 14, 22, 45, 11, 13, 16"

    raw_data = st.text_input(
        "Enter packet delays separated by commas (milliseconds)",
        value=default_data
    )

    if st.button("Analyze Latency Data", type="primary"):

        try:
            data = np.array(
                [float(x.strip()) for x in raw_data.split(",")],
                dtype=float
            )

            if len(data) < 2:
                st.error("Enter at least two observations.")

            elif not np.all(np.isfinite(data)):
                st.error("Enter only finite numeric values.")

            else:
                # Mean
                mean = float(np.mean(data))

                # Central moments, population definition
                deviations = data - mean

                mu1 = float(np.mean(deviations))
                mu2 = float(np.mean(deviations ** 2))
                mu3 = float(np.mean(deviations ** 3))
                mu4 = float(np.mean(deviations ** 4))

                st.markdown("---")
                st.subheader("Descriptive Statistics")

                c1, c2, c3 = st.columns(3)

                c1.metric("Number of packets", len(data))
                c2.metric("Mean delay", f"{mean:.4f} ms")
                c3.metric(
                    "Standard deviation",
                    f"{np.sqrt(mu2):.4f} ms"
                )

                st.subheader("First Four Central Moments")

                moments = pd.DataFrame({
                    "Moment": [
                        "First central moment (μ1)",
                        "Second central moment (μ2)",
                        "Third central moment (μ3)",
                        "Fourth central moment (μ4)"
                    ],
                    "Value": [mu1, mu2, mu3, mu4]
                })

                st.dataframe(moments, use_container_width=True)

                st.latex(
                    r"\mu_r=\frac{1}{n}"
                    r"\sum_{i=1}^{n}(x_i-\bar{x})^r"
                )

                st.write(f"Mean: x̄ = {mean:.6f} ms")

                st.write(
                    f"μ1 = {mu1:.6f}, "
                    f"μ2 = {mu2:.6f}, "
                    f"μ3 = {mu3:.6f}, "
                    f"μ4 = {mu4:.6f}"
                )

                st.subheader("Skewness")

                if mu2 > 0:
                    gamma1 = mu3 / (mu2 ** 1.5)
                    beta1 = (mu3 ** 2) / (mu2 ** 3)

                    st.latex(
                        r"\gamma_1=\frac{\mu_3}{\mu_2^{3/2}}"
                    )

                    st.metric(
                        "Moment coefficient of skewness (γ1)",
                        f"{gamma1:.6f}"
                    )

                    st.write(f"Pearson's β1 = {beta1:.6f}")

                    if gamma1 > 0.1:
                        st.write(
                            "Interpretation: the distribution is "
                            "positively skewed, with a longer right tail."
                        )
                    elif gamma1 < -0.1:
                        st.write(
                            "Interpretation: the distribution is "
                            "negatively skewed, with a longer left tail."
                        )
                    else:
                        st.write(
                            "Interpretation: the distribution is "
                            "approximately symmetric by this measure."
                        )

                else:
                    st.warning(
                        "Skewness is undefined because all delays "
                        "are identical."
                    )

                st.subheader("Kurtosis")

                if mu2 > 0:
                    beta2 = mu4 / (mu2 ** 2)
                    gamma2 = beta2 - 3

                    st.latex(
                        r"\beta_2=\frac{\mu_4}{\mu_2^2}"
                    )

                    st.metric(
                        "Kurtosis coefficient (β2)",
                        f"{beta2:.6f}"
                    )

                    st.metric(
                        "Excess kurtosis (γ2)",
                        f"{gamma2:.6f}"
                    )

                    if gamma2 > 0:
                        st.write(
                            "Interpretation: positive excess kurtosis "
                            "(leptokurtic relative to a normal distribution)."
                        )
                    elif gamma2 < 0:
                        st.write(
                            "Interpretation: negative excess kurtosis "
                            "(platykurtic relative to a normal distribution)."
                        )
                    else:
                        st.write(
                            "Interpretation: kurtosis equals the "
                            "normal-distribution reference value."
                        )

                else:
                    st.warning(
                        "Kurtosis is undefined because all delays "
                        "are identical."
                    )

                # Data table
                packet_df = pd.DataFrame({
                    "Packet number": np.arange(1, len(data) + 1),
                    "Delay (ms)": data
                })

                st.subheader("Packet Delay Data")
                st.dataframe(packet_df, use_container_width=True)

                
                # Line chart
                fig_line = px.line(
                    packet_df,
                    x="Packet number",
                    y="Delay (ms)",
                    markers=True,
                    title="Packet Delay by Observation"
                )

                fig_line.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#E5E7EB",
                    margin=dict(l=20, r=20, t=60, b=20)
                )

                st.plotly_chart(
                    fig_line,
                    use_container_width=True
                )

                # Histogram
                fig_hist = px.histogram(
                    packet_df,
                    x="Delay (ms)",
                    nbins=min(10, len(data)),
                    title="Distribution of Packet Delays"
                )

                fig_hist.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="#E5E7EB",
                    margin=dict(l=20, r=20, t=60, b=20)
                )

                st.plotly_chart(
                    fig_hist,
                    use_container_width=True
                )


                st.caption(
                    "Moments and coefficients use population "
                    "moment formulas (division by n). The skewness "
                    "and kurtosis are descriptive statistics, not "
                    "a formal network anomaly detector."
                )

                st.success("Latency analysis completed successfully.")

        except ValueError:
            st.error(
                "Invalid input. Enter numbers separated by commas, "
                "for example: 10, 12, 15, 22."
            )

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption(
    "Applied Mathematics-I | Module VI | "
    "Python and Streamlit Mini Project"
)
