# Robotics, Vision and Control - Personal Studies 🤖

Repositório dedicado ao estudo e implementação de algoritmos fundamentais de robótica, baseados no livro **"Robotics, Vision and Control: Fundamental Algorithms in Python"** de Peter Corke. O foco é o domínio de cinemática, transformações espaciais e visão computacional utilizando o ecossistema `roboticstoolbox`.

## 🚀 Diferencial Técnico: Infraestrutura como Código
Para garantir a reprodutibilidade e evitar conflitos de dependências (especialmente a incompatibilidade do **NumPy 2.0** com bibliotecas de robótica), este projeto utiliza **Docker** e **VS Code Dev Containers**. 

Isso permite que todo o ambiente de desenvolvimento — incluindo drivers de interface gráfica e bibliotecas de sistema — seja provisionado automaticamente, mantendo o sistema host "limpo".

### Stack 
* **OS:** Ubuntu 22.04 (via Docker)
* **Linguagem:** Python 3.10
* **Principais Bibliotecas:**
  * `roboticstoolbox-python`
  * `spatialmath-python`
  * `sympy` (Cálculo simbólico)
  * `numpy < 2.0` (Versão estável para compatibilidade com spatialmath)

---

## 🛠️ Como Replicar este Ambiente

Este projeto foi configurado para ser executado de forma isolada, garantindo que qualquer pessoa consiga rodar os exemplos sem configurar manualmente o Python na máquina local.

### Pré-requisitos
1. **Docker** instalado e em execução.
2. **Visual Studio Code**.
3. Extensão **[Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)** da Microsoft instalada no VS Code.

### Passo a Passo
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/lucasfroes232/robotics-vision-control-studies.git](https://github.com/lucasfroes232/robotics-vision-control-studies.git)
   cd robotics-vision-control-studies
2. **Abra no VS Code:**
    code .

3. **Inicie o Ambiente:**
   Ao abrir a pasta, o VS Code detectará a configuração. Clique no botão azul no canto inferior esquerdo e selecione:
   > **Dev Containers: Reopen in Container**

4. **Aguarde a Automação:**
   O Docker irá baixar as imagens, configurar o Ubuntu e instalar todas as dependências automaticamente.

---

## 💻 Como Executar

### Shell Interativo (RTBTool)
Para usar o terminal interativo do livro com todos os imports pré-carregados (numpy, roboticstoolbox, spatialmath), rode no terminal do VS Code:

    python3 -m roboticstoolbox.bin.rtbtool

### Scripts de Estudo
Para rodar scripts específicos na pasta `src/`:

    python3 src/capitulo2_teste.py

---

## 📂 Estrutura do Projeto
* `.devcontainer/`: Definição do ambiente Docker e extensões do VS Code.
* `src/`: Scripts Python organizados por temas do livro.
* `.gitignore`: Filtro de arquivos de sistema e cache.

---

## 👤 Autor
**Lucas Froes Belinassi** Graduando em Engenharia de Computação pela **UFSCar (São Carlos)**.  
Pesquisador no **LARIS** (Laboratory of Autonomous Robots and Intelligent Systems).  
Áreas de interesse: Path Planning, UAVs, SLAM e Robótica Móvel.

