import streamlit as st
import random
import time

# Set up page
st.set_page_config(page_title="🃏 Memory Game", layout="centered")
st.title("🧠 Memory Card Game")
st.write("Flip the cards and try to match all pairs!")

# Initialize game
if "cards" not in st.session_state:
    emojis = ['🍎', '🚗', '🐶', '🎵', '🌟', '🏀', '📚', '🎲']
    cards = emojis * 2
    random.shuffle(cards)
    st.session_state.cards = cards
    st.session_state.revealed = [False] * 16
    st.session_state.matched = [False] * 16
    st.session_state.selected = []
    st.session_state.moves = 0
    st.session_state.last_action_time = 0

# Function to reveal or match logic
def handle_click(i):
    if st.session_state.revealed[i] or st.session_state.matched[i]:
        return
    st.session_state.revealed[i] = True
    st.session_state.selected.append(i)

# Handle timed reset for unmatched cards
if len(st.session_state.selected) == 2:
    idx1, idx2 = st.session_state.selected
    if st.session_state.cards[idx1] == st.session_state.cards[idx2]:
        st.session_state.matched[idx1] = True
        st.session_state.matched[idx2] = True
        st.session_state.selected = []
    else:
        now = time.time()
        if st.session_state.last_action_time == 0:
            st.session_state.last_action_time = now
        elif now - st.session_state.last_action_time >= 0.7:
            st.session_state.revealed[idx1] = False
            st.session_state.revealed[idx2] = False
            st.session_state.selected = []
            st.session_state.last_action_time = 0
            st.session_state.moves += 1
            st.experimental_rerun()

# Show card grid
cols = st.columns(4)
for i in range(16):
    with cols[i % 4]:
        if st.session_state.revealed[i] or st.session_state.matched[i]:
            st.button(st.session_state.cards[i], key=str(i), disabled=True)
        else:
            if st.button("❓", key=str(i)):
                handle_click(i)

# Show stats
st.markdown(f"### Moves: {st.session_state.moves}")
if all(st.session_state.matched):
    st.success("🎉 Congratulations! You've matched all the cards!")

# Restart game
if st.button("🔄 Restart Game"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()
