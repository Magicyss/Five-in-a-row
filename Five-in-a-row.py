import pygame
import time
'''
主要有四个相关类
Chess主要作为棋子类
Board主要作为棋盘，用于存储下棋的状态
Judger主要负责判断当前状态下的胜负
Runner主要负责整个程序的维护以及运行
'''
class Chess():
    colour=[]
    position=(0,0)
    def __init__(self,colour,position):
        self.colour=colour
        self.position=position
    #定义棋子自己的移动的方法
    def move(self):
        pass
class Board():
    board=[[0 for _ in range(15)] for i in range(15)]
    def __init__(self,rate=50):
        self.rate=rate#窗口比例大小
        pass
    def move(self,chess):
        #向棋盘中添加某个棋子
        if self.board[chess.position[0]][chess.position[1]]==0:
            self.board[chess.position[0]][chess.position[1]]=chess
            return True
        else:
            return False

    def initialize(self, screen):
        #画出整个棋盘
        for h in range(1, 16):
            pygame.draw.line(screen, [0, 0, 0], [self.rate, h * self.rate], [15*self.rate, h * self.rate], 1)
            pygame.draw.line(screen, [0, 0, 0], [h * self.rate, self.rate], [h * self.rate, 15*self.rate])
        pygame.draw.rect(screen, [0, 0, 0], [0.9*self.rate, 0.9*self.rate, 14.2*self.rate, 14.2*self.rate], 3)
        # 在棋盘上标出特殊点位
        pygame.draw.circle(screen, [0, 0, 0], [8*self.rate, 8*self.rate], 5, 0)
        pygame.draw.circle(screen, [0, 0, 0], [4*self.rate, 4*self.rate], 3, 0)
        pygame.draw.circle(screen, [0, 0, 0], [4*self.rate, 12*self.rate], 3, 0)
        pygame.draw.circle(screen, [0, 0, 0], [12*self.rate, 4*self.rate], 3, 0)
        pygame.draw.circle(screen, [0, 0, 0], [12*self.rate, 12*self.rate], 3, 0)

    def reset(self):
        for i in range(15):
            for j in range(15):
                self.board[i][j]=0


class Judger():

    def __init__(self):
        pass

    #判断程序起点
    def judge(self,board,chess):
        #以落下的棋子为起点，向左上、正上、右上、正右、右下、正下、左下、正左八个方向做递归判断
        #分别为1、2、3、4、5、6、7、8
        if self.judgedetail(board.board,chess.position[0]-1,chess.position[1]-1,chess,1,1)+self.judgedetail(board.board,chess.position[0]+1,chess.position[1]+1,chess,1,5)-1==5:
            return True
        elif self.judgedetail(board.board,chess.position[0],chess.position[1]-1,chess,1,2)+self.judgedetail(board.board,chess.position[0],chess.position[1]+1,chess,1,6)-1==5:
            return True
        elif self.judgedetail(board.board,chess.position[0]+1,chess.position[1]-1,chess,1,3)+self.judgedetail(board.board,chess.position[0]-1,chess.position[1]+1,chess,1,7)-1==5:
            return True
        elif self.judgedetail(board.board,chess.position[0]+1,chess.position[1],chess,1,4)+self.judgedetail(board.board,chess.position[0]-1,chess.position[1],chess,1,8)-1==5:
            return True
        else:
            return False

    #递归检测是否已经有人胜出
    def judgedetail(self,board,x,y,chess,flag,direction):
        if x<=-1 or y<=-1 or x>=15 or y>= 15:
            return flag
        if direction==1:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x-1,y-1,chess,flag+1,direction)
            else:
                return flag
        if direction==2:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x,y-1,chess,flag+1,direction)
            else:
                return flag
        if direction==3:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x+1,y-1,chess,flag+1,direction)
            else:
                return flag
        if direction==4:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x+1,y,chess,flag+1,direction)
            else:
                return flag
        if direction==5:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x+1,y+1,chess,flag+1,direction)
            else:
                return flag
        if direction==6:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x,y+1,chess,flag+1,direction)
            else:
                return flag
        if direction==7:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x-1,y+1,chess,flag+1,direction)
            else:
                return flag
        if direction==8:
            if board[x][y]==0:
                return flag
            if board[x][y].colour==chess.colour:
                return self.judgedetail(board,x-1,y,chess,flag+1,direction)
            else:
                return flag
        return flag



class Runner():

    def run(self):
        # 定义黑色和白色
        black_color = [0, 0, 0]
        white_color = [255, 255, 255]
        judger=Judger()
        # 创建棋盘对象实例
        board = Board()
        board.rate=60
        board.reset()
        # 用于判断是下黑棋还是白棋
        is_black = True
        # pygame初始化函数，固定写法
        pygame.init()
        pygame.display.set_caption('五子棋')  # 改标题
        screen = pygame.display.set_mode((16*board.rate, 16*board.rate))
        # 给窗口填充颜色
        screen.fill([125, 95, 24])
        board.initialize(screen)  # 给棋盘类发命令，调用函数将棋盘画出来
        pygame.display.flip()  # 刷新窗口显示
        while True:
            for event in pygame.event.get():
                # 根据事件的类型，进行判断
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYUP:
                    pass
                # pygame.MOUSEBUTTONDOWN表示鼠标的键被按下
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # button表示鼠标左键
                    x, y = event.pos  # 拿到鼠标当前在窗口上的位置坐标
                    # 将鼠标的(x, y)窗口坐标，转化换为棋盘上的坐标
                    column = round((x - board.rate) / board.rate)#四舍五入转换
                    row= round((y - board.rate) / board.rate)
                    if column<0 or row<0 or column>14 or row>14:
                        continue
                    if is_black:
                        chess=Chess(black_color,(column,row))
                    else:
                        chess = Chess(white_color, (column, row))
                    if board.move(chess):
                        is_black = not is_black
                        pos = [board.rate * (column + 1), board.rate * (row + 1)]
                        pygame.draw.circle(screen, chess.colour, pos, int(0.45*board.rate), 0)
                        pygame.display.flip()
                        # 调用判断胜负函数
                        if judger.judge(board,chess):
                            if is_black:
                                print("白棋赢了")
                            else:
                                print("黑棋赢了")
                            return False


run =Runner()
while True:
    if run.run():
        break
