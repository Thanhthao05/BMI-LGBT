def Status(height,weight):
    BMI=weight/(height*height)
    if BMI<18.5:
        return "thin"
    elif 18.5<=BMI<25:
        return "normal"
    elif 25<=BMI<30:
        return "fat"
    else:
        return "obesity"
def BMI(height,weight):
    bmi=(weight/(height*height))
    return bmi