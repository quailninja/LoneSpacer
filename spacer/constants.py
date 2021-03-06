import arcade
from sys import platform

if platform == "linux" or platform == "linux2":
    full = False
elif platform == "darwin":
    full = False
elif platform == "win32":
    full = True

width, height = arcade.get_display_size()

if not full:
    height -= 100
# SCREEN INFORMATION
FULLSCREEN = full
SCREEN_WIDTH = width
SCREEN_HEIGHT = height
SCREEN_TITLE = "The Loan Spacer"
TITLE_SIZE = 40
TITLE_FONT = "Race Guard"
BACKGROUND_IMG = "spacer/assets/images/space.png"
TITLE_LINE_HEIGHT = 100
DEFAULT_LINE_HEIGHT = 100
TITLE_FONT_SIZE = 40
DEFAULT_FONT_SIZE = 18
DEBRIS_AMOUNT = 7
ANNOUNCEMENT_TIME = 240
ANNOUNCEMENT_GROUP = "messages"
# SHIP
SHIP_MAX_SPEED = 7.3
SHIP_TURN_AMOUNT = 3
SHIP_FORWARD_THRUST = 0.37
SHIP_REVERSE_THRUST = 0.18
SHIP_RADIUS = 15
SHIP_SCALE = 0.3
PLAYER_LIFE = 50
SHIP_GROUP = "player"
SHIP_IMG = "spacer/assets/images/playership.png"
# SHIELD
SHIELD_LIFE = 10
SHIELD_SCALE = 0.1
SHIELD_RADIUS = 20
SHIELD_GROUP = "shield"
SHIELD_IMG = "spacer/assets/images/shield.png"
# LOOT
HEALTH_IMAGE = "spacer/assets/images/health.png"
SHIELD_IMAGE = "spacer/assets/images/powerup_shield.png"
LOOT_GROUP = "loot"
# BULLET
BULLET_RADIUS = 10
BULLET_SPEED = 16
BULLET_LIFE = 60
BULLET_SCALE = 0.6
PLAYER_BULLET_IMG = "spacer/assets/images/laserGreen11.png"
ENEMY_BULLET_IMG = "spacer/assets/images/laserRed03.png"
PLAYER_BULLET = "p_bullet"
ENEMY_BULLETS = "e_bullet"
# DAMAGE
LOW_DAMAGE = 1
AVERAGE_DAMAGE = 2
HIGH_DAMAGE = 3
# MISSILE
MISSILE_RADIUS = 11
MISSILE_SPEED = 13
MISSILE_LIFE = 1
MISSILE_SCALE = 0.8
MISSILE_IMG = "spacer/assets/images/missile.png"
MISSILE_GROUP = "missile"
# ----------------------------------ENEMY SHIPS--------------------------------
ENEMY_SHIP_RADIUS = 15
BOSS_RADIUS = 40
ENEMY_SHIP_SCALE = 0.3
ENEMY_GROUP = "enemy"
# SHIP IMAGES
ENEMY1_IMG = "spacer/assets/images/enemy1.png"
ENEMY2_IMG = "spacer/assets/images/enemy2.png"
ENEMY3_IMG = "spacer/assets/images/enemy3.png"
ENEMY4_IMG = "spacer/assets/images/enemy4.png"
BOSS_IMG = "spacer/assets/images/boss.png"
# SPEED
SLOW_SPEED = 1
MEDIUM_SPEED = 2
FAST_SPEED = 3
# HEALTH
LOW_HEALTH = 1
MEDIUM_HEALTH = 4
HIGH_HEALTH = 10
BOSS_HEALTH = 100
# RANGE
CLOSE_RANGE = 125
MEDIUM_RANGE = 250
FAR_RANGE = 300
BOSS_RANGE = 500
# SWARM DISTANCE
CLOSE_SWARM = 6
AVERAGE_SWARM = 15
FAR_SWARM = 25
# SHOT RATES
VERY_SLOW_SHOT_RATE = 450
SLOW_SHOT_RATE = 300
AVERAGE_SHOT_RATE = 165
FAST_SHOT_RATE = 90
FASTEST_SHOT_RATE = 50
BOSS_MISSILE_CHANCE = 100
# SPAWN RATES
MINIMUM_ENEMIES = 3
MAXIMUM_ENEMIES = 37
SLOW_SPAWN_RATE = 200
MEDIUM_SPAWN_RATE = 110
FAST_SPAWN_RATE = 75
LOW_SPAWN_AMOUNT = 5
MEDIUM_SPAWN_AMOUNT = 13
HIGH_SPAWN_AMOUNT = 20
# POINT VALUES
BLACK_POINTS = 1
GREEN_POINTS = 2
BLUE_POINTS = 5
RED_POINTS = 10
BOSS_POINTS = 500
# -------------------------------END ENEMY SHIPS--------------------------------
# PARTICLE EFFECTS
PARTICLE_GRAVITY = 0.05
PARTICLE_FADE_RATE = 8
# Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5
PARTICLE_COUNT = 10
PARTICLE_RADIUS = 2
PARTICLE_COLORS = [
    arcade.color.ALIZARIN_CRIMSON,
    arcade.color.COQUELICOT,
    arcade.color.LAVA,
    arcade.color.KU_CRIMSON,
    arcade.color.DARK_TANGERINE,
]
PARTICLE_SPARKLE_CHANCE = 0.02
EXPLOSION_GROUP = "particles"
# --- SMOKE
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5
SMOKE_CHANCE = 0.25
SMOKE_GROUP = "smoke"
# LEVEL/HUD
LEVEL_GROUP = "level"
SCORE_GROUP = "score"
HUD_FONT_SIZE = 20
HUD_FONT_NAME = "Space Mission"
HUD_SPACE = 30
LEVEL_TWO = 50
LEVEL_THREE = 125
LEVEL_FOUR = 200
LEVEL_BOSS = 300
DEMO_LEVEL_TWO = 5
DEMO_LEVEL_THREE = 13
DEMO_LEVEL_FOUR = 20
DEMO_LEVEL_BOSS = 30
# HUDBAR
HEALTHBAR_WIDTH = 120
HEALTHBAR_HEIGHT = 25
SHIELDBAR_WIDTH = 80
SHIELDBAR_HEIGHT = 25
HUD_GROUP = "health"
# SOUNDS
SOUND_GROUP = "sounds"
PLAYER_LASER = "spacer/assets/sounds/laser.wav"
ENEMY_LASER = "spacer/assets/sounds/enemy_laser.wav"
EXPLOSION = "spacer/assets/sounds/explosion.wav"
SHIELD_UP = "spacer/assets/sounds/shield_up.wav"
SHIELD_DOWN = "spacer/assets/sounds/shield_down.wav"
MISSILE = "spacer/assets/sounds/missile.wav"
BACKGROUND_MUSIC = "spacer/assets/sounds/background_music.mp3"
TITLE_MUSIC = "spacer/assets/sounds/title_loop.mp3"
