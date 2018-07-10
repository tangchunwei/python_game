# 导入资源
import  pygame
from pygame.locals import  *
import  time
# 定义飞机类
class HeroPlane(object):
    # 初始化窗口对象以及坐标
    def __init__(self,screen_temp):
        self.x=210
        self.y=700
        self.screen=screen_temp
        # 加载飞机图片
        self.image=pygame.image.load("./feiji/hero1.png")
        # 存储发射出去的对象引用
        self.bullet_list=[]
    def display(self):
        # 填充飞机到屏幕
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def move_left(self):
        # 向左移动
        self.x-=5
    def move_right(self):
        # 向右运动
        self.x+=5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
# 定义敌机类
class EnemyPlane(object):
    # 初始化窗口对象以及坐标
    def __init__(self,screen_temp):
        self.x=0
        self.y=0
        self.screen=screen_temp
        # 加载飞机图片
        self.image=pygame.image.load("./feiji/enemy0.png")
        # 存储发射出去的对象引用
        self.bullet_list=[]
        self.direction="right"
    def display(self):
        # 填充飞机到屏幕
        self.screen.blit(self.image,(self.x,self.y))
        # for bullet in self.bullet_list:
        #     bullet.display()
        #     bullet.move()
    def move(self):
        # 控制飞机方向
        if self.direction=='right':
            self.x+=5
        elif self.direction=='left':
            self.x-=5
        # 控制左右移动
        if self.x>480-50:
            self.direction='left'
        elif self.x<0:
            self.direction='right'


    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

# 定义子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x=x+40
        self.y=y-20
        self.screen=screen_temp
        self.image=pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=5
    def judge(self):
        if self.y<0:
            return  True
        else:
            return  False


# 定义函数
def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
def main():
    # 创建窗口
    screen=pygame.display.set_mode((480,852),0,32)
    # 创建背景图片
    background=pygame.image.load("./feiji/background.png")
    # 创建一个飞机对象
    hero=HeroPlane(screen)
    # 创建一个敌机对象
    enemy=EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)
if __name__=="__main__":
    main()