<template>
	<div>
		<button @click="listPokemonInConsole(0)">TESTE CARALHOOOOOO</button>
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
            pokemons: []
        }
    },

	methods: {
		listPokemonInConsole(pokemonId) {
			console.log(this.pokemons[pokemonId]);
		},
	},
};
</script>
