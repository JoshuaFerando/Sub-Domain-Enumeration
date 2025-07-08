import requests
import threading
import time


# Subdomain Enumeration Class
# This class is used to perform multi-threaded subdomain enumeration
# using a given wordlist by sending HTTP GET requests and checking for live subdomains.


class subdomainEnumeration:
    
    # Initialize the enumeration object with path, base URL, word count, and thread count
    def __init__(self, wordlist_path,url,count,total_threads):
        self.wordlist_path = wordlist_path
        self.total_threads = total_threads
        self.count=count
        self.wordlist = self.load_wordlist()
        self.url=url
        self.attack_url=self.create_attack_url()

    # Loads the wordlist from the given file path.
    # Strips each line and adds it to the list.
    def load_wordlist(self):
        try:
          
            with open(self.wordlist_path, 'r') as file:
                wordlist=[]
                for line in file:
                    username = line.strip()
                    wordlist.append(username)
                    self.count+=1
                return wordlist
            file.close()
        except FileNotFoundError:
            print(f"[!] File not found: {self.wordlist_path}")
            return []
        
    # Display Attack Details
    def display_wordlist(self):
            print("*"*35)
            print("Target URL:",self.url)
            print("Wordlist Used:",self.wordlist_path)
            print("Total Sub-Domain To check:",self.count)
            print("*"*35,"\n\n")
            print("The Various Sub-Domains found are...\n")


    
    # Create complete subdomain URLs from base URL and wordlist
    def create_attack_url(self):
        attack_url=[]
        for i in range (0,self.count):
            url=self.url+"/"+self.wordlist[i]
            attack_url.append(url)
        return attack_url
    
    # Send HTTP GET requests to subdomains in the given index range.
    # Print URLs with HTTP 200 (OK) response.
    def attack_single(self,start_index,end_index):
        for i in range (start_index,end_index):
            url=self.attack_url[i]
            try:
                response = requests.get(url)
                response_code=response.status_code
                if (response_code==200):
                    print(url,end="\n")
                
            except (ConnectionError,ConnectionResetError,ConnectionRefusedError,ConnectionAbortedError) as e:
                time.sleep(1)
                print("Going except")
                i-=1
               
    # Launch multiple threads to perform subdomain enumeration concurrently    
    def attack_multi(self):
        counter=0
        while(counter<self.total_threads):
            start_index=int(self.count/self.total_threads*(counter))
            end_index=int(self.count/self.total_threads*(counter+1))
            (threading.Thread(target=self.attack_single, args=(start_index,end_index))).start()
            counter+=1


def banner():
    print(
        """
███████╗██╗   ██╗██████╗       ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██╔════╝██║   ██║██╔══██╗      ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████╗██║   ██║██████╔╝█████╗██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    █████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
╚════██║██║   ██║██╔══██╗╚════╝██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
███████║╚██████╔╝██████╔╝      ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚══════╝ ╚═════╝ ╚═════╝       ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝
                                                                                                                    

        CLI Subdomain Enumerator 
        """)


if __name__ == "__main__":

    banner()

    # Configuration
    url = "https://www.google.com"
    wordlist_path = "small.txt"
    # Increasing the total_threads can create ConnectionReset Erro.If such reduce the value
    total_threads=72
    count=0

    # Create instance and start attack
    subEnum=subdomainEnumeration(wordlist_path,url,count,total_threads)
    subEnum.display_wordlist()
    subEnum.attack_multi()



