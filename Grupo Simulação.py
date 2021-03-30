from vpython import *
import numpy as np

#Função para encontrar w para cada planeta:
#A partir do raio da órbita dada "dist_r", retorna a velocidade angular da órbita
def w(dist_r):
  ##Definindo a velocidade angular de cada planeta usando a terceira lei de Kepler
  ##K=T²/R³, vamos descobrir K do sistema solar usando os dados da Terra
  k = (365.26 ** 2) / (100 ** 3)  # dias²/(cUA)³
  #velocidade angular de cada planeta é dada por w=2π/T, onde T=(K/R³)^(1/2)
  return 2 * np.pi / ((k * (dist_r ** 3)) ** (1 / 2))

#Função para encontrar a rotação dos corpos:
#A partir do período de rotação "t_rot", retorna a velocidade angular de rotação
def w_rot(t_rot):
  ##velocidade angular de rotação da Terra -> T_rot=1 dia
  w_rot=2*np.pi/t_rot
  return w_rot

#Função para a inclinação dos corpos:
#A partir da angulação "degree", retorna o vetor para inclinar o objeto
def axis(degree):
  return vec(np.cos(radians(degree)), -np.sin(radians(degree)), 0)

#Função para o eixo de rotação:
#A partir da angulação "degree", retorna o vetor para o eixo de rotação
def axis_r(degree):
  return vec(np.sin(radians(degree)), np.cos(radians(degree)), 0)

#Função para calcular a posição dos corpos:
##A partir do raio da órbita "r_planet", velocidade angular desta "w_planet" 
##e parâmetro de tempo "time", retorna o vetor de posição do corpo (x,y,z)
def pos(r_planet,w_planet,time):
  ##Podemos escrever a posição x,z de cada planeta como uma função de t (dias)
  ##z=-R*sen(wt), x=R*cos(wt)
  x = r_planet * np.cos(w_planet * time)
  y = 0
  z = -r_planet * np.sin(w_planet * time)
  return vector(x,y,z)

scene.autoscale = False
scene.range = 200  ##Escala da animação
cUA = 1 #1495.979 #Mm

#Colocando a iluminação no lugar do Sol
scene.lights = []
lamp = local_light(pos=vector(0, 0, 0), color=color.white)

#Raio da órbita de cada corpo (em cUA)
##Estas distâncias são as reais, usadas para calcular os períodos de translação
R_Mercury = 46.6697*cUA ##Afélio
R_Venus = 72.8*cUA ##Afélio
R_Earth = 100*cUA  ##Distância média (1 UA)
R_Mars = 166.6*cUA ##Afélio
R_Jupiter = 545.88*cUA ##Afélio
R_Saturn = 1011.596*cUA ##Afélio
R_Uranus = 	2011*cUA ##Afélio
R_Neptune = 3033*cUA ##Afélio
R_Moon=10*cUA #(fora de escala)
R_Fobos= 9.377 #Mm
R_Deimos= 23.460 #Mm

#Posições iniciais de cada corpo em cUA
r_Sun = vector(0, 0, 0)
r_Mercury = vector(R_Mercury, 0, 0)
r_Venus = vector(R_Venus, 0, 0)
r_Earth = vector(R_Earth, 0, 0)
r_Mars = vector(R_Mars, 0, 0)
r_Jupiter = vector(R_Jupiter, 0, 0)
r_Saturn= vector(R_Saturn, 0, 0)
r_Uranus= vector(R_Uranus, 0, 0)
r_Neptune= vector(R_Neptune, 0, 0)
r_Moon= vector(R_Earth+R_Moon, 0, 0)
r_Fobos= vector(R_Mars+R_Fobos, 0, 0)
r_Deimos= vector(R_Mars+R_Deimos, 0, 0)

##Inclinação dos Planetas (usado para fazer o movimento de rotação)
axis_Sun = axis(7.5)
rot_Sun = axis_r(7.5)
axis_Mercury = axis(0)
rot_Mercury = axis_r(0)
axis_Venus = axis(177.3)
rot_Venus = axis_r(177.3)
axis_Earth = axis(23.5)
rot_Earth = axis_r(23.5)
axis_Mars = axis(25.19)
rot_Mars = axis_r(25.19)
axis_Jupiter = axis(3.12)
rot_Jupiter = axis_r(3.12)
axis_Saturn = axis(26.73)
rot_Saturn = axis_r(26.73)
axis_Uranus = axis(97.86)
rot_Uranus = axis_r(97.86)
axis_Neptune = axis(29.58)
rot_Neptune = axis_r(29.58)

