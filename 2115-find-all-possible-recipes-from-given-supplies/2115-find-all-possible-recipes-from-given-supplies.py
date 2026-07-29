#top1
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        self.cookbook = {}
        for recipe, ingredient in zip(recipes, ingredients):
            self.cookbook[recipe] = ingredient
		# recipes are mapped to ingredients in dictionary for easy lookup
		
        self.set_supplies = set(supplies)
        # transform to set for easy lookup
        self.visited_recipes = {}
        self.canCook = set()
        for recipe, recipe_ingredients in self.cookbook.items():
            self.checkRecipe(recipe, recipe_ingredients)

        return list(self.canCook)
		
    def checkRecipe(self, recipe: str, ingredients: List[str]) -> Bool:
        # see if we have already checked this recipe first
        if recipe in self.visited_recipes and self.visited_recipes[recipe] == 0:
            return False

        if recipe in self.visited_recipes and self.visited_recipes[recipe] == 1:
            return True
        
        if recipe in self.visited_recipes and self.visited_recipes[recipe] == -1:
            return False

        self.visited_recipes[recipe] = 0
        for ingredient in ingredients:
            if ingredient not in self.set_supplies:
                # ingredient is not in the supplies list, but maybe its a recipe itself
                if ingredient not in self.cookbook:
                    # this is not a recipe, its an ingredient we dont have
                    self.visited_recipes[recipe] = -1
                    return False
                else:
                # now need to check if this recipe can be made
                    if ingredient not in self.canCook:
                        # which check to see if we already know we can make this one
                        if not self.checkRecipe(ingredient, self.cookbook[ingredient]):
                            self.visited_recipes[recipe] = -1
                            return False
        # all ingredients are checked, none have failed
        self.canCook.add(recipe)
        self.visited_recipes[recipe] = 1
        return True