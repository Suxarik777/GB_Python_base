import html_creator as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

#xg.new_create(dp.data_collection()) # в данном случае получается что мы в том числе и получаем данные 
# т . к . там return data

# поэтому возьмём эти данные и отправим сразу в генерацию html
hc.new_create(xg.new_create(dp.data_collection()))