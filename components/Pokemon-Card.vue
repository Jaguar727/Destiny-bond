<template>
	<div>
		<div
			class="
				bg-purple-6
				br-8
				justify-content-center
				d-flex
				flex-column
				position-relative
                pokemon-card-size
			"
		>
			<img
				class="pokemon-card-img mx-auto"
				:src="`https://serebii.net${pokemonImage}`"
			/>
			<p
				class="
					color-white-1
					font-16
					mx-auto
					position-absolute
					pokemon-card-id
				"
			>
				{{ pokemonId }}
			</p>
			<p class="color-white font-32 mx-auto">{{ pokemonName }}</p>
			<div class="d-flex mx-auto pb-24">
				<PokemonTypePill :pokemonType="pokemonType1" />
				<PokemonTypePill
					class="ml-16"
					v-if="pokemonType2"
					:pokemonType="pokemonType2"
				/>
			</div>
		</div>
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
    transform: scale(1.1);
    transition: 0.3s;
}
</style>

<script>
export default {
	props: {
		pokemonId: String,
		pokemonImage: String,
		pokemonName: String,
		pokemonType1: String,
		pokemonType2: String,
	},
};
</script>