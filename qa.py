import openai
openai.api_key = "OPENAI_API_KEY"
def create_prompt(context,query):
    # header = "Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry, Please reframe the question' \n "
    return context + "\n\n" + query + "\n"

def generate_answer(prompt):
    response = openai.Completion.create(
    model = "model",
    prompt=prompt,
    temperature=0,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop = ['END']
    )
    return (response.choices[0].text).strip()