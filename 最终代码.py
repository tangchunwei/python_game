# 导入资源
import  pygame
from pygame.locals import  *
import  time
import  random
# 定义基类的基类
class Base(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x=x
        self.y=y
        self.screen=screen_temp
        # 加载飞机图片
        self.image=pygame.image.load(image_name)
        # 存储发射出去的对象引用
        self.bullet_list=[]
# 定义飞机基类
class BasePlane(Base):
    # 初始化窗口对象以及坐标
    def __init__(self,screen_temp,x,y,image_name):
        Base.__init__(self,screen_temp,x,y,image_name)
    def display(self):
        # 填充飞机到屏幕
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            # 判断子弹是否越界
            if bullet.judge():
                self.bullet_list.remove(bullet)

# 定义飞机类
class HeroPlane(BasePlane):
    # 初始化窗口对象以及坐标
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,700,"./feiji/hero1.png")
    def move_left(self):
        # 向左移动
        self.x-=5
    def move_right(self):
        # 向右运动
        self.x+=5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
# 定义敌机类
class EnemyPlane(BasePlane):
    # 初始化窗口对象以及坐标
    def __init__(self,screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.direction="right"
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
        random_num=random.randint(1,100)
        if random_num ==8 or random_num==20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
# 定义子弹基类
class BaseBullet(Base):
    def __init__(self,screen_temp,x,y,image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
# 定义玩家子弹类
class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")
    def move(self):
        self.y-=5
    def judge(self):
        if self.y<0:
            return  True
        else:
            return  False
# 定义敌机子弹类
class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self, screen_temp, x+25, y+40, "./feiji/bullet1.png")
    def move(self):
        self.y+=5
    def judge(self):
        if self.y>852:
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
        enemy.move()  #调用敌机移动方法
        enemy.fire()    #调用敌机发射子弹方法
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)
if __name__=="__main__":
    main()