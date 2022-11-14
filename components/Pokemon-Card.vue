<template>
	<div>
		<NuxtLink
			:to="`/pokemon/${pokemon.intId}`"
			class="
				bg-purple-6
				br-8
				justify-content-center
				d-flex
				flex-column
				position-relative
				pokemon-card-size
				text-decoration-none
			"
		>
			<img class="pokemon-card-img mx-auto" :src="`https://serebii.net${pokemon.artwork}`" />
			<p class="color-white-1 font-16 mx-auto position-absolute pokemon-card-id">
				{{ pokemon.id }}
			</p>
			<p class="color-white font-32 mx-auto">{{ pokemon.name }}</p>
			<div class="d-flex mx-auto pb-16 mt-8">
				<PokemonTypePill :pokemonType="pokemon.types[0]" />
				<PokemonTypePill class="ml-16" v-if="pokemon.types[1]" :pokemonType="pokemon.types[1]" />
			</div>
		</NuxtLink>
	</div>
</template>

<style scoped>
.pokemon-card-img {
	width: 192px;
	height: 192px;
}

.pokemon-card-id {
	top: 16px;
	right: 16px;
}

.pokemon-card-size {
	width: 100%;
	height: 320px;
	transition: 0.3s;
}

.pokemon-card-size:hover {
	transform: scale(1.06);
	transition: 0.3s;
}
</style>

<script>
export default {
	props: {

		pokemon: Object,
	},
};
</script>