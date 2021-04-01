from turtle import Turtle

COLORS = ["yellow", "yellow", "green", "green", "orange", "orange", "blue", "blue"]


class ObjectManager:
    objects_dict = {}

    def objects_generate(self):
        y = 40
        x = 355
        for i in range(8):
            self.objects_dict[i] = []
            for j in range(15):
                new_car = Turtle(shape='square')
                new_car.shapesize(0.5, 2)
                new_car.penup()
                new_car.goto(x=x, y=y)
                new_color = COLORS[i]
                new_car.color(new_color)
                self.objects_dict[i].append(new_car)
                x -= 51
            if COLORS[i] == 'yellow':
                self.objects_dict[i].append(1)
            elif COLORS[i] == 'green':
                self.objects_dict[i].append(3)
            elif COLORS[i] == 'orange':
                self.objects_dict[i].append(5)
            elif COLORS[i] == 'blue':
                self.objects_dict[i].append(7)
            x = 355
            y += 30
        return self.objects_dict
