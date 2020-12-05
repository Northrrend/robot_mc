import mcpi.minecraft as minecraft
import mcpi.block as block


server = 'mc.xjqpro.com'
me = 'your ID'
mc = minecraft.Minecraft.create(server)

mc.postToChat('Create a ball')
my_id = mc.getPlayerEntityId(me)
my_tilepos = mc.entity.getTilePos(my_id)
x = int(my_tilepos.x)
y = int(my_tilepos.y)
z = int(my_tilepos.z)
r=10
x_int = x - r
z_int = z + 2*r + 5
y_int = 0
x_c = x
y_c = r
z_c = z + r + 5
for i in range(r*2):
    for j in range(r*2):
        for k in range(r*2):
            if ((x_int+k - x_c)**2 + (y_int+i - y_c)**2 + (z_int-j - z_c)**2) <= r**2:
                mc.setBlock(x_int+k, y_int+i, z_int+j, block.Block(1))
