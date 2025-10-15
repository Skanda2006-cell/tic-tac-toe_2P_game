import streamlit as st

# --- Functions ---

def initialize_game():
    """Initializes or resets the game state."""
    st.session_state.board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.player = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

def check_winner():
    """Checks for a winner and returns 'X', 'O', or None."""
    board = st.session_state.board
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def handle_click(i, j):
    """Handles the logic when a cell is clicked."""
    if not st.session_state.game_over and st.session_state.board[i][j] == '':
        st.session_state.board[i][j] = st.session_state.player
        winner = check_winner()
        if winner:
            st.session_state.winner = winner
            st.session_state.game_over = True
        else:
            # Check for a draw (if all cells are filled)
            if all(all(cell for cell in row) for row in st.session_state.board):
                st.session_state.game_over = True
            else:
                # Switch player
                st.session_state.player = 'O' if st.session_state.player == 'X' else 'X'

# --- App Layout and Logic ---

# Initialize session state by calling the function
if 'board' not in st.session_state:
    initialize_game()

st.title("🎮 Tic-Tac-Toe 2 Player Game")
st.markdown("Play with a friend! First to align 3 wins ✨")

# Display board and handle moves
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        # Use a non-breaking space for a consistent button height
        display_value = cell_value if cell_value else " " 
        
        cols[j].button(
            display_value, 
            key=f"cell_{i}_{j}", 
            on_click=handle_click, 
            args=(i, j),
            disabled=st.session_state.game_over,
            use_container_width=True # Makes buttons fill the column
        )

# Display status message
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.game_over:
    st.info("🤝 It's a draw!")
else:
    st.markdown(f"**Next Turn: Player {st.session_state.player}**")

# Reset button
if st.button("🔄 Restart Game"):
    initialize_game()
    st.rerun() # Immediately rerun the script to reflect the reset state
