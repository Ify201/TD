"""
TOWER DEFENSE GAME - PROJECT SKELETON
A structural outline for planning and building out the game.
Fill in each section as you implement it.
"""

# -------------------------------
# Imports & Constants
# -------------------------------
# - pygame (or chosen framework) import and version notes
# - Screen dimensions, FPS, tile size
# - Color constants (RGB tuples)
# - Global game constants (starting gold, starting lives, wave delay timers)
# - Asset file paths (images, sounds, fonts)


# -------------------------------
# Variable Initialisation
# -------------------------------
# - Game state variables (menu, playing, paused, game_over)
# - Player resources: gold, lives, score
# - Current wave number / wave timer
# - Lists/groups: active enemies, active towers, active projectiles
# - Grid/path representation (tile map, waypoints for enemy path)
# - Mouse/selection state (selected tower type, hovered tile)
# - Clock object for frame timing


# -------------------------------
# Asset Loading
# -------------------------------
# - Load and scale sprite images (towers, enemies, projectiles, UI icons)
# - Load sound effects and background music
# - Load fonts for UI text
# - Load level/map data (from file, dict, or hardcoded list)


# -------------------------------
# Map / Grid Setup
# -------------------------------
# - Define the grid dimensions and tile size
# - Define the enemy path as a list of waypoints (x, y coordinates)
# - Mark which tiles are buildable vs path tiles
# - Function: draw_grid() - renders grid lines/tiles to screen
# - Function: is_tile_buildable(tile_pos) - validation check


# -------------------------------
# Enemy Class(es)
# -------------------------------
# - Base Enemy class: position, health, speed, reward value, path index
# - Method: move() - advance along waypoints each frame
# - Method: take_damage(amount) - reduce health, handle death
# - Method: draw(screen) - render enemy + health bar
# - Subclasses for enemy variants (fast, tanky, flying, boss) with stat overrides
# - Method: reached_end() - check if enemy reached the base (lose a life)


# -------------------------------
# Tower Class(es)
# -------------------------------
# - Base Tower class: position, range, damage, fire_rate, cost, target
# - Method: find_target(enemy_list) - targeting logic (closest/first/strongest)
# - Method: shoot() - spawn a projectile toward target
# - Method: draw(screen) - render tower + range indicator when selected
# - Subclasses for tower types (basic, splash/AOE, slow, sniper) with stat overrides
# - Upgrade logic: upgrade_tower(tower) - increases stats, costs gold


# -------------------------------
# Projectile Class
# -------------------------------
# - Position, velocity/direction, speed, damage, target reference
# - Method: move() - travel toward target each frame
# - Method: check_collision(enemy_list) - detect hit, apply damage, handle splash
# - Method: draw(screen) - render projectile sprite


# -------------------------------
# Wave / Spawner Logic
# -------------------------------
# - Wave definitions (enemy types, counts, spawn intervals per wave)
# - Function: spawn_wave(wave_number) - queues enemies to spawn
# - Function: update_spawner(dt) - handles timed spawning within a wave
# - Logic for wave progression and difficulty scaling
# - Detect wave cleared -> trigger next wave / rest period


# -------------------------------
# Tower Placement & Input Handling
# -------------------------------
# - Handle mouse click: select tower type from UI, place on grid
# - Validate placement (enough gold, tile buildable, not occupied)
# - Deduct gold on successful placement
# - Handle tower selection (click existing tower to view/upgrade/sell)
# - Handle keyboard shortcuts (pause, speed up, escape menu)


# -------------------------------
# Collision & Combat Resolution
# -------------------------------
# - Tower-to-enemy range checks each frame
# - Projectile-to-enemy hit detection
# - Splash/AOE damage application to multiple enemies
# - Enemy death handling (reward gold, remove from list, play effect)
# - Enemy reaching base (deduct life, remove from list)


# -------------------------------
# UI / HUD Rendering
# -------------------------------
# - Draw gold, lives, score, current wave counter
# - Draw tower selection panel/buttons
# - Draw tower info panel when a tower is selected (stats, upgrade/sell buttons)
# - Draw pause menu / game over screen / victory screen
# - Draw range indicators, placement previews (valid/invalid highlight)


# -------------------------------
# Game State Management
# -------------------------------
# - Function: check_game_over() - lives <= 0
# - Function: check_victory() - all waves cleared
# - Function: reset_game() - reinitialize all state variables
# - Function: pause_game() / resume_game()
# - Save/load high score or progress (optional)


# -------------------------------
# Main Game Loop
# -------------------------------
# - Event handling (quit, mouse, keyboard)
# - Update phase: move enemies, update towers, update projectiles, spawner tick
# - Collision/combat resolution phase
# - Draw phase: background, grid, entities, UI, overlays
# - Clock tick / delta time calculation
# - State-based branching (menu vs playing vs paused vs game_over)


# -------------------------------
# Entry Point
# -------------------------------
# - Initialize pygame/framework
# - Create screen/window
# - Call setup functions (load assets, init variables, build map)
# - Run main loop
# - Clean up / quit on exit