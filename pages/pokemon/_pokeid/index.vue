<template>
	<div>
		<Header />
		<div class="position-fixed h-100 w-100 top-0 top-25 bg-budega">
			<div class="pt-92 container">
				<div class="row">
					<div
						class="
							col-xl-6
							d-flex
							flex-column
							align-items-center
							justify-content-center
						"
					>
						<img
							class="bg-purple-6 p-24 br-8"
							:src="`https://serebii.net${pokemon.artwork}`"
							alt=""
						/>
						<div class="col-xl d-flex justify-content-center mt-16">
							<PokemonTypePill
								class="mr-24"
								:pokemonType="pokemon.types[0]"
							/>
							<PokemonTypePill
								:pokemonType="pokemon.types[1]"
								v-if="pokemon.types[1]"
							/>
						</div>
					</div>
					<div class="col-xl-6">
						<p class="color-white p-16 font-24 font-bold">
							{{ pokemon.id }}
							{{ pokemon.name }}
						</p>

						<div
							class="
								color-white
								p-8
								font-24
								bg-purple-6
								d-flex
								justify-content-around
								br-8
								align-items-center
							"
						>
							<p>
								{{ pokemon.abilities[0] }}
							</p>
							<p v-if="pokemon.abilities[1]">
								{{ pokemon.abilities[1] }}
							</p>
							<p v-if="pokemon.abilities[2]">
								{{ pokemon.abilities[2] }}
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	async asyncData({ $axios, params }) {
		try {
			let pokemon = await $axios.$get(`/api/pokemon/${params.pokeid}`);
			return {
				pokemon: pokemon[0],
			};
		} catch (error) {
			console.log(error);
		}
	},
};
</script>