import arcade

# SCREEN INFORMATION
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "The Loan Spacer"
TITLE_SIZE = 40
TITLE_FONT = "Race Guard"
BACKGROUND_IMG = "spacer/assets/images/space.png"


# SHIP
SHIP_MAX_SPEED = 5
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 15
SHIP_SCALE = 0.3
PLAYER_LIFE = 50
SHIP_GROUP = "player"
SHIP_IMG = "spacer/assets/images/playerShip3_green.png"
DEAD_IMG = "spacer/assets/images/spaceman.png"
# BULLET
BULLET_RADIUS = 10
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_SCALE = 0.6
PLAYER_BULLET_IMG = "spacer/assets/images/laserGreen11.png"
ENEMY_BULLET_IMG = "spacer/assets/images/laserRed03.png"
PLAYER_BULLET = "p_bullet"
ENEMY_BULLETS = "e_bullet"
# ----------------------------------ENEMY SHIPS--------------------------------
ENEMY_SHIP_RADIUS = 15
ENEMY_SHIP_SCALE = 0.3
ENEMY_GROUP = "enemy"
# SHIP IMAGES
BLACK1_IMG = "spacer/assets/images/enemyBlack1.png"
BLACK2_IMG = "spacer/assets/images/enemyBlack2.png"
BLACK3_IMG = "spacer/assets/images/enemyBlack3.png"
BLACK4_IMG = "spacer/assets/images/enemyBlack4.png"
BLACK5_IMG = "spacer/assets/images/enemyBlack5.png"
BLUE1_IMG = "spacer/assets/images/enemyBlue1.png"
BLUE2_IMG = "spacer/assets/images/enemyBlue2.png"
BLUE3_IMG = "spacer/assets/images/enemyBlue3.png"
BLUE4_IMG = "spacer/assets/images/enemyBlue4.png"
BLUE5_IMG = "spacer/assets/images/enemyBlue5.png"
GREEN1_IMG = "spacer/assets/images/enemyGreen1.png"
GREEN2_IMG = "spacer/assets/images/enemyGreen2.png"
GREEN3_IMG = "spacer/assets/images/enemyGreen3.png"
GREEN4_IMG = "spacer/assets/images/enemyGreen4.png"
GREEN5_IMG = "spacer/assets/images/enemyGreen5.png"
RED1_IMG = "spacer/assets/images/enemyRed1.png"
RED2_IMG = "spacer/assets/images/enemyRed2.png"
RED3_IMG = "spacer/assets/images/enemyRed3.png"
RED4_IMG = "spacer/assets/images/enemyRed4.png"
RED5_IMG = "spacer/assets/images/enemyRed5.png"
# SPEED
SLOW_SPEED = 1
MEDIUM_SPEED = 2
FAST_SPEED = 3
# HEALTH
LOW_HEALTH = 1
MEDIUM_HEALTH = 4
HIGH_HEALTH = 10
# RANGE
CLOSE_RANGE = 125
MEDIUM_RANGE = 250
FAR_RANGE = 300
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
# -------------------------------END ENEMY SHIPS--------------------------------
# PARTICLE EFFECTS
PARTICLE_GRAVITY = 0.05
PARTICLE_FADE_RATE = 8
# Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5
PARTICLE_COUNT = 5
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
LEVEL_THREE = 150
LEVEL_FOUR = 300
# HEALTHBAR
HEALTHBAR_WIDTH = 120
HEALTHBAR_HEIGHT = 25
HEALTH_GROUP = "health"
