const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')

module.exports = {
  target: 'node',
  node:{
    __dirname: false,
  },
  plugins:[
    new CopyWebpackPlugin([
      {
        from: path.resolve(__dirname, './static'),
        to:  path.resolve(__dirname, 'build'),
        ignore: ['.*']
      }
    ]),
    new CopyWebpackPlugin([
      {
        from: path.resolve(__dirname, './index.html'),
        to:  path.resolve(__dirname, 'build'),
        ignore: ['.*']
      }
    ])
  ],
  entry: {
    app: ['babel-polyfill', './index.js'],
  },
  // proxy: {
  //   '/static':{
  //     target:'localhost:8080',
  //     pathRewrite: {'/static':'/serverstatic'}
  //   }
  // },
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'app.bundle.js',
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['env'],
        },
      },
    ],
  },
};
