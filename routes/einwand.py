from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/roll")
def roll_einwaende():
    einwand_1 = random.randint(1, 5)
    einwand_2 = random.randint(1, 5)
    while einwand_2 == einwand_1:
        einwand_2 = random.randint(1, 5)
    return {"einwand_1": einwand_1, "einwand_2": einwand_2}
