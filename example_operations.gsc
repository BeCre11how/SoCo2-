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
  ]
]
