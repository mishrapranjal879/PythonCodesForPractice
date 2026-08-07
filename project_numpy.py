import streamlit as st
import numpy as np

# -----------------------------
# Initialize Session State
# -----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = ""


# -----------------------------
# Check Winner
# -----------------------------
def check_winner(board):

    # Check rows
    for row in board:
        if np.sum(row) == 3:
            return "X"
        elif np.sum(row) == -3:
            return "O"

    # Check columns
    for col in board.T:
        if np.sum(col) == 3:
            return "X"
        elif np.sum(col) == -3:
            return "O"

    # Main diagonal
    if np.trace(board) == 3:
        return "X"
    elif np.trace(board) == -3:
        return "O"

    # Secondary diagonal
    if np.trace(np.fliplr(board)) == 3:
        return "X"
    elif np.trace(np.fliplr(board)) == -3:
        return "O"

    # Draw
    if not (board == 0).any():
        return "DRAW"

    return None


# -----------------------------
# Make Move
# -----------------------------
def make_move(row, col):

    if st.session_state.game_over:
        return

    if st.session_state.board[row][col] != 0:
        return

    st.session_state.board[row][col] = st.session_state.current

    result = check_winner(st.session_state.board)

    if result == "DRAW":
        st.session_state.game_over = True
        st.session_state.message = "🤝 It's a Draw!"

    elif result == "X":
        st.session_state.game_over = True
        st.session_state.message = "🎉 Player X Wins!"

    elif result == "O":
        st.session_state.game_over = True
        st.session_state.message = "🎉 Player O Wins!"

    else:
        st.session_state.current *= -1


# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮")

st.title("🎮 Tic Tac Toe")

current_player = "❌ X" if st.session_state.current == 1 else "⭕ O"

if not st.session_state.game_over:
    st.subheader(f"Current Turn: {current_player}")

symbols = {
    1: "❌",
    -1: "⭕",
    0: " "
}

# Create board
for i in range(3):
    cols = st.columns(3)

    for j in range(3):
        cols[j].button(
            symbols[st.session_state.board[i][j]],
            key=f"{i}-{j}",
            use_container_width=True,
            on_click=make_move,
            args=(i, j)
        )

# Show Result
if st.session_state.message:
    st.success(st.session_state.message)

st.write("")

# Restart Button
if st.button("🔄 Restart Game"):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False
    st.session_state.message = ""
    st.rerun()