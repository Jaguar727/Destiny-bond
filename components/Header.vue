<template>
	<div class="bg-purple-4 position-fixed top-0 z-max w-100 header-shadow">
		<div
			class="
				d-flex
				justify-content-between
				align-items-center
				text-center
				container
			"
		>
			<Banette-Logo />
			<div class="d-flex col-xl-3 color-white bg-purple-5 br-3 p-12 justify-content-between align-items-center">
                <div class="">Search Pokemon</div>
				<div class="material-icons icon-small">search</div>
			</div>

			<div
				class="
					header-link-group
					font-24 font-bold
					justify-content-center
					d-flex
				"
			>
				<NuxtLink class="header-link" to="/">Home</NuxtLink>
				<NuxtLink class="header-link mlr-40" to="#">Pokedex</NuxtLink>
				<NuxtLink class="header-link" to="#">About</NuxtLink>
			</div>
		</div>
	</div>
</template>

<style scoped>
.header-link {
	color: white;
	text-decoration: none;
}

.header-link-group {
	left: 0;
	right: 0;
}

.z-max {
	z-index: 99;
}

.header-shadow {
    box-shadow: 0px 4px 8px 0px #00000026;

}
</style>
