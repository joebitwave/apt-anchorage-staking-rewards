import streamlit as st
import pandas as pd
from datetime import datetime
import io

# Static Wallets List data
wallets_list = [
    {"Wallet Name": "Aptos Mainnet Wallet 1", "Address": "0xca78412b2d681145a88a771b4f7d5ea36bb949b7352d9415c4c1f46a7ac7acf7"},
    {"Wallet Name": "Aptos Mainnet Wallet 10", "Address": "0x03150576115e2c791261359f0d71dec72799f7ed87620f609420d6e03265e7e7"},
    {"Wallet Name": "Aptos Mainnet Wallet 102", "Address": "0x49b1cf68f684f08393c813f42623626a0cbb45bb65aa3e34fdf89519573575ee"},
    {"Wallet Name": "Aptos Mainnet Wallet 103", "Address": "0x6151a52845b113c7db63c9d5b7d0c73e12db1018bb85ae625c382b521f508f76"},
    {"Wallet Name": "Aptos Mainnet Wallet 104", "Address": "0x14feff5a873d3c6ce8694ce984eb179318fca2b4ac7b39bda2417be45eb6f7d8"},
    {"Wallet Name": "Aptos Mainnet Wallet 105", "Address": "0xced7fd303286dd08181a4519b472350ea4c79468acf50a8eb657dd249ddf9bbc"},
    {"Wallet Name": "Aptos Mainnet Wallet 106", "Address": "0xfe538f0ea4514e360e636ee62df8d19cb9ed46c31296b7920c69e8b67685fa0d"},
    {"Wallet Name": "Aptos Mainnet Wallet 109", "Address": "0x53f6882b38de7d94dad91359d28647a5245985eda0d3953e3c23aaaa2dc2016e"},
    {"Wallet Name": "Aptos Mainnet Wallet 118", "Address": "0xac426d1b7372f4bfee01c1908ab50ababe8fd5330f593d56926d25d38e53e21b"},
    {"Wallet Name": "Aptos Mainnet Wallet 127", "Address": "0x07f8a3e094c96db6e44442e1c35a1fd0314694db111895ac3adc462f891e8504"},
    {"Wallet Name": "Aptos Mainnet Wallet 130", "Address": "0xfcc0da16fd27ff72a0d3d82b9b2b2a6a238814f3f0440362b2462ab3d2dd975b"},
    {"Wallet Name": "Aptos Mainnet Wallet 132", "Address": "0x834b4d54d30d3c58a5f791cd4bc80ce5919c062575f8b98c1b671b1a222e29ac"},
    {"Wallet Name": "Aptos Mainnet Wallet 138", "Address": "0x94cb091c5fcba2a168f0b5cf0828405bcce298573a6cc881646210ed5cade8e1"},
    {"Wallet Name": "Aptos Mainnet Wallet 139", "Address": "0x81621cf9fa1a44495a5a8f12ad2b44280c8e91292c7f381cb3d5d7c19575bd21"},
    {"Wallet Name": "Aptos Mainnet Wallet 140", "Address": "0xfd19d127572992c7987f6b0de55d2d83f874fb0097626f2859e01d62bc547728"},
    {"Wallet Name": "Aptos Mainnet Wallet 148", "Address": "0x2eecfeafdec570ebeb171cbec071ebd3eed699af62d3466f282e4f30f7d40c47"},
    {"Wallet Name": "Aptos Mainnet Wallet 151", "Address": "0xa7c35b85a72c967777d3fcffd739368af9a2c676e23797c66357769b2cbbf341"},
    {"Wallet Name": "Aptos Mainnet Wallet 154", "Address": "0x07c0f53feccc51bcb3949243ae730db38eee482631a2ee432b28752f2ec19a3f"},
    {"Wallet Name": "Aptos Mainnet Wallet 155", "Address": "0xe026e8f4d0ce45c7bdc413455a5444dc8ef5dc405720c0bc2b652bcf3678f0b7"},
    {"Wallet Name": "Aptos Mainnet Wallet 157", "Address": "0x7581ea8156533ccd8f7fa3b78032fcbcee99e63aa5c9e068914950e2b84da608"},
    {"Wallet Name": "Aptos Mainnet Wallet 169", "Address": "0x8d6aabfbdf88a7199d286c35ef0a92abc6e0aafd5de09c747f19cfcf4b4c5670"},
    {"Wallet Name": "Aptos Mainnet Wallet 17", "Address": "0x82a209a061f02239359417545d804f78fbbe4d3dfe9a7fbf748a21365ed20d9d"},
    {"Wallet Name": "Aptos Mainnet Wallet 175", "Address": "0x1d2cf6993441ae8717a6ef7e29ed7aa07ec3110514354e16e9b633b59bb94a91"},
    {"Wallet Name": "Aptos Mainnet Wallet 184", "Address": "0x5b84f643a92ec5259123be474679f28f5f232e9ab178db0de38b79edd28419b7"},
    {"Wallet Name": "Aptos Mainnet Wallet 185", "Address": "0xce7ff9f0b8bbf80b240bd86c389a3bbfe9bb59219da0679680fe2acd6fb85393"},
    {"Wallet Name": "Aptos Mainnet Wallet 19", "Address": "0x9342065552aa86d663bd13b1b43000da75add0f1fa422882d56377a9e6208a3a"},
    {"Wallet Name": "Aptos Mainnet Wallet 268", "Address": "0x0bb4d4cea83abc7acef52cb4e167805be446d647b91989c6e0b4f71c45e54baa"},
    {"Wallet Name": "Aptos Mainnet Wallet 303", "Address": "0x5711fd997e7ad78dbbf1e8cb0b89af50f4f013d6114afb2fd0c520fa763f68e2"},
    {"Wallet Name": "Aptos Mainnet Wallet 306", "Address": "0xb64719986e834691b58d2c5ee923a367ffcb80eed93e8b71c5e0b5fe189fac49"},
    {"Wallet Name": "Aptos Mainnet Wallet 307", "Address": "0x702ebda8da252a8771b9cfa7d5cf837549ddb6d4863a875a114298649d9faaec"},
    {"Wallet Name": "Aptos Mainnet Wallet 308", "Address": "0xabc5ddee336de6fd180a987ddecfa7e6d0f9399741f9f08f0b6789548e92f6ef"},
    {"Wallet Name": "Aptos Mainnet Wallet 55", "Address": "0x6e745e1fec530a6e8cbb37636591da99da53114dd6dd63732d3d6b0fe3d3a6ef"},
    {"Wallet Name": "Aptos Mainnet Wallet 58", "Address": "0xee86edd0102ba974725bce23b126d922aaf76d3e53f715a842aaffa301483ed3"},
    {"Wallet Name": "Aptos Mainnet Wallet 62", "Address": "0xc017e802c25f519f26209785a88c2688b2b75caeca3624f12fdf9274a02874d5"},
    {"Wallet Name": "Aptos Mainnet Wallet 70", "Address": "0x8d4184a18addf3a54ee2d8c120e9b1de5e929f22057b87b9ef2abee38c6784bd"},
    {"Wallet Name": "Aptos Mainnet Wallet 71", "Address": "0xdd79bb077b5480786e4aad7823c2f56368d7c7cdb4350d0cafa735939c1c2d4c"},
    {"Wallet Name": "Aptos Mainnet Wallet 75", "Address": "0x75d82b3fb50875a6858311ff7686b4a5062ed1547ca615c664b6e5b8c4cad399"},
    {"Wallet Name": "Aptos Mainnet Wallet 78", "Address": "0xd6d70afbe79d002f1ad135025deccd5a8257c61a4725c8b69291929173717bbb"},
    {"Wallet Name": "Aptos Mainnet Wallet 84", "Address": "0x8a2b9c9815d07e049dab7b02ad6104bff5adb539948b731ceaf38f8c6f151bf4"},
    {"Wallet Name": "Aptos Mainnet Wallet 85", "Address": "0x9503582321f1ddf75ee5bce7c6a27f3ad105c2f4b6426367c662e93f46cd4f0c"},
    {"Wallet Name": "Aptos Mainnet Wallet 88", "Address": "0x28007cdf67281f26c30bccb7651c582880fff7007bb83fc85a3e080213e7b3ae"},
    {"Wallet Name": "Aptos Mainnet Wallet 93", "Address": "0x64b21481a432f9a9afdc134bad91e8a3361556db8fdb618978780b201ca0c913"},
    {"Wallet Name": "Aptos Mainnet Wallet 97", "Address": "0x256724e94b026171601ff9d16fb5eb8ef08b10b7b19e374e017653db84816787"},
    {"Wallet Name": "Aptos Mainnet Wallet 98", "Address": "0x40236e3f4ee2f7e1b15795edc10d8bf7e07aad93ae94051a3efe7a95efef02f7"},
    {"Wallet Name": "Aptos - Do Kwon", "Address": "0x5aba5dd7021e53e8ee3aab8e0759ff3a634cb52c83c149dbea812c064f5c1b4b"},
    {"Wallet Name": "Aptos Mainnet Wallet 90", "Address": "0x887dbc66257a99518b98ffc0b86ab84dd9974aea1667498623540d5bbb66bfba"},
    {"Wallet Name": "Aptos Mainnet Wallet 87", "Address": "0x9ff36d0476bd923f29e43fae2c251d5a02c3532e4dde18270ff2882378d62226"},
    {"Wallet Name": "Aptos Mainnet Wallet 76", "Address": "0xb75ba0117fd363a54dc976636d003958bf36124cc9bfc6f8e8a953f053ab14ca"},
    {"Wallet Name": "Aptos Mainnet Wallet 74", "Address": "0x4b705711e08994790da690388ad07f5391f7258aa47af41c7e5545cd28c4a4ab"},
    {"Wallet Name": "Aptos Mainnet Wallet 73", "Address": "0x9b95702596a45d806ae6ef2a17b955e140c79fed84590ea2aa7f0fdc3440dd00"},
    {"Wallet Name": "Aptos Mainnet Wallet 67", "Address": "0xe96d0792cd62b99f434e542c5dd9b4e146e71bad5ccbff65c51a350f9972d0fe"},
    {"Wallet Name": "Aptos Mainnet Wallet 66", "Address": "0xd90a51dc740b22ac487139962e6e0e0c2b694b98af01ddc39c4ae46d62ae3e9c"},
    {"Wallet Name": "Aptos Mainnet Wallet 65", "Address": "0x7b7ebee202201e23f3d443d97d8884a83dd5933be59e033ce8273dd82b66af1a"},
    {"Wallet Name": "Aptos Mainnet Wallet 6", "Address": "0x1af1823ca71a9cbd37005e7a4b4b3815fb26ce25cc53ec633aadd7ebade11dc2"},
    {"Wallet Name": "Aptos Mainnet Wallet 53", "Address": "0x0bddf6990a52fce1c29f69b6196150143e9ac44e4984bbc52741e60f422817da"},
    {"Wallet Name": "Aptos Mainnet Wallet 52", "Address": "0x258bc02e81cc57b7e3383eb5866513428257fefde8e69684215add52aa0abd8b"},
    {"Wallet Name": "Aptos Mainnet Wallet 50", "Address": "0xb71a9c7dbce47be1706566aeb2b47d60f24b52aec039bd78e58fee77a71bece4"},
    {"Wallet Name": "Aptos Mainnet Wallet 48", "Address": "0xb69f4f7bb52ed7b111afe95d6492bb5addeac81fa734f087f5b6315981ac9f90"},
    {"Wallet Name": "Aptos Mainnet Wallet 39", "Address": "0x1720fe518f0a2573a61704de1d07f430df87a1549e70697c54d56c0445ee88f7"},
    {"Wallet Name": "Aptos Mainnet Wallet 37", "Address": "0x065e1ec4bfffd4592379e729e5a595254bda27cc3521889e1770aa3370cacd18"},
    {"Wallet Name": "Aptos Mainnet Wallet 36", "Address": "0x6171a66ef37f2c9f5065142b01d8139409453b29753fe19cb0356be08c930751"},
    {"Wallet Name": "Aptos Mainnet Wallet 32", "Address": "0x834b4d54d30d3c58a5f791cd4bc80ce5919c062575f8b98c1b671b1a222e29ac"},
    {"Wallet Name": "Aptos Mainnet Wallet 31", "Address": "0xf949e46b05a1414ec6b5de673ce331e4dd6e351e43dc2b70f2e3639d468eba6f"},
    {"Wallet Name": "Aptos Mainnet Wallet 301", "Address": "0xaaa9c5fb3b4855e1569321041febcc1146b44af3f08893d4ce41846cc7e25645"},
    {"Wallet Name": "Aptos Mainnet Wallet 267", "Address": "0xed2c3d0826094963df0ee80c3b28555e3024f5ecf6b9beb88f26379fa19b3b7f"},
    {"Wallet Name": "Aptos Mainnet Wallet 266", "Address": "0x1df9fc0f3908ddc1025c91d774ba7954404ae710a3ebc4d25bc7bf7fcb26ffb4"},
    {"Wallet Name": "Aptos Mainnet Wallet 264 " , "Address": "0xa32e6f8dc6747b53d75e57e79b539aa641711604aaedac98ab84a73f30c7617a"},
    {"Wallet Name": "Aptos Mainnet Wallet 260", "Address": "0xe87747b6faa3f5095341714fba8edf6b4b88489cdf33e1192fe23c8fb3509dc6"},
    {"Wallet Name": "Aptos Mainnet Wallet 259", "Address": "0x9201d69100aaa13f6ae3e2f7db87f08cb25c43f6134bd62855970e2f13e81898"},
    {"Wallet Name": "Aptos Mainnet Wallet 258", "Address": "0x53496ba0c3974434add4bea19ba2dc5aa63713dc30b566ff5062d94357d8b348"},
    {"Wallet Name": "Aptos Mainnet Wallet 257", "Address": "0x74b0c27c7d3b89b22962f6a609ef9a11cde10756045273163f35175e7cb164f5"},
    {"Wallet Name": "Aptos Mainnet Wallet 256", "Address": "0x81f33081a7546b9b3a040f7bfa047ff28a5bb9707072074ad57469b0e885218d"},
    {"Wallet Name": "Aptos Mainnet Wallet 254", "Address": "0x0d24ecb979d3031f198f0e76ed22894c1b8f8af5ab944f5659c6f0bcc628f10a"},
    {"Wallet Name": "Aptos Mainnet Wallet 251", "Address": "0x38e1b87887946977b5170a299bbaba2e2b728c5ef96847a4482973706c810112"},
    {"Wallet Name": "Aptos Mainnet Wallet 250", "Address": "0x6a6783b060213b4892c6da38530ccd274329bcbc4972d37f3ee4dc7b15db1640"},
    {"Wallet Name": "Aptos Mainnet Wallet 249", "Address": "0x6c84007e93701be49838cde2be39a26f4acfffb3b45d028080649809c8d77952"},
    {"Wallet Name": "Aptos Mainnet Wallet 248", "Address": "0x8b2b0f85b2c6d913f97f0ad5180c6f8a295c08b86ed7d07a63545b97c4b00355"},
    {"Wallet Name": "Aptos Mainnet Wallet 247", "Address": "0x67575e0d56a26a1a6dc6005a7b0c4647b2b5c78a2234aac52cba2bfc713ecf0d"},
    {"Wallet Name": "Aptos Mainnet Wallet 246", "Address": "0xbf4eae0d614b8a7207cd0f8df9cc3fb5a3663616ec76ab397d82d29de712f693"},
    {"Wallet Name": "Aptos Mainnet Wallet 245", "Address": "0xb1fe5517c3a927978a9e50b89a4f582d11bf8f987ff77630723a9c49960db018"},
    {"Wallet Name": "Aptos Mainnet Wallet 243", "Address": "0x072c78c9ce114fbb9acadb0ac1e235cd9fc0fc4c3ee618d4416818c43ecc01c9"},
    {"Wallet Name": "Aptos Mainnet Wallet 24", "Address": "0xc65d3d252f87d4244048771c803ae5247bd349822a7df66893806441e1b4e90f"},
    {"Wallet Name": "Aptos Mainnet Wallet 238", "Address": "0xf74922a3ef2331f5621959aad09a4067bead090525aae564024554f2f93f4d18"},
    {"Wallet Name": "Aptos Mainnet Wallet 236", "Address": "0x4d94fde3604cc27f9c2547b487ab4beaf559ccabe97e278925fa38cfc4ec6765"},
    {"Wallet Name": "Aptos Mainnet Wallet 233", "Address": "0x202191439b23bca6bfce51597124291f951daccd60fa7c678d78858c7612d3e5"},
    {"Wallet Name": "Aptos Mainnet Wallet 230", "Address": "0x5c7009064f63e2b82a6999e69e7359bfa129f37249791ce30ef47c4f0c42c66a"},
    {"Wallet Name": "Aptos Mainnet Wallet 23", "Address": "0x0773be794dd34c38407d9cf8e9f6b382c81ebee4334aec8b4939fcc6cd0e0e33"},
    {"Wallet Name": "Aptos Mainnet Wallet 228", "Address": "0x9f2e063d93e00d795e881137d3b7a5e4ee540daae00d610223e349a1ec41a0ae"},
    {"Wallet Name": "Aptos Mainnet Wallet 227", "Address": "0x55111beec1a5247ab4577e9870832b9588929fffe3e1b0ecc56eb3da4d1dd8ab"},
    {"Wallet Name": "Aptos Mainnet Wallet 226", "Address": "0xc23c6b1b157b4ef4da1d97312d0f0d2359914ffd541048744ef4be0a7c61efb9"},
    {"Wallet Name": "Aptos Mainnet Wallet 222", "Address": "0xa91ea5957f7b8dae65e52e28e4bf582bd8a2000a27e9672753ef73decbf7be07"},
    {"Wallet Name": "Aptos Mainnet Wallet 221", "Address": "0xc4599c79e78aa795b14633f035ae9755dee9600927624d11a8064acc6f305486"},
    {"Wallet Name": "Aptos Mainnet Wallet 220", "Address": "0x9189f547224e8136338649c3bc3ea3af5ae81e165c83fb3afcd356b0b00ad4be"},
    {"Wallet Name": "Aptos Mainnet Wallet 218", "Address": "0xddef941d8d67604f6f8cd7370e199655a749576111cf1e179af702da23dd2b22"},
    {"Wallet Name": "Aptos Mainnet Wallet 216", "Address": "0xaa07d109863572d2c7f3850b47fb43e47b457998902e8c64f3b9bc44fe66f148"},
    {"Wallet Name": "Aptos Mainnet Wallet 214", "Address": "0x4a37786aa960a0fa8b5d547182b61d41be313aedc6c8a6a62b2ebc8a9496db5a"},
    {"Wallet Name": "Aptos Mainnet Wallet 213", "Address": "0x43f294b8144b1ccc53821084d5e5a8d8e01c0a49304f5103fc5dff74659b3107"},
    {"Wallet Name": "Aptos Mainnet Wallet 212", "Address": "0x32e83d55b9e536919837285b2501a93f43862f99297a27ef776154a94c6989a5"},
    {"Wallet Name": "Aptos Mainnet Wallet 211", "Address": "0xf8a0e99649ba484f2e2dd0ea5c2d30b4ef85f77e10bb13222be94afbf0974d7d"},
    {"Wallet Name": "Aptos Mainnet Wallet 210", "Address": "0xc5ec99a7823519ea8535adc22c114132342484eae7b71cce18c4a6a3f0b8669a"},
    {"Wallet Name": "Aptos Mainnet Wallet 209", "Address": "0x677aa8bad1137f9afd54f19929f071bda27f2bcc23b476d0f24efa81a8c43e36"},
    {"Wallet Name": "Aptos Mainnet Wallet 208", "Address": "0x79446f36e69792bad7dc1c2c271b57dceb9132364f425abcba1c91dcc16903a0"},
    {"Wallet Name": "Aptos Mainnet Wallet 207", "Address": "0x5f72f368a64e36af7245b5f0de541de8c8d289622166ae09b72249bf911b841a"},
    {"Wallet Name": "Aptos Mainnet Wallet 206", "Address": "0x215ef071cb38327801144643eaffcf8f9da70b5e0424f6142a83c7377a6e0715"},
    {"Wallet Name": "Aptos Mainnet Wallet 205", "Address": "0x535558440c939163fbff65253a4ce2cf7a16b3144337dbea1f8e0e5cdeb89ffe"},
    {"Wallet Name": "Aptos Mainnet Wallet 204", "Address": "0x21b22d459a29cdd663e7bcfd7f1906dd93d8d9fe8099b4c68fe93aadb6250de6"},
    {"Wallet Name": "Aptos Mainnet Wallet 203", "Address": "0x48ef004ba16b0a3ea7f04d32a9bef6573169197654c40c81ee46b4dd0ae9f892"},
    {"Wallet Name": "Aptos Mainnet Wallet 202", "Address": "0x9931f41f7286e16c227dd7ecdacfa438042faf83e352e4602211eae92bd4871b"},
    {"Wallet Name": "Aptos Mainnet Wallet 201", "Address": "0xf66a130c734a112a5d84c718a1e82a70f2b94ee1195a042cbd5f27081810d7f5"},
    {"Wallet Name": "Aptos Mainnet Wallet 200", "Address": "0xccc221485ee530f3981f4beca12f010d2e7bb38d3fe30bfcf7798d99f4aabb33"},
    {"Wallet Name": "Aptos Mainnet Wallet 199", "Address": "0xb4df284e06648c3fa3bd0c39266f48ba6a97607d04f8a92bd17f658dcc2a1bd3"},
    {"Wallet Name": "Aptos Mainnet Wallet 198", "Address": "0xdff789994702c4638b0da2c11e2cc69ea63438c2643debfc01a60a8c17e79ff3"},
    {"Wallet Name": "Aptos Mainnet Wallet 197", "Address": "0xcd30fbbda98b2aed026772c13e5ed90a7f056b589ef9e78cd96415e1af12451c"},
    {"Wallet Name": "Aptos Mainnet Wallet 195", "Address": "0x5870c0c294fb3916567a759937b6ac82732ff35ef284b5563503b9dfc84c8d4b"},
    {"Wallet Name": "Aptos Mainnet Wallet 194", "Address": "0x96617758ab2df2e871c2248384a43c4427a0a072e789538bea083283d2fef0b5"},
    {"Wallet Name": "Aptos Mainnet Wallet 193", "Address": "0x54ba224e60b095a35322a851adf92e81dd6cb7fd9ee4e2e9a281681501892ec8"},
    {"Wallet Name": "Aptos Mainnet Wallet 192", "Address": "0x6064d2f4c38b65e9b78fbdf8a80f084159341d47b5e0c192492923326d1bed0a"},
    {"Wallet Name": "Aptos Mainnet Wallet 191", "Address": "0x2fccfed3d745d80b8f72dc5235bec7d82d5fe80c63ab851e4eb22e1829cdcdaa"},
    {"Wallet Name": "Aptos Mainnet Wallet 190", "Address": "0xaa321de84b692666439086bf2bd251f56c9a5d7cc129d8600442093519d8100b"},
    {"Wallet Name": "Aptos Mainnet Wallet 189", "Address": "0x94685b08149f4eae3c75d21287a2f3b74131dae2a0cb7b04adcefca0af644229"},
    {"Wallet Name": "Aptos Mainnet Wallet 188", "Address": "0xc4fce0915e96da42bafa97db7e497896e87763bdd3634486ec4e8a5353183503"},
    {"Wallet Name": "Aptos Mainnet Wallet 187", "Address": "0x08ef33d146a95f085fbcf9fd0ed5362de7bc69db5c7d5d9dfd3d8c8acd92b559"},
    {"Wallet Name": "Aptos Mainnet Wallet 186", "Address": "0x0756c80f0597fc221fe043d5388949b34151a4efe5753965bbfb0ed7d0be08ea"},
    {"Wallet Name": "Aptos Mainnet Wallet 183", "Address": "0x8a78c7d3a66bb09251622a682f8d1336cf134677487f636c8e815717345784a3"},
    {"Wallet Name": "Aptos Mainnet Wallet 176", "Address": "0xe016e35ae14826e5831913482c7a625c29a9a2b17e330490ffa2b0515e1710ba"},
    {"Wallet Name": "Aptos Mainnet Wallet 174", "Address": "0x5cb5ca99d8947a08ee951ed9c994cebd946dacdf4d98441645eca5e6499fb285"},
    {"Wallet Name": "Aptos Mainnet Wallet 171", "Address": "0xba417747fc94afde338f5031f556ee5ecec3da795f9e4afa607c724c5fe801bc"},
    {"Wallet Name": "Aptos Mainnet Wallet 168", "Address": "0x035efecb0c07a0ff0367ab01bd38840b796ad4df1959363a0d55495b2bb9fdc2"},
    {"Wallet Name": "Aptos Mainnet Wallet 153", "Address": "0xaae3dbc92ad472ce5312b6e1f79ec467f37d027ca6064e78475c0f724feea088"},
    {"Wallet Name": "Aptos Mainnet Wallet 144", "Address": "0xfadb6980891ab838639e617255324332ba75f58714b2ee281b5984d0819202df"},
    {"Wallet Name": "Aptos Mainnet Wallet 141", "Address": "0x406daf87d651396bed15d8b4b55664a5639e5e1205292e14405307e85f56d37a"},
    {"Wallet Name": "Aptos Mainnet Wallet 137", "Address": "0x4c58a38833d6527902c12287c65b83103ae08374e1191ff7fe74b07d43a4dd55"},
    {"Wallet Name": "Aptos Mainnet Wallet 128", "Address": "0xecc2110cd190b2101709b5d51674379ee8005cffa29f2d3344c083cbff25b13d"},
    {"Wallet Name": "Aptos Mainnet Wallet 126", "Address": "0xc466f174b6533c1516b9389ec50e7d518369f08cbef8815a7308a6462ed5fb0b"},
    {"Wallet Name": "Aptos Mainnet Wallet 119", "Address": "0xe266a1b119c6c149a76a66cfd017514bdd8f9191cf53a8d3c40baaca405f16de"},
    {"Wallet Name": "Aptos Mainnet Wallet 115", "Address": "0xf8174d6de06b5ff961279015d5c080902ff19f20bcb2d1bc109d9efa4eeee2e8"},
    {"Wallet Name": "Aptos Mainnet Wallet 114", "Address": "0xe3dab0aa348eee08c8e0cc9ecf56650ad9f9a98b78224ca045abd50bea3503dd"},
    {"Wallet Name": "Aptos Mainnet Wallet 113", "Address": "0xa162e0449405eeae3b492eb9cd24534d32e0bdb1cc92c1083cfbd6d712efb89b"},
    {"Wallet Name": "Aptos Mainnet Wallet 110", "Address": "0x7664cec5d893f8ca41d69621a31920a9310488405936e346749035feb2abad81"},
    {"Wallet Name": "Aptos Mainnet Wallet 108", "Address": "0xfeba00184ee586791e741485ca7579e32168fcd78224f65d7add9defe9abbe52"},
    {"Wallet Name": "Aptos Mainnet Wallet 100", "Address": "0x2db22014a577bca5d9e17fefbad3d14c94249f6be5069a6910706d88071a458c"}
]

