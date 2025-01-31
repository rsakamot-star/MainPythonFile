import requests
import webbrowser

class openwindow:
    def __init__(self,score,name,zenith,energy):
        self.opend_url = False
        self.score = score
        self.name = name
        self.energy = str(energy[1:])[1:-1].replace(' ', '')
        self.zenith = str(zenith[1:])[1:-1].replace(' ', '')
        self.flag = True
        self.n = 5
    def send_score(self):
        url = "https://rsakamoto.pythonanywhere.com/update_score"
        params = {"score":str(round(self.score, 1)), "name":self.name,"zenith":self.zenith,"energy":self.energy}
        try:
            requests.get(url, params=params, timeout=(self.n,self.n))
            webbrowser.open("https://rsakamoto.pythonanywhere.com")
            self.flag = False
        except:
            #n += 1
            #print(n)
            requests.get(url, params=params, timeout=(100,100))
            webbrowser.open("https://rsakamoto.pythonanywhere.com")
            self.flag = False



