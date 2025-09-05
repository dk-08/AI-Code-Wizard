import gradio as gr
from gemini_helper import generate_code, run_code
def handle_prompt(prompt):
    code = generate_code(prompt)
    return code, ""  
def execute_code(code):
    result = run_code(code)
    return result

with gr.Blocks(title="AI Code Wizard", css="#output-box {font-family: monospace; white-space: pre-wrap; color: black;}") as demo:
    gr.Markdown("## AI Code Wizard\nGenerate & run Python code instantly")
    with gr.Row():
        with gr.Column(scale=1):
            prompt = gr.Textbox(
                label="Prompt",
                placeholder="e.g., write a code for bubble sort",
                lines=2,
            )
            generate_btn = gr.Button("Generate Code", variant="primary")
        with gr.Column(scale=2):
            code_box = gr.Code(
                label="Generated Code (editable)",
                language="python",
                interactive=True,
                lines=20,
            )
        with gr.Column(scale=1):
            output_box = gr.Textbox(
                label="Execution Result",
                interactive=False,
                lines=20,
                elem_id="output-box"
            )
            run_btn = gr.Button("▶ Run Code", variant="secondary")

    generate_btn.click(handle_prompt, inputs=prompt, outputs=[code_box, output_box])
    run_btn.click(execute_code, inputs=code_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch()
