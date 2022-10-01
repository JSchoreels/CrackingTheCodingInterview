# 16.10 Living People: Given a list of people with their birth and death years, implement a method to
# compute the year with the most number of peoplealive. You mayassume that all people were born
# between 1900 and 2000 (inclusive). If a person was alive during any portion of thatyear, they should
# be included in that year's count. For example, Person (birth= 1908, death= 1909) is included in the
# counts for both 1908 and 1909.

def living_people(births : list, deaths : list):
    i_birth = 0
    i_death = 0
    assert len(births) == len(deaths)
    livings = [0] * (2 * len(births))
    living = 0
    births.sort() # side effect, copy the array for real usage
    deaths.sort() # side effect, copy the array for real usage
    while i_birth < len(births) and i_death < len(deaths):
        while i_birth < len(births) and (i_death >= len(deaths) or births[i_birth] <= deaths[i_death]):
            living += 1
            livings[i_birth + i_death] = (births[i_birth], living)
            i_birth += 1
        while i_death < len(deaths) and (i_birth >= len(births) or deaths[i_death] <= births[i_birth]):
            living -= 1
            livings[i_birth + i_death] = (deaths[i_death], living)
            i_death += 1
    print(livings)
    max_living = -1
    max_living_year = -1
    for living_info in livings:
        if living_info[1] > max_living:
            max_living = living_info[1]
            max_living_year = living_info[0]
    return max_living_year


print(living_people([1,2,3,4,5,6,7,8,9,10], [3,5,7,9,11,13,15,17,20,23]))