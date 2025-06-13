# 🏓 Ping Pong 2 Players

A classic two-player ping pong game built with Python and Pygame. Challenge your friends in this fast-paced arcade-style game!

## ✨ Features

- **Two-player local multiplayer** - Play with a friend on the same keyboard
- **Dynamic ball physics** - Realistic ball movement with random velocity variations
- **Score tracking** - First to 5 points wins
- **Game over screen** - Winner announcement with restart functionality
- **Smooth controls** - Responsive paddle movement
- **Clean retro design** - Minimalist white-on-black aesthetic

## 🎮 Controls

### Player 1 (Left Paddle)
- **W** - Move up
- **S** - Move down

### Player 2 (Right Paddle)
- **↑** - Move up
- **↓** - Move down

### Game Controls
- **Enter** - Restart game after game over
- **X** - Close game window

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Pygame library

### Setup
1. **Clone or download** the game file
2. **Install Pygame** if you haven't already:
   ```bash
   pip install pygame
   ```
3. **Run the game**:
   ```bash
   python ping_pong.py
   ```

## 🎯 How to Play

1. **Launch the game** - Run the Python script
2. **Player positioning** - Player 1 controls the left paddle, Player 2 controls the right paddle
3. **Objective** - Hit the ball with your paddle to send it to your opponent
4. **Scoring** - You score a point when the ball passes your opponent's paddle
5. **Winning** - First player to reach 5 points wins the game
6. **Restart** - Press Enter after game over to play again

## 🛠️ Technical Details

### Game Specifications
- **Resolution**: 1000x600 pixels
- **Frame Rate**: 60 FPS (Pygame default)
- **Ball Speed**: Adaptive with physics-based movement
- **Paddle Speed**: 4 pixels per frame

### Code Structure
- **Game Class** - Main game logic, scoring, and collision detection
- **Ball Class** - Ball physics, movement, and bouncing mechanics
- **Paddle Class** - Player paddle controls and movement
- **Modular Design** - Clean separation of concerns for easy modification

## 🎨 Customization

Want to modify the game? Here are some easy tweaks:

### Change Game Settings
```python
# In the Game class __init__ method
WIDTH, HEIGHT = 1200, 800  # Change window size
self.speed = 2             # Adjust ball speed (in Ball class)
self.speed = 6             # Adjust paddle speed (in Paddle class)
```

### Modify Winning Score
```python
# In check_winner method
if self.score_1 == 10:  # Change from 5 to 10
if self.score_2 == 10:  # Change from 5 to 10
```

### Color Themes
```python
# Change colors throughout the code
screen.fill("navy")           # Background color
pygame.draw.rect(screen, "yellow", self.my_pad)  # Paddle color
pygame.draw.ellipse(screen, "red", self.rect)    # Ball color
```

## 🐛 Known Issues

- Ball may occasionally get stuck in paddle (rare collision edge case)
- No AI opponent - requires two human players

## 🤝 Contributing

Feel free to fork this project and submit pull requests for:
- Bug fixes
- New features (AI opponent, power-ups, etc.)
- Code optimizations
- Visual enhancements

## 📝 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 🎉 Acknowledgments

- Built with Python and Pygame
- Inspired by the classic Pong arcade game
- Perfect for learning game development basics

---

**Enjoy the game! 🏓**

*Created with ❤️ for retro gaming enthusiasts*