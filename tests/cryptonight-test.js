const { cryptonight, cryptonight_lite } = require('../');
const { test } = require('./helper');

describe('cryptonight', () => {
    it('cryptonight', () => {
        test('cryptonight-slow.txt', (data) => cryptonight(data, false));
    });

    it('cryptonight fast', () => {
        test('cryptonight-fast.txt', (data) => cryptonight(data, true));
    });

    it('cryptonight v7', () => {
        test('cryptonight-slow-v7.txt', (data) => cryptonight(data, 1));
    });

    it('cryptonight lite', () => {
        test('cryptonight-lite.txt', (data) => cryptonight_lite(data, 0));
    });

    it('cryptonight lite v7', () => {
        test('cryptonight-lite-v7.txt', (data) => cryptonight_lite(data, 1));
    });
});