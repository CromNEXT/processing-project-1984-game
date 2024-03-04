P = False
E = False
D = 0
#enemy 기본 좌표
X3 = 750
Y3 = 50

C = False
X1 = 8
Y1 = 100
A1 = False

#player 기본좌표
X = 750
Y = 1000
#속도
XV = 25
YV = 25
GL = False #왼쪽 이동
GR = False #오른쪽 이동
GU = False #위로 이동
GD = False #아래로 이동
#폭탄
YB = 655
BV = 15
A = False
#색깔
R = 0     #player
G = 217
B = 252
R1 = 0    #player 막대
B1 = 0
G1 = 255
R2 = 200  #enemy
G2 = 217  
B2 = 252
R4 = 255  #enemy 막대
BCR = 0   #배경색
BCB = 0
BCG = 0    
Mode1 = False #색상모드 1
Mode2 = False #색상모드 2
V1 = False
def setup():
    size (1500, 1200)
    background(0)
   
def draw():
    global X,Y,XV,YV,GL,GR,GU,GD,XC,YC,YB,R,G,B,Mode1,Mode2, X3,Y3, X1, C, A1, Y1, R2,G2,B2,G1,BV,V1,R1,B1,A,D,R4,BCR,BCG,BCB,E,P
    background(BCR,BCG,BCB)
    fill(255)
    noStroke()
    rect(random(width),random(height),10,10)
    fill(255)
    stroke(0)
    rect(0,400,width,2)
    #player
    fill(R,G,B)
    rect(X-25,Y-35,50,70)  #몸통
    rect(X-85,Y-5,85,30)  #좌측
    rect(X,Y-5,85,30)  #우측
    fill(R1,G1,B1)
    rect(X-50,Y-25,10,30)
    rect(X+45,Y-25,10,30)    
    rect(X-5,Y-55,10,40)  #머리
    #enemy
    fill(R2,G2,B2)
    rect(X3-25,Y3-35,50,70)
    rect(X3-85,Y3-25,85,30)
    rect(X3,Y3-25,85,30)
    fill(R4,0,0)
    rect(X3-50,Y3-5,10,30)
    rect(X3+45,Y3-5,10,30)    
    rect(X3-5,Y3+15,10,40)

    #움직임
    if (C):
        X3 = X3 + X1
   
    if X3 > width :
        X1 = -5-random(25)
    if X3 < 0 :
        X1 = 5+random(25)


   
    if (GL):
        X = X-XV
        GL = False
    elif (GR):    
        X = X+XV
        GR = False
    elif (GU):    
        Y = Y-YV
        GU = False
    elif (GD):    
        Y = Y+YV
        GD = False
   
    #이탈방지 코드    
    if X < 0:
        X = 1499
    if X > width:
        X = 1
    if Y < 450:
        Y = 1200
    if Y > height:
        Y = 1200
    if (YB < 0):
        YB = Y  
       
    #색상
    if (Mode1):
        R = 195
        G = 255
        B = 3  
    if (Mode2):
        R = 0
        G = 217
        B = 252          
    if (V1):
        G1 = random(255)
        R1 = random(255)
        B1 = random(255)
        R = random(255)
        G = random(255)
        B = random(255)
        BV = 25
    #폭탄 코드
    fill(random(255),0,0)
    if (A):
        ellipse(X,YB,50,50)
        YB = YB-BV
       
    else:
        YB = Y
    if (YB < 0):
        YB = Y
       
    fill(random(200),0,0)
   
    if (A1):
        ellipse(X3,Y1, 15, 15)
        Y1 = Y1 + 10
    else:
        Y1 = Y3
    if (Y1 > 1200):
        Y1 = Y3 + 50
   
    #점수판
    textSize(32)
    fill(0, 102, 153)
    text("Point : {}".format(D), 10, 30)
   
   
    #피격판정    
    #enemy
    if (YB < Y3 and X3 - 45 <= X <= X3 + 45):
        D = D + 100
        A = False
        A1 = False
        C = False
        P = False
         
     
    #player
    if (Y-10 < Y1 < Y+30 and X - 25 <= X3 <= X + 25):

        A = False
        D = 0
        A1 = False
        C = False
        V1 = False
        BCR = 0  
        BCB = 0
        BCG = 0  
        R2 = 200  
        G2 = 217  
        B2 = 252
        R4 = 255
        delay(1000)
        P = False
   
    #이벤트
    if (D == 0):
        textSize(50)
        fill(255)
        text("Welcome Player", 600, 200)
        textSize(20)
        text("Press (B) or (b) and game start", 1100, 200)
        text("You can move Using 'W','A','S','D' ", 100, 200)
        text("You can move Using 'W','A','S','D' ", 100, 200)
        textSize(100)
        text("1984", 615, 400)
    if (D == 100):   #100점 혜택
        V1 = True
       
    if (D == 200):   #200점 혜택
        R2 = 255
        G2 = 255
        B2 = 255
        BV = 30
   
    if (D >= 300):  #300점 혜택
        Y1 = Y1 + 15
        R2 = 255
        G2 = 0
        B2 = 0    
        BV = 35
        BCR = 169
        BCG = 142
        BCB = 255
        XV = 40
        YV = 40
   
    if (D >= 500): #500점 효과
        Y1 = Y1 + 20
        BCR = 252
        BCG = 48
        BCB = 252
 
       
    if (D >= 700): #700점 효과
        Y1 = Y1 + 30
        BCR = 190
        BCG = 198
        BCB = 106
        BV =  40
       
    if (D == 900): #900점 효과
        R4 = 0
        BCR = random(0,150)
        BCB = 0
        BCG = 0
        BV =  45
   
    if (D == 1000):  #1000점 효과
       
        R2 = 0
        B2 = 0
        G2 = 0
        BCR = 255
        BCG = 255
        BCB = 255
        textSize(100)
        fill(0, 100, 100)
        text("Good! Please Press L Button", 10, 600)

    if (D > 1000):
        D = 1000
   
    if (D == 1000 and E == True):
        background(0)
        textSize(100)
        fill(0, 100, 100)
        text("You Win", 600, 600)
        fill(0, 100, 0)
        text("Score : {}".format(D), 400, 400)
        delay(1000)    

    if (P):
        D = 900
       
   
def keyPressed(): #키보드 조작
    global GL,GR,GU,GD,Mode1,Mode2,A, X3, X1, C, A1,E,P
    #폭탄 on/off
    if ((key == 'b') or (key=='B')): #B키
        A = True
    if ((key == 'm') or (key=='M')): #M키
        A = False          
    #조종
    if ((key == 'a') or (key == 'A')): #A키
        GL = True
    elif ((key == 'd') or (key == 'D')): #D키
        GR = True
    elif ((key == 'w') or (key == 'W')): #W키
        GU = True  
    elif ((key == 's') or (key == 'S')): #S키  
        GD = True        
    #색상
    if ((key == 'j') or (key == 'J')): #J키
        Mode1 = True
        Mode2 = False
    if ((key == 'k') or (key == 'K')): #K키
        Mode2 = True  
        Mode1 = False  
    #인공지능 시작
    if ((key == 'b') or (key == 'B')): #T키
        C = True
        A1 = True
    if ((key == 'l') or (key == 'L')):
        E = True
    if ((key == 'p') or (key == 'P')):
        P = True       
