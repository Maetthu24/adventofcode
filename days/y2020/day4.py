from common.aocdays import AOCDay, day
import re

DEBUG = True

@day(4)
class Day4(AOCDay):
    test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split("\n")


    test_input_2 = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".split("\n")

    test_input_3 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".split("\n")


    def test(self, input_data):
        p1 = self.part1(self.test_input).__next__()
        assert p1 == 2, f'{p1} != 2'

        p2 = self.part2(self.test_input_2).__next__()
        assert p2 == 0, f'{p2} != 0'

        p3 = self.part2(self.test_input_3).__next__()
        assert p3 == 4, f'{p3} != 4'

    def common(self, input_data):
        pass

    def part1(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')

        regexes = [
            'byr:.+',
            'iyr:.+',
            'eyr:.+',
            'hgt:.+',
            'hcl:.+',
            'ecl:.+',
            'pid:.+',
        ]
        
        passports = 0
        for pp in input_data:
            is_valid = True
            for regex in regexes:
                if re.search(regex, pp) == None:
                    is_valid = False
                    break
            
            if is_valid:
                passports += 1

        yield passports

    def part2(self, input_data):
        input_data = '\n'.join(input_data).split('\n\n')

        regexes = [
            r'byr:((19[2-9]\d)|(200[0-2]))',
            r'iyr:((201\d)|2020)',
            r'eyr:((202\d)|2030)',
            r'hgt:(((1(([5-8]\d)|(9[0-3])))cm)|((59)|(6\d)|(7[0-6])in))',
            r'hcl:(#[0-9a-f]{6})( |$|\n)',
            r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
            r'pid:(\d{9})( |$|\n)',
        ]

        passports = 0
        for pp in input_data:
            is_valid = True
            for regex in regexes:
                if re.search(regex, pp) == None:
                    is_valid = False
                    break
            
            if is_valid:
                passports += 1

        yield passports
