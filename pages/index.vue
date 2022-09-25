<template>
	<div class="bg-purple-6">
		<Header />
		<div class="container bg-purple-5">
			<div class="color-purple-1">TESTE CARALHOOOOOO</div>
			<Pokemon-Card
				class="d-flex mx-auto justify-content-center"
				:pokemonImage="pokemons[3].artwork"
				:pokemonName="pokemons[3].name"
				:pokemonId="pokemons[3].id"
				:pokemonType1="pokemons[3].types[0]"
				:pokemonType2="pokemons[3].types[1]"
			/>
			<div
				class="bg-black color-white mt-32"
				@click="listPokemonInConsole(1)"
			>
				TESTANDO AINDAAAAA {{ pokemons[323].name }}
				<img
					:src="`https://serebii.net/${pokemons[323].icon}`"
					alt=""
				/>
			</div>

			<div class="row plr-40">
				<div
                    class="col-lg-6 d-flex justify-content-center  col-xl-4"
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
