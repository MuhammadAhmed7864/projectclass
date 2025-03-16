import streamlit as st
import streamlit.components.v1 as components

def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Type Casting
    word_count_str = str(word_count)
    vowel_count_str = str(vowel_count)
    
    # Operators
    contains_python = "Python" in text
    avg_word_length = char_count / word_count if word_count > 0 else 0
    
    return word_count, char_count, vowel_count, word_count_str, vowel_count_str, contains_python, avg_word_length

def main():
    st.set_page_config(page_title="Text Analysis Tool", layout="centered")
    
    # Custom CSS
    st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        .stTextArea, .stTextInput {
            border-radius: 10px;
            border: 1px solid #ccc;
            padding: 10px;
            width: 100%;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("📊 Text Analysis Tool")
    
    text = st.text_area("✍️ Enter a paragraph:", height=200)
    
    if st.button("Analyze Text"):
        if text.strip():
            word_count, char_count, vowel_count, word_count_str, vowel_count_str, contains_python, avg_word_length = analyze_text(text)
            
            st.subheader("📌 Analysis Results:")
            st.write(f"🔢 **Total Words:** {word_count_str}")
            st.write(f"📄 **Total Characters (including spaces):** {char_count}")
            st.write(f"🗣️ **Total Vowels:** {vowel_count_str}")
            st.write(f"📏 **Average Word Length:** {avg_word_length:.2f}")
            
            if contains_python:
                st.success("✅ The paragraph contains the word 'Python'.")
            else:
                st.warning("❌ The paragraph does not contain the word 'Python'.")
            
            # Search and Replace
            st.subheader("🔍 Search and Replace")
            search_word = st.text_input("Enter a word to search for:")
            replace_word = st.text_input("Enter a word to replace it with:")
            
            if search_word and replace_word and st.button("Replace Word"):
                modified_text = text.replace(search_word, replace_word)
                st.write("✏️ **Modified Paragraph:**")
                st.write(modified_text)
            
            # Uppercase and Lowercase Conversion
            st.subheader("🔠 Text Transformations")
            st.write("🔤 **Uppercase Paragraph:**")
            st.code(text.upper(), language="text")
            
            st.write("🔡 **Lowercase Paragraph:**")
            st.code(text.lower(), language="text")
        else:
            st.warning("⚠️ Please enter a paragraph to analyze.")

if __name__ == "__main__":
    main()
