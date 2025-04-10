import streamlit as st

# Page setup
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")
st.title("❌ Tic-Tac-Toe ⭕

Play with a friend! Take turns and try to win!")

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current = "X"
    st.session_state.winner = None
    st.session_state.win_combo = []

# Winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
    [0, 4, 8], [2, 4, 6]              # diagonals
]

# Check for winner
def check_winner():
    for combo in winning_combinations:
        a, b, c = combo
        if st.session_state.board[a] == st.session_state.board[b] == st.session_state.board[c] != "":
            st.session_state.winner = st.session_state.board[a]
            st.session_state.win_combo = combo
            return

# Game grid
cols = st.columns(3)
for i in range(9):
    highlight = "background-color: lightgreen;" if i in st.session_state.win_combo else ""
    with cols[i % 3]:
        if st.session_state.board[i] or st.session_state.winner:
            st.markdown(
                f"<div style='text-align:center; font-size:40px; {highlight}'>{st.session_state.board[i]}</div>",
                unsafe_allow_html=True,
            )
        else:
            if st.button(" ", key=i):
                st.session_state.board[i] = st.session_state.current
                check_winner()
                if not st.session_state.winner:
                    st.session_state.current = "O" if st.session_state.current == "X" else "X"

# Status display
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif "" not in st.session_state.board:
    st.info("🤝 It's a draw!")
else:
    st.write(f"Player **{st.session_state.current}**'s turn.")

# Restart button
if st.button("🔁 Restart Game"):
    for key in ["board", "current", "winner", "win_combo"]:
        del st.session_state[key]
    st.experimental_rerun()
