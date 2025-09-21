import os
import sys
import html_generator

number_article = 6

render = html_generator.gen_html()

def directory_existe(path):
    if not os.path.exists(path):
        print(f"Le dossier '{path}' n'existe pas.")
        return

    else:
        parse(path)

def parse(path):
    file_list = os.listdir(path)

    if len([x for x in file_list if x[-3:] == ".md"]) != 1:
        print("le dossier ne contienne pas de fichier md ou en contien plusieur")
    else:
        file = open(path + "/" + [x for x in file_list if x[-3:] == ".md"][0], "r")

        html = ""

        code = False

        for i in file:
            if not code:
                if i[:3] == "![[" and i[-3:] == "]]\n" : # gestion des image
                    filename = i[3:-3]

                    if not os.path.exists("./img/" + str(number_article)):
                        os.mkdir("./img/" + str(number_article))

                    os.system("cp " + '"' + path + "/" + filename + '" "' + "./img/" + str(number_article) + '"')

                    print("copy image :", filename)

                    render.add_img("../img/" + str(number_article) + "/" + filename)

                elif i[0] == "#":
                    render.add_titre(i)

                elif i[:3] == "```":
                    code = True
                    tmp_code = i[3:]
                elif i != "\n":
                    render.add_p(i[:-1])
            else:
                if i[:3] == "```":
                    code = False
                    render.add_code(tmp_code)
                else:
                    tmp_code += i



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <chemin_du_dossier>")
    else:
        directory_existe(sys.argv[1])

open("article/" + str(number_article) + ".html", "w+").write(render.render())