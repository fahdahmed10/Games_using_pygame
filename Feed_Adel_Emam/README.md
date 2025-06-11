<div align="center">

# 🍖 Feed Adel Emam

### *An Arcade-Style Catching Game*

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://pygame.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com)

*Help feed the legendary Egyptian actor Adel Emam in this fun, fast-paced catching game!*

[🎮 Play Now](#-installation) · [📖 Documentation](#-game-overview) · [🐛 Report Bug](issues) · [💡 Request Feature](issues)

---

</div>

## 📋 Table of Contents

- [🎯 Game Overview](#-game-overview)
- [✨ Features](#-features)
- [🚀 Installation](#-installation)
- [🎮 How to Play](#-how-to-play)
- [📁 Required Files](#-required-files)
- [🎵 Game Mechanics](#-game-mechanics)
- [🖼️ Screenshots](#️-screenshots)
- [🛠️ Technical Details](#️-technical-details)
- [🎭 Cultural Context](#-cultural-context)
- [🔧 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🎯 Game Overview

**Feed Adel Emam** is an arcade-style catching game built with Python and Pygame. Control the legendary Egyptian actor as he tries to catch falling meat. The game features progressive difficulty, sound effects, and a nostalgic Egyptian theme.

> *"Comedy is the food of the soul, but meat is the food of the body!"* - The Game's Philosophy

---

## ✨ Features

<table>
<tr>
<td>

### 🎪 Gameplay
- **Progressive Difficulty** - Speed increases with score
- **Lives System** - 5 lives to start with
- **Score Tracking** - Beat your high score
- **Instant Restart** - Press 'P' to play again

</td>
<td>

### 🎨 Media
- **Custom Graphics** - Egyptian-themed sprites
- **Sound Effects** - Immersive audio feedback
- **Background Music** - Continuous soundtrack
- **Smooth Animation** - 60 FPS gameplay

</td>
</tr>
</table>

---

## 🚀 Installation

### Prerequisites

Make sure you have Python 3.6+ installed on your system.

```bash
python --version
```

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/feed-adel-emam.git
   cd feed-adel-emam
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python feed_adel_emam.py
   ```

### Alternative Installation

```bash
# Install pygame directly
pip install pygame

# Download and run
python your_game_file.py
```

---

## 🎮 How to Play

<div align="center">

### Controls

| Key | Action |
|-----|--------|
| **W** | Move Up ⬆️ |
| **S** | Move Down ⬇️ |
| **P** | Restart Game 🔄 |

</div>

### Objective

1. **Catch the Meat** 🥩 - Move Adel Emam vertically to catch falling food
2. **Avoid Missing** ❌ - Don't let meat fall off the screen
3. **Score High** 🏆 - Each catch increases your score and game speed
4. **Stay Alive** ❤️ - You have 5 lives, use them wisely!

---

## 📁 Required Files

Ensure these files are in your game directory:

### 🖼️ Images
```
📁 game_directory/
├── 🖼️ adel_emam.jpeg    # Background image
├── 🖼️ g3an.jpeg         # Player character sprite
└── 🖼️ meat.jpg          # Food item sprite
```

### 🎵 Audio Files
```
📁 game_directory/
├── 🎵 main.mp3          # Background music
├── 🔊 quit.mp3          # Game over sound
├── 🔊 el72.mp3          # Miss sound effect
└── 🔊 hit.mp3           # Catch sound effect
```

> **📌 Note:** All images will be automatically resized to 50x50 pixels for sprites.

---

## 🎵 Game Mechanics

<div align="center">

### Scoring System

| Action | Points | Effect |
|--------|--------|--------|
| Catch Food 🥩 | **+1** | Speed increases by 0.5 |
| Miss Food ❌ | **-1 Life** | Play miss sound |
| Game Over 💀 | **Final Score** | Show restart option |

### Difficulty Progression

```
Initial Speed: 5 pixels/frame
Speed Increase: +0.5 per catch
Maximum Lives: 5
Game Resolution: 800x400
Frame Rate: 60 FPS
```

</div>

---

## 🖼️ Screenshots

<div align="center">

### Gameplay
```
┌─────────────────────────────────────────────────────────┐
│ Score: 15                               Lives: 3        │
│─────────────────────────────────────────────────────────│
│                                                         │
│    🧔                                            🥩 ➡️   │
│  Adel Emam         Background Image                     │
│                                                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Game Over Screen
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                   🚫 Game Overrrrrr! 🚫                 │
│                                                         │
│              Press P to feed Adel Emam again           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

</div>

---

## 🛠️ Technical Details

<div align="center">

| Specification | Value |
|---------------|-------|
| **Language** | Python 3.6+ |
| **Framework** | Pygame |
| **Resolution** | 800x400 pixels |
| **Frame Rate** | 60 FPS |
| **Movement** | Delta-time based |
| **Audio Format** | MP3, WAV |
| **Image Format** | JPEG, PNG |

</div>

### Code Structure

```python
# Main Components
├── 🎮 Game Initialization
├── 🖼️ Asset Loading (Images, Sounds, Fonts)
├── 🔄 Game Loop
│   ├── Event Handling
│   ├── Game Logic
│   ├── Collision Detection
│   └── Rendering
├── 🎵 Audio Management
└── 🔄 State Management
```

---

## 🎭 Cultural Context

This game celebrates **Adel Emam** (عادل إمام), affectionately known as "El Zaeem" (الزعيم - The Leader), one of Egypt's most beloved comedic actors. With a career spanning over five decades, Adel Emam has become an icon of Arab cinema and theater.

> The playful concept of "feeding" this legendary figure reflects the warmth and humor characteristic of Egyptian popular culture.

---

## 🔧 Troubleshooting

<details>
<summary><strong>🚨 Common Issues & Solutions</strong></summary>

### 🔴 pygame.error: No such file or directory
**Problem:** Missing image or audio files
```bash
# Solution: Verify all files exist
ls -la *.jpeg *.jpg *.mp3
```

### 🔴 ModuleNotFoundError: No module named 'pygame'
**Problem:** Pygame not installed
```bash
# Solution: Install pygame
pip install pygame
# or
pip3 install pygame
```

### 🔴 Audio not playing
**Problem:** Audio system issues
```bash
# Check audio files exist and are readable
file *.mp3
```

### 🔴 Game runs too fast/slow
**Problem:** Frame rate issues
```python
# The game uses delta-time, but you can adjust:
clock.tick(60)  # Try different values: 30, 120
```

</details>

---

## 🏆 Tips for High Scores

<div align="center">

| 💡 Strategy | 📝 Description |
|-------------|----------------|
| **🎯 Center Position** | Stay in the middle for quick reactions |
| **🔮 Predict Movement** | Anticipate where food will appear |
| **⏱️ Practice Timing** | Get comfortable with increasing speed |
| **😌 Stay Calm** | Don't panic as difficulty increases |
| **🎵 Use Audio Cues** | Listen for sound effects to improve timing |

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **💾 Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **📤 Push** to the branch (`git push origin feature/AmazingFeature`)
5. **🔀 Open** a Pull Request

### Ideas for Contributions
- 🎨 New character sprites
- 🎵 Additional sound effects
- 🏆 High score system
- 🎮 New game modes
- 🌍 Localization

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

## 🎉 Enjoy the Game!

**Made with ❤️ for the Egyptian gaming community**

[⬆️ Back to Top](#-feed-adel-emam)

---

*"الكوميديا طعام الروح، لكن اللحمة طعام الجسم!"*

</div>