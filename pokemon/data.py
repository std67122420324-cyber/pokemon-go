pokemon_types = [
  'Water','Fire','Grass','Flying','Rock','Ground',
  'Steel','Electric','Fairy','Ghost','Dark','Dragon',
  'Ice','Bug','Fighting','Poison','Psychic','Normal',
  'Shadow'
]


from pokemon.models import Type
types = [Type(name=type) for type in pokemon_types]