import streamlit as st
import time

# Initialize session state
if 'story' not in st.session_state:
    st.session_state.story = """Once upon a time, in a land far away, there lived a curious traveler who sought wisdom from the mountains and the seas.

The journey was long and filled with challenges, but each step brought new understanding. Through storms and sunshine, the traveler pressed on, collecting stories from every village and town.

Years passed, and the traveler grew older but wiser. The collection of tales became a treasure more valuable than gold, for in them lived the hopes, dreams, and lessons of countless souls.

And so the story continues, written in the hearts of all who dare to listen..."""

if 'show_confirm' not in st.session_state:
    st.session_state.show_confirm = False

if 'fade_out' not in st.session_state:
    st.session_state.fade_out = False

# Custom CSS for fade-out animation
st.markdown("""
    <style>
    .story-container {
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 20px;
        transition: opacity 0.8s ease-out;
    }
    .fade-out {
        opacity: 0;
    }
    .stButton button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📖 Story Reader")

# Display story with fade-out class if needed
if st.session_state.story:
    fade_class = "fade-out" if st.session_state.fade_out else ""
    st.markdown(f'<div class="story-container {fade_class}">', unsafe_allow_html=True)
    st.markdown(st.session_state.story)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Confirmation dialog
    if st.session_state.show_confirm:
        st.warning("⚠️ Are you sure you want to delete this story? This action cannot be undone.")
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
        # Done button
        if st.button("🗑️ DONE - Delete Story", type="secondary"):
            st.session_state.show_confirm = True
            st.rerun()
else:
    st.info("📝 The story has been deleted. You have a clean slate!")
    if st.button("↻ Start New Story"):
        st.session_state.story = """Once upon a time, in a land far away, there lived a curious traveler who sought wisdom from the mountains and the seas.

The journey was long and filled with challenges, but each step brought new understanding. Through storms and sunshine, the traveler pressed on, collecting stories from every village and town.

Years passed, and the traveler grew older but wiser. The collection of tales became a treasure more valuable than gold, for in them lived the hopes, dreams, and lessons of countless souls.

And so the story continues, written in the hearts of all who dare to listen..."""
        st.session_state.show_confirm = False
        st.session_state.fade_out = False
        st.rerun()

# Handle fade-out completion
if st.session_state.fade_out:
    time.sleep(0.8)  # Wait for animation
    st.session_state.story = None
    st.session_state.show_confirm = False
    st.session_state.fade_out = False
    st.rerun()