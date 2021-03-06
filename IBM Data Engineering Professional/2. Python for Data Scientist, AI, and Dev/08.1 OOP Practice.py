source: https://www.youtube.com/watch?v=C0p5570Ggng&list=PL3PVN2diT6UPG9DOVzXjmVdaiILJ-hRXg&index=3&t=17s

---------------------------------------------------------------------------------------------------------------
#Simple function

programmer = 'eka'
def programmer_makan():
  print('{} makan nasi'.format(programmer))

petani = 'putra'
def petani_makan():
  print('{} makan nasi'.format(petani))

dokter = 'putri'
def dokter_makan():
  print('{} makan nasi'.format(dokter))

programmer_makan()
petani_makan()
dokter_makan()

#output
eka makan nasi
putra makan nasi
putri makan nasi

---------------------------------------------------------------------------------------------------------------
#class 1 fungsi dan 1 variabel 'nama'

class Manusia(object):
  nama = None

  def makan(self):
    print('{} makan nasi'.format(self.nama))

#manusia kalau belum lahir belum bisa makan, maka lahirkan dulu dengan var programmer baru bisa makan
programmer = Manusia()      #lahirkan dulu - ini adalah buat object
programmer.makan()          #fungsi 'makan' baru bisa dipanggil kalau ada objectnya

#output
None makan nasi

---------------------------------------------------------------------------------------------------------------
#Diberi nama

class Manusia(object):
  nama = None

  #fungsi konstruktor
  def __init__(self,nama): #buat funsi init yang menerima nama
    self.nama = nama 

  def makan(self):
    print('{} makan nasi'.format(self.nama))

programmer = Manusia('Eka') 
programmer.makan()

petani = Manusia('Putra') 
petani.makan()

dokter = Manusia('Putri') 
dokter.makan()

#output
Eka makan nasi
Putra makan nasi
Putri makan nasi

---------------------------------------------------------------------------------------------------------------
#Inheritence(keturunan/warisan)- dengan class Manusia di atas

class ManusiaMilenial(Manusia):
  email = None

  def set_email(self, email):
    self.email = email

  def info(self):
    print('nama = {}, email = {}'.format(self.nama, self.email))

programmer = ManusiaMilenial('Eka')
programmer.set_email('eka@gmail.com')
programmer.info()

#output
nama = Eka, email = eka@gmail.com

---------------------------------------------------------------------------------------------------------------
#Encapsulation - Memberikan akses private tertentu

class ManusiaMilenial(Manusia):
  email = None
  
  #__ artinya access private
  __password = None

  def set_email(self, email):
    self.email = email

  def set_pass(self,password):
    self.__password = password

  def __samarkan_password(self):
    return self.__password.replace(self.__password[:3], '*'*3)

  def info(self):
    print('nama = {}, email = {}, pass = {}'.format(self.nama, self.email, self.__samarkan_password()))

programmer = ManusiaMilenial('Eka')
programmer.set_email('eka@gmail.com')
programmer.set_pass('patrickstar')

programmer.info()

#output
nama = Eka, email = eka@gmail.com, pass = ***rickstar

---------------------------------------------------------------------------------------------------------------
#polymorphisme - banyak bentuk dengan attribute berbeda

class Programmer(ManusiaMilenial):
  def info(self):
    print('nama : {}, email : {}'.format(self.nama, self.email))

class Influencer(ManusiaMilenial):
   def info(self):
    print('nama = {} / email = {}'.format(self.nama, self.email))

orang = ManusiaMilenial('Aldi')
orang.set_email('aldira@gmail.com')
orang.set_pass('spongebob')
orang.info()

programmer = Programmer('Eka')
programmer.set_email('eka@gmail.com')
programmer.set_pass('patrickstar')
programmer.info()

influencer = Influencer('Putra')
influencer.set_email('putra@gmail.com')
influencer.set_pass('patrickstar12')
influencer.info()

#output
nama = Aldi, email = aldira@gmail.com, pass = ***ngebob
nama : Eka, email : eka@gmail.com
nama = Putra / email = putra@gmail.com
