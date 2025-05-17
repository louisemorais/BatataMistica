
import os
import re
import aiohttp
import asyncio
import json
import ssl

from backend.tts import speak


def limparresposta(resposta: str) -> str:
    return re.sub(r"<think>.*?</think>", "", resposta, flags=re.DOTALL).strip()

class ChutesAILLM:

    def __init__(token: str, message: str):
        x = ChutesAILLM.invoke_chute(token, message)
        asyncio.run(x)


    @staticmethod
    async def invoke_chute(token,message):
        api_token = token


        headers = {
            "Authorization": "Bearer " + api_token,
            "Content-Type": "application/json"
        }

        body = {
            "model": "deepseek-ai/DeepSeek-V3-0324",
            "messages": [
                {
                    "role": "user",
                    "content": f"{message}"
                }
            ],
            "stream": True,
            "max_tokens": 1024,
            "temperature": 0.7
        }

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        full_response = ""
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://llm.chutes.ai/v1/chat/completions",
                headers=headers,
                json=body,
                ssl=ssl_context
            ) as response:
                async for line in response.content:
                    line = line.decode("utf-8").strip()
                    if not line or not line.startswith("data: "):
                        continue
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk_json = json.loads(data)
                        # Verifica se existe a estrutura esperada
                        if (
                            "choices" in chunk_json and
                            len(chunk_json["choices"]) > 0 and
                            "delta" in chunk_json["choices"][0] and
                            "content" in chunk_json["choices"][0]["delta"]
                        ):
                            full_response += chunk_json["choices"][0]["delta"]["content"]
                    except Exception as e:                        continue
        print(limparresposta(full_response))
        speak(limparresposta(full_response))

