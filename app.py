import streamlit as st
import time
import os

# Specify your story file here - change this to your actual file name
STORY_FILE = "draft.txt"

# Initialize session state
if 'show_confirm' not in st.session_state:
    st.session_state.show_confirm = False

if 'fade_out' not in st.session_state:
    st.session_state.fade_out = False

# Function to read story from file
def read_story():
    if os.path.exists(STORY_FILE):
        with open(STORY_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    return None

# Function to delete story file
def delete_story():
    if os.path.exists(STORY_FILE):
        os.remove(STORY_FILE)

# Custom CSS for fade-out animation
st.markdown("""
    <style>
    .story-container {
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 20px;
        transition: opacity 0.8s ease-out;
        white-space: pre-wrap;
        line-height: 1.6;
    }
    .fade-out {
        opacity: 0;
    }
    .stButton button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title(".")

# Read story from file
story = read_story()

# Display story with fade-out class if needed
if story:
    fade_class = "fade-out" if st.session_state.fade_out else ""
    st.markdown(f'<div class="story-container {fade_class}">', unsafe_allow_html=True)
    st.markdown(story)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Confirmation dialog
    if st.session_state.show_confirm:
        st.warning("This action cannot be undone.")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✓ Yes, Delete", type="primary"):
                st.session_state.fade_out = True
                st.rerun()
        
        with col2:
            if st.button("✗ Cancel"):
                st.session_state.show_confirm = False
                st.rerun()
    else:
        # Done butto
        if st.button("🗑️ DONE - Delete ", type="secondary"):
            st.session_state.show_confirm = True
            st.rerun()
else:
    st.error(f"❌  '{STORY_FILE}' not found or has been deleted.")
    st.info("📝 You have a clean slate!")

# Handle fade-out completion and actual deletion
if st.session_state.fade_out:
    time.sleep(0.8)  # Wait for animation
    delete_story()
    st.session_state.show_confirm = False
    st.session_state.fade_out = False
    st.rerun()
