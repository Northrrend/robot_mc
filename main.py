import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("192.168.199.195")
me = 'xjq'


def my_pos(name):
    my_id = mc.getPlayerEntityId(name)
    pos = mc.entity.getPos(my_id)
    print pos.x, pos.y, pos.z


def player_ls():
    player_list = mc.getPlayerEntityIds()
    for player in player_list:
        pos = mc.entity.getPos(player)
        print str(player) + ' at (' + str(pos.x) + ' , ' + str(pos.y) + ' , ' + str(pos.z) + ')'


def assemble(name):
    mc.postToChat('Time to classroom')
    my_id = mc.getPlayerEntityId(name)
    my_pos = mc.entity.getPos(my_id)
    player_list = mc.getPlayerEntityIds()
    i = 0
    for player in player_list:
        i += 1
        if player != my_id:
            mc.entity.setPos(player, my_pos.x+i, my_pos.y, my_pos.z+i)


def prepare(name, r):
    mc.postToChat('Clear some space for class')
    my_id = mc.getPlayerEntityId(name)
    my_tilepos = mc.entity.getTilePos(my_id)
    x = int(my_tilepos.x)
    y = int(my_tilepos.y)
    z = int(my_tilepos.z)
    x0 = x - r
    z0 = z - r
    y0 = y + 1
    x1 = x + r
    z1 = z + r
    y1 = y + 100
    mc.setBlocks(x0, y0, z0, x1, y1, z1, block.Block(0))


#AIR                 = Block(0)
#STONE               = Block(1)
#GRASS               = Block(2)
#DIRT                = Block(3)
#SAND                = Block(12)
#SANDSTONE           = Block(24)


def pyramid(name, n):
    mc.postToChat('Create a pyramid')
    my_id = mc.getPlayerEntityId(name)
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


#my_pos(me)
#player_ls()
#assemble(me)
#prepare(me, 100)
#pyramid(me, 50)
