class Point:
  def __init__(self, x, y, c='#000000'):
    self.x=x
    self.y=y
    self.c=c
  
t_L = [
  [
    Point(0,0),
    Point(0,1),
    Point(0,2),
    Point(1,2)
  ],

  [
    Point(2,0),  
    Point(0,1),  
    Point(1,1),  
    Point(2,1) 
  ],

  [
    Point(0,0), 
    Point(1,0),
    Point(1,1),
    Point(1,2) 
  ],

   [
    Point(0,0), 
    Point(1,0), 
    Point(0,1), 
    Point(2,0)
   ]
]


t_O = [
  [
    Point(0,0), 
    Point(1,0), 
    Point(0,1), 
    Point(1,1)
  ],
  [
    Point(0,0),
    Point(1,0),
    Point(0,1), 
    Point(1,1) 
  ],
  [
    Point(0,0), 
    Point(1,0),
    Point(0,1),
    Point(1,1) 
  ],
  [
    Point(0,0),
    Point(1,0), 
    Point(0,1), 
    Point(1,1) 
  ]
  ]

t_I = [
  [
    Point(0,0), 
    Point(1,0), 
    Point(2,0), 
    Point(3,0)
  ],
  [
    Point(0,0), 
    Point(0,1),  
    Point(0,2), 
    Point(0,3), 
    
  ],
   [
    Point(0,0), 
    Point(1,0),  
    Point(2,0),
    Point(3,0)  
  ],
  [
    Point(0,0), 
    Point(0,1), 
    Point(0,2), 
    Point(0,3) 
    
  ]
  ]

t_T = [
  [
    Point(0,0),
    Point(1,0),  
    Point(2,0),
    Point(1,1)
  ],
  [
    Point(0,0),
    Point(0,1),
    Point(1,1),
    Point(0,2)
  ],
  [
    Point(1,0),  
    Point(0,1),
    Point(1,1),
    Point(2,1)
  ],
  [
    Point(0,1),
    Point(1,0),  
    Point(1,1),
    Point(1,2)
  ]
  ]
  

t_J = [
  [
    Point(1,0),  
    Point(1,1),
    Point(0,2),
    Point(1,2)
  ],
  [
    Point(0,0),
    Point(0,1),
    Point(1,1),
    Point(2,1)
  ],
  [
    Point(0,0),
    Point(1,0),  
    Point(0,1),
    Point(0,2)
  ],
  [
    Point(0,0),
    Point(1,0),  
    Point(1,1),
    Point(1,2)
  ]
  ]

t_S = [
  [
    Point(1,0),  
    Point(2,0),
    Point(0,1),
    Point(1,1)
  ],
  [
    Point(0,0),
    Point(0,1),
    Point(1,1),
    Point(1,2)
  ],
  [
    Point(1,0),  
    Point(2,0),
    Point(0,1),
    Point(1,1)
  ],
  [
    Point(0,0),
    Point(0,1),
    Point(1,1),
    Point(1,2)
  ]
  ]


t_Z = [
  [
    Point(0,0),
    Point(1,0),  
    Point(1,1),
    Point(2,1)
  ],
  [
    Point(1,0),  
    Point(0,1),
    Point(1,1),
    Point(0,2)
  ],
  [
    Point(0,0),
    Point(1,0),  
    Point(1,1),
    Point(2,1)
  ],
  [
    Point(1,0),  
    Point(0,1),
    Point(1,1),
    Point(0,2)
  ]
  ]
