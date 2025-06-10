namespace SpriteKind {
    export const heal = SpriteKind.create()
    export const statue = SpriteKind.create()
    export const enemyimage = SpriteKind.create()
    export const deleteimage = SpriteKind.create()
    export const boss = SpriteKind.create()
}
browserEvents.Equals.onEvent(browserEvents.KeyEvent.Pressed, function () {
	
})
function Normalise (sender: Sprite, targetX: number, targetY: number, desiredVelo: number, ifX: boolean) {
    if (ifX) {
        return (targetX - sender.x) / Math.sqrt((targetX - sender.x) ** 2 + (targetY - sender.y) ** 2) * desiredVelo
    } else {
        return (targetY - sender.y) / Math.sqrt((targetX - sender.x) ** 2 + (targetY - sender.y) ** 2) * desiredVelo
    }
}
sprites.onDestroyed(SpriteKind.Projectile, function (sprite4) {
    projectMax.value += 1
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite8, otherSprite) {
    sprites.destroy(otherSprite)
    if (playerClass != 1 && playerClass != 2) {
        sprites.destroy(sprite8)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile4`, function (sprite, location) {
    toriel_create(2)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite6, location4) {
    createValidRoom("fromUp", sprite6.x, scene.screenHeight() - 24)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.statue, function (sprite9, otherSprite2) {
    timer.throttle("action", 500, function () {
        if (otherSprite2.image.equals(lisOfClasses[0])) {
            if (game.ask("do you wish to acquire", "the ways of magic?")) {
                blockSettings.writeNumberArray(savechoice, [
                15,
                0,
                4,
                4,
                0,
                player_hitbox.x,
                player_hitbox.y,
                50,
                1,
                50,
                0
                ])
                toriel_create(3)
            }
        } else if (otherSprite2.image.equals(lisOfClasses[1])) {
            if (game.ask("do you wish to acquire", "the ways of thievery?")) {
                blockSettings.writeNumberArray(savechoice, [
                15,
                1,
                4,
                4,
                0,
                player_hitbox.x,
                player_hitbox.y,
                70,
                1,
                75,
                0
                ])
                toriel_create(3)
            }
        } else if (otherSprite2.image.equals(lisOfClasses[2])) {
            if (game.ask("do you wish to acquire", "the ways of honor?")) {
                blockSettings.writeNumberArray(savechoice, [
                15,
                2,
                6,
                6,
                0,
                player_hitbox.x,
                player_hitbox.y,
                40,
                1,
                90,
                0
                ])
                toriel_create(3)
            }
        } else if (otherSprite2.image.equals(lisOfClasses[3])) {
            if (game.ask("do you wish to acquire", "the ways of archery?")) {
                blockSettings.writeNumberArray(savechoice, [
                15,
                3,
                5,
                5,
                0,
                player_hitbox.x,
                player_hitbox.y,
                60,
                1,
                75,
                0
                ])
                toriel_create(3)
            }
        } else {
            BossFightStart()
        }
    })
})
sprites.onOverlap(SpriteKind.enemyimage, SpriteKind.deleteimage, function (sprite2, otherSprite3) {
    sprites.destroy(otherSprite3)
    sprites.destroy(sprite2)
})
function toriel_create (phase: number) {
    if (1 == phase) {
        tiles.setCurrentTilemap(tilemap`level1`)
        player_hitbox = sprites.create(assets.image`player`, SpriteKind.Player)
        tiles.placeOnRandomTile(player_hitbox, sprites.dungeon.collectibleBlueCrystal)
        game.showLongText("A long time ago, a terrible demon trapped you in an infinite maze.", DialogLayout.Bottom)
        animation.runImageAnimation(
        player_hitbox,
        assets.animation`torielAwaken`,
        250,
        false
        )
        pause(2250)
        controller.moveSprite(player_hitbox, 50, 50)
        notcreatingroom = true
    } else if (2 == phase && notcreatingroom) {
        notcreatingroom = false
        tiles.placeOnTile(player_hitbox, tiles.getTileLocation(1, 1))
        controller.moveSprite(player_hitbox, 0, 0)
        tiles.setCurrentTilemap(tilemap`level`)
        mySprite = sprites.create(assets.image`mage`, SpriteKind.statue)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(3, 2))
        mySprite.y += -4
        mySprite1 = sprites.create(assets.image`rouge`, SpriteKind.statue)
        tiles.placeOnTile(mySprite1, tiles.getTileLocation(6, 4))
        mySprite1.y += -4
        mySprite = sprites.create(assets.image`knight`, SpriteKind.statue)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(3, 4))
        mySprite.y += -4
        mySprite = sprites.create(assets.image`archer`, SpriteKind.statue)
        tiles.placeOnTile(mySprite, tiles.getTileLocation(6, 2))
        mySprite.y += -4
        controller.moveSprite(player_hitbox, 50, 50)
        notcreatingroom = true
    } else if (3 == phase) {
        currentprojeclist = scaling.createRotations(listofprojec[blockSettings.readNumberArray(savechoice)[1]], 360)
sprites.destroyAllSpritesOfKind(SpriteKind.statue, effects.disintegrate, 500)
        scene.cameraShake(4, 1000)
        sprites.destroy(player_hitbox)
        player_create()
        unlockDoors()
        controller.moveSprite(player_hitbox, 0, 0)
        story.printCharacterText("Goodluck.", "Mysterious Voice")
        controller.moveSprite(player_hitbox, moverSpeed, moverSpeed)
    } else {
        guide = sprites.create(assets.image`theGuide`, SpriteKind.statue)
        guide.y += -8
    }
}
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    if (player_alive) {
        if (100 == roomscleard) {
            story.printCharacterText("...", "Mysterious Voice")
        } else {
            prexp = EXP
            controller.moveSprite(player_hitbox, 0, 0)
            story.printCharacterText("It would seem you have " + EXP + " \"Exp\".", "Mysterious Voice")
            story.printCharacterText("What do you wish to upgrade?", "Mysterious Voice")
            story.showPlayerChoices("I wish to be swifter", "I wish to conjure more", "I wish to have more Vitality", "I wish my conjure to be swifter")
            if ("I wish to be swifter" == story.getLastAnswer()) {
                story.printCharacterText("One EXP per pixel per second.", "Mysterious Voice")
                request_upgrades = Math.trunc(game.askForNumber("How faster do you wish to be?", 3))
                if (request_upgrades >= 0 && request_upgrades <= EXP) {
                    EXP += request_upgrades * -1
                    moverSpeed += request_upgrades
                }
            } else if ("I wish to conjure more" == story.getLastAnswer()) {
                story.printCharacterText("Twenty EXP per extra projectile.", "Mysterious Voice")
                request_upgrades = Math.trunc(game.askForNumber("how many extra projectiles do you wish for?", 3)) * 20
                if (request_upgrades >= 0 && request_upgrades <= EXP) {
                    EXP += request_upgrades * -1
                    projectMax.max += request_upgrades / 20
                    projectMax.value += request_upgrades / 20
                }
            } else if ("I wish to have more Vitality" == story.getLastAnswer()) {
                story.printCharacterText("Five EXP per HP.", "Mysterious Voice")
                request_upgrades = Math.trunc(game.askForNumber("How much HP do you wish for?", 3)) * 5
                if (request_upgrades >= 0 && request_upgrades <= EXP) {
                    EXP += request_upgrades * -1
                    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).max += request_upgrades / 5
                    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).value += request_upgrades / 5
                }
            } else if ("I wish my conjure to be swifter" == story.getLastAnswer()) {
                story.printCharacterText("One EXP per pixel per second.", "Mysterious Voice")
                request_upgrades = Math.trunc(game.askForNumber("How swift would you like your conjure?", 3))
                if (request_upgrades >= 0 && request_upgrades <= EXP) {
                    EXP += request_upgrades * -1
                    projectilespeed += request_upgrades
                }
            }
            if (request_upgrades > prexp) {
                story.printCharacterText("Due to the current EXP shortage in the market, i cannot accept loans", "Mysterious Voice")
            } else if (request_upgrades <= 0) {
                story.printCharacterText("As you have entered an invalid amount, your account has not been charged.", "Mysterious Voice")
            } else {
                story.printCharacterText("Your remaining balance is " + EXP + " \"Exp\".", "Mysterious Voice")
            }
            controller.moveSprite(player_hitbox, moverSpeed, moverSpeed)
        }
    } else if (game.ask("clear all settings?")) {
        blockSettings.clear()
    }
})
function BossFightStart () {
    player_hitbox.setPosition(20, scene.screenHeight() / 2)
    controller.moveSprite(player_hitbox, 0, 0)
    story.printCharacterText("...", "???")
    guide.setImage(img`
        . . . . . . . . . . . . . . . . 
        . . . . 2 2 2 2 2 . . . . . . . 
        . . . 2 2 2 2 2 2 2 2 . . . . . 
        . . . 5 5 5 2 2 2 2 2 . . . . . 
        . . . 4 4 4 5 2 2 2 2 2 . . . . 
        . . . 4 f f 4 5 2 2 2 2 . . . . 
        . . . 4 f f 4 5 2 2 2 2 . . . . 
        . . . 4 4 f 4 5 2 2 2 2 . . . . 
        . . . 4 4 4 4 5 2 2 2 2 2 . . . 
        . . . . 4 4 f 5 2 2 2 2 2 . . . 
        . . . . f f 4 5 2 2 2 2 2 . . . 
        . . . . 4 4 4 5 2 2 2 2 2 2 . . 
        . . . . 4 4 4 2 2 2 2 2 2 2 2 . 
        . 2 2 2 4 4 4 2 2 2 2 2 2 2 2 2 
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
        `)
    story.printCharacterText("=)", "THE DEMON KING")
    color.FadeToWhite.startScreenEffect(1000)
    scene.cameraShake(5, 1000)
    color.pauseUntilFadeDone()
    guide.setKind(SpriteKind.boss)
    tiles.setCurrentTilemap(tilemap`room0`)
    guide.setImage(assets.image`finalboss`)
    guide.setPosition(scene.cameraProperty(CameraProperty.X), scene.cameraProperty(CameraProperty.Y))
    color.startFadeFromCurrent(color.originalPalette, 500)
}
browserEvents.onMouseMove(function (x2, y2) {
    mouseX = x2
    mouseY = y2
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite5) {
    mySprite5 = sprites.create(img`
        2 
        `, SpriteKind.deleteimage)
    mySprite5.setPosition(sprite5.x, sprite5.y)
    mySprite5.lifespan = 100
    if (sprites.allOfKind(SpriteKind.Enemy).length == 0) {
        unlockDoors()
    }
})
function unlockDoors () {
    for (let value of tiles.getTilesByType(assets.tile`myTile`)) {
        tiles.setWallAt(value, false)
    }
    for (let value2 of tiles.getTilesByType(assets.tile`myTile0`)) {
        tiles.setWallAt(value2, false)
    }
    for (let value3 of tiles.getTilesByType(assets.tile`myTile1`)) {
        tiles.setWallAt(value3, false)
    }
    for (let value4 of tiles.getTilesByType(assets.tile`myTile2`)) {
        tiles.setWallAt(value4, false)
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite22, location2) {
    createValidRoom("fromLeft", scene.screenWidth() - 24, sprite22.y)
})
browserEvents.MouseLeft.onEvent(browserEvents.MouseButtonEvent.Pressed, function (x, y) {
    if (player_alive) {
        if (projectMax.value > 0) {
            projectMax.value += -1
            angle = Math.round(spriteutils.radiansToDegrees(spriteutils.angleFrom(player_image, spriteutils.pos(x, y))))
            if (angle < 0) {
                angle += 360
            }
            if (playerClass == 2) {
                playershot = sprites.createProjectileFromSprite(assets.image`empty`, player_image, 0, 0)
                sprites.setDataNumber(playershot, "swordindex", 0)
                sprites.setDataNumber(playershot, "orgin", angle)
                sprites.setDataNumber(playershot, "Xoffset", Normalise(player_image, x, y, 10, true))
                sprites.setDataNumber(playershot, "Yoffset", Normalise(player_image, x, y, 10, false))
                playershot.lifespan = projectilespeed * 10
            } else {
                playershot = sprites.createProjectileFromSprite(currentprojeclist[angle], player_image, Normalise(player_image, x, y, projectilespeed, true), Normalise(player_image, x, y, projectilespeed, false))
                if (playerClass == 1) {
                    playershot.vy += player_hitbox.vy
                    playershot.vx += player_hitbox.vx
                    playershot.lifespan = 15 / (projectilespeed / 1000)
                }
            }
            playershot.setFlag(SpriteFlag.AutoDestroy, true)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite7, location5) {
    createValidRoom("fromRight", 24, sprite7.y)
})
function loadSaves () {
    scene.setBackgroundImage(assets.image`menuSprite`)
    tiles.setCurrentTilemap(tilemap`level14`)
    savechoice = "Save " + game.askForNumber("Which save would you like to load?", 2)
    if (blockSettings.exists(savechoice)) {
        game.showLongText("" + savechoice + " is a room " + ("" + blockSettings.readNumberArray(savechoice)[4]) + classnames[blockSettings.readNumberArray(savechoice)[1]], DialogLayout.Full)
        story.showPlayerChoices("Load " + savechoice, "Erase " + savechoice, "Back")
        if (story.checkLastAnswer("Load " + savechoice)) {
            currentprojeclist = scaling.createRotations(listofprojec[blockSettings.readNumberArray(savechoice)[1]], 360)
player_create()
        } else if (story.checkLastAnswer("Erase " + savechoice)) {
            blockSettings.remove(savechoice)
            blockSettings.remove("" + savechoice + " Ex")
            blockSettings.remove("" + savechoice + " Ey")
            loadSaves()
        } else {
            loadSaves()
        }
    } else {
        if (game.ask("This save is empty", "Make a new one?.")) {
            toriel_create(1)
        } else {
            loadSaves()
        }
    }
}
statusbars.onZero(StatusBarKind.Health, function (status) {
    player_alive = false
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
    sprites.destroyAllSpritesOfKind(SpriteKind.Food, effects.disintegrate, 2000)
    pause(1000)
    blockSettings.remove(savechoice)
    blockSettings.remove("" + savechoice + " Ex")
    blockSettings.remove("" + savechoice + " Ey")
    story.printCharacterText("Ah...", "Mysterious Voice")
    story.printCharacterText("It seems your vessel has shattered...", "Mysterious Voice")
    game.splash(roomscleard)
    story.printCharacterText("Rest now, but do not give up!", "Mysterious Voice")
    loadSaves()
})
function createValidRoom (enteredFrom: string, locationX: number, locationY: number) {
    timer.throttle("action", 500, function () {
        player_hitbox.setPosition(scene.screenWidth() / 2, scene.screenHeight() / 2)
        if (notcreatingroom) {
            notcreatingroom = false
            if (roomscleard + 1 == 100) {
                if (!(game.ask("Mysterious Voice", "The fina| room 1ies ahead"))) {
                    notcreatingroom = true
                    return
                }
            }
            if (statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).value < statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).max) {
                statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).value += 1
            }
            roomscleard += 1
            if (roomscleard == 50) {
                EXP += 21
                room = 15
            } else if (roomscleard == 100) {
                room = 4
            } else if (roomscleard == 99) {
                EXP += 2
                if ("fromLeft" == enteredFrom) {
                    room = 1
                } else if ("fromDown" == enteredFrom) {
                    room = 3
                } else if ("fromRight" == enteredFrom) {
                    room = 5
                } else if ("fromUp" == enteredFrom) {
                    room = 9
                }
            } else {
                EXP += 1
                room = blockSettings.readNumberArray(enteredFrom)[randint(0, 7)]
                if (15 == room && Math.percentChance(25)) {
                    room = 16
                }
            }
            blockSettings.writeNumberArray(savechoice, [
            room,
            playerClass,
            statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).max,
            statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).value,
            roomscleard,
            locationX,
            locationY,
            moverSpeed,
            projectMax.max,
            projectilespeed,
            EXP
            ])
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
            sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
            sprites.destroyAllSpritesOfKind(SpriteKind.StatusBar)
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
            sprites.destroyAllSpritesOfKind(SpriteKind.Food)
            for (let index = 0; index < Math.round(roomscleard / 4); index++) {
                mySprite3 = sprites.create(assets.image`enemyHitbox`, SpriteKind.Enemy)
                mySprite3.setPosition(locationX, locationY)
                while (spriteutils.distanceBetween(mySprite3, spriteutils.pos(locationX, locationY)) <= 40) {
                    mySprite3.setPosition(randint(20, scene.screenWidth() - 20), randint(24, scene.screenHeight() - 24))
                }
            }
            list2 = []
            for (let value5 of sprites.allOfKind(SpriteKind.Enemy)) {
                list2.push(value5.x)
            }
            blockSettings.writeNumberArray("" + savechoice + " Ex", list2)
            list2 = []
            for (let value6 of sprites.allOfKind(SpriteKind.Enemy)) {
                list2.push(value6.y)
            }
            blockSettings.writeNumberArray("" + savechoice + " Ey", list2)
            sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
            player_create()
        }
    })
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite82, otherSprite4) {
    sprites.destroy(otherSprite4)
    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, player_hitbox).value += -1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite3, location3) {
    createValidRoom("fromDown", sprite3.x, 24)
})
function player_create () {
    let index4: number;
room = blockSettings.readNumberArray(savechoice)[0]
    tiles.setCurrentTilemap(listOfRooms[room])
    playerClass = blockSettings.readNumberArray(savechoice)[1]
    player_hitbox = sprites.create(img`
        . . a a a a a a . . 
        . a a c c c c a a . 
        a a c c c c c c a a 
        a c c c c c c c c a 
        a c c c c c c c c a 
        a c c c c c c c c a 
        a c c c c c c c c a 
        a a c c c c c c a a 
        . a a c c c c a a . 
        . . a a a a a a . . 
        `, SpriteKind.Player)
    roomscleard = blockSettings.readNumberArray(savechoice)[4]
    player_hitbox.setPosition(blockSettings.readNumberArray(savechoice)[5], blockSettings.readNumberArray(savechoice)[6])
    for (let index2 = 0; index2 <= 9; index2++) {
        tiles.setWallAt(tiles.getTileLocation(index2, 0), true)
        tiles.setWallAt(tiles.getTileLocation(index2, 6), true)
    }
    for (let index3 = 0; index3 <= 6; index3++) {
        tiles.setWallAt(tiles.getTileLocation(0, index3), true)
        tiles.setWallAt(tiles.getTileLocation(9, index3), true)
    }
    if (blockSettings.exists("" + savechoice + " Ex") && blockSettings.exists("" + savechoice + " Ey") && 0 < blockSettings.readNumberArray("" + savechoice + " Ex").length) {
        if (roomscleard == 50) {
            player_hitbox.sayText("Halfway there...", 1000, true)
            scene.cameraShake(4, 1000)
        } else if (roomscleard == 99) {
            player_hitbox.sayText("one more room...", 2000, true)
        } else if (roomscleard == 100) {
            toriel_create(4)
        } else {
            index4 = 0
            while (index4 <= blockSettings.readNumberArray("" + savechoice + " Ex").length - 1) {
                mySprite3 = sprites.create(assets.image`enemyHitbox`, SpriteKind.Enemy)
                mySprite4 = sprites.create(assets.image`enemySprite`, SpriteKind.enemyimage)
                mySprite3.setFlag(SpriteFlag.Invisible, true)
                mySprite4.setFlag(SpriteFlag.GhostThroughWalls, true)
                mySprite4.follow(mySprite3, 100)
                mySprite3.follow(player_hitbox, 40)
                mySprite4.setPosition(blockSettings.readNumberArray("" + savechoice + " Ex")[index4], blockSettings.readNumberArray("" + savechoice + " Ey")[index4])
                mySprite3.setPosition(blockSettings.readNumberArray("" + savechoice + " Ex")[index4], blockSettings.readNumberArray("" + savechoice + " Ey")[index4])
                index4 += 1
            }
        }
    }
    player_image = sprites.create(lisOfClasses[playerClass], SpriteKind.Food)
    statusbar = statusbars.create(20, 4, StatusBarKind.Health)
    statusbar.max = blockSettings.readNumberArray(savechoice)[2]
    statusbar.value = blockSettings.readNumberArray(savechoice)[3]
    statusbar.attachToSprite(player_hitbox, 10, 0)
    moverSpeed = blockSettings.readNumberArray(savechoice)[7]
    controller.moveSprite(player_hitbox, moverSpeed, moverSpeed)
    projectMax = statusbars.create(4, 15, StatusBarKind.Energy)
    projectMax.max = blockSettings.readNumberArray(savechoice)[8]
    projectMax.value = blockSettings.readNumberArray(savechoice)[8]
    projectMax.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    projectMax.attachToSprite(player_hitbox, 0, -7)
    projectilespeed = blockSettings.readNumberArray(savechoice)[9]
    EXP = blockSettings.readNumberArray(savechoice)[10]
    player_image.setFlag(SpriteFlag.Ghost, true)
    if (100 == roomscleard) {
    	
    } else if (99 == roomscleard) {
        for (let value7 of tiles.getTilesByType(assets.tile`myTile`)) {
            tiles.setWallAt(value7, false)
        }
    } else if (sprites.allOfKind(SpriteKind.Enemy).length == 0) {
        unlockDoors()
    }
    for (let value of tiles.getTilesByType(sprites.dungeon.collectibleInsignia)) {
        mySprite2 = sprites.create(assets.image`heart`, SpriteKind.heal)
        tiles.placeOnTile(mySprite2, value)
        mySprite2.y += 8
    }
    player_alive = true
    notcreatingroom = true
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.heal, function (sprite, otherSprite) {
    statusbars.getStatusBarAttachedTo(StatusBarKind.Health, sprite).value = statusbars.getStatusBarAttachedTo(StatusBarKind.Health, sprite).max
    sprite.setVelocity(0, 5000000000)
})
let swordangle = 0
let mySprite2: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite4: Sprite = null
let list2: number[] = []
let mySprite3: Sprite = null
let room = 0
let currentprojeclist: Image[] = []
let playershot: Sprite = null
let player_image: Sprite = null
let angle = 0
let mySprite5: Sprite = null
let mouseY = 0
let mouseX = 0
let projectilespeed = 0
let request_upgrades = 0
let EXP = 0
let prexp = 0
let roomscleard = 0
let guide: Sprite = null
let moverSpeed = 0
let mySprite1: Sprite = null
let mySprite: Sprite = null
let notcreatingroom = false
let player_hitbox: Sprite = null
let savechoice = ""
let playerClass = 0
let projectMax: StatusBarSprite = null
let player_alive = false
let lisOfClasses: Image[] = []
let classnames: string[] = []
let listOfRooms: tiles.TileMapData[] = []
namespace userconfig {
    export const ARCADE_SCREEN_WIDTH = 160
    export const ARCADE_SCREEN_HEIGHT = 112
}
listOfRooms = [
tilemap`room0`,
tilemap`room1`,
tilemap`room2`,
tilemap`room3`,
tilemap`room4`,
tilemap`room5`,
tilemap`room6`,
tilemap`room7`,
tilemap`room8`,
tilemap`room9`,
tilemap`room10`,
tilemap`room11`,
tilemap`room12`,
tilemap`room13`,
tilemap`room14`,
tilemap`room15`,
tilemap`healroom`
]
let listofprojec = [
img`
    . f f f f . 
    f f 1 1 f f 
    f 1 1 1 1 f 
    f 1 1 1 1 f 
    f f 1 1 f f 
    . f f f f . 
    `,
img`
    . f 1 1 1 1 . 
    f f d d d d 1 
    . f 1 1 1 1 . 
    `,
assets.image`sword`,
assets.image`arrow`
]
classnames = [
" Mage.",
" Rouge.",
" Knight.",
" Archer."
]
lisOfClasses = [
assets.image`mage`,
assets.image`rouge`,
assets.image`knight`,
assets.image`archer`,
assets.image`mage0`,
assets.image`rouge0`,
assets.image`knight0`,
assets.image`archer0`
]
player_alive = false
loadSaves()
blockSettings.writeNumberArray("fromRight", [
4,
5,
6,
7,
12,
13,
14,
15
])
blockSettings.writeNumberArray("fromUp", [
8,
9,
10,
11,
12,
13,
14,
15
])
blockSettings.writeNumberArray("fromLeft", [
1,
3,
5,
7,
9,
11,
13,
15
])
blockSettings.writeNumberArray("fromDown", [
2,
3,
6,
7,
10,
11,
14,
15
])
game.onUpdateInterval(1, function () {
    if (playerClass == 2) {
        for (let value8 of sprites.allOfKind(SpriteKind.Projectile)) {
            swordangle = Math.round(sprites.readDataNumber(value8, "orgin") + (sprites.readDataNumber(value8, "swordindex") - projectilespeed / 2))
            sprites.changeDataNumberBy(value8, "swordindex", 2)
            if (swordangle < 0) {
                swordangle += 360
            } else if (360 < swordangle) {
                swordangle += -360
            }
            value8.setImage(currentprojeclist[swordangle])
            value8.setPosition(sprites.readDataNumber(value8, "Xoffset") + player_image.x, sprites.readDataNumber(value8, "Yoffset") + player_image.y)
        }
    }
})
game.onUpdate(function () {
    if (player_alive) {
        player_image.setPosition(player_hitbox.x, player_hitbox.y - 5)
        if (0 < player_hitbox.vx) {
            player_image.setImage(lisOfClasses[playerClass])
            projectMax.setOffsetPadding(-7, 0)
        } else if (player_hitbox.vx < 0) {
            projectMax.setOffsetPadding(-7, -14)
            player_image.setImage(lisOfClasses[playerClass + 4])
        }
    }
})
