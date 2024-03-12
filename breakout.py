
from game import *
import mediapipe as mp
import cv2

def main(score, balls):
    # inicializamos la clase Hands y almacenarla en una variable
    handsMp = mp.solutions.hands
    # cargamos componente con las herramientas que nos permitira dibujar mas adelante
    drawingMp = mp.solutions.drawing_utils
    # cargamos los estilos en la variable mp_drawing_styles
    mp_drawing_styles = mp.solutions.drawing_styles
    # iniciamos una captura de video en la camara 1
    cap = cv2.VideoCapture(0)
    with handsMp.Hands(static_image_mode=False,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
           # guardamos en la variable succes el estado de la captura y en image la captura
            #success, image = cap.read()
            step = 0
            run = True
            while run:
#####################################################################3
                _, image = cap.read()
                #height, width, _ = image.shape
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks is not None:
                    for hand_landmarks in results.multi_hand_landmarks:
                        drawingMp.draw_landmarks(image,hand_landmarks,handsMp.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
#####################################################################
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                        if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y):
                            estado='1'
                        else:
                            estado='0'
                        if (hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y):
                             estado=estado+'1'
                        else:
                            estado=estado+'0'
                        if (hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y):
                             estado=estado+'1'
                        else:
                            estado=estado+'0'
                        if (hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y):
                             estado=estado+'1'
                        else:
                            estado=estado+'0'
                        
                        #if estado== '1000':
                        if estado == '0000':
                            
                            if hand_landmarks.landmark[4].x < hand_landmarks.landmark[0].x:
                                paddle.moveRight(12)
                            #print('LEFT')
                            elif hand_landmarks.landmark[4].x > hand_landmarks.landmark[0].x:
                        #elif estado=='1100':
                                paddle.moveLeft(12)
                            #print('RIGHT')
                        elif estado=='0001':
                            run = False
                            #print('EXIT')

                            
                        all_sprites_list.update()

                        if ball.rect.y < 40:
                            ball.velocity[1] = -ball.velocity[1]
                            wall_sound.play()

                        if ball.rect.x >= WIDTH - wall_width - 10:
                            ball.velocity[0] = -ball.velocity[0]
                            wall_sound.play()

                        if ball.rect.x <= wall_width:
                            ball.velocity[0] = -ball.velocity[0]
                            wall_sound.play()

                        if ball.rect.y > HEIGHT:
                            ball.rect.x = WIDTH // 2 - 5
                            ball.rect.y = HEIGHT // 2 - 5
                            ball.velocity[1] = ball.velocity[1]
                            balls += 1
                            if balls == 4:
                                font = pygame.font.Font('./text_style/DSEG14Classic-Bold.ttf', 70)
                                text = font.render("GAME OVER", 1, WHITE)
                                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                                screen.blit(text, text_rect)
                                pygame.display.update()
                                pygame.time.wait(2000)
                                run = False

                        if pygame.sprite.collide_mask(ball, paddle):
                            ball.rect.x += ball.velocity[0]
                            ball.rect.y -= ball.velocity[1]
                            ball.bounce()
                            paddle_sound.play()

                        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
                        for brick in brick_collision_list:
                            ball.bounce()
                            brick_sound.play()
                            if len(brick_collision_list) > 0:
                                step += 1
                                for i in range(0, 448, 28):
                                    if step == i:
                                        ball.velocity[0] += 1
                                        ball.velocity[1] += 1
                            if 380.5 > brick.rect.y > 338.5:
                                score += 1
                                brick.kill()
                            elif 338.5 > brick.rect.y > 294:
                                score += 3
                                brick.kill()
                            elif 294 > brick.rect.y > 254.5:
                                score += 5
                                brick.kill()
                            else:
                                score += 7
                                brick.kill()
                            if len(all_bricks) == 0:
                                font = pygame.font.Font('./text_style/DSEG14Classic-Bold.ttf', 70)
                                text = font.render("SCREEN CLEARED", 1, WHITE)
                                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                                all_sprites_list.add(ball)
                                screen.blit(text, text_rect)
                                pygame.display.update()
                                pygame.time.wait(2000)
                                run = False

                        screen.fill(BLACK)

                        pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
                        pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
                        pygame.draw.line(screen, GREY, [(WIDTH - wall_width / 2) - 1, 0], [(WIDTH - wall_width / 2) - 1, HEIGHT], wall_width)

                        pygame.draw.line(screen, BLUE, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2], [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
                        pygame.draw.line(screen, BLUE, [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2], [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

                        pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 212.5], [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)
                        pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 212.5], [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)

                        pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
                        pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)

                        pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
                        pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)

                        pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
                        pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)

                        font = pygame.font.Font('./text_style/DSEG14Classic-Bold.ttf', 70)
                        text = font.render(str(f"{score:03}"), 1, WHITE)
                        screen.blit(text, (80, 120))
                        text = font.render(str(balls), 1, WHITE)
                        screen.blit(text, (520, 41))
                        text = font.render('000', 1, WHITE)
                        screen.blit(text, (580, 120))
                        text = font.render('1', 1, WHITE)
                        screen.blit(text, (20, 40))

                        all_sprites_list.draw(screen)

                        pygame.display.update()

                        clock.tick(FPS)
                # Voltee la imagen horizontalmente para obtener una vista de selfie.
                #cv2.imshow('MediaPipe', cv2.flip(image, 1))
                ## en caso de teclear la letra q suspendemos la operacion
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            pygame.quit()
    cap.release()


if __name__ == '__main__':
    main(score, balls)