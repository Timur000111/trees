import pygame
import sys
import math
import matplotlib.pyplot as plt

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BST Visualization")

FONT = pygame.font.SysFont(None, 24)

class BSTNode:
    def __init__(self, key, x, y, depth=0):
        self.key = key
        self.left = None
        self.right = None
        self.x = x
        self.y = y
        self.depth = depth

def draw_node(node):
    if node:
        if node.left:
            pygame.draw.line(SCREEN, (0,0,0), (node.x, node.y), (node.left.x, node.left.y), 2)
        if node.right:
            pygame.draw.line(SCREEN, (0,0,0), (node.x, node.y), (node.right.x, node.right.y), 2)
        pygame.draw.circle(SCREEN, (255,255,255), (node.x, node.y), 20)
        pygame.draw.circle(SCREEN, (0,0,0), (node.x, node.y), 20, 2)
        img = FONT.render(str(node.key), True, (0,0,0))
        rect = img.get_rect(center=(node.x, node.y))
        SCREEN.blit(img, rect)
        draw_node(node.left)
        draw_node(node.right)

def insert_bst(root, key, x=WIDTH//2, y=50, depth=0):
    if not root:
        return BSTNode(key, x, y, depth)
    offset = WIDTH // (2 ** (depth + 2))
    if key < root.key:
        root.left = insert_bst(root.left, key, x - offset, y + 80, depth + 1)
    else:
        root.right = insert_bst(root.right, key, x + offset, y + 80, depth + 1)
    return root

def main():
    root = None
    keys = []
    input_active = True
    input_text = ''
    
    clock = pygame.time.Clock()
    while True:
        SCREEN.fill((240, 240, 240))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if input_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        key = int(input_text)
                        keys.append(key)
                        root = insert_bst(root, key)
                    except ValueError:
                        pass
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode
        
        draw_node(root)
        
        pygame.draw.rect(SCREEN, (255,255,255), (10, HEIGHT-40, 200, 30))
        pygame.draw.rect(SCREEN, (0,0,0), (10, HEIGHT-40, 200, 30), 2)
        prompt = FONT.render("Enter number: " + input_text, True, (0,0,0))
        SCREEN.blit(prompt, (15, HEIGHT-35))
        
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

def plot_complexity():
    n = [100, 1000, 10000, 100000]
    bst = [x for x in n]
    logn = [math.log2(x) for x in n]
    logBn = [math.log2(x)/math.log2(32) for x in n]
    
    plt.figure()
    plt.plot(n, bst, label='BST (O(n))')
    plt.plot(n, logn, label='AVL/RB (O(log n))')
    plt.plot(n, logBn, label='B-Tree (O(log_B n))')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n')
    plt.ylabel('Cost')
    plt.title('Time Complexity Comparison')
    plt.legend()
    plt.show()


