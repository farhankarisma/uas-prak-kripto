import streamlit as st
from PIL import Image
import base64
from pathlib import Path

def set_custom_style():
    """Set custom CSS styles for the application."""
    st.markdown("""
        <style>
        .cipher-card {
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #f0f2f6;
            margin: 10px 0;
        }
        .cipher-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .cipher-description {
            font-size: 16px;
            color: #666;
            margin-bottom: 15px;
        }
        .stButton button {
            width: 100%;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #666;
            margin-bottom: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

def create_cipher_card(title, description, page_name):
    """Create a card for each cipher tool."""
    with st.container():
        st.markdown(f"""
            <div class="cipher-card">
                <div class="cipher-title">{title}</div>
                <div class="cipher-description">{description}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Go to {title}", key=page_name):
            st.switch_page(f"pages/{page_name}.py")

def main():
    # Page configuration
    st.set_page_config(
        page_title="Cipher Tools Home",
        page_icon="🔒",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom styling
    set_custom_style()
    
    # Main title and description
    st.markdown('<p class="main-title">🔐 Classical Cipher Tools</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Explore different classical encryption methods</p>',
        unsafe_allow_html=True
    )
    
    # Create two columns for the cipher cards
    col1, col2 = st.columns(2)
    
    # ROT13 Cipher Card
    with col1:
        create_cipher_card(
            "ROT13 Cipher",
            """
            ROT13 is a simple letter substitution cipher that replaces a letter 
            with the 13th letter after it in the alphabet. It's often used for 
            hiding spoilers or puzzle answers.
            """,
            "rot13"
        )
    
    # Affine Cipher Card
    with col2:
        create_cipher_card(
            "Affine Cipher",
            """
            Affine cipher is a type of monoalphabetic substitution cipher that 
            combines multiplication and addition modulo 26. It's an extension of 
            the shift cipher.
            """,
            "affine"
        )
    
    # Information section
    st.markdown("---")
    st.markdown("### How to Use")
    
    # Create columns for instructions
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        1. Choose a cipher tool from the options above
        2. Enter your text or upload a file
        3. Set the required parameters
        4. Process your text
        5. Download the results
        """)
    
    with col2:
        st.markdown("""
        **Features:**
        - Text and file input support
        - Real-time encryption/decryption
        - Download results as text files
        - Educational examples and explanations
        """)
    
if __name__ == "__main__":
    main()