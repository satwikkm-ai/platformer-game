@namespace
class SpriteKind:
    coin = SpriteKind.create()
    flower = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.game_over(False)
    game.set_game_over_effect(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_a_pressed():
    if Fire.vy == 0:
        Fire.vy = -155
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile2)

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite2):
    global bee
    bee = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(bee,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 1 1 1 f 1 1 1 f . . . . 
                        . . . f 1 1 1 1 1 1 1 f . . . . 
                        . . . f 1 1 1 f 1 1 1 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f f 5 5 5 5 5 f f . . . . 
                        . . . f 5 5 5 f 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f f 5 5 5 5 5 f f . . . . 
                        . . . f 5 5 5 f 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.flower, on_on_overlap2)

bee: Sprite = None
flower2: Sprite = None
coin2: Sprite = None
Fire: Sprite = None
scene.set_background_color(9)
Fire = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            f f f f f f f f f f f . . . . . 
            f f 4 4 4 4 4 4 4 f f . . . . . 
            f 4 4 4 4 f 4 4 4 4 f . . . . . 
            f f 4 4 4 4 4 4 4 f f . . . . . 
            f f f f f f f f f f f . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Fire, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
Fire.ay = 389
scene.camera_follow_sprite(Fire)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile6
""")):
    coin2 = sprites.create(img("""
            . . . . f f f f f f f . . . . . 
                    . . f f 5 5 5 5 5 5 5 f f . . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    . f 5 5 5 4 4 4 4 5 5 5 5 f . . 
                    f 5 5 5 5 5 5 5 5 4 5 5 5 5 f . 
                    f 5 5 4 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 4 5 5 5 5 5 5 5 5 5 5 f . 
                    f 5 5 4 5 5 5 5 4 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 4 4 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 4 4 5 5 5 5 5 f . 
                    f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                    . f 5 5 5 4 4 5 5 5 5 5 5 f . . 
                    . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                    . . f f 5 5 5 5 5 5 5 f f . . . 
                    . . . . f f f f f f f . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.coin)
    animation.run_image_animation(coin2,
        [img("""
                . . . . f f f f f f f . . . . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        f 5 5 5 5 5 4 4 4 4 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 4 4 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 4 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 4 5 5 5 5 4 5 5 5 5 f . 
                        f 5 5 5 4 5 5 5 5 4 4 5 5 5 f . 
                        f 5 5 5 4 4 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 4 4 4 4 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 4 4 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 4 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 4 5 5 5 5 4 5 5 5 f . . 
                        . f 5 5 4 5 5 5 5 4 4 5 5 f . . 
                        . f 5 5 4 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . f f f f f f f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 4 4 4 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 4 5 5 f . . . 
                        . . f 5 5 4 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . f 5 5 4 4 4 5 5 f . . . . 
                        . . . f 5 5 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f f f f f . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . f f f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f f f . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . f f f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . f 5 4 5 f . . . . . . 
                        . . . . . f 5 4 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 4 5 f . . . . . . 
                        . . . . . f 5 4 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f f f . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . f f f . . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . . 
                        . . . . . . f f f . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . f 5 5 4 4 4 5 5 f . . . . 
                        . . . f 5 5 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . . 
                        . . . . . f f f f f . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . f f f f f f f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 4 4 4 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 4 5 5 f . . . 
                        . . f 5 5 4 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f 5 5 5 5 5 f . . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . f f f f f f f . . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . f 5 5 5 5 4 4 4 4 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 4 4 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 4 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 4 5 5 5 5 4 5 5 5 f . . 
                        . f 5 5 4 5 5 5 5 4 4 5 5 f . . 
                        . f 5 5 4 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . f f f f f f f . . . . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        f 5 5 5 5 5 4 4 4 4 5 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 4 4 5 5 5 f . 
                        f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 4 5 5 5 5 5 5 5 5 5 f . 
                        f 5 5 5 4 5 5 5 5 4 5 5 5 5 f . 
                        f 5 5 5 4 5 5 5 5 4 4 5 5 5 f . 
                        f 5 5 5 4 4 5 5 5 5 5 5 5 5 f . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 f f . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    tiles.place_on_tile(coin2, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile7
""")):
    flower2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 2 . . 2 . . . . . . . 
                    . . . . 2 2 2 2 2 2 . . . . . . 
                    . . . . . e . . e . . . . . . . 
                    . . . . . e . . e . . . . . . . 
                    . . . . a a a a a a . . . . . . 
                    . . . . 7 2 2 2 2 7 . . . . . . 
                    . . . . . 7 3 3 7 . . . . . . . 
                    . . . . . . 7 7 . . . . . . . . 
                    . . . 7 7 7 6 7 6 7 7 7 . . . . 
                    . . . . 7 7 7 7 7 7 7 . . . . . 
                    . . . . 7 7 6 7 6 7 7 . . . . . 
                    . . . . . . 7 6 7 . . . . . . . 
                    . . . . . . . 7 . . . . . . . .
        """),
        SpriteKind.flower)
    tiles.place_on_tile(flower2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))