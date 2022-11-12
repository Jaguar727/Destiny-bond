<template>
	<div class="bg-purple-6">
		<Header />
        <div class="bg-gradient position-fixed a w-100 top-0 start-0"></div>
		<div class="container">
			<div class="row plr-40">
				<div
					class="col-lg-6 d-flex justify-content-center col-xl-4"
					v-for="(pokemon, index) in pokemons"
					:key="pokemon._id"
					:index="index"
				>
					<Pokemon-Card
						class="mb-16"
						:pokemonImage="pokemons[index].artwork"
						:pokemonName="pokemons[index].name"
						:pokemonId="pokemons[index].id"
						:pokemonType1="pokemons[index].types[0]"
						:pokemonType2="pokemons[index].types[1]"
					/>
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

<style scoped>
    .a {
        height: 100vh;   
    }
</style>
