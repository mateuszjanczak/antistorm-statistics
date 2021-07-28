from webbot import Browser

web = Browser(showWindow = False)
web.go_to('antistorm.eu')
web.type('Dąbrowa Tarnowska', id = 'autocompl')
html = web.find_elements(id = "dodatkoweInformacje")[0].get_attribute('outerHTML')

print(html)