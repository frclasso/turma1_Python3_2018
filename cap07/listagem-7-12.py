s = 'Corrupção, corrução ou corrompimento, em sentido lato, corresponde à ' \
    'ideia de decomposição. Na esfera das relações humanas em particular, está' \
    ' relacionado ao subornoː[1] ato ou efeito de se corromper, oferecer algo para ' \
    'obter vantagem em negociata onde se favorece uma pessoa e se prejudica outra.' \
    ' Busca oferecer ou prometer vantagem indevida a qualquer pessoa, para determiná-lo' \
    ' a praticar, omitir ou retardar ato de ofício, conforme o artigo 333 do ' \
    'Código Penal brasileiro de 1940.[2]' \
    'Segundo Calil Simão, é pressuposto necessário, para instalação da corrupção, ' \
    'a ausência de interesse ou compromisso com o bem comum. "A corrupção social ' \
    'ou estatal é caracterizada pela incapacidade moral dos cidadãos de assumir ' \
    'compromissos voltados ao bem comum. Vale dizer, os cidadãos mostram-se ' \
    'incapazes de fazer coisas que não lhes tragam uma gratificação pessoal' \
    'Entre os crimes contra a administração pública previstos no Código Penal ' \
    'Brasileiro, estão o exercício arbitrário ou abuso de poder, a falsificação ' \
    'de papéis públicos, a má-gestão praticada por administradores públicos, ' \
    'a apropriação indébita previdenciária, a lavagem ou ocultação de bens' \
    ' oriundos de corrupção, emprego irregular de verbas ou rendas públicas, ' \
    'contrabando ou descaminho, a corrupção ativa e passiva, entre outros.[3]'

p =0
while p <= len(s):
    p = s.find('corrupção', p)
    if p >= 0:
        print('Posicao: ', p)
        p += 1