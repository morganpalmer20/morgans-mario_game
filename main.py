@namespace
class SpriteKind:
    points = SpriteKind.create()
    monster = SpriteKind.create()
list2: List[tiles.Location] = []

def on_a_pressed():
    if bob.vy == 0:
        bob.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.points, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2)
    if bob.y < otherSprite2.y:
        info.change_score_by(3)
    else:
        info.change_life_by(-1)
        music.play(music.melody_playable(music.thump),
            music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.monster, on_on_overlap2)

monsters: Sprite = None
coin: Sprite = None
bob: Sprite = None
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111999999999999999999999999999999999999999999999
        9999999999999999999999991111111111999999999999999999999999999999999999999999999999999999999999999999999999999911111119999999999999999999999999999999999999999999
        9999999999999999999999991111111111999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111199999999999999999999999999999999999
        9999999999999999999999991111111111999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111999999999999999999999999
        9999999999999999999999991111111111999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111199999999999999999999999
        9999999999999999911111111111111111119999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111199999999999999999999999
        9999999999999999911111111111111111119999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111199999999999999999999999
        9999999999999999911111111111111111119999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111111999999999999999999999
        9999999999999999911111111111111111119999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111111999999999999999999999
        9999999999991111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111999999999999999999999
        9999999999991111111111111111111111111199999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111111999999999999999999999
        9999999999991111111111111111111111111199999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111111999999999999999999999
        9999999999991111111111111111111111111199999999999999999999999999999999999999999999999999999999999999991111111111111111111111111999999999999999999999999999999999
        9999999999991111111111111111111111111199999999999999999999999999999999999999999999999999999999999999991111111111111111111111111999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999991111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999991111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999911111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999991111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999991111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999911111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999911111111111111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999991111111111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111199999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911199999111111111111119999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111119999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111199999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111199999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111111119999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111111111119999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111111111119999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999911111111111111111111111111111119999999
        9999999999999999999999999911111199999999999999999999999999999999999999999999999111111111999999999999999999999999999999999911111111111111111111111111111119999999
        9999999999999999999999999111111199999999999999999999999999999999999999999999999111111111199999999999999999999999999999999911111111111111111111111111111119999999
        9999999999999999999999911111111199999999999999999999999999999999999999999911111111111111199999999999999999999999999999999911111111111111111111111111111119999999
        9999999999999999999991111111111111119999999999999999999999999999999999999111111111111111199999999999999999999999999999999999111111111111111111111111111119999999
        9999999999999999999991111111111111119999999999999999999999999999999999911111111111111111199999999999999999999999999999999999111111111111111111111111111119999999
        9999999999999999999911111111111111119999999999999999999999999999999999111111111111111111199999999999999999999999999999999999111111111111111111111111111119999999
        9999999999999999999111111111111111111999999999999999999999999999999911111111111111111111119999999999999999999999999999999999111111111111111111111111111119999999
        9999999999999999999111111111111111111199999999999999999999999999999911111111111111111111119999999999999999999999999999999999999999111111111111111111999999999999
        9999999999999999999111111111111111111119999999999999999999999999999111111111111111111111119999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111999999999999999999999999999111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111999999999999999999999999999111111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111999999999999999999999999999111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111111199999999999999999999999111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111111199999999999999999999999111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111111199999999999999999999999111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111111199999999999999999999999111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999991111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111199999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111199999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111199999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111119999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111199999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111199999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111119999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111199999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111119999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111111111999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999999999999999
        9999999999999999999999999999999999999999999911111111199999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999999999999999
        9999999999999999999999999999999999999999999111111111199999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999999999999999
        9999999999999999999999999999999999999999911111111111199999999999999999999999999999999999999999999999999999111111111111111111111111111111111119999999999999999999
        9999999999999999999999999999999999999999911111111111111111999999999999999999999999999999999999999999999999999111111111111111111111111111111119999999999999999999
        9999999999999999999999999999999999999999911111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999911111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999991111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999911111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999111111111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999111111111111111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999111111111111111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999111111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999111111111111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999991111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""))
bob = sprites.create(img("""
        . . . . . . . . . b 5 b . . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 b c 5 5 d 4 c . . 
            . b b b b 5 5 5 b f d d 4 4 4 b 
            . b d 5 b 5 5 b c b 4 4 4 4 b . 
            . . b 5 5 b 5 5 5 4 4 4 4 b . . 
            . . b d 5 5 b 5 5 5 5 5 5 b . . 
            . b d b 5 5 5 d 5 5 5 5 5 5 b . 
            b d d c d 5 5 b 5 5 5 5 5 5 b . 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(bob, 100, 100)
bob.set_position(10, 75)
info.set_life(3)
scene.camera_follow_sprite(bob)
bob.ay = 350
for value in sprites.all_of_kind(SpriteKind.monster):
    sprites.destroy(value)
for value2 in sprites.all_of_kind(SpriteKind.points):
    sprites.destroy(value2)
for value3 in tiles.get_tiles_by_type(assets.tile("""
    myTile0_enemys
""")):
    coin = sprites.create(img("""
            . . b b b b . . 
                    . b 5 5 5 5 b . 
                    b 5 d 3 3 d 5 b 
                    b 5 3 5 5 1 5 b 
                    c 5 3 5 5 1 d c 
                    c d d 1 1 d d c 
                    . f d d d d f . 
                    . . f f f f . .
        """),
        SpriteKind.points)
    for value4 in list2:
        tiles.place_on_tile(coin, value4)
        tiles.set_tile_at(value4, assets.tile("""
            transparency16
        """))
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        myTile0enemysfr
    """)):
        monsters = sprites.create(assets.image("""
            shark
        """), SpriteKind.monster)
        tiles.set_tile_at(value5, assets.tile("""
            transparency16
        """))
        tiles.place_on_tile(monsters, value5)