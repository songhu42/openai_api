import openai
import config
openai.api_key = config.API_KEY

question = input("대한민국에서 가장 큰 섬은 어디이며, 면적은?")

# temperature : 창의성 지수 높아진다. 
# response = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=1024, n=1, stop=None, temperature=0.8)

# ChatGPT-4 모델을 사용한 대화 생성
# model_name = "gpt-4o-mini"
model_name = "gpt-4o"

client = openai.OpenAI(
    api_key=openai.api_key
)

response = client.chat.completions.create( 
  model=model_name,  
  messages=[
      {"role": "system", "content": "너는 정확한 도우미 역할을 해. 한국어로 대답해줘."},  # 시스템 역할 (모델의 행동 정의)
      {"role": "user", "content": "대한민국에서 가장 큰 섬은 어디이며, 면적은?"}  # 사용자 메시지
  ], 
  temperature=0.9,
  top_p=1.0,
  max_tokens=1000
)

# 모델의 응답 출력
# print(response)
print(response.choices[0].message.content)
