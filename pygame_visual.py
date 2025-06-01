import pygame
import time

CELL_SIZE = 100
MARGIN = 5

COLOR_EMPTY = (255, 255, 255)
COLOR_TAXI = (0, 0, 255)
COLOR_TAXI_PASSENGER = (255, 165, 0)
COLOR_OBSTACLE = (0, 0, 0)
COLOR_TEXT = (0, 0, 0)
COLOR_BG = (200, 200, 200)
COLOR_STATUS_SUCCESS = (0, 128, 0)
COLOR_STATUS_FAIL = (255, 0, 0)

def draw_grid(screen, env, font, taxi_pos, has_passenger, grid_size):
    for r in range(grid_size):
        for c in range(grid_size):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN)
            color = COLOR_EMPTY
            if (r, c) in env.obstacles:
                color = COLOR_OBSTACLE
            pygame.draw.rect(screen, color, rect)

            for name, (pr, pc) in env.passenger_locs.items():
                if (r, c) == (pr, pc):
                    txt = font.render(name, True, COLOR_TEXT)
                    screen.blit(txt, (pc * CELL_SIZE + 30, pr * CELL_SIZE + 30))

    taxi_color = COLOR_TAXI_PASSENGER if has_passenger else COLOR_TAXI
    pygame.draw.rect(screen, taxi_color,
                     pygame.Rect(taxi_pos[1] * CELL_SIZE, taxi_pos[0] * CELL_SIZE,
                                 CELL_SIZE - MARGIN, CELL_SIZE - MARGIN))

def run_simulation_with_recorded_steps(env, steps, passenger_loc, destination, status):
    pygame.init()

    grid_size = env.grid_size
    width = height = grid_size * CELL_SIZE
    screen = pygame.display.set_mode((width, height + 50))  
    pygame.display.set_caption("Smart Taxi RL")
    font = pygame.font.SysFont(None, 36)
    font_small = pygame.font.SysFont(None, 28)
    clock = pygame.time.Clock()

    env.reset(passenger_loc=passenger_loc, destination=destination)

    for step_idx, (taxi_pos, has_passenger, action) in enumerate(steps, start=1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        env.taxi_pos = taxi_pos
        env.has_passenger = has_passenger

        screen.fill(COLOR_BG)
        draw_grid(screen, env, font, taxi_pos, has_passenger, grid_size)

        step_text = font_small.render(f"Step: {step_idx}/{len(steps)}", True, COLOR_TEXT)
        screen.blit(step_text, (10, height + 10))

        color_status = COLOR_STATUS_SUCCESS if status == "BERHASIL" else COLOR_STATUS_FAIL
        status_text = font_small.render(f"Status: {status}", True, color_status)
        screen.blit(status_text, (200, height + 10))

        pygame.display.flip()
        clock.tick(2)  

    time.sleep(3)
    pygame.quit()
