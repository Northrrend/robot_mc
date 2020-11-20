import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("mc.xjqpro.com")
me = 'tony'

mc.postToChat('Hello World!')

my_id = mc.getPlayerEntityId('tony')
pos = mc.entity.getPos(my_id)

print pos.x, pos.y, pos.z

mc.setBlock(x, y, z, block.Block(24))
