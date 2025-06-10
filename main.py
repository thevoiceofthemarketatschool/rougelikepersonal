@namespace
class SpriteKind:
    eater = SpriteKind.create()
    enemyimage = SpriteKind.create()
    statuekind = SpriteKind.create()
def Normalise(sender: Sprite, targetX: number, targetY: number, desiredVelo: number, ifX: bool):
    if ifX:
        return (targetX - sender.x) / Math.sqrt((targetX - sender.x) ** 2 + (targetY - sender.y) ** 2) * desiredVelo
    else:
        return (targetY - sender.y) / Math.sqrt((targetX - sender.x) ** 2 + (targetY - sender.y) ** 2) * desiredVelo

def on_on_destroyed(sprite4):
    projectMax.value += 1
sprites.on_destroyed(SpriteKind.projectile, on_on_destroyed)

def on_on_overlap(sprite9, otherSprite2):
    
    def on_throttle():
        if otherSprite2.image.equals(lisOfClasses[0]):
            if game.ask("do you wish to acquire", "the ways of magic?"):
                blockSettings.write_number_array(savechoice,
                    [15,
                        0,
                        4,
                        4,
                        0,
                        player_hitbox.x,
                        player_hitbox.y,
                        50,
                        1,
                        50,
                        0])
                toriel_create(3)
        elif otherSprite2.image.equals(lisOfClasses[1]):
            if game.ask("do you wish to acquire", "the ways of thievery?"):
                blockSettings.write_number_array(savechoice,
                    [15,
                        1,
                        4,
                        4,
                        0,
                        player_hitbox.x,
                        player_hitbox.y,
                        70,
                        1,
                        75,
                        0])
                toriel_create(3)
        elif otherSprite2.image.equals(lisOfClasses[2]):
            if game.ask("do you wish to acquire", "the ways of honor?"):
                blockSettings.write_number_array(savechoice,
                    [15,
                        2,
                        6,
                        6,
                        0,
                        player_hitbox.x,
                        player_hitbox.y,
                        40,
                        1,
                        90,
                        0])
                toriel_create(3)
        elif otherSprite2.image.equals(lisOfClasses[3]):
            if game.ask("do you wish to acquire", "the ways of archery?"):
                blockSettings.write_number_array(savechoice,
                    [15,
                        3,
                        5,
                        5,
                        0,
                        player_hitbox.x,
                        player_hitbox.y,
                        60,
                        1,
                        75,
                        0])
                toriel_create(3)
        else:
            BossFight()
    timer.throttle("action", 500, on_throttle)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.statuekind, on_on_overlap)

