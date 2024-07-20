#Add OpenAI library
import openai

openai.api_key = '<YOUR_API_KEY>'
openai.api_base =  '<YOUR_ENDPOINT_NAME>' 
openai.api_type = 'azure' # Necessary for using the OpenAI library with Azure OpenAI
openai.api_version = '2022-12-01' # This likely will change with future releases

deployment_name = 'hello' # SDK calls this "engine", but naming
                                           # it "deployment_name" for clarity
prompt = 'What is Azure OpenAI?'
response = openai.Completion.create(engine=deployment_name, prompt=prompt)

print(response.choices[0].text)
response = openai.ChatCompletion.create(
    engine=deployment_name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)

print(response['choices'][0]['message']['content'])