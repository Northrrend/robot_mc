import mcpi.minecraft as minecraft
import mcpi.block as block


server = 'mc.xjqpro.com'
me = 'your ID'
mc = minecraft.Minecraft.create(server)

my_id = mc.getPlayerEntityId(me)
pos = mc.entity.getPos(my_id)
print pos.x, pos.y, pos.z