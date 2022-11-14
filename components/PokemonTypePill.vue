<template>
	<div>
		<div
			class="
				br-50
				pill-size
				d-flex
				align-items-center
				justify-content-center
                text-capitalize
			"
			:class="`pill-type-${pokemonType}`"
		>
			{{ pokemonType }}
		</div>
	</div>
</template>

<script>
export default {
	props: {
		pokemonType: String,
	},
};
</script>

<style scoped>
.pill-size {
	width: 100px;
	height: 24px;
}
</style>