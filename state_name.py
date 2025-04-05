import  turtle
import pandas as pd

screen = turtle.Screen()
image = "indian map states outline.gif"
screen.addshape(image)

screen.bgpic(image)
turtle.shape(image)


# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)

state_name = {
    "state" :["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
              "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
              "Meghalaya", "Mizoram", "Nagaland","Odisha", "Punjab","Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
              "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"],
    "x" :[-64.0, 188.0, 160.0, 56.0, -6.0, -147.0, -183.0, -103.0, -83.0, 45.0, -113.0, -106.0, -70.0, -114.0, 189.0,
          142.0, 174.0, 198.0, 32.0, -122.0, -143.0, 105.0, 97.0, -66.0, -63.0, 150.0, -20.0, -54.0],
    "y" :[-125.0, 134.0, 97.0, 73.0, -2.0, -115.0, 31.0, 138.0, 190.0, 37.0, -126.0, -199.0, 36.0, -38.0, 64.0, 76.0,
          40.0, 91.0, -24.0, 169.0, 94.0, 83.0, 112.0, -204.0, -64.0, 45.0, 90.0, 158.0],
}

data = pd.DataFrame(state_name)
# data.to_csv("28_states_India.csv")
print(data)


turtle.mainloop()
