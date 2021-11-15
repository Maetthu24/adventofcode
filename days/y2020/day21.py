from common.aocdays import AOCDay, day

DEBUG = True

@day(21)
class Day21(AOCDay):
    test_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split("\n")

    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 5, f'{p1} != 5'

        p2 = self.part2(self.test_input).__next__()
        assert p2 == 'mxmxvkd,sqjhc,fvjkl', f'{p2} != "mxmxvkd,sqjhc,fvjkl"'

    def common(self, input_data):
        input_data = self.test_input

    def part1(self, input_data):
        ingredients = set()
        allergens = set()
        
        lines = []

        for line in input_data:
            i = []
            a = []
            for ing in line.split(' (')[0].split(' '):
                i.append(ing)
                ingredients.add(ing)
            
            for al in line.split(' (')[1][:-1].split(', '):
                a.append(al.replace('contains ', ''))
                allergens.add(al.replace('contains ', ''))

            lines.append((i, a))

        allergen_mappings = {}

        for (i, a) in lines:
            for al in a:
                if al not in allergen_mappings:
                    allergen_mappings[al] = set(i)
                else:
                    allergen_mappings[al] = set(i).intersection(allergen_mappings[al])
        
        possible_ingredients = set()
        impossible_count = 0

        for i in allergen_mappings.values():
            possible_ingredients = possible_ingredients.union(i)

        for (i, a) in lines:
            for ing in i:
                if ing not in possible_ingredients:
                    impossible_count += 1

        yield impossible_count

    def part2(self, input_data):
        ingredients = set()
        allergens = set()
        
        lines = []

        for line in input_data:
            i = []
            a = []
            for ing in line.split(' (')[0].split(' '):
                i.append(ing)
                ingredients.add(ing)
            
            for al in line.split(' (')[1][:-1].split(', '):
                a.append(al.replace('contains ', ''))
                allergens.add(al.replace('contains ', ''))

            lines.append((i, a))

        allergen_mappings = {}

        for (i, a) in lines:
            for al in a:
                if al not in allergen_mappings:
                    allergen_mappings[al] = set(i)
                else:
                    allergen_mappings[al] = set(i).intersection(allergen_mappings[al])
        
        assignments = []
        while len(assignments) < len(allergens):
            assigned = None
            for (al, i) in allergen_mappings.items():
                if len(i) == 1:
                    assigned = next(iter(i))
                    assignments.append((al, assigned))
                    break
            
            for al in allergen_mappings.keys():
                if assigned in allergen_mappings[al]:
                    allergen_mappings[al].remove(assigned)
        
        assignments.sort(key=lambda x: x[0])
        yield ','.join(list(map(lambda x: x[1], assignments)))
