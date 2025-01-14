from openai import OpenAI

client = OpenAI(
    api_key='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'
)

def get_car_ai_bio(model, brand, year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas, características, e o que torna esse carro único.
    '''

    message = message.format(brand, model, year)

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": message}
        ],
        max_tokens=1000,
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content