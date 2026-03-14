import roboticstoolbox as rtb

print("🤖 Carregando o modelo cinemático do Puma 560...")
puma = rtb.models.DH.Puma560()

print("🖥️ Solicitando abertura da interface gráfica ao X11...")
# O parâmetro 'block=True' é essencial para o script não terminar e fechar a janela na mesma hora
puma.plot(puma.qz, block=True)

print("✅ Janela fechada. Teste finalizado com sucesso!")