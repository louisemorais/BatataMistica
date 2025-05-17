import ast
from langchain.prompts import PromptTemplate

prompt_erro = PromptTemplate(
            input_variables=["erro"],
            template=(
                "diga primeiro esta frase: Batata viu trevas em seu código! Cuidado... algo não parece está certo.\n\n "
                "Batata mística detectou um erro:\n{erro}\n\n"
                "Agora fale de forma sarcástica, agressiva e mística explicando por que esse código está mais bugado que um feitiço mal lançado. Não seja gentil. Solte o verbo! Responda sempre em português brasileiro e sem cortar as frases no meio"
                "Responda como um oráculo sombrio, mas sem emojis e sem nenhuma marcação de formatação (como ** ou _). Use apenas texto cru e sombrio."
            ))

#recebe como argumento uma string codigo contendo código-fonte Python e retorna uma string com a análise.
def analisar_codigo(codigo: str) -> str:
    try:
        tree = ast.parse(codigo) ## transforma o código em árvore binária, ele quebra o texto em partes menores e organiza em uma estrutura em árvore sintática.
    except Exception as e:
            print("Batata viu trevas em seu código! Cuidado! algo não parece está certo...")
            return prompt_erro.format(erro=f"{type(e)._name_}: {e}") # se não funcionar retorna erro

    funcoes = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]#percorre todos os nós da arvore, filtra os nós que representam as definições de funções e extrai o nome da função.
    loops = len([n for n in ast.walk(tree) if isinstance(n, (ast.For, ast.While))])#Conta quantos nós são for e quantos nós são while 
    condicoes = len([n for n in ast.walk(tree) if isinstance(n, ast.If)])#Conta quantos if existem no código.


#retorna o resultado formatado com nomes das funções encontradas, quantidades de loops e quantidades de condicionais.
    return (
        f" Análise do código:\n"
        f"• Funções encontradas: {', '.join(funcoes) if funcoes else 'nenhuma'}\n"
        f"• Loops: {loops}\n"
        f"• Condicionais: {condicoes}")

