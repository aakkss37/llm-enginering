import gradio as gr
from dotenv import load_dotenv

load_dotenv(override=True)

def respond(message, history):
    # Simple echo response for demonstration
    # You can replace this with actual chatbot logic (e.g., LLM integration)
    response = f"**Echo:** {message}"
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})
    return "", history
    

if __name__ == "__main__":
    
    with gr.Blocks() as demo:
        gr.Markdown("# Business Analyst")
        
        chatbot = gr.Chatbot(
            render_markdown=True,
            show_label=False,
            height=600
        )
        
        with gr.Row():
            msg = gr.Textbox(
                placeholder="Type your message here...",
                show_label=False,
                scale=6
            )
            submit_btn = gr.Button("Send", scale=1)
        
        clear_btn = gr.Button("Clear Chat")
        
        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        submit_btn.click(respond, [msg, chatbot], [msg, chatbot])
        clear_btn.click(lambda: [], None, chatbot, queue=False)
    
    demo.launch(theme=gr.themes.Soft(), inbrowser=True)