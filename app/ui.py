import gradio as gr
from src.inference import translate

dialects = ["bilaspuri", "mandeali", "kangri", "kulluvi"]

def run_ui(text, dialect):
    return translate(text, dialect)

demo = gr.Interface(
    fn=run_ui,
    inputs=[gr.Textbox(lines=3, placeholder="Enter Himachali dialect text..."), gr.Dropdown(dialects, value="bilaspuri")],
    outputs="text",
    title="Himachali → Hindi Translator",
    description="Translate short phrases from Himachali dialects to Hindi."
)

if __name__ == "__main__":
    demo.launch()
