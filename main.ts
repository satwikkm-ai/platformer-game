namespace SpriteKind {
    export const coin = SpriteKind.create()
    export const flower = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.gameOver(false)
    game.setGameOverEffect(false, effects.melt)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Fire.vy == 0) {
        Fire.vy = -155
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile3`, function (sprite, location) {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.coin, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.flower, function (sprite, otherSprite) {
    bee = sprites.create(img`
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
        `, SpriteKind.Enemy)
    sprites.destroy(otherSprite)
    animation.runImageAnimation(
    bee,
    [img`
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
        `,img`
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
        `],
    100,
    true
    )
    bee.setPosition(Fire.x + 80, Fire.y - 0)
    bee.follow(Fire)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    if (Fire.y < otherSprite.y) {
        info.changeScoreBy(3)
    } else {
        info.changeLifeBy(-1)
    }
})
let bee: Sprite = null
let flower: Sprite = null
let coin: Sprite = null
let Fire: Sprite = null
scene.setBackgroundColor(9)
Fire = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    2 2 2 2 2 2 2 2 2 2 2 2 f f f f 
    f f f f f f f f f f f 2 f 4 4 f 
    f f 4 4 4 4 4 4 4 f f 2 f 2 5 f 
    f 4 4 4 4 5 4 4 4 4 f 2 f 5 2 f 
    f f 4 4 4 4 4 4 4 f f 2 f 2 5 f 
    f f f f f f f f f f f 2 f 4 4 f 
    2 2 2 2 2 2 2 2 2 2 2 2 f f f f 
    `, SpriteKind.Player)
controller.moveSprite(Fire, 100, 0)
tiles.setCurrentTilemap(tilemap`level1`)
Fire.ay = 389
scene.cameraFollowSprite(Fire)
info.setLife(5)
for (let value of tiles.getTilesByType(assets.tile`myTile6`)) {
    coin = sprites.create(img`
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
        `, SpriteKind.coin)
    animation.runImageAnimation(
    coin,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
    tiles.placeOnTile(coin, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
}
for (let value of tiles.getTilesByType(assets.tile`myTile7`)) {
    flower = sprites.create(img`
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
        `, SpriteKind.flower)
    tiles.placeOnTile(flower, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
}
