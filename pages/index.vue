<template>
	<div>
		<div class="d-flex">
			<div class="color-purple-1">TESTE CARALHOOOOOO</div>
			<div
				class="bg-black color-white mt-32"
				@click="listPokemonInConsole(1)"
			>
				TESTANDO AINDAAAAA {{ pokemons[323].name }}
                <img :src="`https://serebii.net/${pokemons[323].icon}`" alt="">
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

	data() {
		return {
			pokemons: [],
		};
	},

	methods: {
		listPokemonInConsole(pokemonId) {
			console.log(this.pokemons[pokemonId]);
		},
	},
};
</script>