def on_on_overlap2(sprite8, otherSprite):
    sprites.destroy(otherSprite)
    if playerClass != 1:
        sprites.destroy(sprite8)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_overlap_tile(sprite, location):
    toriel_create(2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite6, location4):
    createValidRoom("fromUp", sprite6.x, scene.screen_height() - 24)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    createValidRoom("fromDown", sprite3.x, 24)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
        """),
    on_overlap_tile3)

def toriel_create(phase: number):
    global player_hitbox, notcreatingroom, mySprite, mySprite1, currentprojeclist, guide
    if 1 == phase:
        tiles.set_current_tilemap(tilemap("""
            level1
            """))
        player_hitbox = sprites.create(assets.image("""
            player
            """), SpriteKind.player)
        tiles.place_on_random_tile(player_hitbox, sprites.dungeon.collectible_blue_crystal)
        story.print_character_text("A long time ago, a terrible demon trapped you in an infinite maze.",
            "Mysterious Voice")
        animation.run_image_animation(player_hitbox,
            assets.animation("""
                torielAwaken
                """),
            250,
            False)
        pause(2250)
        controller.move_sprite(player_hitbox, 50, 50)
        notcreatingroom = True
    elif 2 == phase and notcreatingroom:
        notcreatingroom = False
        tiles.place_on_tile(player_hitbox, tiles.get_tile_location(1, 1))
        controller.move_sprite(player_hitbox, 0, 0)
        tiles.set_current_tilemap(tilemap("""
            level
            """))
        mySprite = sprites.create(assets.image("""
            mage
            """), SpriteKind.statuekind)
        tiles.place_on_tile(mySprite, tiles.get_tile_location(3, 2))
        mySprite.y += -4
        mySprite1 = sprites.create(assets.image("""
            rouge
            """), SpriteKind.statuekind)
        tiles.place_on_tile(mySprite1, tiles.get_tile_location(6, 4))
        mySprite1.y += -4
        mySprite = sprites.create(assets.image("""
            knight
            """), SpriteKind.statuekind)
        tiles.place_on_tile(mySprite, tiles.get_tile_location(3, 4))
        mySprite.y += -4
        mySprite = sprites.create(assets.image("""
            archer
            """), SpriteKind.statuekind)
        tiles.place_on_tile(mySprite, tiles.get_tile_location(6, 2))
        mySprite.y += -4
        controller.move_sprite(player_hitbox, 50, 50)
        notcreatingroom = True
    elif 3 == phase:
        currentprojeclist = scaling.create_rotations(listofprojec[blockSettings.read_number_array(savechoice)[1]],
            360)
        sprites.destroy_all_sprites_of_kind(SpriteKind.statuekind, effects.disintegrate, 500)
        scene.camera_shake(4, 1000)
        sprites.destroy(player_hitbox)
        player_create()
        unlockDoors()
        controller.move_sprite(player_hitbox, 0, 0)
        story.print_character_text("Hmm...", "Mysterious Voice")
        story.print_character_text("It appears that only a fraction of it was in that statue...",
            "Mysterious Voice")
        story.print_character_text("You must defeat the demon to regain your old status.",
            "Mysterious Voice")
        story.print_character_text("Goodluck.", "Mysterious Voice")
        controller.move_sprite(player_hitbox, moverSpeed, moverSpeed)
    else:
        guide = sprites.create(assets.image("""
                theGuide
                """),
            SpriteKind.statuekind)
        guide.y += -8

def on_menu_pressed():
    global prexp, request_upgrades, EXP, moverSpeed, projectilespeed
    if player_alive:
        if 100 == roomscleard:
            story.print_character_text("...", "Mysterious Voice")
        else:
            prexp = EXP
            controller.move_sprite(player_hitbox, 0, 0)
            story.print_character_text("It would seem you have " + convert_to_text(EXP) + " \"Exp\".",
                "Mysterious Voice")
            story.print_character_text("What do you wish to upgrade?", "Mysterious Voice")
            story.show_player_choices("I wish to be swifter",
                "I wish to conjure more",
                "I wish to have more Vitality",
                "I wish my conjure to be swifter")
            if "I wish to be swifter" == story.get_last_answer():
                story.print_character_text("One EXP per pixel per second.", "Mysterious Voice")
                request_upgrades = int(game.ask_for_number("How faster do you wish to be?", 3))
                if request_upgrades >= 0 and request_upgrades <= EXP:
                    EXP += request_upgrades * -1
                    moverSpeed += request_upgrades
            elif "I wish to conjure more" == story.get_last_answer():
                story.print_character_text("Twenty EXP per extra projectile.", "Mysterious Voice")
                request_upgrades = int(game.ask_for_number("how many extra projectiles do you wish for?", 3)) * 20
                if request_upgrades >= 0 and request_upgrades <= EXP:
                    EXP += request_upgrades * -1
                    projectMax.max += request_upgrades
                    projectMax.value += request_upgrades
            elif "I wish to have more Vitality" == story.get_last_answer():
                story.print_character_text("Five EXP per HP.", "Mysterious Voice")
                request_upgrades = int(game.ask_for_number("How much HP do you wish for?", 3)) * 5
                if request_upgrades >= 0 and request_upgrades <= EXP:
                    EXP += request_upgrades * -1
                    statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).max += request_upgrades
                    statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).value += request_upgrades
            elif "I wish my conjure to be swifter" == story.get_last_answer():
                story.print_character_text("One EXP per pixel per second.", "Mysterious Voice")
                request_upgrades = int(game.ask_for_number("How swift would you like your conjure?", 3))
                if request_upgrades >= 0 and request_upgrades <= EXP:
                    EXP += request_upgrades * -1
                    projectilespeed += request_upgrades
            if request_upgrades > prexp:
                story.print_character_text("Due to the current EXP shortage in the market, i cannot accept loans",
                    "Mysterious Voice")
            elif request_upgrades <= 0:
                story.print_character_text("As you have entered an invalid amount, your account has not been charged.",
                    "Mysterious Voice")
            else:
                story.print_character_text("Your remaining balance is " + convert_to_text(EXP) + " \"Exp\".",
                    "Mysterious Voice")
            controller.move_sprite(player_hitbox, moverSpeed, moverSpeed)
    else:
        if game.ask("clear all settings?"):
            blockSettings.clear()
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def BossFight():
    player_hitbox.set_position(20, scene.screen_height() / 2)
    controller.move_sprite(player_hitbox, 0, 0)
    animation.run_image_animation(guide,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e 9 e f . . . .
                . . . f e e e e 9 9 e f . . . .
                . . f f e e e e 9 e e f . . . .
                . f f e e e e e 9 e e f . . . .
                f f e e e e 9 9 9 e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e 9 9 e f . . . .
                . . f f e e e e 9 e e f . . . .
                . f f e e e e e 9 e e f . . . .
                f f e e e e 9 9 9 e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e 9 e e f . . . .
                . . f f e e e e 9 e e f . . . .
                . f f e e e e e 9 e e f . . . .
                f f e e e e 9 9 9 e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e 9 e e f . . . .
                . f f e e e e e 9 e e f . . . .
                f f e e e e 9 9 9 e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e 9 e e f . . . .
                f f e e e e 9 9 9 e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e 9 9 9 e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e 9 9 e e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e 9 e e e e f f f f .
                f e e e e e e 9 e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """)],
        100,
        False)
    story.print_character_text("...", "Mysterious Voice")
    story.print_character_text("}{3}{", "Mysterious Voice?")
    animation.run_image_animation(guide,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a a f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c c f . . .
                . . . . f e e e e c a 5 f . . .
                . . . . f e e e e c c c f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e c 4 f . . .
                . . . . f e e e e c 5 5 f . . .
                . . . . f e e e e c c 4 f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e 4 4 f . . .
                . . . . f e e e e 4 5 5 f . . .
                . . . . f e e e e c 4 4 f . . .
                . . . . f e e e e c c e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e 4 4 f . . .
                . . . . f e e e e 4 5 5 f . . .
                . . . . f e e e e 4 4 4 f . . .
                . . . . f e e e e c 4 e f . . .
                . . . f f e e e e c e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e 4 4 f . . .
                . . . . f e e e e 4 5 5 f . . .
                . . . . f e e e e 4 4 4 f . . .
                . . . . f e e e e 4 4 e f . . .
                . . . f f e e e e 4 e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """)],
        100,
        False)
    story.print_character_text("}{0VV UN|=0R+UN@+3...", "No...")
    animation.run_image_animation(guide,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e e e f . . .
                . . . . f f e e e e 4 4 f . . .
                . . . . f e e e e 4 5 5 f . . .
                . . . . f e e e e 4 4 4 f . . .
                . . . . f e e e e 4 4 e f . . .
                . . . f f e e e e 4 e f f . . .
                . . . f e e e e e e e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e e f f . . .
                . . . . . f e e e e 2 2 f . . .
                . . . . f f e e e 2 4 4 f . . .
                . . . . f e e e 2 4 5 5 f . . .
                . . . . f e e e 2 4 4 4 f . . .
                . . . . f e e e 2 4 4 2 f . . .
                . . . f f e e e 2 4 2 f f . . .
                . . . f e e e e e 2 e f . . . .
                . . . f e e e e e e e f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e e 2 f f . . .
                . . . . . f e e e 2 2 2 f . . .
                . . . . f f e e 2 2 4 4 f . . .
                . . . . f e e 2 2 4 5 5 f . . .
                . . . . f e e 2 2 4 4 4 f . . .
                . . . . f e e 2 2 4 4 2 f . . .
                . . . f f e e 2 2 4 2 f f . . .
                . . . f e e e e 2 2 2 f . . . .
                . . . f e e e e e 2 2 f . . . .
                . . f f e e e e e e e f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f e 2 2 f f . . .
                . . . . . f e e 2 2 2 2 f . . .
                . . . . f f e 2 2 2 4 4 f . . .
                . . . . f e 2 2 2 4 5 5 f . . .
                . . . . f e 2 2 2 4 4 4 f . . .
                . . . . f e 2 2 2 4 4 2 f . . .
                . . . f f e 2 2 2 4 2 f f . . .
                . . . f e e e 2 2 2 2 f . . . .
                . . . f e e e e 2 2 2 f . . . .
                . . f f e e e e e 2 2 f . . . .
                . f f e e e e e e e e f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f e 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f e e 2 2 2 2 2 f . . . .
                . . . f e e e 2 2 2 2 f . . . .
                . . f f e e e e 2 2 2 f . . . .
                . f f e e e e e e 2 2 f . . . .
                f f e e e e e e e e e f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f e 2 2 2 2 2 2 f . . . .
                . . . f e e 2 2 2 2 2 f . . . .
                . . f f e e e 2 2 2 2 f . . . .
                . f f e e e e e 2 2 2 f . . . .
                f f e e e e e e e 2 2 f f f f .
                f e e e e e e e e e e e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f e 2 2 2 2 2 2 f . . . .
                . . f f e e 2 2 2 2 2 f . . . .
                . f f e e e e 2 2 2 2 f . . . .
                f f e e e e e e 2 2 2 f f f f .
                f e e e e e e e e 2 2 e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f e 2 2 2 2 2 2 f . . . .
                . . f f e e 2 2 2 2 2 f . . . .
                . f f e e e e 2 2 2 2 f . . . .
                f f e e e e e e 2 2 2 f f f f .
                f e e e e e e e e 2 2 e e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f e 2 2 2 2 2 2 f . . . .
                . f f e e e 2 2 2 2 2 f . . . .
                f f e e e e e 2 2 2 2 f f f f .
                f e e e e e e e 2 2 2 2 e e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f e e 2 2 2 2 2 2 f . . . .
                f f e e e e 2 2 2 2 2 f f f f .
                f e e e e e e 2 2 2 2 2 2 e f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f e 2 2 2 2 2 2 2 f . . . .
                f f e e e 2 2 2 2 2 2 f f f f .
                f e e e e e 2 2 2 2 2 2 2 2 f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f 2 2 2 2 2 2 2 2 f . . . .
                f f e e 2 2 2 2 2 2 2 f f f f .
                f e e e e 2 2 2 2 2 2 2 2 2 f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f 2 2 2 2 2 2 2 2 f . . . .
                f f e 2 2 2 2 2 2 2 2 f f f f .
                f e e e 2 2 2 2 2 2 2 2 2 2 f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f 2 2 2 2 2 2 2 2 f . . . .
                f f 2 2 2 2 2 2 2 2 2 f f f f .
                f e e 2 2 2 2 2 2 2 2 2 2 2 f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f 2 2 2 2 2 2 2 2 f . . . .
                f f 2 2 2 2 2 2 2 2 2 f f f f .
                f e 2 2 2 2 2 2 2 2 2 2 2 2 f f
                f f f f f f f f f f f f f f f f
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . f f f f f . . . .
                . . . . . f f f 2 2 2 f f . . .
                . . . . . f 2 2 2 2 2 2 f . . .
                . . . . f f 2 2 2 2 4 4 f . . .
                . . . . f 2 2 2 2 4 5 5 f . . .
                . . . . f 2 2 2 2 4 4 4 f . . .
                . . . . f 2 2 2 2 4 4 2 f . . .
                . . . f f 2 2 2 2 4 2 f f . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . . f 2 2 2 2 2 2 2 f . . . .
                . . f f 2 2 2 2 2 2 2 f . . . .
                . f f 2 2 2 2 2 2 2 2 f . . . .
                f f 2 2 2 2 2 2 2 2 2 f f f f .
                f 2 2 2 2 2 2 2 2 2 2 2 2 2 f f
                f f f f f f f f f f f f f f f f
                """)],
        100,
        False)
    story.print_character_text("Y0U W3R3 t0o L@+3 +00  5^V3 Y0uR |1++|3 GU1D3 ",
        "It cant be...")
    story.print_character_text("MUAHAHAHAHAHA", "...")
    story.print_character_text("...", "???")
    guide.set_image(img("""
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
        """))
    story.print_character_text("=)", "THE DEMON KING")
    color.fade_to_white.start_screen_effect(1000)
    scene.camera_shake(5, 1000)
    color.pause_until_fade_done()
    guide.set_kind(SpriteKind.enemyimage)
    tiles.set_current_tilemap(tilemap("""
        room0
        """))
    guide.set_image(assets.image("""
        finalboss
        """))
    guide.set_position(scene.camera_property(CameraProperty.X),
        scene.camera_property(CameraProperty.Y))
    color.start_fade_from_current(color.original_palette, 500)

