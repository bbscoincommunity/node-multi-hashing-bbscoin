{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "scryptn.c",
                "keccak.c",
                "skein.c",
                "x11.c",
                "quark.c",
                "bcrypt.c",
                "groestl.c",
                "blake.c",
                "fugue.c",
                "qubit.c",
                "hefty1.c",
                "shavite3.c",
                "cryptonight.c",
                "cryptonight_lite.c",
                "x13.c",
                "boolberry.cc",
                "nist5.c",
                "sha1.c",
                "x15.c",
                "fresh.c",
                "sha3/sph_hefty1.c",
                "sha3/sph_fugue.c",
                "sha3/aes_helper.c",
                "sha3/sph_blake.c",
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_groestl.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/hamsi.c",
                "crypto/oaes_lib.c",
                "crypto/c_keccak.c",
                "crypto/c_groestl.c",
                "crypto/c_blake256.c",
                "crypto/c_jh.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/aesb.c",
                "crypto/wild_keccak.cpp",
            ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++0x",
                "-Wno-implicit-function-declaration",
                "-Wno-missing-field-initializers",
                "-Wno-unused-function",
                "-Wno-unused-const-variable",
                "-Wno-unused-private-field",
            ],
            "xcode_settings": {
                "OTHER_CFLAGS": [
                    "-Wno-implicit-function-declaration",

                    "-Wno-implicit-function-declaration",
                    "-Wno-missing-field-initializers",
                    "-Wno-unused-function",
                    "-Wno-unused-const-variable",
                    "-Wno-unused-private-field"
                ],
            }
        }
    ]
}