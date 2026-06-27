# import random

# num = random.randint(1,100)

# tries = 0

# while True:
#     guessed =int(input("guess the number between 1 - 100"))

#     if guessed == num:
#         print(f"congratulation you found your number in {tries} tries")

#         break
  
#     elif guessed > num:
#         print("sorry you need to go lower")
    
#     elif guessed < num:
#         print("sorry you have to go little upper")

# design a game stone paper and scissors----

import streamlit as st
import random

st.set_page_config(
    page_title="Stone Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Initialize session state
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "message" not in st.session_state:
    st.session_state.message = "Choose your move!"

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""

choices = {
    "Stone": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

def play(player):
    computer = random.choice(list(choices.keys()))
    st.session_state.computer_choice = computer

    if player == computer:
        st.session_state.message = "🤝 It's a Draw!"

    elif (
        (player == "Stone" and computer == "Scissors") or
        (player == "Paper" and computer == "Stone") or
        (player == "Scissors" and computer == "Paper")
    ):
        st.session_state.player_score += 1
        st.session_state.message = "🎉 You Won This Round!"

    else:
        st.session_state.computer_score += 1
        st.session_state.message = "💻 Computer Won This Round!"

    if st.session_state.player_score == 5:
        st.success("🏆 Congratulations! You Won the Game!")
        st.balloons()
        reset()

    elif st.session_state.computer_score == 5:
        st.error("😢 Computer Won the Game!")
        reset()


def reset():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0


# ---------------- UI ---------------- #

st.title("🎮 Stone Paper Scissors")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric("🙋 You", st.session_state.player_score)

with col2:
    st.metric("💻 Computer", st.session_state.computer_score)

st.subheader("Choose Your Move")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🪨 Stone", use_container_width=True):
        play("Stone")

with c2:
    if st.button("📄 Paper", use_container_width=True):
        play("Paper")

with c3:
    if st.button("✂️ Scissors", use_container_width=True):
        play("Scissors")

st.markdown("---")

if st.session_state.computer_choice:
    st.info(
        f"💻 Computer chose: {choices[st.session_state.computer_choice]} "
        f"{st.session_state.computer_choice}"
    )

st.subheader(st.session_state.message)

st.markdown("---")

if st.button("🔄 Reset Game", use_container_width=True):
    reset()
    st.session_state.message = "Choose your move!"
    st.session_state.computer_choice = ""
    st.rerun()









