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
                    "abrufen_klasse",
                    [
                        "abfolge",
                        [
                            "setzen",
                            "double",
                            [
                                "funktion",
                                ["num"],
                                [
                                    "addieren",
                                    ["abrufen", "num"],
                                    ["abrufen", "num"]
                                ]
                            ]
                        ],
                        [
                            "setzen",
                            "a",
                            1
                        ],
                        [
                            "aufrufen",
                            "double",
                            [
                                "abrufen",
                                "a"
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ],
    [
        "neue_klasse",
        "square",
        [
            "parent",
            "shape"
        ],
        [
            "konstruktor",
            [
                "funktion",
                ["a", "side_length"],
                [
                    "setzen_klasse",
                    "shape",
                    "name",
                    ["abrufen", "a"]
                ],
                [
                    "setzen_klasse",
                    "square",
                    "side_length",
                    ["abrufen", "side_length"]
                ]
            ]
        ],
        [
            "square_area",
            [
                "funktion",
                ["thing"],
                [
                    "multiplizieren",
                    ["abrufen", "side_length"],
                    ["abrufen", "side_length"]
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
                ],
                [
                    "setzen_klasse",
                    "circle",
                    "radius",
                    ["abrufen", "radius"]
                ]
            ]
        ],
        [
            "circle_area",
            [
                "funktion",
                ["thing"],
                [
                    "multiplizieren",
                    3.14159,
                    [
                        "multiplizieren",
                        ["abrufen", "radius"],
                        ["abrufen", "radius"]
                    ]
                ]
            ]
        ]
    ]
]
