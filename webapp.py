
import streamlit as st
from matplotlib import pyplot

import words_arithmetic
from words_arithmetic import embedders

pyplot.style.use('dark_background')

# Cached methods
@st.cache(allow_output_mutation=True)
def load_embedder(embedder_name, pretrained):
    # Mutate bar
    return embedders.GensimEmbedder(embedder_name, pretrained)

def default_operand(i):
    if i==0 : return "-"
    elif i==1 : return "+"
    else: return "+"

def default_word(i):
    if i==0 : return "Man"
    elif i==1 : return "Woman"
    else: return ""

# Page properties
st.set_page_config(
    page_title="Words arithmetic",
    page_icon=":ocean:",
    layout="centered",
    initial_sidebar_state="auto",
)

#navigation_page = st.sidebar.radio("Navigate to", [PAGE_PREDICTIONS, PAGE_PERFORMANCE])
available_models = embedders.GensimEmbedder.available_models()
engine = st.sidebar.selectbox('Select an engine', ["Gensim"])
model = st.sidebar.selectbox('Select a model', available_models)

st.sidebar.markdown(
f"""
**How does it work ?**

Word embedding is a technique used in natural language processing (NLP) tasks to convert unstructured text data to numerical vectors. 
Once words are turned into vectors, one can easily sum or substract them.
"""
)
st.sidebar.markdown(
f"""
*Made by [pauldes](https://github.com/pauldes). Code on [GitHub](https://github.com/pauldes/words-arithmetic).*
"""
)

st.title("🌊 Words arithmetic")
st.markdown(
f"""
*Performing arithmetic on words using word embeddings.*
"""
)
embedder = load_embedder("basic embedder", model)
col1, col2 = st.beta_columns([1, 3])
num_words = col1.number_input("Number of words", min_value=1, max_value=9, value=2, step=1, format="%i")
base_word = col2.text_input('Base word', "King")
sequence = [("+", base_word)]
embedder.flush()
for i in range(num_words):
    operand = default_operand(i)
    word = default_word(i)
    sequence.append(("operand-placeholder", "word-placeholder"))
    sequence[i+1] = (col1.radio(f'Operand n°{i}', ["+", "-"], 0 if operand=="+" else 1), col2.text_input(f'Word n°{i}', word))

for (operand, word) in sequence:
    clean_word = word
    if operand == "+":
        embedder.add(clean_word)
    elif operand == "-":
        embedder.sub(clean_word)
    else:
        raise ValueError(f"Unsupported operand {operand}")

st.subheader("Results")
res = embedder.res()
first_res_word = list(res.keys())[0]
equation = "".join(f"{operand} {word} " if i>0 else f"{word} " for i,  (operand, word) in enumerate(sequence)) + f"= **{first_res_word}**"
st.info(equation)

widths = list(res.values())
labels = list(res.keys())

fig, ax = pyplot.subplots()
pyplot.barh(y=range(len(widths), 0, -1), width=widths, height=0.8, tick_label=labels, color="#34B7EB")
ax.autoscale()
ax.set_xlim(max([min(widths)-0.05, 0.0]), min([max(widths)+0.05, 1.0]))
st.pyplot(fig, transparent=True)
