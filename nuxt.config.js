export default {
	// Global page headers: https://go.nuxtjs.dev/config-head
	head: {
		title: "pokedex-vue",
		htmlAttrs: {
			lang: "en",
		},
		meta: [
			{ charset: "utf-8" },
			{
				name: "viewport",
				content: "width=device-width, initial-scale=1",
			},
			{ hid: "description", name: "description", content: "" },
			{ name: "format-detection", content: "telephone=no" },
		],
		link: [
			{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
			{ rel: "stylesheet", href: "/css/default.css" },
			{
				rel: "stylesheet",
				href: "https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;500;600;700;800;900&display=swap",
			},
		],
	},

	// Global CSS: https://go.nuxtjs.dev/config-css

	// Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
	plugins: [{ src: "~/plugins/axios.js" }],

	// Auto import components: https://go.nuxtjs.dev/config-components
	components: true,

	// Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
	buildModules: [],

	// Modules: https://go.nuxtjs.dev/config-modules
	modules: ["@nuxtjs/axios", "@nuxtjs/device", "@nuxtjs/proxy"],

	axios: {
		proxy: true,
	},

	proxy: {
		"/api/": {
			target: process.env.BACKEND_URL || "http://localhost:5000/",
			pathRewrite: { "^/api/": "" },
			changeOrigin: true,
		},
	},

	// Build Configuration: https://go.nuxtjs.dev/config-build
	build: {},
};
