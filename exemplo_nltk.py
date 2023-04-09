import nltk
from nltk.chat.util import Chat, reflections

reflections_pt = {
    'eu': 'você',
    'eu sou': 'você é',
    'eu era': 'você era',
    'eu iria': 'você iria',
    'eu irei': 'você irá',
    'meu': 'seu',
    'você': 'eu',
    'você é': 'eu sou',
    'você era': 'eu era',
    'você irá': 'eu irei',
    'seu': 'meu'
}

pares = [
    [
        r'oi|olá|opa|oie',
        ['olá', 'como vai?', 'tudo bem?']
    ],
    [
        r'qual o seu nome?',
        ['Meu nome é chat e sou um chatbot']
    ],
    [
        r'(.*) idade?',
        ['Não tenho idade, mas fui criado uns dias atrás']
    ],
    [
        r'meu nome é (.*)',
        ['Olá %1']
    ],
    [
        r'eu trabalho na empresa (.*)',
        ['Eu conheço a empresa %1']
    ],
    [
        r'(.*) (cidade|país)',
        ['São Paulo, SP, Brasil']
    ],
    [
        r'quit',
        ['Até mais!']
    ]
]

print('Olá! sou o chat!')
chat = Chat(pares, reflections_pt)
chat.converse()