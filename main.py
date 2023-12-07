import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="YOUBET", page_icon=":burrito:", layout="wide")

st.title("YouBet")

st.header("Introduction")
st.markdown("YouBet, our La Liga predictor, is built on a robust foundation of extensive match statistics meticulously collected and ingeniously engineered. In order to provide accurate and insightful predictions, we have leveraged cutting-edge techniques to gather data spanning the last seven seasons.")

gif_url = "https://www.gifcen.com/wp-content/uploads/2022/12/messi-gif-23.gif"

# Display the GIF
st.image(gif_url, use_column_width=True)

st.header("Data Scraping")
st.markdown("We have implemented a sophisticated scraping mechanism that retrieves diverse match statistics from various sources, ensuring a comprehensive dataset for analysis. This includes information on goals, offensive and defensive actions, and in-game dynamics.")

st.header("Feature Engineering")
st.subheader('Goal Offense and Goal Defense')
st.markdown("One of the key features of YouBet is our innovative goal offense and goal defense metrics. We calculate a weighted average of the last 3, 5, and 10 matches to derive the offensive and defensive prowess of each team. This allows us to capture the recent performance trends and fine-tune our predictions.")

st.subheader('Offense and Defense Ratings')
st.markdown("To evaluate the offensive and defensive capabilities of teams, we have introduced metrics that encompass a broad spectrum of actions, including shots, corners, clearances, blocks, interceptions, and more. These metrics are then normalized to a scale of 10, providing a standardized measure for comparison.")

st.subheader('In-Game Score')
st.markdown("Understanding the dynamics of a match is crucial for accurate predictions. Our in-game score metric takes into account various in-game actions such as passes, fouls, cards, and more, providing a comprehensive snapshot of each team's performance during a match.")

st.subheader('Win, Draw, and Loss Streaks')
st.markdown("In tandem with comprehensive match statistics, YouBet incorporates win, draw, and loss streaks into its predictive model. These streaks offer valuable insights into the recent performance trajectory of each team. By analyzing historical streaks, YouBet captures the momentum and form of teams leading up to a match.")

st.subheader('Team Position in the League')
st.markdown("Understanding the context of each match involves considering the league standings of the participating teams. YouBet meticulously incorporates the position of each team in the league before a match into its predictions. This contextual information adds depth to the analysis, allowing YouBet to account for the relative strengths and weaknesses of teams based on their standings.")

st.subheader('Betting Odds Analysis')
st.markdown("In addition to in-depth match statistics, team dynamics, win streaks, draw streaks, and loss streaks, YouBet incorporates betting odds analysis into its predictive framework. By considering the odds set by bookmakers before each match, YouBet gains valuable insights into market expectations and sentiments.")
st.markdown("This integration allows YouBet to factor in external perceptions of team strengths and potential outcomes. By analyzing betting odds, YouBet provides a holistic view for more accurate predictions, taking into account not only the on-field performance but also external assessments of team capabilities.")


st.subheader("Push cabron")

# st.balloons()

st.code("for i in range(5):\nprint(i)")

with st.sidebar:
    selection = st.radio("select one", ["a", 2])

if selection == 1:
    st.write("1")
else:
    st.write("3")

import random

def generate_random_color():
    """Generate a random color in RGB format."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def display_color(color):
    """Display the color and its RGB values."""
    st.subheader('Random Color')
    st.markdown(f"RGB: {color[0]}, {color[1]}, {color[2]}")
    st.write(f"Color: #{color[0]:02X}{color[1]:02X}{color[2]:02X}", unsafe_allow_html=True)
    st.write(
        f'<div style="width: 100px; height: 100px; background-color: rgb({color[0]}, {color[1]}, {color[2]})"></div>',
        unsafe_allow_html=True
    )

# Streamlit app code
st.title('Random Color Generator')
button_clicked = st.button('Generate Random Color')

if button_clicked:
    random_color = generate_random_color()
    display_color(random_color)

st.multiselect("Buy", ["milk", "apples", "potatoes"])

col1, col2 = st.columns(2)
col1.write("Hi my name is column 1")
col2.write("hello")

tab1, tabs = st.tabs(["Tab1", "hellow"])

with tab1:
    st.image("images/Audi.jpg")

select=st.radio("whats you favourite car?", options=["Audi", "BMW", "Ferrari"])

if select == "Audi":
    st.image("images/Audi.jpg")

x = st.text_input("Enter text: ")
print(x)

y = st.date_input("Enter date: ")
print(y)

df = {"a":[1, 2], "b":[2, 3]}
st.table(df)
