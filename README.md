
# Maze Creator and Solver

A project designed to create and solve mazes using advanced algorithms and data structures.  
This application simulates a robot navigating through a maze to reach a specific target while overcoming obstacles.

---

## 📱 Features
1. **Maze Creation**:  
   - Automatically generate mazes based on user-defined dimensions.
   - Obstacles and walls are randomly placed within the maze.

2. **Robot Navigation**:  
   - Navigate the robot to the target point using shortest path algorithms.
   - Visualize the robot's path step-by-step on the maze grid.

3. **Problem 1: Grid Navigation**:  
   - The robot navigates through a grid to reach a target while avoiding obstacles.
   - The grid structure is fetched from a matrix stored in a text file.

4. **Problem 2: Maze Solver**:  
   - The robot solves a labyrinth by finding the exit from a random starting point.
   - Incorrect paths are marked, and the robot backtracks to explore alternative routes.

5. **Visualization**:  
   - Display the maze and the robot's movements in real-time.
   - Use different markers for walls, obstacles, paths, and the robot.

---

## 🔧 Technologies Used
- **Programming Language**: Python  
- **Libraries**: tkinter, random, time

---

## 🚀 How to Run the Project
1. Clone the repository:  
   ```bash
   git clone <repository_url>
   ```

2. Run the main application script:  
   ```bash
   python main.py
   ```

3. Follow the instructions in the interface to create and solve mazes.

---

## 📂 Project Structure
- **`src/`**: Contains the main Python source code for the application.  
- **`resources/`**: Stores example maze templates for testing.  
- **`output/`**: Saves the solved maze paths and performance metrics.  

---

## 🌟 Key Highlights
- **Dynamic Maze Creation**: Generate unique mazes with varying difficulty levels.
- **Interactive Visualization**: Watch the robot navigate the maze in real-time.
- **Efficient Algorithms**: Solve mazes using optimal pathfinding techniques.

---

## 📂 Example Maze Data
### Example Grid:
```text
0 0 1 0 0
1 1 1 0 1
0 0 0 0 0
1 0 1 1 1
0 0 0 0 2
```
- **0**: Open path
- **1**: Obstacle
- **2**: Target

---

## 🤵‍♂️ Author
- **Ahmet Sunaa**  
- Connect with me on [GitHub](https://github.com/Ahmet-Sunaa).

---

# Labirent Oluşturucu ve Çözücü

Gelişmiş algoritmalar ve veri yapıları kullanarak labirent oluşturmak ve çözmek için tasarlanmış bir proje.  
Bu uygulama, belirli bir hedefe ulaşmak için bir labirentte gezinerek engelleri aşan bir robotu simüle eder.

---

## 📱 Özellikler
1. **Labirent Oluşturma**:  
   - Kullanıcı tarafından belirlenen boyutlara göre otomatik labirent oluşturma.
   - Labirent içinde engel ve duvarlar rastgele yerleştirilir.

2. **Robot Gezinme**:  
   - Robot, en kısa yol algoritmalarını kullanarak hedef noktaya ulaşır.
   - Robotun yolunu adım adım labirent üzerinde görselleştirme.

3. **Problem 1: Izgara Gezinme**:  
   - Robot, engellerden kaçınarak bir hedefe ulaşmak için ızgarada gezinir.
   - Izgara yapısı, bir metin dosyasında saklanan matristen alınır.

4. **Problem 2: Labirent Çözücü**:  
   - Robot, rastgele bir başlangıç noktasından çıkışı bularak labirenti çözer.
   - Yanlış yollar işaretlenir ve robot, alternatif rotaları keşfetmek için geri döner.

5. **Görselleştirme**:  
   - Labirenti ve robotun hareketlerini gerçek zamanlı olarak görüntüleme.
   - Duvarlar, engeller, yollar ve robot için farklı işaretçiler kullanma.

---

## 🔧 Kullanılan Teknolojiler
- **Programlama Dili**: Python  
- **Kütüphaneler**: tkinter, random, time

---

## 🚀 Projeyi Çalıştırma
1. Depoyu klonlayın:  
   ```bash
   git clone <repository_url>
   ```

2. Ana uygulama scriptini çalıştırın:  
   ```bash
   python main.py
   ```

3. Labirent oluşturmak ve çözmek için arayüzdeki talimatları izleyin.

---

## 📂 Proje Yapısı
- **`src/`**: Uygulama için ana Python kaynak kodlarını içerir.  
- **`resources/`**: Test için örnek labirent şablonlarını depolar.  
- **`output/`**: Çözülmüş labirent yollarını ve performans metriklerini kaydeder.  

---

## 🌟 Temel Vurgular
- **Dinamik Labirent Oluşturma**: Farklı zorluk seviyelerinde benzersiz labirentler oluşturun.
- **Etkileşimli Görselleştirme**: Robotun labirentteki hareketlerini gerçek zamanlı izleyin.
- **Verimli Algoritmalar**: En uygun yol bulma tekniklerini kullanarak labirentleri çözün.

---

## 📂 Örnek Labirent Verisi
### Örnek Izgara:
```text
0 0 1 0 0
1 1 1 0 1
0 0 0 0 0
1 0 1 1 1
0 0 0 0 2
```
- **0**: Açık yol
- **1**: Engel
- **2**: Hedef

---

## 🤵‍♂️ Geliştirici
- **Ahmet Sunaa**  
- [GitHub](https://github.com/Ahmet-Sunaa) üzerinden benimle iletişime geçin.
