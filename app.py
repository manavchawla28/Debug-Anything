import openai
import gradio as gr

openai_api_key = "ADD OPEN AI API KEY HERE"

def run(input1, input2):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{input1}"},
            {"role": "user", "content": f"{input2}"}
        ],
        max_tokens=1839,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    answer = response['choices'][0]['message']['content']
    return answer

examples=[["Please help fix my code (which can be found at the end of this prompt marked \\CODE\\ I received the following error : ", "Please correct my code"],]
demo = gr.Interface(
    fn=run,
    inputs=[gr.Textbox(lines=4, placeholder="Cut and paste input 1 here", label="input 1"), gr.Textbox(lines=4, placeholder="Cut and paste input 2 here", label="input 2")],
    outputs="text",
    title="Code Debugger",
    description="Use this application to debug your code",
    examples=examples,
    allow_flagging=False,  
)
demo.launch()
