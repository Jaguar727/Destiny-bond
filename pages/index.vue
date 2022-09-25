<template>
	<div>
        <Header/>
		<div class="">
			<div class="color-purple-1">TESTE CARALHOOOOOO</div>
			<div class="bg-black color-white mt-32" @click="listPokemonInConsole(1)">
				TESTANDO AINDAAAAA {{ pokemons[323].name }}
				<img :src="`https://serebii.net/${pokemons[323].icon}`" alt="" />
			</div>

			<div v-for="(pokemon, index) in pokemons" :key="pokemon._id" :index="index">
				<div class="d-flex align-items-center ptb-16 mtb-8 bg-purple-1 col-4 mx-auto plr-8 br-3">
					
                    <img :src="`https://serebii.net/${pokemons[index].icon}`" alt="" />
					
                    <p class="text-gray-1 mtb-8 ml-16">
						{{ pokemons[index].name }}
					</p>
					
                    <PokemonTypePill class="mlr-16" :pokemonType="pokemons[index].types[0]" />
					<PokemonTypePill v-if="pokemons[index].types[1]" :pokemonType="pokemons[index].types[1]" />
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	async asyncData({ $axios }) {
		try {
			const pokemon = await $axios.$get("/api/pokemon");
			return {
				pokemons: pokemon,
			};
		} catch (error) {
			console.log(error);
		}
	},

	methods: {
		listPokemonInConsole(pokemonId) {
			console.log(this.pokemons[pokemonId]);
		},
	},
};
</script>
