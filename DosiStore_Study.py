from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import unittest, time

class Test(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        options.add_argument('--incognito')
        #options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)


    #GNB 메뉴 이동 확인 테스트 (Home / Explore / Marketplace / Notice)
    @unittest.skip("pass") 
    def test_GNB(self):
        time.sleep(1)
        self.driver.get("https://opsteststore1-dosi-store.line-apps-beta.com/")
        
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Explore']").click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, "https://opsteststore1-dosi-store.line-apps-beta.com/explore")
        print("explore 이동 확인")
    
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Marketplace']").click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, "https://opsteststore1-dosi-store.line-apps-beta.com/marketplace")
        print("marketplace 이동 확인")

        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Notice']").click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, "https://opsteststore1-dosi-store.line-apps-beta.com/notice")
        print("Notice 이동 확인")
        
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Home']").click()
        time.sleep(5)
        self.assertEqual(self.driver.current_url, "https://opsteststore1-dosi-store.line-apps-beta.com/")
        print("Home 이동 확인")
    
    
    
    #GNB 메뉴 이동 확인 테스트 (Discode / twitter / wallet)
    @unittest.skip("pass")
    def test_GNB2(self): #디스코드 / 트위터 / Wallet GNB 확인 테스트
        time.sleep(1)
        self.driver.get("https://opsteststore1-dosi-store.line-apps-beta.com/")
        time.sleep(5)
                
        time.sleep(3)
        discord_btn = self.driver.find_element(By.XPATH, "//*[@id='__next']//header/div/div[3]/ul/a[1]")
        discord_btn.click()
        
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get_window_position(self.driver.window_handles[1])

        time.sleep(1)
        self.assertEqual(self.driver.current_url, "https://discord.com/invite/SCkEdqTJG7")
        print("Discord 초대 화면 진입 확인")
        self.driver.close()
        time.sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        self.driver.get_window_position(self.driver.window_handles[0])
        
        time.sleep(3)
        twitter_btn = self.driver.find_element(By.XPATH, "//*[@id='__next']//header/div/div[3]/ul/a[2]/div/div")
        twitter_btn.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get_window_position(self.driver.window_handles[1])
        
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "https://twitter.com/DOSI_official")
        print("Twitter 화면 진입 확인")
        self.driver.close()
        time.sleep(1)
        
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        self.driver.get_window_position(self.driver.window_handles[0])
        
        time.sleep(3)
        wallet_btn = self.driver.find_element(By.XPATH,"//*[@id='__next']//header/div/div[3]/ul/div[1]/div")
        wallet_btn.click()
        
        



    #페이지 선호 언어 변경 테스트
    @unittest.skip("pass")
    def test_ChangeLanguage(self):
        time.sleep(1)
        self.driver.get("https://opsteststore1-dosi-store.line-apps-beta.com/")
        time.sleep(10)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #스크롤 끝까지 내리기
        time.sleep(2)
        
        default_language = self.driver.find_element(By.XPATH, "//*[@id='menu-button-:R5bakjf5tmH1:']/span")
        if default_language.text == 'English' : #기본 언어 영어 설정 상태 시, 반환
            return
        
        else :
            self.driver.find_element(By.XPATH, "//*[@id='menu-button-:R5bakjf5tmH1:']").click() #언어 변경 버튼 선택
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[text()='English']").click() #English 선택
            time.sleep(1)
            self.assertEqual(self.driver.current_url, "https://opsteststore1-dosi-store.line-apps-beta.com/en-US")
            print("페이지 선호 언어 변경 확인")
            
    
    
    #XLT 확인 테스트
    @unittest.skip("pass")
    def test_XLT(self):
        time.sleep(1)
        self.driver.get("https://opsteststore1-dosi-store.line-apps-beta.com/")
        time.sleep(10)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #스크롤 끝까지 내리기
        time.sleep(2)
        
        #default_language = self.driver.find_element(By.XPATH, "//*[@id='menu-button-:R5bakjf5tmH1:']/span")
        #if default_language.text == 'English' : #기본 언어 영어 설정 상태 시, 반환
        
        xlt_1 = self.driver.find_element(By.XPATH,'//*[@id="__next"]//div/div/ul/li[1]/a').text
        print(xlt_1)
        
        if xlt_1 == "서비스 이용 약관" :
            print("XLT 확인 완료")
        else : 
            print("XLT 확인 Fail")
        
        xlt_2 = self.driver.find_element(By.XPATH, '//*[@id="__next"]//div/div/ul/li[3]/a').text
        print(xlt_2)
        
        if xlt_2 == "개인정보 수집 및 이용 동의서" :
            print("XLT 확인 완료")
        else : 
            print("XLT 확인 Fail")
            
        xlt_3 = self.driver.find_element(By.XPATH, '//*[@id="__next"]//div/div/ul/li[5]/a').text
        print(xlt_3)
        
        if xlt_3 == "광고성 정보수신동의서" :
            print("XLT 확인 완료")
        else : 
            print("XLT 확인 Fail")
            
            
    #Login 테스트
    @unittest.skip("pass")       
    def test_LoginLINE(self):
        time.sleep(1)
        self.driver.get("https://opsteststore1-dosi-store.line-apps-beta.com/")
        time.sleep(10)
        
        wallet_btn = self.driver.find_element(By.XPATH,"//*[@id='__next']//header/div/div[3]/ul/div[1]/div")
        wallet_btn.click()
        
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get_window_position(self.driver.window_handles[1])
        
        time.sleep(3)
        LineLoginBtn= self.driver.find_element(By.XPATH, "//*[@id='social-providers']/a[1]")
        LineLoginBtn.click()
        
        time.sleep(3)
        email_textfield = self.driver.find_element(By.NAME, 'tid')
        email_textfield.send_keys('34353644@yopmail.com') 
        password_textfield = self.driver.find_element(By.NAME, 'tpasswd')
        password_textfield.send_keys('linepay123!')
        
        login_btn = self.driver.find_element(By.CLASS_NAME, 'MdBtn01')
        login_btn.send_keys(Keys.ENTER)
        
        try:
            time.sleep(5)
            allow_btn = self.driver.find_element(By.XPATH, '//*[@class="c-button l-btn c-button--allow"]')
            allow_btn.click()
        except:
            print('PASS: (Allow) There is nothing to be allowed.')
            pass


        #월렛 연동 화면
        time.sleep(10)
        Wallet_login_confirmBtn = self.driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/div/div/button')

        time.sleep(1)
        act = ActionChains(self.driver)
        act.move_to_element(Wallet_login_confirmBtn).move_by_offset(0,-20).click().perform()
        
        #창전환
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0]) 
        self.driver.get_window_position(self.driver.window_handles[0])



if __name__ == "__main__":
    try:
        test_suite = unittest.TestSuite()

        test_suite.addTest(Test('test_GNB'))
        test_suite.addTest(Test('test_GNB2'))
        test_suite.addTest(Test('test_ChangeLanguage'))
        test_suite.addTest(Test('test_XLT'))
        test_suite.addTest(Test('test_LoginLINE'))

        runner = unittest.TextTestRunner()
        runner.run(test_suite)
    except:
        print('TEST ERROR: Failed to perform unit test.')