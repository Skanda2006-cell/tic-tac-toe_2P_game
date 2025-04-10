import streamlit as st

# Title and style
st.set_page_config(page_title="Tic-Tac-Toe", layout="centered")
st.markdown("<h1 style='text-align:center;'>❌ Tic-Tac-Toe ⭕</h1>", unsafe_allow_html=True)

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Winning combinations
winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

# Check for winner
def check_winner():
    for combo in winning_combos:
        a, b, c = combo
        if st.session_state.board[a] == st.session_state.board[b] == st.session_state.board[c] != "":
            return st.session_state.board[a], combo
    return None, []

# Make a move
def make_move(index):
    if st.session_state.board[index] == "" and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        winner, combo = check_winner()
        if winner:
            st.session_state.winner = (winner, combo)
        elif "" not in st.session_state.board:
            st.session_state.winner = ("Draw", [])
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Display the game board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        idx = i * 3 + j
        cell = st.session_state.board[idx]
        highlight = (
            st.session_state.winner
            and idx in st.session_state.winner[1]
        )

        btn_label = "❌" if cell == "X" else "⭕" if cell == "O" else "⬜️"
        btn_style = "font-size:36px; height:80px; width:100%;"

        if highlight:
            btn_style += " background-color:#a5d6a7; border: 3px solid green;"

        with cols[j]:
            st.markdown(
                f"""<button style="{btn_style}" disabled>{btn_label}</button>""",
                unsafe_allow_html=True,
            ) if cell else st.button(
                btn_label, key=idx, on_click=make_move, args=(idx,),
                use_container_width=True,
            )

# Show game status
if st.session_state.winner:
    winner = st.session_state.winner[0]
    if winner == "Draw":
        st.info("🤝 It's a Draw!")
    else:
        st.success(f"🎉 Player {winner} wins!")

else:
    st.markdown(f"**Current Player: {'❌' if st.session_state.current_player == 'X' else '⭕'}**")

# Restart game
if st.button("🔄 Restart"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
