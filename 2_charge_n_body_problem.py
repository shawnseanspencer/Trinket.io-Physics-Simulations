"""
NOTE: TO BE RUN IN TRINKET.IO ONLY. DOES NOT WORK OTHERWISE (I HAVE TRIED). 
"""

from vpython import *
scene = canvas()

k = 9e9 #Nm^2/C^2
q0 = 1e-6 #C
m = 0.01 #kg
R = 0.2 #m
t = 0 #s
dt = 0.00001 #s

n = 0
m = 0
qs = []

"""
Interesting Starting Configurations:

Closely packed for a while
[0.0630258, 0.140156, 0]
[0.13988, 0.0321996, 0]
[-0.0279815, -0.129536, 0]
[Negative, Positive, Negative]

Draw a Wavefunction
[0.0231054, 0.168656, 0] 
[0.0869021, -0.123165, 0] 
[-0.0507241, -0.121592, 0] 
[Positive, Negative, Negative]

[0.0133694, 0.15555, 0]
[ -0.0420202, -8.75812e-3, 0]
[ 0.0252095, -0.143925, 0]
[Negative, Positive, Negative]

Fast helix spiral
[ -0.0588875, 0.131621, 0 ]
[ -0.110597, -0.116282, 0 ]
[ -0.118817, -0.0283689, 0 ]
[Positive, Negative, Positive]

tries and fails steal your girl
[ 0.0218972, -0.0736916, 0 ]
[ -0.0392993, 0.0895526, 0 ]
[ 0.031588, 0.0835304, 0 ]
[Positive, Negative, Positive]

tries to steal your girl v2
[ -0.0714905, 0.181817, 0 ]
[ 0.180104, -0.0455606, 0 ]
[ 0.175737, 0.037184, 0 ]
[Negative, Negative, Positive]

wishy washy
[ -0.104081, 0.01285, 0 ]
[ 0.101868, 0.16961, 0 ]
[ -0.150881, -0.152969, 0 ] 
[Negative, Negative, Positive]

slowwwwww then FAST
[ -0.112771, -0.127642, 0 ]
[ 0.0680241, 0.144069, 0 ]
[ 0.0484932, 0.13644, 0 ]
[Negative, Positive, Negative]

slow and meandering
[-0.12894029585064024, -0.09144188879240325, 0]
[0.12414935370093305, -0.06014605396237896, 0]
[-0.18712531946938862, 0.08187469949096321, 0]
['Positive', 'Positive', 'Negative']

"""



def particle_amounts(evt):
    console.log(evt)
    if evt.id is "neg_particles":
      neg_particles = evt.value
    elif evt.id is "pos_particles":
      pos_particles = evt.value

pos_slider = slider(
    bind = particle_amounts,
    max = 10,
    min = 0,
    step=1,
    value = 2,
    id = "pos_particles",
    length = 275
)
neg_slider = slider(
    bind = particle_amounts,
    max = 10,
    min = 0,
    step=1,
    value = 1,
    id = "neg_particles",
    length = 275
)

random_positions_var = True
def random_positions(evt):
    global random_positions_var
    random_positions_var = not random_positions_var
    if random_positions_var: evt.text = "Not Random"
    else: evt.text = "Random Positiong"
        

random_button = button(
    bind = random_positions,
    text = "Not Random",
    pos = scene.title_anchor,
)

running = False

def run(b):
    global running
    running = not running
    if running: b.text = "Stop"
    else: b.text = "Run"
    
run_button = button(
    text = "Run",   
    pos = scene.title_anchor,
    bind = run,
    disabled = True
)

place_particles = False

def particle_placer(b):
    global place_particles
    place_particles = not place_particles
    if place_particles: b.text = "Place Particles"
    else: b.text = "Particles Placed"
    
place_particles_button = button(
    text = "Place Particles",   
    pos = scene.title_anchor,
    bind = particle_placer,
)

temp = 0
dtemp = 0.01
while temp < 1000:
  rate(24)
  if place_particles:
      place_particles_button.disabled = True
      run_button.disabled = False
      neg_particles = neg_slider.value
      pos_particles = pos_slider.value
      
      #Random Particle Positions
      if random_positions_var:
          while n < pos_particles:
              rt = R*vector(2*random()-1,2*random()-1,0)
              new_particle = sphere(
                  pos=rt, 
                  radius = R/20, 
                  make_trail=True,
                  q = q0
              )
              new_particle.color = color.red
              qs.append(new_particle)
              n += 1
          
          while m < neg_particles:
              rt = R*vector(2*random()-1,2*random()-1,0)
              new_particle = sphere(
                  pos=rt, 
                  radius = R/20, 
                  make_trail=True,
                  q = -q0
              )
              new_particle.color = color.cyan
              qs.append(new_particle)
              m += 1
        
      else:
          #Defaulted to the "tries to steal your girl" set of points 
          pos_particle_positions_matrix = [
          [ 0.0218972, -0.0736916, 0 ],
          [ 0.031588, 0.0835304, 0 ]
          ]
          neg_particle_positions_matrix = [
          [ -0.0392993, 0.0895526, 0 ],
          ]
          
          pos_vector_matrix = []
          neg_vector_matrix = []
          for i in range(len(pos_particle_positions_matrix)):
              pos_vector_matrix += vector(
                  pos_particle_positions_matrix[i][0],
                  pos_particle_positions_matrix[i][1],
                  pos_particle_positions_matrix[i][2]
              )
          for i in range(len(neg_particle_positions_matrix)):
              neg_vector_matrix += vector(
                  neg_particle_positions_matrix[i][0],
                  neg_particle_positions_matrix[i][1],
                  neg_particle_positions_matrix[i][2]
              )
          while n < len(pos_vector_matrix):
              rt = pos_vector_matrix[n]
              print(rt)
              new_particle = sphere(
                  pos = rt, 
                  radius = R/20, 
                  make_trail=True,
                  q = q0
              )
              new_particle.color = color.red
              qs.append(new_particle)
              n += 1
          while m < len(neg_vector_matrix):
              rt = neg_vector_matrix[m]
              print(rt)
              new_particle = sphere(
                  pos = rt, 
                  radius = R/20, 
                  make_trail=True,
                  q = -q0
              )
              new_particle.color = color.cyan
              qs.append(new_particle)
              m += 1
          
          
      if running:
         break
  temp += dtemp
  
charges = []
for q in qs:
    if q.q > 0:
        charge = "Positive"
    else:
        charge = "Negative"
    q.m = m
    q.p = q.m * vector(0,0,0)
    q.F = vector(0,0,0)
    
    print(f"[{q.pos.x}, {q.pos.y}, {q.pos.z}]")
    charges.append(charge)
    
print(charges)
while True:
  rate(100)
  if running:
    break


while t < 1000:
    rate(100000)
    if running:
        for i in range(len(qs)):
            qs[i].F = vector(0,0,0)
            for j in range(len(qs)):
                if i != j:
                    rt = qs[j].pos - qs[i].pos
                    if rt.mag < 1e-2:
                      qs[i].F = vector(0,0,0)
                      continue
                    qs[i].F += -k * qs[i].q*qs[j].q*norm(rt)/(mag(rt)**2)
        for q in qs:
            q.p += q.F * dt
            q.pos += q.p/q.m * dt
        
        t += dt
