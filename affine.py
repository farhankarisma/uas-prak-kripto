import streamlit as st
import string

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular multiplicative inverse of a modulo m."""
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return None

class AffineCipher:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
        self.letter_to_index = {letter: index for index, letter in enumerate(self.alphabet)}
        self.index_to_letter = {index: letter for index, letter in enumerate(self.alphabet)}
        
    def validate_key(self, a):
        """Validate if 'a' is coprime with 26."""
        if gcd(a, 26) != 1:
            return False
        return True
        
    def encrypt(self, plaintext, a, b):
        """Encrypt the plaintext using Affine Cipher."""
        if not self.validate_key(a):
            return "Error: 'a' must be coprime with 26"
            
        ciphertext = ""
        plaintext = plaintext.upper()
        
        for char in plaintext:
            if char in self.letter_to_index:
                # E(x) = (ax + b) mod 26
                x = self.letter_to_index[char]
                encrypted_index = (a * x + b) % 26
                ciphertext += self.index_to_letter[encrypted_index]
            else:
                ciphertext += char
                
        return ciphertext
        
    def decrypt(self, ciphertext, a, b):
        """Decrypt the ciphertext using Affine Cipher."""
        if not self.validate_key(a):
            return "Error: 'a' must be coprime with 26"
            
        plaintext = ""
        a_inverse = mod_inverse(a, 26)
        ciphertext = ciphertext.upper()
        
        for char in ciphertext:
            if char in self.letter_to_index:
                # D(y) = a^(-1)(y - b) mod 26
                y = self.letter_to_index[char]
                decrypted_index = (a_inverse * (y - b)) % 26
                plaintext += self.index_to_letter[decrypted_index]
            else:
                plaintext += char
                
        return plaintext

# Streamlit UI
def main():
    st.title("Affine Cipher Encoder/Decoder")
    
    # Create tabs for encrypt and decrypt
    tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])
    
    cipher = AffineCipher()
    
    with tab1:
        st.header("Encryption")
        plaintext = st.text_input("Enter text to encrypt:", key="encrypt_input")
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Enter key 'a' (must be coprime with 26):", min_value=1, value=5, key="encrypt_a")
        with col2:
            b = st.number_input("Enter key 'b':", min_value=0, value=8, key="encrypt_b")
            
        if st.button("Encrypt", key="encrypt_button"):
            if plaintext:
                result = cipher.encrypt(plaintext, a, b)
                st.success(f"Encrypted text: {result}")
            else:
                st.warning("Please enter text to encrypt")
    
    with tab2:
        st.header("Decryption")
        ciphertext = st.text_input("Enter text to decrypt:", key="decrypt_input")
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Enter key 'a' (must be coprime with 26):", min_value=1, value=5, key="decrypt_a")
        with col2:
            b = st.number_input("Enter key 'b':", min_value=0, value=8, key="decrypt_b")
            
        if st.button("Decrypt", key="decrypt_button"):
            if ciphertext:
                result = cipher.decrypt(ciphertext, a, b)
                st.success(f"Decrypted text: {result}")
            else:
                st.warning("Please enter text to decrypt")

if __name__ == "__main__":
    main()