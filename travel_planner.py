import streamlit as st
import openai
from helper.trip_planner_assistant import trip_start_message, prompt_trip

# Set the OpenAI API key
openai.api_key = st.secrets["openai_key"]


# Define the function to call GPT-3.5-turbo API
def ask_gpt3_turbo(start_message, prompt):
    start_message.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        max_tokens=4010,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=start_message,
    )
    return response.choices[0].message.content


def ask_gpt3_turbo_stream(start_message, prompt):
    start_message.append({"role": "user", "content": prompt})
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        temperature=0.5,
        max_tokens=12000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=start_message,
        stream=True,
    )
    return completion


def main():
    st.title("AI Travel Planner")

    destination = st.text_input("Tempat Tujuan")
    start_date = st.date_input("Tanggal Mulai Perjalanan")
    end_date = st.date_input("Tanggal Akhir Perjalanan")
    preference = st.multiselect(
        "Preferensi Tujuan",
        [
            "Alam",
            "Arsitektur",
            "Sejarah dan Budaya",
            "Halal",
            "Kuliner",
            "Local Event",
            "Workshop",
        ],
    )
    preference = ", ".join(preference)
    button = st.button("Kirim")

    if button:
        chunks = ""
        res_box = st.empty()
        completion = ask_gpt3_turbo_stream(
            trip_start_message,
            prompt_trip.format(destination, start_date, end_date, preference),
        )
        for chunk in completion:
            if chunk.choices[0].finish_reason is None:
                chunks = chunks + chunk.choices[0].delta.content
                res_box.markdown(body=chunks, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
