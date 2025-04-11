import streamlit as st

# Initialize session state variables
if 'board' not in st.session_state:
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
if 'player' not in st.session_state:
    st.session_state.player = 'X'
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title("🎮 Tic-Tac-Toe 2 Player Game")
st.markdown("Play with a friend! First to align 3 wins ✨")

# Check winner
def check_winner():
    board = st.session_state.board
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Display board and handle moves
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        if cols[j].button(cell_value or " ", key=f"{i}{j}", disabled=cell_value != '' or st.session_state.game_over):
            st.session_state.board[i][j] = st.session_state.player
            winner = check_winner()
            if winner:
                st.session_state.winner = winner
                st.session_state.game_over = True
            else:
                # Check for draw
                is_draw = all(all(cell != '' for cell in row) for row in st.session_state.board)
                if is_draw:
                    st.session_state.game_over = True
                else:
                    st.session_state.player = 'O' if st.session_state.player == 'X' else 'X'

# Status
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.game_over:
    st.info("🤝 It's a draw!")
else:
    st.markdown(f"**Next Turn: Player {st.session_state.player}**")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.player = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False
