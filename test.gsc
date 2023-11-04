[
  "abfolge",
  [
    "setzen",
    "quadruple",
    [
      "funktion",
      ["num"],
      [
        "multiplizieren",
        ["abrufen", "num"],
        ["multiplizieren", ["abrufen", "num"], 2]
      ]
    ]
  ],
  [
    "setzen",
    "b",
    4
  ],
  [
    "ausgeben",
    [
      "aufrufen",
      "quadruple",
      ["abrufen", "b"]
    ]
  ],
  [
    "setzen",
    "difference",
    [
      "funktion",
      ["x", "y"],
      [
        "absolutwert",
        ["differenz", ["abrufen", "x"], ["abrufen", "y"]]
      ]
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen",
      "difference",
      
        ["abrufen", "b"],
        10
      
    ]
  ],
  [
    "setzen",
    "sumOfSquares",
    [
      "funktion",
      ["x", "y"],
      [
        "addieren",
        [
          "multiplizieren",
          ["abrufen", "x"],
          ["abrufen", "x"]
        ],
        [
          "multiplizieren",
          ["abrufen", "y"],
          ["abrufen", "y"]
        ]
      ]
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen",
      "sumOfSquares",
      3, 4
    ]
  ],
  [
  "abfolge",
  [
    "setzen",
    "a",
    10
  ],
  [
    "setzen",
    "b",
    5
  ],
  [
    "ausgeben",
    [
      "addieren",
      ["abrufen", "a"],
      ["abrufen", "b"]
    ]
  ],
  [
    "ausgeben",
    [
      "differenz",
      ["abrufen", "a"],
      ["abrufen", "b"]
    ]
  ],
  [
    "ausgeben",
    [
      "multiplizieren",
      ["abrufen", "a"],
      ["abrufen", "b"]
    ]
  ],
  [
    "ausgeben",
    [
      "dividieren",
      ["abrufen", "a"],
      ["abrufen", "b"]
    ]
  ],
  [
    "setzen",
    "complexCalculation",
    [
      "funktion",
      ["x", "y"],
      [
        "dividieren",
        [
          "addieren",
          ["abrufen", "x"],
          ["multiplizieren", ["abrufen", "x"], ["abrufen", "y"]]
        ],
        ["differenz", ["abrufen", "y"], 2]
      ]
    ]
  ],
  [
    "ausgeben",
    [
      "aufrufen",
      "complexCalculation",
      ["abrufen", "a"],
      ["abrufen", "b"]
    ]
  ]
],
[
    "setzen",
    "a",
    3
  ],
  [
    "setzen",
    "b",
    2
  ],
  [
    "ausgeben",
    [
      "power",
      ["abrufen", "a"],
      ["abrufen", "b"]
    ]
  ]

]