def on_on_overlap3(sprite2, otherSprite3):
    sprites.destroy(otherSprite3)
    sprites.destroy(sprite2)
sprites.on_overlap(SpriteKind.eater, SpriteKind.enemyimage, on_on_overlap3)

def on_overlap_tile4(sprite22, location2):
    createValidRoom("fromLeft", scene.screen_width() - 24, sprite22.y)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile4)

def on_mouse_move(x2, y2):
    global mouseX, mouseY
    mouseX = x2
    mouseY = y2
browserEvents.on_mouse_move(on_mouse_move)

def on_on_destroyed2(sprite5):
    global mySprite5
    mySprite5 = sprites.create(img("""
        2
        """), SpriteKind.eater)
    mySprite5.set_position(sprite5.x, sprite5.y)
    mySprite5.lifespan = 100
    if len(sprites.all_of_kind(SpriteKind.enemy)) == 0:
        unlockDoors()
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed2)

def unlockDoors():
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile
        """)):
        tiles.set_wall_at(value, False)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile0
        """)):
        tiles.set_wall_at(value2, False)
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile1
        """)):
        tiles.set_wall_at(value3, False)
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
        """)):
        tiles.set_wall_at(value4, False)

def on_overlap_tile5(sprite7, location5):
    createValidRoom("fromRight", 24, sprite7.y)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
        """),
    on_overlap_tile5)

def loadSaves():
    global savechoice, currentprojeclist
    scene.set_background_image(assets.image("""
        menuSprite
        """))
    tiles.set_current_tilemap(tilemap("""
        blankMap
        """))
    story.show_player_choices("Save 1", "Save 2", "Save 3")
    savechoice = story.get_last_answer()
    if blockSettings.exists(savechoice):
        game.show_long_text("" + savechoice + " is a room " + str(blockSettings.read_number_array(savechoice)[4]) + classnames[blockSettings.read_number_array(savechoice)[1]],
            DialogLayout.FULL)
        story.show_player_choices("Load " + savechoice, "Erase " + savechoice, "Back")
        if story.check_last_answer("Load " + savechoice):
            if blockSettings.read_number_array(savechoice)[1] != 0:
                currentprojeclist = scaling.create_rotations(listofprojec[blockSettings.read_number_array(savechoice)[1]],
                    360)
            player_create()
        elif story.check_last_answer("Erase " + savechoice):
            blockSettings.remove(savechoice)
            blockSettings.remove("" + savechoice + " Ex")
            blockSettings.remove("" + savechoice + " Ey")
            loadSaves()
        else:
            loadSaves()
    else:
        toriel_create(1)

def on_on_zero(status):
    global player_alive
    player_alive = False
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    sprites.destroy_all_sprites_of_kind(SpriteKind.food, effects.disintegrate, 1000)
    pause(1000)
    blockSettings.remove(savechoice)
    blockSettings.remove("" + savechoice + " Ex")
    blockSettings.remove("" + savechoice + " Ey")
    story.print_character_text("Ah...", "Mysterious Voice")
    story.print_character_text("It seems your vessel has shattered...", "Mysterious Voice")
    story.print_character_text("Rest now, but do not give up!", "Mysterious Voice")
    loadSaves()
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_mouse_left_button_pressed(x, y):
    global angle, playershot
    if player_alive:
        if projectMax.value > 0:
            projectMax.value += -1
            angle = Math.round(spriteutils.radians_to_degrees(spriteutils.angle_from(player_image, spriteutils.pos(x, y))))
            if angle < 0:
                angle += 360
            if playerClass == 2:
                playershot = sprites.create_projectile_from_sprite(assets.image("""
                    empty
                    """), player_image, 0, 0)
                sprites.set_data_number(playershot, "swordindex", 0)
                sprites.set_data_number(playershot, "orgin", angle)
                sprites.set_data_number(playershot,
                    "Xoffset",
                    Normalise(player_image, x, y, 10, True))
                sprites.set_data_number(playershot,
                    "Yoffset",
                    Normalise(player_image, x, y, 10, False))
                playershot.lifespan = projectilespeed * 10
            else:
                playershot = sprites.create_projectile_from_sprite(currentprojeclist[angle],
                    player_image,
                    Normalise(player_image, x, y, projectilespeed, True),
                    Normalise(player_image, x, y, projectilespeed, False))
                if playerClass == 1:
                    playershot.lifespan = 15 / (projectilespeed / 1000)
            playershot.set_flag(SpriteFlag.AUTO_DESTROY, True)
browserEvents.mouse_left.on_event(browserEvents.MouseButtonEvent.PRESSED,
    on_mouse_left_button_pressed)

def createValidRoom(enteredFrom: str, locationX: number, locationY: number):
    global notcreatingroom, roomscleard, EXP, room, mySprite3, list2
    player_hitbox.set_position(scene.screen_width() / 2, scene.screen_height() / 2)
    if notcreatingroom:
        notcreatingroom = False
        if roomscleard + 1 == 100:
            if not (game.ask("Mysterious Voice", "The fina| room 1ies ahead")):
                notcreatingroom = True
                return
        if statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).value < statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).max:
            statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).value += 1
        roomscleard += 1
        if roomscleard == 50:
            EXP += 21
            room = 15
        elif roomscleard == 100:
            room = 4
        elif roomscleard == 99:
            EXP += 2
            if "fromLeft" == enteredFrom:
                room = 1
            elif "fromDown" == enteredFrom:
                room = 3
            elif "fromRight" == enteredFrom:
                room = 5
            elif "fromUp" == enteredFrom:
                room = 9
        else:
            EXP += 1
            room = blockSettings.read_number_array(enteredFrom)[randint(0, 7)]
        blockSettings.write_number_array(savechoice,
            [room,
                playerClass,
                statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).max,
                statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).value,
                roomscleard,
                locationX,
                locationY,
                moverSpeed,
                projectMax.max,
                projectilespeed,
                EXP])
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
        sprites.destroy_all_sprites_of_kind(SpriteKind.status_bar)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemyimage)
        sprites.destroy_all_sprites_of_kind(SpriteKind.food)
        for index in range(Math.round(roomscleard / 4)):
            mySprite3 = sprites.create(assets.image("""
                enemyHitbox
                """), SpriteKind.enemy)
            mySprite3.set_position(locationX, locationY)
            while spriteutils.distance_between(mySprite3, spriteutils.pos(locationX, locationY)) <= 30:
                mySprite3.set_position(randint(20, scene.screen_width() - 20),
                    randint(24, scene.screen_height() - 24))
        list2 = []
        for value5 in sprites.all_of_kind(SpriteKind.enemy):
            list2.append(value5.x)
        blockSettings.write_number_array("" + savechoice + " Ex", list2)
        list2 = []
        for value6 in sprites.all_of_kind(SpriteKind.enemy):
            list2.append(value6.y)
        blockSettings.write_number_array("" + savechoice + " Ey", list2)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        sprites.destroy_all_sprites_of_kind(SpriteKind.eater)
        player_create()
def player_create():
    global room, playerClass, player_hitbox, roomscleard, mySprite3, mySprite4, player_image, statusbar, moverSpeed, projectMax, projectilespeed, EXP, player_alive, notcreatingroom
    room = blockSettings.read_number_array(savechoice)[0]
    tiles.set_current_tilemap(listOfRooms[room])
    playerClass = blockSettings.read_number_array(savechoice)[1]
    player_hitbox = sprites.create(img("""
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
            """),
        SpriteKind.player)
    roomscleard = blockSettings.read_number_array(savechoice)[4]
    player_hitbox.set_position(blockSettings.read_number_array(savechoice)[5],
        blockSettings.read_number_array(savechoice)[6])
    for index2 in range(10):
        tiles.set_wall_at(tiles.get_tile_location(index2, 0), True)
        tiles.set_wall_at(tiles.get_tile_location(index2, 6), True)
    for index3 in range(7):
        tiles.set_wall_at(tiles.get_tile_location(0, index3), True)
        tiles.set_wall_at(tiles.get_tile_location(9, index3), True)
    if blockSettings.exists("" + savechoice + " Ex") and blockSettings.exists("" + savechoice + " Ey") and 0 < len(blockSettings.read_number_array("" + savechoice + " Ex")):
        if roomscleard == 50:
            player_hitbox.say_text("Halfway there...", 1000, True)
            scene.camera_shake(4, 1000)
        elif roomscleard == 99:
            player_hitbox.say_text("one more room...", 2000, True)
        elif roomscleard == 100:
            toriel_create(4)
        else:
            index4 = 0
            while index4 <= len(blockSettings.read_number_array("" + savechoice + " Ex")) - 1:
                mySprite3 = sprites.create(assets.image("""
                    enemyHitbox
                    """), SpriteKind.enemy)
                mySprite4 = sprites.create(assets.image("""
                        enemySprite
                        """),
                    SpriteKind.enemyimage)
                mySprite4.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
                mySprite4.follow(mySprite3, 100)
                mySprite3.follow(player_hitbox, 50)
                mySprite4.set_position(blockSettings.read_number_array("" + savechoice + " Ex")[index4],
                    blockSettings.read_number_array("" + savechoice + " Ey")[index4])
                mySprite3.set_position(blockSettings.read_number_array("" + savechoice + " Ex")[index4],
                    blockSettings.read_number_array("" + savechoice + " Ey")[index4])
                index4 += 1
    player_image = sprites.create(lisOfClasses[playerClass], SpriteKind.food)
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.max = blockSettings.read_number_array(savechoice)[2]
    statusbar.value = blockSettings.read_number_array(savechoice)[3]
    statusbar.attach_to_sprite(player_hitbox, 10, 0)
    moverSpeed = blockSettings.read_number_array(savechoice)[7]
    controller.move_sprite(player_hitbox, moverSpeed, moverSpeed)
    projectMax = statusbars.create(4, 15, StatusBarKind.energy)
    projectMax.max = blockSettings.read_number_array(savechoice)[8]
    projectMax.value = blockSettings.read_number_array(savechoice)[8]
    projectMax.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    projectMax.attach_to_sprite(player_hitbox, 0, -7)
    projectilespeed = blockSettings.read_number_array(savechoice)[9]
    EXP = blockSettings.read_number_array(savechoice)[10]
    player_image.set_flag(SpriteFlag.GHOST, True)
    if 100 == roomscleard:
        pass
    elif 99 == roomscleard:
        for value7 in tiles.get_tiles_by_type(assets.tile("""
            myTile
            """)):
            tiles.set_wall_at(value7, False)
    elif len(sprites.all_of_kind(SpriteKind.enemy)) == 0:
        unlockDoors()
    player_alive = True
    notcreatingroom = True

def on_on_overlap4(sprite82, otherSprite4):
    sprites.destroy(otherSprite4)
    statusbars.get_status_bar_attached_to(StatusBarKind.health, player_hitbox).value += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

swordangle = 0
statusbar: StatusBarSprite = None
mySprite4: Sprite = None
list2: List[number] = []
mySprite3: Sprite = None
room = 0
currentprojeclist: List[Image] = []
playershot: Sprite = None
player_image: Sprite = None
angle = 0
mySprite5: Sprite = None
mouseY = 0
mouseX = 0
projectilespeed = 0
request_upgrades = 0
EXP = 0
prexp = 0
roomscleard = 0
guide: Sprite = None
moverSpeed = 0
mySprite1: Sprite = None
mySprite: Sprite = None
notcreatingroom = False
playerClass = 0
player_hitbox: Sprite = None
savechoice = ""
projectMax: StatusBarSprite = None
player_alive = False
lisOfClasses: List[Image] = []
classnames: List[str] = []
listOfRooms: List[tiles.TileMapData] = []
@namespace
class userconfig:
    ARCADE_SCREEN_WIDTH = 160
    ARCADE_SCREEN_HEIGHT = 112
listOfRooms = [tilemap("""
        room0
        """),
    tilemap("""
        room1
        """),
    tilemap("""
        room2
        """),
    tilemap("""
        room3
        """),
    tilemap("""
        room4
        """),
    tilemap("""
        room5
        """),
    tilemap("""
        room6
        """),
    tilemap("""
        room7
        """),
    tilemap("""
        room8
        """),
    tilemap("""
        room9
        """),
    tilemap("""
        room10
        """),
    tilemap("""
        room11
        """),
    tilemap("""
        room12
        """),
    tilemap("""
        room13
        """),
    tilemap("""
        room14
        """),
    tilemap("""
        room15
        """)]
listofprojec = [img("""
        . . f f f f f f . .
        . f f 1 1 1 1 f f .
        f f 1 1 1 1 1 1 f f
        f 1 1 1 1 1 1 1 1 f
        f 1 1 1 1 1 1 1 1 f
        f 1 1 1 1 1 1 1 1 f
        f 1 1 1 1 1 1 1 1 f
        f f 1 1 1 1 1 1 f f
        . f f 1 1 1 1 f f .
        . . f f f f f f . .
        """),
    img("""
        . f 1 1 1 1 .
        f f d d d d 1
        . f 1 1 1 1 .
        """),
    assets.image("""
        sword
        """),
    assets.image("""
        arrow
        """)]
classnames = [" Mage.", " Rouge.", " Knight.", " Archer."]
lisOfClasses = [assets.image("""
        mage
        """),
    assets.image("""
        rouge
        """),
    assets.image("""
        knight
        """),
    assets.image("""
        archer
        """),
    assets.image("""
        mage0
        """),
    assets.image("""
        rouge0
        """),
    assets.image("""
        knight0
        """),
    assets.image("""
        archer0
        """)]
player_alive = False
loadSaves()
blockSettings.write_number_array("fromRight", [4, 5, 6, 7, 12, 13, 14, 15])
blockSettings.write_number_array("fromUp", [8, 9, 10, 11, 12, 13, 14, 15])
blockSettings.write_number_array("fromLeft", [1, 3, 5, 7, 9, 11, 13, 15])
blockSettings.write_number_array("fromDown", [2, 3, 6, 7, 10, 11, 14, 15])

def on_update_interval():
    global swordangle
    if playerClass == 2:
        for value8 in sprites.all_of_kind(SpriteKind.projectile):
            swordangle = Math.round(sprites.read_data_number(value8, "orgin") + (sprites.read_data_number(value8, "swordindex") - projectilespeed / 2))
            sprites.change_data_number_by(value8, "swordindex", 2)
            if swordangle < 0:
                swordangle += 360
            elif 360 < swordangle:
                swordangle += -360
            value8.set_image(currentprojeclist[swordangle])
            value8.set_position(sprites.read_data_number(value8, "Xoffset") + player_image.x,
                sprites.read_data_number(value8, "Yoffset") + player_image.y)
game.on_update_interval(1, on_update_interval)

def on_on_update():
    if player_alive:
        player_image.set_position(player_hitbox.x, player_hitbox.y - 5)
        if 0 < player_hitbox.vx:
            player_image.set_image(lisOfClasses[playerClass])
            projectMax.set_offset_padding(-7, 0)
        elif player_hitbox.vx < 0:
            projectMax.set_offset_padding(-7, -14)
            player_image.set_image(lisOfClasses[playerClass + 4])
game.on_update(on_on_update)
