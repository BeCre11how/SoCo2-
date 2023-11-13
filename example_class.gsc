[
    "abfolge",
    [
        "neue_klasse",
        "shape",
        "name",
        [
            "konstruktor",
            [
                "funktion",
                ["a"],
                [
                    "setzen_klasse",
                    "shape",
                    "name",
                    ["abrufen", "a"]
                ]
            ]
        ],
        [
            "shape_density",
            [
                "funktion",
                ["thing", "weight"],
                [
                "dividieren",
                ["aufrufen", ["abrufen_klasse",
                 ["abrufen", "thing"],
                 "area"
                ], ["abrufen", "thing"]
                ]
                ,["abrufen", "weight"]
                ]
            ]
        ]
    ],
    [
        "neue_klasse",
        "square",
        "side_length",
        [
            "parent",
            "shape"
        ],
        [
            "konstruktor",
            [
                "funktion",
                ["name", "side_length"],
                [
                    "setzen_klasse",
                    "shape",
                    "name",
                    ["abrufen", "a"]
                ,
                [
                    "setzen_klasse",
                    "square",
                    "side_length",
                    ["abrufen", "side_length"]
                ]]
            ]
        ],
        [
            "area",
            [
                "funktion",
                ["thing"],

                   [ "multiplizieren",
                    ["abrufen_klasse", ["abrufen", "thing"], "side_length"],
                     ["abrufen_klasse", ["abrufen", "thing"], "side_length"]
                    ]

            ]
        ]
    ],
    [
        "neue_klasse",
        "circle",
        "radius",
        [
            "parent",
            "shape"
        ],
        [
            "konstruktor",
            [
                "funktion",
                ["a", "radius"],
                [
                    "setzen_klasse",
                    "shape",
                    "name",
                    ["abrufen", "a"]
                ,
                [
                    "setzen_klasse",
                    "circle",
                    "radius",
                    ["abrufen", "radius"]
                ]]
            ]
        ],
        [
            "area",
            [
                "funktion",
                ["thing"],
                [
                    "multiplizieren",
                    3.14159,
                    [
                        "power",
                        ["abrufen_klasse", ["abrufen", "thing"], "radius"],2
                    ]
                ]
            ]
        ]
    ],
    [
        "setzen", "ci_name",

        ["circle_new", "cir", "2"]



    ],
    [
        "setzen", "sq_name",

        ["square_new", "sq", "3"]



    ],
  [
    "setzen",
    "cir",
    [
      "circle_new",
      "Circle Shape",
      2.5
    ]
  ],
  [
    "setzen",
    "sq",
    [
      "square_new",
      "Square Shape",
      4.0
    ]
  ],
  [
    "setzen",
    "circle_density",
    [
      "aufrufen_klasse",
      "cir",
      "shape_density",
      "cir" , 5
    ]
  ],
  [
    "setzen",
    "square_density",
    [
      "aufrufen_klasse",
      "sq",
      "shape_density",
        "sq", 5
    ]
  ],
  [
    "addieren",
    ["abrufen", "circle_density"],
    ["abrufen", "square_density"]
  ]



]
