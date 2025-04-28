class gen_html:
    title = ""
    content = [""]

    def render(self):
        html = """<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="../style/style.css">

        <title>""" + self.title + """</title>
        
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/atom-one-dark.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/highlight.min.js"></script>
        <script>hljs.highlightAll();</script>

        <style>
            pre code.hljs {
                border-radius: 10px;
                text-indent: 0em;
            }
            
            .img1{
                max-width: 33%;
                height: auto;
            }
        </style>

    </head>
    <body>
        <div class="top">
            <strong><h1 class="titre">Le blog de Cartoone</h1></strong>
        </div>
        <div class="meunu">
            ̼<p id="home_btn">home</p>
            <p id="aboutme_btn">about-me</p>
            <p id="article_btn">article</p>
            <script>
                const home_btn = document.getElementById("home_btn");
                home_btn.addEventListener("click", (event) => {open("/index.html","_self")})

                const about_me = document.getElementById("aboutme_btn");
                about_me.addEventListener("click", (event) => {open("/about-me.html","_self")})

                const article_btn = document.getElementById("article_btn");
                article_btn.addEventListener("click", (event) => {open("/search-article.html","_self")})
            </script>
        </div>

        <div class="main">
            <div class="text">
                """ + "".join(self.content) + """
            </div>
        </div> 
    </body>
</html>"""

        return html
    
    def add_img(self, path):
        self.content += ["""
                <div class="img_container_center">
                    <img src=\"""" + path + """">
                </div>\n"""]
        
    def add_p(self, text):
        self.content += ["\n                <p>" + text + "</p>\n"]

    def add_titre(self, text):
        level = 0

        while text[0] == "#":
            text = text[1:]
            level += 1

        self.content += [f"\n                <h{level}>" + text[1:-1] + f"</h{level}>\n"]

    def add_code(self, text):
        if text[:7] == "python\n":
            self.content += ['\n<pre><code class="python">' + text[7:-1] + '</code></pre>\n']
        else:
            self.content += ['\n<pre><p class="highlight_part">' + text[7:-1] + '</p></pre>\n']