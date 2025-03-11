import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

def apply_custom_css():
    """Apply custom CSS for a professional look."""
    st.markdown("""
        <style>
        /* General layout */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Header styling */
        .app-header {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            border-left: 5px solid #1E88E5;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        /* Title and header */
        h1 {
            color: #1E88E5;
            font-weight: 700;
        }
        
        h2 {
            color: #374151;
            font-weight: 600;
            margin-top: 1.5rem;
        }
        
        h3 {
            color: #4B5563;
            font-weight: 500;
        }
        
        /* Input container */
        .input-container {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            border: 1px solid #e5e7eb;
        }
        
        /* Section styling */
        .section {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            border: 1px solid #e5e7eb;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        /* Results container */
        .results-container {
            background-color: #f0f7ff;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
            border-left: 5px solid #1E88E5;
        }
        
        /* Success message */
        .high-approval {
            background-color: #d1fae5;
            border-left: 5px solid #10b981;
            padding: 1rem;
            border-radius: 5px;
        }
        
        .medium-approval {
            background-color: #fef3c7;
            border-left: 5px solid #f59e0b;
            padding: 1rem;
            border-radius: 5px;
        }
        
        .low-approval {
            background-color: #fee2e2;
            border-left: 5px solid #ef4444;
            padding: 1rem;
            border-radius: 5px;
        }
        
        /* Tips container */
        .tips-container {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1rem;
            border-left: 3px solid #6366f1;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: white;
            border-radius: 4px;
            color: #374151;
            border: 1px solid #e5e7eb;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #e3f2fd;
            color: #1E88E5;
        }
        
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: #1E88E5;
        }
        
        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 1rem;
        }
        
        /* Form label styling */
        .input-label {
            font-weight: 500;
            color: #374151;
            margin-bottom: 0.25rem;
        }
        
        /* Footnote */
        .footnote {
            font-size: 0.8rem;
            color: #6B7280;
            font-style: italic;
        }
        
        /* Button styling */
        .stButton>button {
            font-weight: 500;
        }
        
        /* Helper container */
        .helper-text {
            font-size: 0.8rem;
            color: #6B7280;
            margin-top: 0.25rem;
        }
        
        /* Info tooltip */
        .info-tooltip {
            color: #1E88E5;
            font-size: 1rem;
            cursor: help;
        }
        
        /* Status markers */
        .status-complete {
            color: #10b981;
            font-weight: 600;
        }
        
        .status-pending {
            color: #f59e0b;
            font-weight: 600;
        }
        
        /* Timeline */
        .timeline {
            border-left: 2px solid #e5e7eb;
            padding-left: 1rem;
            margin-left: 0.5rem;
        }
        
        .timeline-item {
            margin-bottom: 1rem;
            position: relative;
        }
        
        .timeline-item:before {
            content: '';
            position: absolute;
            left: -1.4rem;
            top: 0.25rem;
            width: 0.8rem;
            height: 0.8rem;
            background-color: #1E88E5;
            border-radius: 50%;
        }
        
        /* Gauge chart container */
        .gauge-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 250px;
        }
        
        /* Hide Streamlit defaults */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def create_header():
    """Display a header with a logo and title."""
    st.markdown("""
    <div class="app-header">
        <h1>Credit Risk Assessment</h1>
        <p>Enter your financial details to evaluate your loan approval odds.</p>
    </div>
    """, unsafe_allow_html=True)

def create_input_form():
    """Create a styled input form for the credit risk assessment.
    Returns a dictionary of input values, and also saves them to session state.
    """
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
    st.subheader("Financial Information")
    
    # Initialize session state for input values if they don't exist
    if 'annual_inc' not in st.session_state:
        st.session_state.annual_inc = 48000.0
    if 'dti' not in st.session_state:
        st.session_state.dti = 20.0
    if 'fico_range_low' not in st.session_state:
        st.session_state.fico_range_low = 700
    if 'loan_amnt' not in st.session_state:
        st.session_state.loan_amnt = 9000.0
    if 'revol_bal' not in st.session_state:
        st.session_state.revol_bal = 5000.0
    if 'term' not in st.session_state:
        st.session_state.term = '36 months'
    if 'emp_length' not in st.session_state:
        st.session_state.emp_length = '3 years'
    if 'home_ownership' not in st.session_state:
        st.session_state.home_ownership = 'MORTGAGE'
    if 'purpose' not in st.session_state:
        st.session_state.purpose = 'debt_consolidation'
    
    with st.expander("Loan Details", expanded=True):
        loan_amnt = st.number_input(
            "Loan Amount ($)", 
            min_value=1000.0, 
            max_value=100000.0, 
            value=st.session_state.loan_amnt, 
            step=500.0,
            help="The amount you are requesting to borrow.",
            key="loan_amnt"  # Use session state keys for consistency
        )
        
        term_options = ['36 months', '60 months']
        term = st.select_slider(
            "Loan Term", 
            options=term_options,
            value=st.session_state.term,
            help="The duration of the loan.",
            key="term"
        )
        
        purpose_options = [
            'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 
            'house', 'major_purchase', 'medical', 'moving', 'other', 
            'renewable_energy', 'small_business', 'vacation', 'wedding'
        ]
        purpose_display = {
            'credit_card': 'Credit Card Refinancing',
            'debt_consolidation': 'Debt Consolidation',
            'educational': 'Education',
            'home_improvement': 'Home Improvement',
            'house': 'House Purchase',
            'major_purchase': 'Major Purchase',
            'medical': 'Medical Expenses',
            'moving': 'Moving & Relocation',
            'other': 'Other',
            'renewable_energy': 'Renewable Energy',
            'small_business': 'Small Business',
            'vacation': 'Vacation',
            'wedding': 'Wedding'
        }
        
        # Find index of current value in purpose_options
        default_index = purpose_options.index(st.session_state.purpose) if st.session_state.purpose in purpose_options else 1
        
        purpose = st.selectbox(
            "Loan Purpose", 
            options=purpose_options,
            format_func=lambda x: purpose_display.get(x, x),
            index=default_index,
            help="The reason for taking the loan.",
            key="purpose"
        )
    
    with st.expander("Personal Details", expanded=True):
        annual_inc = st.number_input(
            "Annual Income ($)", 
            min_value=0.0, 
            max_value=500000.0, 
            value=st.session_state.annual_inc, 
            step=1000.0,
            help="Your yearly income before taxes.",
            key="annual_inc"
        )
        
        dti = st.slider(
            "Debt-to-Income Ratio (%)", 
            min_value=0.0, 
            max_value=100.0, 
            value=st.session_state.dti, 
            step=0.5,
            help="Your total monthly debt payments divided by your gross monthly income, expressed as a percentage.",
            key="dti"
        )
        
        revol_bal = st.number_input(
            "Revolving Balance ($)", 
            min_value=0.0, 
            max_value=100000.0, 
            value=st.session_state.revol_bal, 
            step=500.0,
            help="The unpaid balance on your credit card or other revolving accounts.",
            key="revol_bal"
        )
        
        fico_range_low = st.slider(
            "FICO Credit Score", 
            min_value=300, 
            max_value=850, 
            value=st.session_state.fico_range_low, 
            step=5,
            help="Your credit score, ranging from 300 to 850.",
            key="fico_range_low"
        )
        
        emp_length_options = ['< 1 year', '1 year', '2 years', '3 years', '4 years', '5 years', '6 years', '7 years', '8 years', '9 years', '10+ years']
        emp_length = st.select_slider(
            "Employment Length", 
            options=emp_length_options,
            value=st.session_state.emp_length,
            help="How long you have been employed.",
            key="emp_length"
        )
        
        home_ownership_options = ['MORTGAGE', 'RENT', 'OWN', 'OTHER', 'NONE']
        home_ownership_display = {
            'MORTGAGE': 'Mortgage',
            'RENT': 'Rent',
            'OWN': 'Own',
            'OTHER': 'Other',
            'NONE': 'None'
        }
        
        # Find index of current home_ownership in options
        home_idx = home_ownership_options.index(st.session_state.home_ownership) if st.session_state.home_ownership in home_ownership_options else 0
        
        home_ownership = st.radio(
            "Home Ownership", 
            options=home_ownership_options,
            format_func=lambda x: home_ownership_display.get(x, x),
            index=home_idx,
            horizontal=True,
            help="Your housing situation.",
            key="home_ownership"
        )
    
    # Visual clues for invalid inputs
    if annual_inc <= 0:
        st.warning("⚠️ Annual Income must be greater than 0.")
    if loan_amnt <= 0:
        st.warning("⚠️ Loan Amount must be greater than 0.")
    
    # Calculate some ratios to show in form summary
    loan_to_income_ratio = (loan_amnt / annual_inc) * 100 if annual_inc > 0 else 0
    term_months = 36 if term == '36 months' else 60
    est_monthly_payment = loan_amnt / term_months  # Simple calculation, doesn't factor in interest
    
    # Summary of inputs
    with st.expander("Application Summary", expanded=False):
        st.markdown(f"""
        - Loan amount: **${loan_amnt:,.2f}**
        - Loan term: **{term}**
        - Loan purpose: **{purpose_display.get(purpose, purpose)}**
        - Loan-to-income ratio: **{loan_to_income_ratio:.1f}%**
        - Est. monthly payment: **${est_monthly_payment:.2f}** (excluding interest)
        - Annual income: **${annual_inc:,.2f}**
        - Debt-to-income ratio: **{dti:.1f}%**
        - FICO credit score: **{fico_range_low}**
        - Employment length: **{emp_length}**
        - Home ownership: **{home_ownership_display.get(home_ownership, home_ownership)}**
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Return all inputs as a dictionary
    # Session state is now updated automatically with the input widget keys
    return {
        "annual_inc": annual_inc,
        "dti": dti,
        "fico_range_low": fico_range_low,
        "loan_amnt": loan_amnt,
        "revol_bal": revol_bal,
        "term": term,
        "emp_length": emp_length,
        "home_ownership": home_ownership,
        "purpose": purpose
    }

def get_approval_category(probability):
    """Return a category based on approval probability."""
    if probability >= 0.75:
        return "high", "High Approval Odds", "Your financial profile shows strong indicators for loan approval."
    elif probability >= 0.5:
        return "medium", "Moderate Approval Odds", "Your financial profile shows reasonable indicators for loan approval."
    else:
        return "low", "Low Approval Odds", "Your financial profile may need improvement to increase approval odds."

def get_improvement_tips(inputs, probability):
    """Return personalized tips based on inputs and prediction."""
    tips = []
    
    # Check various factors and provide relevant tips
    if probability < 0.75:
        # Credit score tips
        if inputs["fico_range_low"] < 700:
            tips.append("Improve your credit score by paying bills on time and reducing credit card balances.")
        
        # DTI tips
        if inputs["dti"] > 30:
            tips.append("Work on reducing your debt-to-income ratio by paying down existing debts.")
        
        # Loan amount tips
        loan_to_income = inputs["loan_amnt"] / inputs["annual_inc"]
        if loan_to_income > 0.3:
            tips.append("Consider requesting a smaller loan amount relative to your annual income.")
        
        # Employment length tips
        emp_length_mapping = {'< 1 year': 0, '1 year': 1, '2 years': 2, '3 years': 3, '4 years': 4,
                            '5 years': 5, '6 years': 6, '7 years': 7, '8 years': 8, '9 years': 9,
                            '10+ years': 10}
        if emp_length_mapping[inputs["emp_length"]] < 2:
            tips.append("Lenders often prefer employment stability of 2+ years at the same employer.")
        
        # Revolving balance tips
        if inputs["revol_bal"] > 10000:
            tips.append("Consider reducing your revolving credit balance to improve approval odds.")
    
    if not tips:
        tips.append("Your financial profile looks strong! Continue maintaining your good financial habits.")
    
    return tips

def create_gauge_chart(probability):
    """Create a gauge chart visualization for approval odds."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Approval Odds", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "royalblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#ffcccb'},
                {'range': [30, 50], 'color': '#ffdab9'},
                {'range': [50, 75], 'color': '#fffacd'},
                {'range': [75, 100], 'color': '#ccffcc'}],
            'threshold': {
                'line': {'color': "blue", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=30, r=30, t=50, b=30),
    )
    
    return fig

def create_about_tab():
    """Create the 'About the App' tab content."""
    st.markdown("""
    <div class="section">
        <h2>About the Credit Risk Assessment App</h2>
        <p>This application is designed to help you understand your loan approval odds before applying, potentially saving you time and protecting your credit score from unnecessary inquiries.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section">
        <h3>The Model</h3>
        <p>This app uses an Artificial Neural Network (ANN) trained on LendingClub data from 2007-2018, covering millions of loan applications. The model analyzes various financial factors to predict approval probability.</p>
        
        <h3>Key Features</h3>
        <ul>
            <li><strong>Personalized Assessment:</strong> Get a tailored evaluation based on your specific financial situation</li>
            <li><strong>Instant Results:</strong> Receive immediate feedback on your loan approval odds</li>
            <li><strong>Improvement Tips:</strong> Discover actionable steps to improve your approval chances</li>
            <li><strong>Educational Content:</strong> Learn about key factors that influence loan decisions</li>
        </ul>
        
        <h3>Data Privacy</h3>
        <p>Your data is processed locally in your browser and is not stored or shared with third parties. No personal information is retained after you close the application.</p>
        
        <h3>Disclaimer</h3>
        <p>This tool provides estimates based on historical data and general lending practices. Results are for educational purposes only and do not guarantee approval from any specific lender.</p>
        
        <div class="footnote">
            Last updated: March 2025<br>
            Version: 1.0.3
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_how_it_works_tab():
    """Create the 'How It Works' tab content with detailed information."""
    st.markdown("""
    <div class="section">
        <h2>How It Works</h2>
        <p>The Credit Risk Assessment App uses machine learning to evaluate your loan approval odds based on key financial factors.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Process overview
    st.markdown("""
    <div class="section">
        <h3>The Assessment Process</h3>
        
        <div class="timeline">
            <div class="timeline-item">
                <strong>Data Input</strong><br>
                You provide key financial details such as income, credit score, loan amount, and more.
            </div>
            
            <div class="timeline-item">
                <strong>Data Processing</strong><br>
                Your inputs are processed and transformed to match the format used by our machine learning model.
            </div>
            
            <div class="timeline-item">
                <strong>AI Prediction</strong><br>
                Our artificial neural network analyzes your profile against patterns from millions of historical loan applications.
            </div>
            
            <div class="timeline-item">
                <strong>Results & Recommendations</strong><br>
                You receive your approval odds and personalized tips for improvement.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key factors
    st.markdown("""
    <div class="section">
        <h3>Key Factors That Influence Approval</h3>
        
        <h4>Major Impact Factors</h4>
        <ul>
            <li><strong>Credit Score (FICO)</strong>: Higher scores significantly increase approval odds</li>
            <li><strong>Debt-to-Income Ratio (DTI)</strong>: Lower ratios (below 36%) are preferred</li>
            <li><strong>Income</strong>: Higher income relative to loan amount improves chances</li>
        </ul>
        
        <h4>Moderate Impact Factors</h4>
        <ul>
            <li><strong>Employment Length</strong>: Longer employment history increases stability</li>
            <li><strong>Loan Purpose</strong>: Some purposes (debt consolidation, home improvement) may be viewed more favorably</li>
            <li><strong>Loan Amount</strong>: Smaller loans relative to income are easier to approve</li>
        </ul>
        
        <h4>Lesser Impact Factors</h4>
        <ul>
            <li><strong>Revolving Balance</strong>: Lower revolving debt shows responsible credit management</li>
            <li><strong>Home Ownership</strong>: Owning or having a mortgage can sometimes improve odds</li>
            <li><strong>Loan Term</strong>: Shorter terms may have slightly higher approval rates</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips for improving odds
    st.markdown("""
    <div class="section">
        <h3>Tips to Improve Your Approval Odds</h3>
        
        <div class="tips-container">
            <h4>Before Applying</h4>
            <ul>
                <li>Check and improve your credit score</li>
                <li>Pay down existing debts to lower your DTI</li>
                <li>Maintain stable employment</li>
                <li>Consider a smaller loan amount or longer term</li>
                <li>Reduce your revolving credit utilization</li>
                <li>Save for a larger down payment if applicable</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_results(probability, inputs=None, feature_importances=None):
    """Display prediction results in a structured, styled format.
    
    Args:
        probability: The prediction probability from the model
        inputs: Optional dictionary of user inputs
        feature_importances: Optional feature importance data
    """
    # Get inputs from session state if not provided
    if inputs is None:
        inputs = {
            "annual_inc": st.session_state.get("annual_inc", 48000),
            "dti": st.session_state.get("dti", 20),
            "fico_range_low": st.session_state.get("fico_range_low", 700),
            "loan_amnt": st.session_state.get("loan_amnt", 9000),
            "revol_bal": st.session_state.get("revol_bal", 5000),
            "term": st.session_state.get("term", "36 months"),
            "emp_length": st.session_state.get("emp_length", "3 years"),
            "home_ownership": st.session_state.get("home_ownership", "MORTGAGE"),
            "purpose": st.session_state.get("purpose", "debt_consolidation")
        }
    
    category, title, description = get_approval_category(probability)
    
    # Header section
    st.markdown(f"""
    <div class="results-container">
        <h2>Loan Approval Assessment</h2>
        <p>Based on your provided information, here are your loan approval odds:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Approval odds visualization
    st.markdown('<div class="gauge-container">', unsafe_allow_html=True)
    fig = create_gauge_chart(probability)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Text results with proper styling
    st.markdown(f"""
    <div class="{category}-approval">
        <h3>{title}</h3>
        <p>{description}</p>
        <p>Approval Probability: <strong>{probability:.2%}</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Improvement tips
    tips = get_improvement_tips(inputs, probability)
    
    st.markdown("""
    <div class="tips-container">
        <h4>💡 Tips to Improve Your Odds</h4>
        <ul>
    """, unsafe_allow_html=True)
    
    for tip in tips:
        st.markdown(f"<li>{tip}</li>", unsafe_allow_html=True)
    
    st.markdown("""
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature importance section (if provided)
    if feature_importances is not None and len(feature_importances) > 0:
        st.markdown("""
        <div class="section">
            <h4>Most Influential Factors in Your Assessment</h4>
        """, unsafe_allow_html=True)
        
        # Display feature importances visualization or table
        importance_df = pd.DataFrame(feature_importances)
        st.bar_chart(importance_df.set_index('Feature')['Importance'])
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Notes/disclaimer
    st.markdown("""
    <div class="section">
        <h4>Notes</h4>
        <ul>
            <li>Odds above 50% indicate a higher likelihood of approval.</li>
            <li>This assessment is based on historical data and may not reflect current lending practices.</li>
            <li>Adjust your inputs to see how different financial scenarios impact your odds!</li>
        </ul>
        <p class="footnote">Last updated: March 2025 | Disclaimer: This tool provides an estimate only and does not guarantee loan approval.</p>
    </div>
    """, unsafe_allow_html=True)

def create_results_section():
    """Create a section to display prediction results.
    This is called from app2.py and displays results if available in session state.
    """
    if st.session_state.get('prediction_made', False) and 'approval_odds' in st.session_state:
        probability = st.session_state.approval_odds
        # Get current input values from session state
        inputs = {
            "annual_inc": st.session_state.get("annual_inc", 48000),
            "dti": st.session_state.get("dti", 20),
            "fico_range_low": st.session_state.get("fico_range_low", 700),
            "loan_amnt": st.session_state.get("loan_amnt", 9000),
            "revol_bal": st.session_state.get("revol_bal", 5000),
            "term": st.session_state.get("term", "36 months"),
            "emp_length": st.session_state.get("emp_length", "3 years"),
            "home_ownership": st.session_state.get("home_ownership", "MORTGAGE"),
            "purpose": st.session_state.get("purpose", "debt_consolidation")
        }
        display_results(probability, inputs)
    else:
        # No prediction yet
        st.markdown("""
        <div class="section">
            <h3>Your Results Will Appear Here</h3>
            <p>Fill out the form and click "Predict Approval Odds" to see your loan approval probability.</p>
            <div class="timeline">
                <div class="timeline-item">
                    <strong>Step 1:</strong> Enter your financial information
                </div>
                <div class="timeline-item">
                    <strong>Step 2:</strong> Click the "Predict Approval Odds" button
                </div>
                <div class="timeline-item">
                    <strong>Step 3:</strong> Review your approval odds and personalized tips
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Removed main_ui function as it's not used in app2.py