import mcpi.minecraft as minecraft
import mcpi.block as block
import random


server = 'mc.xjqpro.com'
me = 'your ID'
mc = minecraft.Minecraft.create(server)

my_id = mc.getPlayerEntityId(me)
pos = mc.entity.getPos(my_id)
print(pos.x, pos.y, pos.z)

x = random.randint(0, 25535)
z = random.randint(0, 25535)
for y in range(0,255):
    b = mc.getBlock(x, y, z)
    if b == 0:
        break
print(x, y, z)
mc.entity.setPos(x, y, z)
