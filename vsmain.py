import PySimpleGUI as psg


vigets = [
    [psg.Text(text="Имя игрока: "), psg.InputText(key="iname"), ],
    [psg.Text(text="Клетки по Х "), psg.OptionMenu(values=[10, 15, 20, 30], key="cletx", default_value=20),psg.Text(text="Клетки по Y"), psg.OptionMenu(values=[10, 15, 20, 30], key="clety", default_value=20)],
    [psg.Text(text="Цвет"), psg.OptionMenu(values=["red", "purple", "blue"], key="color", default_value="blue")],
    [psg.Text(text="Цвет овоща"), psg.InputText(key="apcolor"), psg.ColorChooserButton(button_text="Цвет")],
    [psg.Radio(text="Круглая", key="circl", group_id=1), psg.Radio(text="Квадратна", key="minec",group_id=1, default=True)],
    [psg.Button(button_text="Да", key="startbut"), psg.Button(button_text="Alt + f4", key="exitbut")],
   
]
wind = psg.Window("Window", vigets)
while True:
    do = wind.read()
    ivent = do[0]
    secivent = do[1]
    print(ivent, secivent)
    if ivent == "startbut":
        break
    if ivent == "exitbut" or psg.WIN_CLOSED == ivent:
        break
  
