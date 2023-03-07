import views
import data
import pygame


class Main:
    def __init__(self) -> None:
        print("cc")
        """
        arbre = data.Node(1,
                          data.Node(2,
                                    data.Node(4)
                                    ),
                          data.Node(3,
                                    data.Node(5,
                                              data.Node(7)
                                              )
                                    )
                          )
                          """
        arbre = data.Node(value=4)
        arbre.insert(22)
        arbre.insert(54)
        arbre.insert(83)
        arbre.insert(85)
        arbre.insert(90)
        arbre.insert(92)
        arbre.insert(102)

        arbre.insert(109)
        print(arbre.height)
        print(arbre.size)
        #arbre.insert(8)
        #arbre.insert(9)
        #arbre.insert(10)
        #arbre.insert(11)
        print(arbre.height)
        print(arbre.size)
        view = views.App()
        sheet = data.SpriteSheet("./resources/spritesheets/spritesheet_default.png",
                                 "./resources/spritesheets/spritesheet_default.xml")
        view.window.blit(sheet.get_sprite("body_blueF.png"), (0, 0))
        print(view.parts.get(1))
        print(arbre.prefix_course())
        for id in arbre.prefix_course():
            sprite = sheet.get_sprite(view.parts.get(id)["name"])
            print(view.parts.get(id)["scale"])
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * view.parts.get(id)["scale"], sprite.get_height() * view.parts.get(id)["scale"]))
            print(view.parts.get(id))
            if view.parts.get(id)["flipped"]:
                view.window.blit(pygame.transform.flip(sprite, True, False), (view.parts.get(id)["offsetX"] + view.parts.get(id)["flipX"], view.parts.get(id)["offsetY"]))
            view.window.blit(sprite, (view.parts.get(id)["offsetX"], view.parts.get(id)["offsetY"]))
        editor = views.EditorView()
        editor.render(view.window)
        view.run()


Main()
