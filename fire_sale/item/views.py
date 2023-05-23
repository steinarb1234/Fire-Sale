from django.shortcuts import render, get_object_or_404
from item.models import Item


def index(request):
    return render(request, 'home/index.html', context={
        'favorite_categories': [
            {'name': 'Fashion',
             'items': [
                 {'name': 'Helmet',
                  'price': '50',
                  'image': 'https://images.unsplash.com/photo-1567954970774-58d6aa6c50dc?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80'
                  },
                 {'name': 'Flower',
                  'price': '6',
                  'image': 'https://plus.unsplash.com/premium_photo-1676478746758-fc6c01e6a96d?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'
                  },
                 {'name': 'My hat',
                  'price': '500',
                  'image': 'https://images.unsplash.com/photo-1521369909029-2afed882baee?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80'
                  },
                 {'name': 'Pink banana socks, very cool, very nice',
                  'price': '15',
                  'image': 'https://images.unsplash.com/photo-1564379976409-79bd0786fff1?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80'
                  },
                 {'name': 'Cool jeans',
                  'price': '60',
                  'image': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'
                  },
                 {'name': 'Skeleton hand tshirt',
                  'price': '9',
                  'image': 'https://images.unsplash.com/photo-1503341504253-dff4815485f1?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'
                  },
                 {'name': 'Flower dress',
                  'price': '12',
                  'image': 'https://images.unsplash.com/photo-1546728151-7124a03bd1db?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'
                  }
             ]},
            {'name': 'Cars',
             'items': [
                 {'name': 'Toyota Corolla 2016',
                  'price': '50',
                  'image': 'https://images.unsplash.com/photo-1626072557464-90403d788e8d?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80'
                  },
                 {'name': 'Strumpastrætó',
                  'price': '6000000',
                  'image': ''
                  },
                 {'name': 'Ford Mustang',
                  'price': '50',
                  'image': ''
                  },
                 {'name': 'Gamla druslan hans afa',
                  'price': '500000',
                  'image': ''
                  }
             ]},
            {'name': 'Trains',
             'items': [
                 {'name': 'Helmet',
                  'price': '50',
                  'image': 'https://images.unsplash.com/photo-1567954970774-58d6aa6c50dc?ixlib=rb-4.0.3&ixid'
                           '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80'
                  },
                 {'name': 'Flower',
                  'price': '6',
                  'image': ''
                  },
                 {'name': 'Helmet',
                  'price': '50',
                  'image': ''
                  },
                 {'name': 'Helmet',
                  'price': '50',
                  'image': ''
                  }
             ]}
        ],
    })

#     return render(request, 'item/index.html', context={
#         'items': Item.objects.all()
#     })

# def get_item_by_id(request, id):
#     return render(request, 'item/item_details.html', {
#         'item': get_object_or_404(Item, pk=id)
#     })
