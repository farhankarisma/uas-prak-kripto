import streamlit as st
from typing import Optional
import string

class ROT13Cipher:
    def __init__(self):
        """Initialize the ROT13 cipher with lookup tables for better performance."""
        # Create lookup tables for lowercase and uppercase letters
        self.lower_lookup = str.maketrans(
            string.ascii_lowercase,
            string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
        )
        self.upper_lookup = str.maketrans(
            string.ascii_uppercase,
            string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
        )
        
    def encrypt(self, text: str) -> str:
        """
        Encrypt/decrypt text using ROT13 cipher (since ROT13 is its own inverse).
        
        Args:
            text (str): The input text to encrypt/decrypt
            
        Returns:
            str: The encrypted/decrypted text
        """
        if not text:
            return ""
            
        # Apply both lowercase and uppercase transformations
        return text.translate(self.lower_lookup).translate(self.upper_lookup)
        
    def process_file(self, file_content: str) -> Optional[str]:
        """
        Process content from an uploaded file.
        
        Args:
            file_content (str): Content from the uploaded file
            
        Returns:
            Optional[str]: Processed text or None if content is invalid
        """
        try:
            return self.encrypt(file_content)
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            return None

def create_download_button(text: str, filename: str):
    """Create a download button for the processed text."""
    st.download_button(
        label="Download result",
        data=text,
        file_name=filename,
        mime="text/plain"
    )

def main():
    st.set_page_config(
        page_title="ROT13 Cipher Tool",
        page_icon="🔐",
        layout="wide"
    )
    
    # Initialize the cipher
    cipher = ROT13Cipher()
    
    # Main title with custom styling
    st.title("🔄 ROT13 Cipher Tool")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Description
    st.markdown("""
    ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet.
    It's often used for hiding spoilers or puzzle answers. Since ROT13 is its own inverse, the same function is used for both encoding and decoding.
    """)
    
    # Create tabs for different input methods
    tab1, tab2 = st.tabs(["Text Input", "File Input"])
    
    with tab1:
        # Text input method
        input_text = st.text_area(
            "Enter your text here:",
            height=150,
            placeholder="Type or paste your text here..."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Process", type="primary"):
                if input_text:
                    result = cipher.encrypt(input_text)
                    st.markdown("### Result:")
                    st.text_area("Processed text:", value=result, height=150)
                    create_download_button(result, "rot13_result.txt")
                else:
                    st.warning("Please enter some text to process.")
    
    with tab2:
        # File input method
        uploaded_file = st.file_uploader(
            "Choose a text file",
            type=['txt'],
            help="Upload a text file to process with ROT13"
        )
        
        if uploaded_file is not None:
            content = uploaded_file.getvalue().decode()
            if st.button("Process File", type="primary"):
                result = cipher.process_file(content)
                if result:
                    st.markdown("### Result:")
                    st.text_area("Processed text:", value=result, height=150)
                    create_download_button(
                        result,
                        f"rot13_{uploaded_file.name}"
                    )
    
    # Add examples section
    with st.expander("See Examples"):
        st.markdown("""
        **Example inputs and their ROT13 outputs:**
        1. "Hello, World!" → "Uryyb, Jbeyq!"
        2. "Secret Message" → "Frperg Zrffntr"
        3. "ROT13" → "EBG13"
        
        *Note: Numbers and special characters remain unchanged.*
        """)
    
    # Add a footer with additional information
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>This tool can be used for both encoding and decoding ROT13 text.</p>
        <p>All processing is done locally in your browser.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()