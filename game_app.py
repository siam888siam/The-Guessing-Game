import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

st.title("🎮 Ultimate Number Guessing Game")

# গেমের রাউন্ড কনফিগারেশন
ROUNDS = {
    1: {"max": 100, "attempts": 6, "title": "Round 1: Beginner 🧠"},
    2: {"max": 1000, "attempts": 11, "title": "Round 2: Pro ☠"},
    3: {"max": 10000, "attempts": 14, "title": "Round 3: Master 😲"},
    4: {"max": 100000, "attempts": 18, "title": "Round 4: God Mode ⚡️"}
}

# সেশন স্টেট ইনিশিয়ালাইজ করা
if "round" not in st.session_state:
    st.session_state.round = 1
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, ROUNDS[st.session_state.round]["max"])
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

current_round = st.session_state.round
config = ROUNDS[current_round]

st.header(config["title"])
st.write(f"১ থেকে {config['max']}-এর মধ্যে একটি সংখ্যা অনুমান করুন। আপনার সর্বোচ্চ সুযোগ: **{config['attempts']}** বার।")

# বর্তমান অবস্থা দেখানো
st.info(f"আপনি ইতিমধ্যে **{st.session_state.attempts}** বার চেষ্টা করেছেন।")

if not st.session_state.game_over:
    user_input = st.number_input(f"আপনার সংখ্যাটি লিখুন (১ - {config['max']}):", min_value=1, max_value=config["max"], step=1, key="user_guess")
    
    if st.button("Submit Guess 🚀"):
        st.session_state.attempts += 1
        
        if user_input == st.session_state.target:
            st.balloons()
            st.success(f"🎉 অভিনন্দন! আপনি সঠিক সংখ্যা **{st.session_state.target}** অনুমান করতে পেরেছেন!")
            
            if current_round < 4:
                st.session_state.round += 1
                # নতুন রাউন্ডের জন্য রিসেট
                st.session_state.target = random.randint(1, ROUNDS[st.session_state.round]["max"])
                st.session_state.attempts = 0
                st.write("🔄 পরবর্তী রাউন্ড লোড হচ্ছে... আবার বাটনে চাপুন!")
            else:
                st.success("🏆 আপনি গেমের সবগুলো রাউন্ড জিতে গেছেন! Super genius status = MAXED OUT! 🧠📈")
                st.session_state.game_over = True
        else:
            if user_input > st.session_state.target:
                st.warning("Too high 📈! আবার চেষ্টা করুন।")
            else:
                st.warning("Too low 📉! আবার চেষ্টা করুন।")
                
            if st.session_state.attempts >= config["attempts"]:
                st.error(f"❌ আপনি হেরে গেছেন! সঠিক সংখ্যাটি ছিল: {st.session_state.target}")
                st.session_state.game_over = True

if st.button("Reset Game 🔄"):
    st.session_state.round = 1
    st.session_state.target = random.randint(1, ROUNDS[1]["max"])
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.write("গেমটি রিসেট হয়েছে।")