import unittest
import main

class TestClass(unittest.TestCase):
    def setUp(self):
        main.DEBUG = False

    def test_move1(self):
        main.Game_Level = 1
        main.Game_Screen = main.default()
        main.refresh_display(main.Game_Screen)
        #Game_Map=[ "NNNWWWNNNN",
        #           "NNNWGWNNNN",
        #           "NNNWNWWWWN",
        #           "NWWWBNBGWN",
        #           "NWGNBPWWWN",
        #           "NWWWWBWNNN",
        #           "NNNNWGWNNN",
        #           "NNNNWWWNNN"]
        main.move(1)
        answer = [ "NNNWWWNNNN",
                   "NNNWGWNNNN",
                   "NNNWNWWWWN",
                   "NWWWBNBGWN",
                   "NWGNBNWWWN",
                   "NWWWWPWNNN",
                   "NNNNWAWNNN",
                   "NNNNWWWNNN"]
        self.assertEqual(main.Game_Map, answer)

    def test_move2(self):
        main.Game_Level = 1
        main.Game_Screen = main.default()
        main.refresh_display(main.Game_Screen)
        main.move(1)
        main.move(0)
        answer = [ "NNNWWWNNNN",
                   "NNNWGWNNNN",
                   "NNNWNWWWWN",
                   "NWWWBNBGWN",
                   "NWGNBPWWWN",
                   "NWWWWNWNNN",
                   "NNNNWAWNNN",
                   "NNNNWWWNNN"]
        self.assertEqual(main.Game_Map, answer)

    def test_move3(self):
        main.Game_Level = 1
        main.Game_Screen = main.default()
        main.refresh_display(main.Game_Screen)
        for i in [1,0,2,2]:
            main.move(i)
        answer = [ "NNNWWWNNNN",
                   "NNNWGWNNNN",
                   "NNNWNWWWWN",
                   "NWWWBNBGWN",
                   "NWAPNNWWWN",
                   "NWWWWNWNNN",
                   "NNNNWAWNNN",
                   "NNNNWWWNNN"]
        self.assertEqual(main.Game_Map, answer)
        main.move(2)
        self.assertEqual(main.Game_Map, answer)

    def test_undo(self):
        main.Game_Level = 1
        main.Game_Screen = main.default()
        main.refresh_display(main.Game_Screen)
        for i in [1,0,2,2]:
            main.move(i)
        main.undo()
        answer = [ "NNNWWWNNNN",
                   "NNNWGWNNNN",
                   "NNNWNWWWWN",
                   "NWWWBNBGWN",
                   "NWGBPNWWWN",
                   "NWWWWNWNNN",
                   "NNNNWAWNNN",
                   "NNNNWWWNNN"]
        self.assertEqual(main.Game_Map, answer)

    def test_start_over(self):
        main.Game_Level = 1
        main.Game_Screen = main.default()
        main.refresh_display(main.Game_Screen)
        for i in [1,0,2,2]:
            main.move(i)
        main.start_over()
        answer = [ "NNNWWWNNNN",
                   "NNNWGWNNNN",
                   "NNNWNWWWWN",
                   "NWWWBNBGWN",
                   "NWGNBPWWWN",
                   "NWWWWBWNNN",
                   "NNNNWGWNNN",
                   "NNNNWWWNNN"]
        self.assertEqual(main.Game_Map, answer)

    def test_move4(self):
        main.Game_Level = 2
        main.Game_Screen = main.default()
        main.refresh_display(main.Game_Screen)

        #Game_Map=["WWWWWNNNN",
        #          "WPNNWNNNN",
        #          "WNBBWNWWW",
        #          "WNBNWNWGW",
        #          "WWWNWWWGW",
        #          "NWWNNNNGW",
        #          "NWNNNWNNW",
        #          "NWNNNWWWW",
        #          "NWWWWWNNN"]
        for i in [3,3,1,1,1,1,3,1,1,2,2,0,3,1,3,0,2,0,3,3,3,1,3,0]:
            main.move(i)
        answer = ["WWWWWNNNN",
                  "WNNNWNNNN",
                  "WNBNWNWWW",
                  "WNBNWNWGW",
                  "WWWNWWWAW",
                  "NWWNNNNPW",
                  "NWNNNWNNW",
                  "NWNNNWWWW",
                  "NWWWWWNNN"]
        self.assertEqual(main.Game_Map, answer)

if __name__=="__main__":
    unittest.main()
