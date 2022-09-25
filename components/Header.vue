<template>
	<div>
		<div
			class="
				bg-purple-3
				d-flex
				justify-content-between
				align-items-center
				plr-32
                text-center
			"
		>
			<Banette-Logo />
            
			<div class=" header-link-group position-absolute font-24 font-bold justify-content-center mx-auto d-flex">
				<NuxtLink class="header-link" to="#">Home</NuxtLink>
				<NuxtLink class="header-link mlr-40" to="#">Pokedex</NuxtLink>
				<NuxtLink class="header-link" to="#">About</NuxtLink>
			</div>

			<div
				class="
					material-icons
					color-white
					bg-purple-4
					br-3
					p-12
					icon-small
				"
			>
				search
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