# Propriedades dos planetas
##o Raio dos planetas está em Mm (Megametros)
Background = sphere(pos=r_Sun, radius=10000*cUA, texture="https://exoplanets.nasa.gov/internal_resources/698/", shininess=0)
Sun = sphere(pos=r_Sun, radius=20, axis=axis_Sun, texture="https://i.imgur.com/SyvqCLF.jpg", emissive=True) #raio deveria ser 696
Mercury = sphere(pos=r_Mercury, radius=2.4397, axis=axis_Mercury, texture="https://i.imgur.com/YttpWJD.jpg")
Venus = sphere(pos=r_Venus, radius=6.0518, axis=axis_Venus, texture="https://i.imgur.com/7VTEX2w.jpeg")
Earth = sphere(pos=r_Earth, radius=6.371, axis=axis_Earth, texture=textures.earth)
Mars = sphere(pos=r_Mars, radius=3.3895, axis=axis_Mars, texture="https://i.imgur.com/Mwsa16j.jpg")
Jupiter = sphere(pos=r_Jupiter, radius=69.911, axis=axis_Jupiter, texture="https://i.imgur.com/RMMtt0K.jpeg")
Saturn = sphere(pos=r_Saturn, radius=58.232, axis=axis_Saturn, texture="https://i.imgur.com/5Pur4IE.jpeg")
Uranus = sphere(pos=r_Uranus, radius=25.362, axis=axis_Uranus, texture="https://i.imgur.com/lwQRzCq.jpg")
Neptune = sphere(pos=r_Neptune, radius=24.622, axis=axis_Neptune, texture="https://i.imgur.com/lyLpoMk.jpg")

#Propridades das luas
var_m=int(input("Você quer ver a trajetória da Lua? Digite 1 se sim ou 0 se não."))
Moon = sphere(pos=r_Moon , radius=1.737, texture="https://i.imgur.com/cnyUPrb.jpg", make_trail=var_m, trail_radius=0.2)
#Aumentamos em 10x o tamanho destes 2 astros para ficarem visíveis
Fobos = sphere(pos=r_Fobos, radius=0.11267, texture="https://i.imgur.com/cnyUPrb.jpg",make_trail=False, trail_radius=0.2)
Deimos = sphere(pos=r_Deimos, radius=0.062, texture="https://i.imgur.com/cnyUPrb.jpg",make_trail=False, trail_radius=0.2)

#Anéis dos gigantes gasosos
Jupiter_ring = extrusion(path=[vec(0, 0, 0), vec(0.5*np.sin(radians(3.12)), 0.5*np.cos(radians(3.12)), 0)], color=color.white, opacity=0.1, shape=[ shapes.circle(radius=129), shapes.circle(radius=92)],texture="https://i.imgur.com/tHRAdnT.png",shininess=0)
Saturn_ring = extrusion(path=[vec(0, 0, 0), vec(0.5*np.sin(radians(26.73)), 0.5*np.cos(radians(26.73)), 0)], color=color.white, opacity=0.8, shape=[ shapes.circle(radius=136.78), shapes.circle(radius=67.7)], texture="https://i.imgur.com/55xfxWx.png",shininess=0)
Uranus_ring = extrusion(path=[vec(0, 0, 0), vec(0.5*np.sin(radians(97.86)), 0.5*np.cos(radians(97.86)), 0)], color=color.white, opacity=0.2, shape=[ shapes.circle(radius=100), shapes.circle(radius=67.7)],texture="https://i.imgur.com/rFiZL68.png",shininess=0)
Neptune_ring = extrusion(path=[vec(0, 0, 0), vec(0.5*np.sin(radians(29.58)), 0.5*np.cos(radians(29.58)), 0)], color=color.white, opacity=0.2, shape=[ shapes.circle(radius=103), shapes.circle(radius=26.840)],texture="https://i.imgur.com/3tKmpy5.png",shininess=0)

##Trajetórias
Me=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Mercury, thickness=0.3, color=color.white)
Ve=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Venus, thickness=0.3, color=color.yellow)
Ea=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Earth, thickness=0.3, color=color.blue)
Mo=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Moon, thickness=0.1, color=color.white)
Ma=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Mars, thickness=0.3, color=color.red)
Fo=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Fobos, thickness=0.01, color=color.white)
De=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Deimos, thickness=0.005, color=color.white)
Ju=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Jupiter, thickness=0.3, color=color.orange)
Sa=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Saturn, thickness=0.3, color=color.yellow)
Ur=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Uranus, thickness=0.3, color=color.cyan)
Ne=ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=R_Neptune, thickness=0.3, color=color.blue)

