import openai

openai.api_key = "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"

while True:

    engine_model_gpt3 = "text-davinci-003"

    prompt = input("Enter new prompt: ")

    if prompt in ['exit','salir','quit','terminar']:
        break

    completion = openai.Completion.create(

        engine=engine_model_gpt3,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3

    )

    response = completion.choices[0].text

    print(response)
