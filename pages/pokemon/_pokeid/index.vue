<template>
	<div>
		<Header />
		<div class="position-fixed h-100 w-100 top-0 top-25 bg-gradient-ghost">
			<div class="pt-92 container">
				<div class="row">
					<div class="col-xl-6 d-flex flex-column align-items-center justify-content-center">
						<img
							class="bg-purple-6 p-24 br-8 mt-16"
							:src="`https://serebii.net${pokemon.artwork}`"
							alt=""
						/>
						<div class="col-xl d-flex justify-content-center mt-16">
							<PokemonTypePill class="mr-24" :pokemonType="pokemon.types[0]" />
							<PokemonTypePill :pokemonType="pokemon.types[1]" v-if="pokemon.types[1]" />
						</div>
					</div>
					<div class="col-xl-6">
						<div class="color-white mtb-16 font-24 font-bold d-flex justify-content-between">
							<p>{{ pokemon.name }}</p>
							<p>{{ pokemon.id }}</p>
						</div>

						<div class="color-white d-flex align-items-center font-24">
                            <p class="mr-24">Abilities: </p>
							<div class="d-flex justify-content-around br-8 align-items-center bg-purple-6 p-8 w-100">
								<p>
									{{ pokemon.abilities[0] }}
								</p>
								<p v-if="pokemon.abilities[1]">
									{{ pokemon.abilities[1] }}
								</p>
								<div v-if="pokemon.abilities[2]" class="text-center">
									<p class="font-16">{{ pokemon.abilities[2] }}</p>
                                    <p class="font-8">Hidden Ability</p>
								</div>
							</div>
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