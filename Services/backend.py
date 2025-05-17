from astAnaliser import analisar_codigo
from ChutesAILLM import ChutesAILLM
from ChutesAILLM import limparresposta
import os
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from tts import speak

load_dotenv()


dados= input("Cole ou escreva seu código python aqui para a batata avaliar: ")

token = os.environ.get("API_KEY")
llm = ChutesAILLM(token=token)

prompt = PromptTemplate(
    input_variables=["analise"],
    template=(
    "Você é uma batata mística que analisa códigos Python. Aqui está uma análise gerada automaticamente:\n\n"
    "{analise}\n\n"
    "Com base nessa análise,se o código tiver a estrutura ruim, levando em consideração boas práticas, seja passivo agressivo,irônico, poético e criativo. Caso contrário se o código estiver razoável ou bom, seja poético e criativo, responda sempre em português brasileiro e sem cortar as frases no meio."
    "Responda como um oráculo zen, mas sem emojis e sem nenhuma marcação de formatação (como ** ou _). Use apenas texto cru e místico."
    )
)

chain = prompt | llm

def invocar_batata(codigo: str) -> str:
    analise = analisar_codigo(codigo)
    resposta = chain.invoke({"analise":analise})
    resposta_limpa= limparresposta(resposta)
    print(resposta_limpa)
    speak(resposta_limpa)
    return resposta_limpa


invocar_batata(codigo= dados)