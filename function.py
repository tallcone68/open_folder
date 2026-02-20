# kode pembantu banget
import os
import time
import subprocess

# exit jir
stop = False

# menu awal
while not stop:
      print('''Halo Raffi Mau Kubantu Apa kali ini?
          
1. cek internet
2. mirroring
3. masuk folder private
4. bersihkan cli
5. exit''')
    
      perintah = input("pilih opsi diatas memakai nomor atau command khusus : ")
    
      # cek internet
      if perintah == '1':
            while True:
                  print('''
1. speedtest
2. ping terus-menerus
3. ping ke website tertentu
4. bersihkan cli
5. menu''')
                  internet = input('pilih opsi diatas memakai nomor atau command khusus : ')

                  # speedtest
                  if internet == '1':
                        host = 'www.google.com'
                        print(f'ping 4 kali ke {host}')
                        os.system(f'ping {host}')

                  # ping terus-menerus
                  elif internet == '2':
                        host = 'www.google.com'
                        print(f'bersiap ping ke {host}....')
                        print('')
                        os.system(f'ping {host} -t')

                  # ping ke website tertentu
                  elif internet == '3':
                        host_custom = input("masukkan URL dari website disini : ")
                        while True:
                              print(f'''
1. ping 4 kali ke {host_custom}
2. ping terus-menerus ke {host_custom}''')
                              kustom = input('pilih berdasarkan nomor atau command khusus : ')
                              
                              # ping empat kali host_custom
                              if kustom == '1':
                                    print(f'ping 4 kali ke {host_custom}')
                                    os.system(f'ping {host_custom}')

                              # ping terus-menerus ke host_custom
                              elif kustom == '2':
                                    print(f'bersiap ping ke {host_custom}......')
                                    print('')
                                    os.system(f'ping {host_custom} -t')
                              
                              # cls
                              elif kustom == 'cls':
                                    os.system('cls')

                              # menu
                              elif kustom == 'exit':
                                    break

                              # perfectos
                              else:
                                    print('tolong ulangi input anda!')

                  # cls
                  elif internet == '4' or internet == 'cls':
                        os.system('cls')

                  # menu
                  elif internet == '5' or internet == 'exit':
                        break

                  # perfectos
                  else:
                        print('tolong ulangi input anda!!')

      # mirroring
      elif perintah == '2':
            while True:
                  print('''
1. mirroring pakai kabel
2. mirroring wireless(hp tertentu)
3. devices list
4. setings
5. bersihkan cli
6. menu''')
                  adb = input('pilih berdasarkan nomor atau command tertentu : ')

                  # mirroring pakai kabel
                  if adb == '1':
                        while True:
                              print('''
1. sertakan audio
2. tidak perlu sertakan audio''')
                              kabel = input('pilih berdasarkan nomor atau command khusus :')

                              # sertakan audio
                              if kabel == '1':
                                    path = 'd:/dekstop 2/scrcpy/adb'
                                    os.chdir(path)
                                    os.system(r'.\scrcpy -d')
                              
                              # tidak perlu sertakan audio
                              elif kabel == '2':
                                    path = 'd:/dekstop 2/scrcpy/adb'
                                    os.chdir(path)
                                    os.system(r'.\scrcpy -d --no-audio')

                              # cls
                              elif kabel == 'cls':
                                    os.system('cls')

                              # menu
                              elif kabel == 'exit':
                                    break

                              # perfectos
                              else:
                                    print('tolong ulangi input anda!!')

                  # mirrorig wireless
                  elif adb == '2':
                        while True:
                              print('''
1. sertakan audio
2. tidak perlu sertakan audio''')
                              kabel = input('pilih berdasarkan nomor atau command khusus :')

                              # sertakan audio
                              if kabel == '1':
                                    path = 'd:/dekstop 2/scrcpy/adb'
                                    os.chdir(path)
                                    os.system(r'.\scrcpy -e')
                              
                              # tidak perlu sertakan audio
                              elif kabel == '2':
                                    path = 'd:/dekstop 2/scrcpy/adb'
                                    os.chdir(path)
                                    os.system(r'.\scrcpy -e --no-audio')

                              # cls
                              elif kabel == 'cls':
                                    os.system('cls')

                              # menu
                              elif kabel == 'exit':
                                    break

                              # perfectos
                              else:
                                    print('tolong ulangi input anda!!')

                  # devices list
                  elif adb == '3':
                        path = 'd:/dekstop 2/scrcpy/adb'
                        os.chdir(path)
                        os.system(r'.\adb devices')
                  
                  # settings
                  elif adb == '4':
                        scrcpy = 'd:/dekstop 2/scrcpy/adb'
                        command = f'start powershell -noexit -command "cd \'{scrcpy}\'"'
                        os.system(command)

                  # cls
                  elif adb == 'cls' or adb == '5':
                        os.system('cls')

                  # menu
                  elif adb == 'exit' or adb == '6':
                        break

                  # perfectos
                  else:
                        print('tolong ulangi input anda!!')

      # masuk folder folder private
      elif perintah == '3' or perintah == '/private':
            shena = 'shena.py'
            letak = 'd:/dekstop 2/vs code/project/private'
            subprocess.Popen(['powershell.exe', '-command', f'python {shena}'],
                             cwd = letak,
                             creationflags=subprocess.CREATE_NEW_CONSOLE
                             )
            print('''
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  sedang menjalankan shena.py.....
                  
                  
                  
                  ''')
            
      # cls
      elif perintah == '4' or perintah == 'cls':
            os.system('cls')

      # exit
      elif perintah == '5' or perintah == 'exit':
            while True:
                  konfirmasi = input('yakin ingin keluar (y/n) : ')
                  
                  # yakin
                  if konfirmasi == 'y':
                        print('log out....')
                        stop = True
                        break

                  # gak yakin
                  elif konfirmasi == 'n':
                        break

                  # perfectos
                  else:
                        print('tolong masukkan input (y) atau (n)')