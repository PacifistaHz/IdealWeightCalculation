import datetime
from unittest import removeResult


def IdealWeightCalculation(height, birthYear, weight, sex):
    age=datetime.datetime.today().year - birthYear
    if sex=="Man":
        k=0.9;
    else:
        k=0.8;
    idealWeight=(height-100+age/10)*k;
    difference=idealWeight-weight;
    if idealWeight==weight:
        message="You are in ideal weight.";
    elif idealWeight>weight:
        message="You are in low weight.";
    elif idealWeight<weight:
        message="You are in high weight.";
    result={"Ideal Weight":idealWeight,"Difference":difference,"Message":message}
    return result

height = int(input("Enter your height: "))
height=int(height)
birthYear=int(input("Enter your birth year: "))
birthYear=int(birthYear)
weight=int(input("Enter your weight: "))
weight=int(weight)
sex=input("Enter your sex(Man:1, Woman:0): ")
sexType={"1":"Man","0":"Woman"}
result=IdealWeightCalculation(height,birthYear,weight, sexType["1"])
print(result)