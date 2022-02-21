# myLinks = ['https://www.google.com.sg/intl/en-GB/about/products?tab=ih',
# 'https://accounts.google.com/ServiceLogin?service=searchandassistant&passive=1209600&continue=https://www.google.co.in/search?q%3Dgarchomp%26source%3Dlnms%26tbm%3Disch%26sfr%3Dvfe&followup=https://www.google.co.in/search?q%3Dgarchomp%26source%3Dlnms%26tbm%3Disch%26sfr%3Dvfe&ec=GAZAAg',
# 'https://bulbapedia.bulbagarden.net/wiki/Garchomp_%28Pok%C3%A9mon%29',
# 'https://pokemon.gameinfo.io/en/pokemon/445-garchomp',
# 'https://www.touchtapplay.com/pokemon-go-garchomps-strengths-and-weaknesses/',
# 'https://bleedingcool.com/games/what-is-the-best-moveset-for-garchomp-in-pokemon-go/',
# 'https://sg.portal-pokemon.com/play/pokedex/445_1',
# 'https://bulbapedia.bulbagarden.net/wiki/Garchomp_%28Pok%C3%A9mon%29',
# 'https://mugen.fandom.com/wiki/Garchomp',
# 'https://tonsoffacts.com/30-fun-and-fascinating-facts-about-garchomp-from-pokemon/',
# 'https://www.serebii.net/pokedex-swsh/garchomp',
# 'https://www.carousell.sg/p/garchomp-pokemon-go-255643164/',
# 'https://pokemongohub.net/post/article/garchomps-science-design-a-military-dragon-force/',
# 'https://www.dexerto.com/cosplay/pokemon-cosplayer-goes-viral-garchomp-outfit-1720639/',
# 'https://bulbapedia.bulbagarden.net/wiki/Garchomp_%28Pok%C3%A9mon%29',
# 'https://www.reddit.com/r/pokemon/comments/e4xg1c/i_made_a_garchomp_based_armor_design/',
# 'https://www.previewsworld.com/Catalog/APR219507',
# 'https://www.dexerto.com/pokemon/best-moveset-for-garchomp-in-pokemon-go-1589779/',
# 'https://bleedingcool.com/games/will-mega-garchomp-debut-after-gible-community-day-in-pokemon-go/',
# 'https://knowyourmeme.com/photos/1886893-pokemon',
# 'https://www.thegamer.com/pokemon-garchomp-fan-art-best-worst/',
# 'https://www.ign.com/wikis/pokemon-unite/Garchomp_Guide_-_Builds_and_Tips',
# 'https://www.dexerto.com/pokemon/best-moveset-for-garchomp-in-pokemon-go-1589779/',
# 'https://litetheironman.medium.com/trainers-school-garchomp-character-guide-7ec642d2fbf2',
# 'https://comicbook.com/anime/news/pokemon-anime-cosplay-garchomp/',
# 'https://www.favorgk.com/products/garchomp-family-pokemon-resin-statue-ppap-studios-pre-order',
# 'https://gamewith.net/pokemon-unite/article/show/28883',
# 'https://bulbapedia.bulbagarden.net/wiki/Cynthia%27s_Garchomp',
# 'https://www.ginx.tv/en/pokemon/what-are-garchomp-s-weaknesses-in-pokemon-brilliant-diamond-and-shining-pearl',
# 'https://gamepress.gg/pokemonmasters/pokemon/cynthia-mega-garchomp',
# 'https://samurai-gamers.com/pokemon-sun-and-moon/strategy-garchomp/',
# 'https://www.reddit.com/r/PokemonUnite/comments/q5yq0p/garchomp_is_such_a_fun_pokemon_to_play_as/',
# 'https://www.serebii.net/potw-swsh/445.shtml',
# 'https://game8.co/games/pokemon-sword-shield/archives/305041',
# 'https://www.facebook.com/BlueRed445/',
# 'https://progameguides.com/pokemon/best-nature-for-gible-gabite-and-garchomp-in-pokemon-brilliant-diamond-and-shining-pearl/',
# 'https://www.dualshockers.com/garchomp-best-moveset/',
# 'https://game8.co/games/Pokemon-UNITE/archives/335481',
# 'https://www.sportskeeda.com/pokemon/what-garchomp-s-weaknesses-pokemon-brilliant-diamond-shining-pearl',
# 'https://dotesports.com/news/best-garchomp-build-in-pokemon-unite',
# 'https://bulbapedia.bulbagarden.net/wiki/Garchomp_%28Pok%C3%A9mon%29',
# 'https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/ss-series/cel25c/145_A/',
# 'https://www.amazon.com/Takara-Tomy-Collection-Moncolle-Garchomp/dp/B07ZQ2THR4',
# 'https://dotesports.com/news/pokemon-unite-players-are-speaking-out-after-being-forced-to-purchase-garchomp-for-weekly-mission',
# 'https://terminalmontage.fandom.com/wiki/Garchomp',
# 'https://thenerdstash.com/pokemon-brilliant-diamond-shining-pearl-what-are-garchomps-weaknesses/',
# 'https://pokemonblog.com/2021/09/18/new-cowboy-holowear-for-garchomp-coming-to-pokemon-unite-on-september-22/',
# 'https://comicbook.com/gaming/news/pokemon-go-fans-disappointed-shiny-garchomp/',
# 'https://gamerant.com/pokemon-go-garchomp-weakness-counters/',
# 'https://game8.co/games/Pokemon-UNITE/archives/335481',
# 'https://policies.google.com/privacy?hl=en-GB&gl=SG&sa=X&ved=2ahUKEwjO1s2apLb1AhULi9gFHTlGC88Q8awCegQIAhAD',
# 'https://policies.google.com/terms?hl=en-GB&gl=SG&sa=X&ved=2ahUKEwjO1s2apLb1AhULi9gFHTlGC88Q8qwCegQIAhAE']


# print(len(myLinks))

def removeGoogle(myLinks):

    filteredLinksNoGoogle = []

    for link in myLinks:
        afterSlashes = (link.partition(r"//"))[2]
        website = (afterSlashes.partition("/"))[0]
        differentBranches = website.split(".")

        if "google" not in differentBranches:
            filteredLinksNoGoogle.append(link)

    return filteredLinksNoGoogle


# import pprint

# pprint.pprint(removeGoogle(myLinks))

# print(len(removeGoogle(myLinks)))