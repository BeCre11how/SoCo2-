[
  "abfolge",

  [
    "setzen",
    "myArray",
    [
      "array", 5,
      1,
      2,
      3,
      4,
      5
  ]
  ],
  [
    "ausgeben",
    [
      "abrufen_klasse",
      "myArray", "array"
    ]
  ],

    [
      "aufrufen_klasse",
      "myArray",
      "set",
      [4, 8]

  ],

    [
    "ausgeben",
    [
      "abrufen_klasse",
      "myArray", "array"
    ]
  ],



  [
    "setzen",
    "index",
    0
  ],
  [
    "solange",
    [
      ["abrufen", "index"],
      "<",
      5
    ],
    [
      "abfolge",
      [
        "ausgeben",

        [
          "aufrufen_klasse",
          "myArray", "get",


          ["abrufen", "index"]
        ]

      ],
      [
        "setzen",
        "index",
        [
          "addieren",
          ["abrufen", "index"],
          1
        ]
      ]
    ]


  ],


  [
    "setzen",
    "myDict",
    [
      "dictionary",
      "key1", "value1",
      "key2", "value2"
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen_klasse",
      "myDict",
      "get",
      "key1"
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen_klasse",
      "myDict",
      "get",
      "key2"
    ]
  ],
   [
    "setzen",
    "myDict2",
    [
      "dictionary",
      "key1b", "value1b",
      "key2b", "value2b"
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen_klasse",
      "myDict2",
      "get",
      "key1b"
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen_klasse",
      "myDict2",
      "get",
      "key2b"
    ]
  ],

     [
    "ausgeben",
    [
     "aufrufen_klasse", "myDict", "merge", [["abrufen_klasse", "myDict", "dictionary"], ["abrufen_klasse", "myDict2",  "dictionary"]]
    ]
  ],
    ["ausgeben",

      [
      "abrufen_klasse",
      "myDict", "dictionary"
    ]
   ],

    [
      "aufrufen_klasse",
      "myDict",
      "set",
      ["key2", "value3"]

  ],
  ["ausgeben",

      [
      "abrufen_klasse",
      "myDict", "dictionary"
    ]
   ]
]
