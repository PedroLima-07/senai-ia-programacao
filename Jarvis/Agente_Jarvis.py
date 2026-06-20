import pyautogui
import time

from agno.agent import Agent
from agno.models.openai import OpenAIChat

API_KEY = "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"

# CRIAR UM ELEMENTO DE SEGURANÇA
pyautogui.PAUSE = 0.5

def clicar(x:int, y:int) -> str:
    pyautogui.click(x, y)
    return f"Clique realizado nas coordenadas ({x}, {y})"

def escrever(texto:str) -> str:
    pyautogui.write(texto,interval=0.05)
    return f"Escrevi: '{texto}' "

def abrir_camera() -> str:
    pyautogui.press('win')
    time.sleep(0.5)
    
    pyautogui.write('Câmera')
    time.sleep(0.5)
    
    pyautogui.press('enter')
    time.sleep(1.5)
    
    return "Câmera aberta"

def tirarfoto() -> str:
    pyautogui.press('space')
    time.sleep(2)
    
    return "Foto tirada"

def abrir_bloco_de_notas() -> str:
    pyautogui.press('win')
    time.sleep(1)
    
    pyautogui.write('Bloco de notas')
    time.sleep(1)
    
    pyautogui.press('enter')
    time.sleep(2)
    
    return "Bloco de notas aberto"


def printar_tela() -> str:
    screenshot = pyautogui.screenshot()
    screenshot.save("Print_do Jarvis.png")
    return "Screenshot tirada e salva como 'Print_do Jarvis.png'"

jarvis = Agent(
    model=OpenAIChat(
        id="meta/llama-3.1-8b-instruct",
        api_key=API_KEY,
        base_url="https://integrate.api.nvidia.com/v1"
    ),
    instructions= """
    Você é um assistente virtual estilo jarvis,
    Você controla o computador usando ferramentas,
    Seja objetivo e execute ações com segurança.
    """,
    tools=[
        clicar,
        escrever,
        abrir_bloco_de_notas,
        printar_tela,
        abrir_camera,
        tirarfoto
    ],
    markdown=True
)

jarvis.print_response(
    """
    Abra o Bloco de Notas, escreva:
    'Ola, eu sou o Jarvis, seu assistente virtual!' 
    e depois tire um print da tela.
    Abra a camera do windows e tire uma foto. 
    """,
    stream =True
    
)