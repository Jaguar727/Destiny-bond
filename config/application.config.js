require('dotenv').config()

const defaultConfig = {
	app: {
		port: 5000,
		clientUrl: "http://localhost:3000",
	},
	mongo: {
		url:`${process.env.MONGODB_CONNECTION_STRING}`,
		config: {
			useNewUrlParser: true,
			useUnifiedTopology: true,
		},
	},
};

module.exports = defaultConfig;
