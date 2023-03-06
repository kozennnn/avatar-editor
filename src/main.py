import views
import data


class Main:
    def __init__(self) -> None:
        print("cc")
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
        print(arbre.height)
        print(arbre.size)
        view = views.App()
        view.run()


Main()
