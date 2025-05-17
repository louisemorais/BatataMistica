import requests
from langchain.llms.base import LLM
from pydantic import Field
import re


class ChutesAILLM(LLM):
    token: str = Field(default="")

    def _call(self, prompt: str, stop: list[str] = None,**kwargs) -> str: #Chamada LLM
        # Verifica se o token foi fornecido
            response = requests.post(
                "https://llm.chutes.ai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Content-Type": "application/json"
                },
                json={ #Parametro da API
                    "model": "deepseek-ai/DeepSeek-R1",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                    "max_tokens": 512,
                    "temperature": 0.7
                }
            )
            if response.status_code != 200:
                return f"Erro na invocação da API: {response.text}"
            return response.json()["choices"][0]["message"]["content"]

    @property
    def _llm_type(self) -> str: # tipo do LLM
        return "chutes_ai"


def limparresposta(resposta: str) -> str: #limpar o thinking da resposta
    return re.sub(r"<think>.*?</think>", "", resposta, flags=re.DOTALL).strip()

