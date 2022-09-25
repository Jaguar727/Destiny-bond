<template>
	<div>
		<div
			class="
				bg-purple-4
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
					color-purple-3
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
	width: 320px;
	height: 320px;
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