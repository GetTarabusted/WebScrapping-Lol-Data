# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:07:06 2021

@author: android01
"""

stats = [{'type': 'ARAM', 'date': 'May 7 2021 7:34 PM', 'win': 'Victory', 'duration': '23m 9s', 
          'champion': 'Kalista', 'kda': [18, 16, 29], 'cs': 93, 'gold': 19016, 'champDamage': 35946, 'takenDamage': 44647}, 
         
         {'type': 'ARAM', 'date': 'May 7 2021 3:52 PM', 'win': 'Defeat', 'duration': '22m 26s', 
          'champion': 'Nasus', 'kda': [14, 15, 17], 'cs': 69, 'gold': 17102, 'champDamage': 30951, 'takenDamage': 53533}, 
         
         {'type': 'ARAM', 'date': 'May 7 2021 3:26 PM', 'win': 'Defeat', 'duration': '23m 0s', 
          'champion': 'Diana', 'kda': [10, 14, 24], 'cs': 48, 'gold': 15618, 'champDamage': 22369, 'takenDamage': 31751}, 
         
         {'type': 'ARAM', 'date': 'May 7 2021 3:00 PM', 'win': 'Victory', 'duration': '20m 58s', 
          'champion': 'Xerath', 'kda': [9, 10, 28], 'cs': 47, 'gold': 14288, 'champDamage': 40192, 'takenDamage': 19782}, 
         
         {'type': 'ARAM', 'date': 'May 7 2021 11:20 AM', 'win': 'Victory', 'duration': '13m 36s', 
          'champion': 'Vayne', 'kda': [11, 6, 12], 'cs': 38, 'gold': 11564, 'champDamage': 16830, 'takenDamage': 16688}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 11:49 AM', 'win': 'Defeat', 'duration': '19m 16s', 
          'champion': 'Akali', 'kda': [12, 10, 9], 'cs': 25, 'gold': 12804, 'champDamage': 14642, 'takenDamage': 21454}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 11:25 AM', 'win': 'Victory', 'duration': '14m 6s', 
          'champion': 'Gwen', 'kda': [4, 7, 17], 'cs': 21, 'gold': 9728, 'champDamage': 8866, 'takenDamage': 18348}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 11:08 AM', 'win': 'Defeat', 'duration': '25m 59s', 
          'champion': 'Zed', 'kda': [8, 12, 21], 'cs': 47, 'gold': 15657, 'champDamage': 33995, 'takenDamage': 27799}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 10:38 AM', 'win': 'Defeat', 'duration': '24m 5s', 
          'champion': 'Qiyana', 'kda': [12, 14, 21], 'cs': 23, 'gold': 15112, 'champDamage': 23402, 'takenDamage': 27931}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 10:12 AM', 'win': 'Defeat', 'duration': '18m 36s', 
          'champion': 'Sylas', 'kda': [3, 10, 15], 'cs': 19, 'gold': 10687, 'champDamage': 17760, 'takenDamage': 27784}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 9:49 AM', 'win': 'Defeat', 'duration': '19m 17s', 
          'champion': 'Darius', 'kda': [5, 15, 20], 'cs': 23, 'gold': 11591, 'champDamage': 14986, 'takenDamage': 40368}, 
         
         {'type': 'ARAM', 'date': 'May 3 2021 9:26 AM', 'win': 'Defeat', 'duration': '13m 23s', 
          'champion': 'Irelia', 'kda': [7, 10, 5], 'cs': 69, 'gold': 10378, 'champDamage': 11208, 'takenDamage': 24086}, 
         
         {'type': 'ARAM', 'date': 'Apr 29 2021 7:38 PM', 'win': 'Victory', 'duration': '17m 25s', 
          'champion': 'Tryndamere', 'kda': [13, 10, 21], 'cs': 49, 'gold': 14027, 'champDamage': 26793, 'takenDamage': 26264}, 
         
         {'type': 'ARAM', 'date': 'Apr 29 2021 7:16 PM', 'win': 'Defeat', 'duration': '14m 53s', 
          'champion': 'Katarina', 'kda': [6, 7, 4], 'cs': 26, 'gold': 9525, 'champDamage': 10420, 'takenDamage': 14183}, 
         
         {'type': 'ARAM', 'date': 'Apr 29 2021 3:18 PM', 'win': 'Victory', 'duration': '16m 35s', 
          'champion': 'Rumble', 'kda': [12, 8, 18], 'cs': 30, 'gold': 12514, 'champDamage': 21470, 'takenDamage': 13896}, 
         
         {'type': 'ARAM', 'date': 'Apr 29 2021 2:57 PM', 'win': 'Defeat', 'duration': '32m 34s', 
          'champion': 'Kassadin', 'kda': [30, 20, 21], 'cs': 88, 'gold': 25029, 'champDamage': 62370, 'takenDamage': 51866}, 
         
         {'type': 'ARAM', 'date': 'Apr 29 2021 2:20 PM', 'win': 'Defeat', 'duration': '12m 28s', 
          'champion': 'Wukong', 'kda': [15, 10, 9], 'cs': 16, 'gold': 11347, 'champDamage': 18543, 'takenDamage': 16511}, 
         
         {'type': 'ARAM', 'date': 'Apr 27 2021 12:09 PM', 'win': 'Defeat', 'duration': '25m 38s', 
          'champion': 'Tryndamere', 'kda': [20, 15, 19], 'cs': 91, 'gold': 19476, 'champDamage': 39007, 'takenDamage': 45001}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 6:44 PM', 'win': 'Victory', 'duration': '24m 55s', 
          'champion': 'Tryndamere', 'kda': [13, 8, 29], 'cs': 87, 'gold': 18281, 'champDamage': 31344, 'takenDamage': 33921}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 4:42 PM', 'win': 'Victory', 'duration': '22m 53s', 
          'champion': 'Azir', 'kda': [5, 12, 27], 'cs': 54, 'gold': 14747, 'champDamage': 35319, 'takenDamage': 23473}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 4:14 PM', 'win': 'Defeat', 'duration': '20m 59s', 
          'champion': "Kai'Sa", 'kda': [8, 9, 26], 'cs': 22, 'gold': 13083, 'champDamage': 25772, 'takenDamage': 17985}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 3:47 PM', 'win': 'Victory', 'duration': '14m 41s', 
          'champion': 'Samira', 'kda': [12, 8, 14], 'cs': 49, 'gold': 11275, 'champDamage': 26512, 'takenDamage': 20985}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 2:26 PM', 'win': 'Defeat', 'duration': '17m 33s', 
          'champion': 'Zoe', 'kda': [7, 7, 10], 'cs': 36, 'gold': 11868, 'champDamage': 19311, 'takenDamage': 17414}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 12:18 PM', 'win': 'Victory', 'duration': '16m 42s', 
          'champion': 'Samira', 'kda': [23, 9, 16], 'cs': 65, 'gold': 16009, 'champDamage': 26750, 'takenDamage': 25684}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 11:55 AM', 'win': 'Defeat', 'duration': '19m 13s', 
          'champion': 'Rammus', 'kda': [5, 11, 16], 'cs': 39, 'gold': 12481, 'champDamage': 15265, 'takenDamage': 30221}, 
         
         {'type': 'ARAM', 'date': 'Apr 26 2021 10:31 AM', 'win': 'Defeat', 'duration': '18m 22s', 
          'champion': 'Sylas', 'kda': [5, 12, 21], 'cs': 18, 'gold': 10986, 'champDamage': 16581, 'takenDamage': 32365}, 
         
         {'type': 'ARAM', 'date': 'Apr 25 2021 7:36 PM', 'win': 'Defeat', 'duration': '23m 51s', 
          'champion': 'Katarina', 'kda': [14, 14, 17], 'cs': 57, 'gold': 16290, 'champDamage': 43531, 'takenDamage': 35112}, 
         
         {'type': 'ARAM', 'date': 'Apr 25 2021 7:07 PM', 'win': 'Victory', 'duration': '21m 21s', 
          'champion': 'Ornn', 'kda': [10, 10, 34], 'cs': 37, 'gold': 15361, 'champDamage': 32328, 'takenDamage': 55813}, 
         
         {'type': 'ARAM', 'date': 'Apr 25 2021 6:43 PM', 'win': 'Victory', 'duration': '23m 13s', 
          'champion': 'Katarina', 'kda': [9, 9, 12], 'cs': 57, 'gold': 14815, 'champDamage': 23955, 'takenDamage': 23852}, 
         
         {'type': 'ARAM', 'date': 'Apr 25 2021 6:11 PM', 'win': 'Defeat', 'duration': '12m 50s', 
          'champion': 'Master Yi', 'kda': [3, 9, 5], 'cs': 35, 'gold': 7916, 'champDamage': 5591, 'takenDamage': 12531}, 
         
         {'type': 'ARAM', 'date': 'Apr 23 2021 7:19 PM', 'win': 'Defeat', 'duration': '11m 59s', 
          'champion': 'Zed', 'kda': [4, 6, 11], 'cs': 47, 'gold': 8562, 'champDamage': 8937, 'takenDamage': 9529}, 
         
         {'type': 'ARAM', 'date': 'Apr 20 2021 5:58 PM', 'win': 'Defeat', 'duration': '12m 53s', 
          'champion': 'Yone', 'kda': [3, 8, 7], 'cs': 37, 'gold': 8381, 'champDamage': 8114, 'takenDamage': 14478}, 
         
         {'type': 'One for All', 'date': 'Apr 19 2021 11:33 PM', 'win': 'Defeat', 'duration': '22m 25s', 
          'champion': 'Darius', 'kda': [22, 11, 7], 'cs': 76, 'gold': 8550, 'champDamage': 4669, 'takenDamage': 28462}, 
         
         {'type': 'ARAM', 'date': 'Apr 8 2021 2:45 PM', 'win': 'Victory', 'duration': '19m 58s', 
          'champion': 'Ornn', 'kda': [14, 11, 30], 'cs': 61, 'gold': 15719, 'champDamage': 23792, 'takenDamage': 41401}, 
         
         {'type': 'ARAM', 'date': 'Apr 8 2021 2:21 PM', 'win': 'Defeat', 'duration': '14m 13s', 
          'champion': 'Thresh', 'kda': [13, 5, 16], 'cs': 35, 'gold': 11961, 'champDamage': 14987, 'takenDamage': 23570}, 
         
         {'type': 'ARAM', 'date': 'Mar 29 2021 2:31 PM', 'win': 'Victory', 'duration': '17m 32s', 
          'champion': 'Kennen', 'kda': [10, 10, 24], 'cs': 29, 'gold': 13067, 'champDamage': 22169, 'takenDamage': 21833}, 
         
         {'type': 'ARAM', 'date': 'Mar 28 2021 6:09 PM', 'win': 'Defeat', 'duration': '21m 31s', 
          'champion': 'Xerath', 'kda': [8, 11, 24], 'cs': 50, 'gold': 14345, 'champDamage': 34532, 'takenDamage': 23371}, 
         
         {'type': 'ARAM', 'date': 'Mar 24 2021 6:44 PM', 'win': 'Victory', 'duration': '22m 29s', 
          'champion': 'Cassiopeia', 'kda': [5, 13, 10], 'cs': 49, 'gold': 14334, 'champDamage': 15237, 'takenDamage': 25475}, 
         
         {'type': 'ARAM', 'date': 'Mar 24 2021 6:19 PM', 'win': 'Victory', 'duration': '17m 57s', 
          'champion': 'Sion', 'kda': [5, 11, 16], 'cs': 26, 'gold': 11381, 'champDamage': 10058, 'takenDamage': 40068}, 
         
         {'type': 'ARAM', 'date': 'Mar 24 2021 5:58 PM', 'win': 'Defeat', 'duration': '9m 32s', 
          'champion': 'Kayn', 'kda': [7, 7, 7], 'cs': 19, 'gold': 7243, 'champDamage': 8729, 'takenDamage': 9404}, 
         
         {'type': 'ARAM', 'date': 'Mar 24 2021 5:43 PM', 'win': 'Victory', 'duration': '15m 52s', 
          'champion': 'Mordekaiser', 'kda': [1, 8, 13], 'cs': 37, 'gold': 9678, 'champDamage': 8811, 'takenDamage': 19890}]