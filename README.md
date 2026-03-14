# Robotics, Vision and Control - Personal Studies 🤖

Repository dedicated to the study and implementation of fundamental robotics algorithms, based on the book **"Robotics, Vision and Control: Fundamental Algorithms in Python"** by Peter Corke. The focus is on mastering kinematics, spatial transformations, and computer vision using the `roboticstoolbox` ecosystem.

## 🚀 Technical Highlight: Infrastructure as Code
To ensure reproducibility and avoid dependency conflicts (especially the incompatibility of **NumPy 2.0** with robotics libraries), this project uses **Docker** and **VS Code Dev Containers**.

This allows the entire development environment — including graphical interface drivers and system libraries — to be automatically provisioned, keeping the host system "clean".

### Stack
* **OS:** Ubuntu 22.04 (via Docker)  
* **Language:** Python 3.10  
* **Main Libraries:**
  * `roboticstoolbox-python`
  * `spatialmath-python`
  * `sympy` (Symbolic computation)
  * `numpy < 2.0` (Stable version for compatibility with spatialmath)

---

## 🛠️ How to Replicate This Environment

This project was configured to run in an isolated environment, ensuring that anyone can execute the examples without manually configuring Python on their local machine.

### Prerequisites
1. **Docker** installed and running.
2. **Visual Studio Code**.
3. The **Dev Containers** extension installed in VS Code.

### Step by Step
1. **Clone the repository:**
   ```bash
   git clone https://github.com/lucasfroes232/robotics-vision-control-studies.git
   cd robotics-vision-control-studies
```

2. **Open in VS Code:**

```bash
code .
```

3. **Start the Environment:**
   When opening the folder, VS Code will detect the configuration. Click the blue button in the lower-left corner and select:

> **Dev Containers: Reopen in Container**

4. **Wait for the Automation:**
   Docker will download the images, configure Ubuntu, and install all dependencies automatically.

---

## 💻 How to Run

### Interactive Shell (RTBTool)

To use the interactive terminal from the book with all imports preloaded (`numpy`, `roboticstoolbox`, `spatialmath`), run in the VS Code terminal:

```bash
python3 -m roboticstoolbox.bin.rtbtool
```

### Study Scripts

To run specific scripts in the `src/` folder:

```bash
python3 src/capitulo2/teste.py
```

---

## 📂 Project Structure

* `.devcontainer/`: Definition of the Docker environment and VS Code extensions.
* `src/`: Python scripts organized by book topics.
* `.gitignore`: Filter for system and cache files.

---

## 👤 Author

**Lucas Froes Belinassi**  
Undergraduate student in Computer Engineering at **UFSCar (São Carlos)**.  
Researcher at **LARIS (Laboratory of Autonomous Robots and Intelligent Systems)**.  
Research interests: Path Planning, UAVs, SLAM, and Mobile Robotics.