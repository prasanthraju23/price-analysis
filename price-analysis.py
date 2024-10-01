def price_analysis(self,link):
        self.driver.get("https://pricehistoryapp.com/")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter name or paste the product link']").send_keys(link+Keys.ENTER)
        sleep(4)
        text = self.driver.find_element(By.XPATH,"//div[@class='content-width mx-auto px-3']").text
        for i in range(len(text)):
            if text[i:i+5] == '. Thi':
                text = text[i+1:]
                break
        
        price_pattern = re.compile(r'(\d+(\.\d+)?)')
        pcur, pmin, pavg, pmax = list(map(float,[match[0] for match in price_pattern.findall(text)]))
        
        if pavg > pcur:
            fairness = 50+(pavg-pcur)*50/(pavg-pmin)
        elif pavg < pcur:
            fairness = 50-(pcur-pavg)*50/(pmax-pavg)
        else:
            fairness = 50
            
        con = self.driver.find_element(By.XPATH,"//p[@class='text-gray-500 dark:text-gray-400 text-sm']").text
        url = self.driver.current_url.replace('/product/','/embed/')
        
        return {'fairness':fairness,'url':url,'context':con,'current':pcur}
    def stop(self):
        self.driver.quit() 
