import mcpi.minecraft as minecraft
import mcpi.block as block


server = 'mc.xjqpro.com'
me = 'your ID'
mc = minecraft.Minecraft.create(server)

my_id = mc.getPlayerEntityId(me)
my_tilepos = mc.entity.getTilePos(my_id)
x = int(my_tilepos.x)
y = int(my_tilepos.y)
z = int(my_tilepos.z)
r = n*2 + 1
x_int = x + r
z_int = z + r
for i in range(n):
    l = 2*(n-i) + 1
    for j in range(l):
        for k in range(l):
            mc.setBlock(x_int-k-i, y + i, z_int-j-i, block.Block(24))