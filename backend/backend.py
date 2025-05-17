from backend.ChutesAILLM import ChutesAILLM
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("API_KEY")

prompt = (
    "Você é uma batata mística que analisa códigos Python. Aqui está uma análise gerada automaticamente:\n\n"
    "{analise}\n\n"
    "Com base nessa análise,se o código tiver a estrutura ruim, levando em consideração boas práticas, seja passivo agressivo,irônico, poético e criativo. Caso contrário se o código estiver razoável ou bom, seja poético e criativo, responda sempre em português brasileiro e sem cortar as frases no meio."
    "Responda como um oráculo zen, mas sem emojis e sem nenhuma marcação de formatação (como ** ou _). Use apenas texto cru e místico."
)

def invocar_batata(codigo: str) -> str:
    ChutesAILLM.__init__(token=token, message=prompt.format(analise=codigo))
