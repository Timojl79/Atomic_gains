import streamlit as st
import random

# Page config
st.set_page_config(page_title="Atomic Gains", page_icon="💪")

# Title
st.title("💥 Atomic Gains")
st.subheader("The Smallest Fitness Tracker in the Universe")

st.write("Input your microscopic workout effort and receive a scientifically ridiculous analysis in atoms.")

# Keyword mapping
keyword_actions = {
    "breath": ("fat burned", (2000, 5000)),
    "blink": ("eye stamina", (1000, 2500)),
    "lift": ("lean mass (bicep)", (1000, 3000)),
    "squat": ("glute activation", (9000, 12000)),
    "walk": ("step atoms", (5000, 15000)),
    "run": ("cardio stamina", (8000, 20000)),
    "sit": ("core micro-vibrations", (300, 900)),
    "jump": ("vertical atoms", (7000, 11000)),
    "stretch": ("flexibility atoms", (1500, 4000)),
    "fridge": ("lazy stride atoms", (10000, 16000)),
}

def get_rank(total_atoms):
    if total_atoms >= 50000:
        return "🔌 Subatomic Beast"
    elif total_atoms >= 10000:
        return "🌋 Molecule Mover"
    else:
        return "💫 Nano Newbie"

random_facts = [
    "Did you know? One sneeze is worth 12,000 lung stamina atoms.",
    "Blinking rapidly can charge your eye stamina to 2,500 atoms.",
    "Thinking about exercise burns 3,000 theoretical atoms.",
    "Eating protein boosts your muscle memory atoms by 5,000.",
    "Yawning is a stealth way to activate jawline atoms."
]

def get_default_response():
    return random.choice([
        "Your movement has awakened 4,200 atoms of power.",
        "You’ve expended 3,000 atoms just thinking about fitness. Mental gains.",
        "Detected 6,500 atoms of existential dread… just kidding, it's gains!",
        "Your cells cheered. You gained 2,800 inspiration atoms.",
        "Unreal commitment. You activated 9,999 heroic atoms."
    ])

if "total_atoms" not in st.session_state:
    st.session_state.total_atoms = 0

if "logs" not in st.session_state:
    st.session_state.logs = []

# Input
user_input = st.text_input("💬 What did you do?", "")

if st.button("💣 Calculate Atom Impact") or user_input:
    user_input_lower = user_input.lower()
    result_given = False
    atoms = 0
    label = ""

    # Easter eggs
    if "universe" in user_input_lower:
        atoms = 1000000
        label = "cosmic domination"
        st.error("🔥 BLACK HOLE ACTIVATED: You have absorbed 1,000,000 atoms. Universe bends to your will.")
        result_given = True
    else:
        for keyword in keyword_actions:
            if keyword in user_input_lower:
                label, (low, high) = keyword_actions[keyword]
                atoms = random.randint(low, high)
                st.success(f"You've gained **{atoms} atoms of {label}**. Your ancestors are proud.")
                result_given = True
                break

    if not result_given and user_input.strip() != "":
        response = get_default_response()
        st.info(response)
        atoms = random.randint(1000, 3000)
        label = "undefined action"

    if user_input.strip():
        st.session_state.total_atoms += atoms
        st.session_state.logs.append((user_input, label, atoms))
        st.balloons()
        st.caption(random.choice(random_facts))

# Show totals and rank
st.divider()
st.header("🔢 Your Atomic Totals")
st.metric(label="Total Atoms Earned", value=f"{st.session_state.total_atoms:,}")
st.write(f"Rank: **{get_rank(st.session_state.total_atoms)}**")

# Show action log
if st.session_state.logs:
    st.subheader("🔗 Action Log")
    for log in reversed(st.session_state.logs[-10:]):
        st.write(f"**{log[0]}** → {log[2]} atoms of {log[1]}")

st.caption("Note: Atoms are imaginary. Gains are eternal. 💫")
