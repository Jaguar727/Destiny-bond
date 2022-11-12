<template>
	<div class="bg-purple-4">
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
			<div
				class="
					material-icons
					color-white
					bg-purple-5
					br-3
					p-12
					icon-small
				"
			>
				search
			</div>
            
			<div class=" header-link-group font-24 font-bold justify-content-center d-flex">
				<NuxtLink class="header-link" to="#">Home</NuxtLink>
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
    left:0;
    right: 0;
}
</style>
