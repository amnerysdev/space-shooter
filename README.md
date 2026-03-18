# .𖥔 ݁ ˖🪐.𖥔 ݁ ˖ Space Shooter

Space Shooter is a 2D arcade-style game built with Python and pygame-ce. The main goal of this project was to get hands-on experience with game development fundamentals: sprite-based OOP architecture, delta-time movement, collision detection, custom events, and audio integration.

The player pilots a spaceship through a starfield, shooting down incoming meteors before they make contact. The game tracks how long the player survives, displayed as a live score counter on screen.


## 📦 Technologies

- `Python 3`
- `pygame-ce` — the actively maintained Community Edition fork of pygame
- `random` — for randomizing meteor spawn positions, directions, and speeds

## 🚀 Features

- **Player Movement:** The player can move freely in all four directions using the arrow keys. Movement is normalized so diagonal movement does not feel faster than cardinal movement. 

- **Laser Shooting with Cooldown:** Pressing the spacebar fires a laser from the ship's nose. A cooldown system prevents the player from spamming shots. Each shot plays a sound effect.

- **Meteor Spawning:** Meteors are spawned every 500 ms via a custom pygame event timer. Each meteor appears at a random `x` position above the visible screen and drifts downward with a slight random horizontal angle. Speed, rotation rate, and direction are all randomized per meteor. Meteors self-destruct after 3 seconds if not destroyed.

- **Pixel-Perfect Collision Detection:** Laser-meteor collisions use pygame's mask-based collision (`collide_mask`), which checks actual pixel overlap rather than bounding rectangles. This prevents false positives from transparent areas around the meteor sprite. Player-meteor collisions end the game immediately.

- **Explosion Animation:** When a laser destroys a meteor, an explosion sprite is spawned at the impact point. The explosion cycles through 21 frames using delta-time-based frame indexing and removes itself automatically when the animation ends. Each explosion also plays a sound effect.

- **Survival Score:** The score is the number of seconds the player has survived, derived from `pygame.time.get_ticks()`. It is displayed at the bottom center of the screen using the Oxanium Bold font, inside a rounded rectangle border.

- **Starfield Background:** 20 star sprites are placed at random positions across the screen at startup, giving the game a space atmosphere. Stars are static — they serve as a decorative background layer.

## 🖇 How to Run

1. Make sure Python 3 is installed.
2. Install pygame-ce:
   ```bash
   pip install pygame-ce
   ```
3. Run the game:
   ```bash
   python code/main.py
   ```

Use the arrow keys to move and spacebar to shoot. Survive as long as possible!

## 💥Preview



https://github.com/user-attachments/assets/565641cf-9362-4514-94b6-6812fd06b858


