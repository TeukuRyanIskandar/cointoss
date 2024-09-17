from fasthtml.common import *

app, rt = fast_app(
    pico=True,
    hdrs=(
        Link(rel='stylesheet', href="https://unpkg.com/normalize.css", type='text/css'),
        Link(rel='stylesheet', href="/assets/css/homepage_styles.css", type='text/css'),
        Link(rel='stylesheet', href="/assets/css/common_styles.css", type='text/css'),
        Link(rel='stylesheet',
             href="https://fonts.googleapis.com/css2?family=Jersey+20+Charted&family=Tiny5&display=swap",
             type='text/css'),
        Style("body, h1 {background-color: #000; font-family: 'Tiny5', sans-serif;}")
    )
)


def navbar():
    return

def homepage():
    return (
        Div(
        Div(
            Div(
                Div(H1("C O I N T O S S"), Img(src="assets/images/coinflip.gif"), cls="cointoss"),
                        Div(
                        Form(
                            Div(
                            Input(
                                cls="input-text",
                                type="text",
                                name="name",
                                placeholder="Enter a username"
                            ),
                            Button(Style("button {background-color: #000; color: #fff; border: 3px solid #41FF00} "),
                                   "Confirm", cls="input-btn"),
                            cls="input"),
                        cls="form-input"),
                    cls="form-items"),
                cls="form-content"),
            cls="form-container"),
        cls="page-wrapper"))


def gamepage():
    return Div(H1("This is the game page"), cls="page-wrapper")


@rt('/')
def get():
    return Title("Cointoss"), homepage()


@rt('/game')
def get():
    return Title("Cointoss"), gamepage()


serve()
