from Chef import Chef
from SouthIndianChef import SouthIndianChef
chef = Chef()
south_chef = SouthIndianChef()

chef.make_biriyani()
chef.make_pizza()
chef.make_salad()
chef.make_special_dish()

south_chef.make_biriyani()
south_chef.make_pizza()
south_chef.make_special_dish()
south_chef.make_idli()
south_chef.make_salad()

# The above code demonstrates inheritance in Python, where the SouthIndianChef class inherits from the Chef class.
# It shows how the SouthIndianChef can use methods from the Chef class and also define its own methods.
# The output will show the dishes made by both the Chef and SouthIndianChef.
# The Chef class has methods for making various dishes, and the SouthIndianChef class extends this functionality
# by adding a method to make idli, which is specific to South Indian cuisine.
# In south chef, the make_special_dish method overrides the one in Chef to provide a South Indian-specific dish (dosa).
# The code also demonstrates how to create instances of both classes and call their methods.
