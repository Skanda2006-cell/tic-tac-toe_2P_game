import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic Tac Toe 🕹️", layout="centered")
st.title("🎮 Tic Tac Toe - 2 Player Mode")

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = np.full((3, 3), "")
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False

# Function to check for winner
def check_winner(board):
    for player in ["X", "O"]:
        # Check rows, columns, diagonals
        for i in range(3):
            if all(board[i, :] == player):
                return player, [(i, j) for j in range(3)]
            if all(board[:, i] == player):
                return player, [(j, i) for j in range(3)]
        if all([board[i, i] == player for i in range(3)]):
            return player, [(i, i) for i in range(3)]
        if all([board[i, 2 - i] == player for i in range(3)]):
            return player, [(i, 2 - i) for i in range(3)]
    if "" not in board:
        return "Draw", []
    return None, []

# Game logic
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        with cols[j]:
            if st.button(st.session_state.board[i, j] or " ", key=f"{i}{j}", disabled=st.session_state.game_over):
                if st.session_state.board[i, j] == "" and not st.session_state.game_over:
                    st.session_state.board[i, j] = st.session_state.current_player
                    winner, win_cells = check_winner(st.session_state.board)
                    if winner:
                        st.session_state.winner = winner
                        st.session_state.win_cells = win_cells
                        st.session_state.game_over = True
                    else:
                        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Display status
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.success("It's a draw! 🤝")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"Player {st.session_state.current_player}'s turn")

# Show winning highlight (optional - could be enhanced with color/emoji)
if st.session_state.get("win_cells"):
    st.write("Winning combination:", st.session_state.win_cells)

# Reset game
if st.button("🔄 Restart Game"):
    st.session_state.board = np.full((3, 3), "")
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.win_cells = []
    st.session_state.game_over = False