# Convert wallets list to DataFrame
wallets_df = pd.DataFrame(wallets_list)

# Create address-to-name mapping
address_to_name = dict(zip(wallets_df['Address'], wallets_df['Wallet Name']))

# Streamlit app title
st.title("Anchorage Transaction Report Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload Anchorage Transaction CSV", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Convert 'End Time' to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Extract month-year for grouping
    df['Month'] = df['End Time'].dt.to_period('M')
    
    # Replace addresses with wallet names
    df['Destination Address'] = df['Destination Address'].map(address_to_name).fillna(df['Destination Address'])
    df['Source Addresses'] = df['Source Addresses'].map(address_to_name).fillna(df['Source Addresses'])
    
    # Initialize output dataframes
    staking_rewards = []
    balance_adjustments = []
    
    # Process Staking Rewards
    staking_df = df[df['Type'] == 'Staking Reward']
    if not staking_df.empty:
        staking_summary = staking_df.groupby(['Month', 'Destination Address']).agg({
            'Asset Quantity (Before Fee)': 'sum',
            'Value (USD)': 'sum'
        }).reset_index()
        staking_summary.columns = ['Month', 'Destination Wallet', 'Total Asset Quantity', 'Total Value (USD)']
        staking_rewards.append(staking_summary)
    
    # Process Balance Adjustments
    balance_df = df[df['Type'] == 'Balance Adjustment']
    if not balance_df.empty:
        balance_summary = balance_df.groupby(['Month', 'Destination Address', 'Source Addresses']).agg({
            'Asset Quantity (Before Fee)': 'sum',
            'Value (USD)': 'sum'
        }).reset_index()
        balance_summary.columns = ['Month', 'Destination Wallet', 'Source Wallet', 'Total Asset Quantity', 'Total Value (USD)']
        balance_adjustments.append(balance_summary)
    
    # Display results
    if staking_rewards:
        st.subheader("Staking Rewards Totals by Month and Destination Wallet")
        st.dataframe(staking_rewards[0])
    else:
        st.write("No Staking Reward transactions found.")
    
    if balance_adjustments:
        st.subheader("Balance Adjustments Totals by Month, Destination, and Source Wallet")
        st.dataframe(balance_adjustments[0])
    else:
        st.write("No Balance Adjustment transactions found.")
    
    # Combine results for download
    if staking_rewards or balance_adjustments:
        output_df = pd.concat(staking_rewards + balance_adjustments, ignore_index=True)
        # Convert Month to string for CSV
        output_df['Month'] = output_df['Month'].astype(str)
        
        # Create CSV buffer
        buffer = io.StringIO()
        output_df.to_csv(buffer, index=False)
        buffer.seek(0)
        
        # Download button
        st.download_button(
            label="Download Results as CSV",
            data=buffer.getvalue(),
            file_name="transaction_totals_by_month.csv",
            mime="text/csv"
        )
else:
    st.write("Please upload a CSV file to analyze.")
