import asyncio
import time

async def chamada_rede(tempo):
  """Simula uma chamada de rede com um tempo de espera especificado."""
  await asyncio.sleep(tempo)
  return f"Resposta da rede após {tempo} segundos"

async def executar_chamadas_rede():
  """Executa três chamadas de rede de forma assíncrona e mede o tempo total."""
  inicio = time.time()

  # Executa as chamadas de rede simultaneamente
  tarefas = [
      chamada_rede(2),  # Simula uma chamada de rede que leva 2 segundos
      chamada_rede(1),  # Simula uma chamada de rede que leva 1 segundo
      chamada_rede(3),  # Simula uma chamada de rede que leva 3 segundos
  ]
  resultados = await asyncio.gather(*tarefas)

  fim = time.time()
  tempo_total = fim - inicio

  print("Resultados das chamadas de rede:")
  for resultado in resultados:
    print(resultado)

  print(f"Tempo total de execução: {tempo_total:.4f} segundos")
  return tempo_total

# Executa a função assíncrona
asyncio.run(executar_chamadas_rede())