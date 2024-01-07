class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, value):
        self.__tags[tag] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud["ajay"] = 20
print(cloud._TagCloud__tags["ajay"])
print(cloud["ajay"])


# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def Price(self):
#         return self.price

#     @Price.setter
#     def Price(self, price):
#         if price < 0:
#             raise ValueError("Price can't be negative")
#         self.price = price

#     # def __getitem__(self):
#     #     return self.price


# product = Product(100)
# print(product.price)
# product.price = 20
# print(product.price)