##Calculando as velocidades angulares da órbita de cada planeta;
w_Mercury = w(R_Mercury)
w_Venus = w(R_Venus)
w_Earth = w(R_Earth)
w_Mars = w(R_Mars)
w_Jupiter = w(R_Jupiter)
w_Saturn = w(R_Saturn)
w_Uranus = w(R_Uranus)
w_Neptune = w(R_Neptune)

##Velocidade Angular das luas podem ser deduzidos por
##w=2π/Τ, onde T=2πR(R^(1/2))/((G * Mt)^(1/2))
T_Moon=27.32#dias
w_Moon=2*np.pi/T_Moon
T_Fobos=0.31875 #dias
w_Fobos=2*np.pi/T_Fobos
T_Deimos=1.25
w_Deimos=2*np.pi/T_Deimos

##Velocidade angular de rotação dos corpos
w_rot_Mercury = w_rot(58.646)
w_rot_Venus = -w_rot(243) #Venus rotates retrograde(east to west)
w_rot_Earth = w_rot(1)
w_rot_Mars = w_rot(0.996)
w_rot_Jupiter = w_rot(0.41)
w_rot_Saturn = w_rot(0.44)
w_rot_Uranus = w_rot(0.72)
w_rot_Neptune = w_rot(0.67)
w_rot_Moon = w_rot(27.32)
w_rot_Sun = w_rot(27)

#Slider para mudar a velocidades
scene.caption = "Vary the speed: \n 0.01x                            10x\n"
def setspeed(s):
  wt.text = '{:1.2f}'.format(s.value)
sl = slider(min=0.01, max=10, value=1, length=220, bind=setspeed)
wt = wtext(text='{:1.2f}'.format(sl.value))

#Menu para mudar o foco da câmera
autocenter = False
scene.center = vector(0,0,0)
def cammenu(x):
  print (x.selected)
  print (x.index)
scene.append_to_caption('       Cam focus:')
cam = menu(bind=cammenu, choices=['Sun','Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])
cam.index=0

#Movimentação dos corpos (a simulação meio que se resume em um grande while)
t = 0
passo = 0.01  # dia

while True:
  dt=sl.value*passo
  rate(30000)
  #Escolhendo o foco da câmera
  cam_choice=[Sun.pos, Mercury.pos, Venus.pos, Earth.pos, Mars.pos, Jupiter.pos, Saturn.pos, Uranus.pos, Neptune.pos]
  scene.center = cam_choice[cam.index]
  ##Sun
  Sun.rotate(angle=w_rot_Sun * dt, axis=rot_Sun)
  ##Mercury
  Mercury.pos = pos(R_Mercury, w_Mercury, t)
  Mercury.rotate(angle=w_rot_Mercury*dt, axis=rot_Mercury)
  ##Venus
  Venus.pos = pos(R_Venus, w_Venus, t)
  Venus.rotate(angle=w_rot_Venus*dt, axis=rot_Venus)
  ##Earth
  Earth.pos = pos(R_Earth, w_Earth, t)
  Earth.rotate(angle=w_rot_Earth*dt, axis=rot_Earth)
  ##Moon
  Moon.pos = pos(R_Moon, w_Moon, t) + Earth.pos
  Moon.rotate(angle=w_rot_Moon*dt, axis=vector(0,1,0))
  Mo.pos = pos(R_Earth, w_Earth, t)
  ##Mars
  Mars.pos = pos(R_Mars, w_Mars, t)
  Mars.rotate(angle=w_rot_Mars*dt, axis=rot_Mars)
  ##Fobos
  Fobos.pos = pos(R_Fobos, w_Fobos, t) + Mars.pos
  Fo.pos = pos(R_Mars, w_Mars, t)
  ##Deimos
  Deimos.pos = pos(R_Deimos, w_Deimos, t) + Mars.pos
  De.pos = pos(R_Mars, w_Mars, t)
  ##Jupiter
  Jupiter.pos = Jupiter_ring.pos = pos(R_Jupiter, w_Jupiter, t)
  Jupiter.rotate(angle=w_rot_Jupiter*dt, axis=rot_Jupiter)
  ##Saturn
  Saturn.pos = Saturn_ring.pos = pos(R_Saturn, w_Saturn, t)
  Saturn.rotate(angle=w_rot_Saturn*dt, axis=rot_Saturn)
  ##Uranus
  Uranus.pos = Uranus_ring.pos = pos(R_Uranus, w_Uranus, t)
  Uranus.rotate(angle=w_rot_Uranus*dt, axis=rot_Uranus)
  ##Neptune
  Neptune.pos = Neptune_ring.pos = pos(R_Neptune, w_Neptune, t)
  Neptune.rotate(angle=w_rot_Neptune*dt, axis=rot_Neptune)

  t = t + dt