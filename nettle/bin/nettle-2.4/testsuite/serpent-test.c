#include "testutils.h"
#include "serpent.h"

static uint8_t *
decode_hex_reverse (const char *hex)
{
  unsigned length = decode_hex_length (hex);
  uint8_t *p = xalloc(length);
  unsigned i;

  decode_hex(p, hex);

  for (i = 0; i < (length+1)/2; i++)
    {
      uint8_t t = p[i];
      p[i] = p[length - 1 - i];
      p[length - 1 - i] = t;
    }
  return p;
}

#define RH(x) decode_hex_reverse(x)
#define RHL(x) decode_hex_length(x), decode_hex_reverse(x)

int
test_main(void)
{
  /* From libgcrypt */
  test_cipher(&nettle_serpent128,
	      HL("0000000000000000 0000000000000000"),
	      HL("D29D576FCEA3A3A7 ED9099F29273D78E"),
	      H("B2288B968AE8B086 48D1CE9606FD992D"));
  test_cipher(&nettle_serpent192,
	      HL("0000000000000000 0000000000000000 0000000000000000"),
	      HL("D29D576FCEABA3A7 ED9899F2927BD78E"),
	      H("130E353E1037C224 05E8FAEFB2C3C3E9"));
  test_cipher(&nettle_serpent256,
	      HL("0000000000000000 0000000000000000"
		 "0000000000000000 0000000000000000"),
	      HL("D095576FCEA3E3A7 ED98D9F29073D78E"),
	      H("B90EE5862DE69168 F2BDD5125B45472B"));
  test_cipher(&nettle_serpent256,
	      HL("0000000000000000 0000000000000000"
		 "0000000000000000 0000000000000000"),
	      HL("0000000001000000 0200000003000000"),
	      H("2061A42782BD52EC 691EC383B03BA77C"));

  /* The first test for each key size from the ecb_vk.txt and ecb_vt.txt
   * files in the serpent package. */

  /* NOTE: These vectors uses strange byte-reversed order of inputs
     and outputs. */
  /* 128 bit key */

  /* vk, 1 */
  test_cipher(&nettle_serpent128,
	      RHL("8000000000000000 0000000000000000"),
	      RHL("0000000000000000 0000000000000000"),
	      RH("49AFBFAD9D5A3405 2CD8FFA5986BD2DD"));

  /* vt, 1 */
  test_cipher(&nettle_serpent128,
	      RHL("0000000000000000 0000000000000000"),
	      RHL("8000000000000000 0000000000000000"),
	      RH("10B5FFB720B8CB90 02A1142B0BA2E94A"));

  /* 192 bit key */

  /* vk, 1 */
  test_cipher(&nettle_serpent192,
	      RHL("8000000000000000 0000000000000000"
		 "0000000000000000"),
	      RHL("0000000000000000 0000000000000000"),
	      RH("E78E5402C7195568 AC3678F7A3F60C66"));

  /* vt, 1 */
  test_cipher(&nettle_serpent192,
	      RHL("0000000000000000 0000000000000000"
		 "0000000000000000"),
	      RHL("8000000000000000 0000000000000000"),
	      RH("B10B271BA25257E1 294F2B51F076D0D9"));

  /* 256 bit key */

  /* vk, 1 */
  test_cipher(&nettle_serpent256,
	      RHL("8000000000000000 0000000000000000"
		 "0000000000000000 0000000000000000"),
	      RHL("0000000000000000 0000000000000000"),
	      RH("ABED96E766BF28CB C0EBD21A82EF0819"));

  /* vt, 1 */
  test_cipher(&nettle_serpent256,
	      RHL("0000000000000000 0000000000000000"
		 "0000000000000000 0000000000000000"),
	      RHL("8000000000000000 0000000000000000"),
	      RH("DA5A7992B1B4AE6F 8C004BC8A7DE5520"));

  /* Test vectors from
     http://www.cs.technion.ac.il/~biham/Reports/Serpent/ */

  /* serpent128 */
  /* Set 4, vector#  0 */
  test_cipher(&nettle_serpent128,
	      HL("000102030405060708090A0B0C0D0E0F"),
	      HL("00112233445566778899AABBCCDDEEFF"),
	      H("563E2CF8740A27C164804560391E9B27"));

  /* Set 4, vector#  1 */
  test_cipher(&nettle_serpent128,
	      HL("2BD6459F82C5B300952C49104881FF48"),
	      HL("EA024714AD5C4D84EA024714AD5C4D84"),
	      H("92D7F8EF2C36C53409F275902F06539F"));

  /* serpent192 */
  /* Set 4, vector#  0 */
  test_cipher(&nettle_serpent192,
	      HL("000102030405060708090A0B0C0D0E0F1011121314151617"),
	      HL("00112233445566778899AABBCCDDEEFF"),
	      H("6AB816C82DE53B93005008AFA2246A02"));

  /* Set 4, vector#  1 */
  test_cipher(&nettle_serpent192,
	      HL("2BD6459F82C5B300952C49104881FF482BD6459F82C5B300"),
	      HL("EA024714AD5C4D84EA024714AD5C4D84"),
	      H("827B18C2678A239DFC5512842000E204"));

  /* serpent256 */
  /* Set 4, vector#  0 */
  test_cipher(&nettle_serpent256,
	      HL("000102030405060708090A0B0C0D0E0F"
		 "101112131415161718191A1B1C1D1E1F"),
	      HL("00112233445566778899AABBCCDDEEFF"),
	      H("2868B7A2D28ECD5E4FDEFAC3C4330074"));

  /* Set 4, vector#  1 */
  test_cipher(&nettle_serpent256,
	      HL("2BD6459F82C5B300952C49104881FF48"
		 "2BD6459F82C5B300952C49104881FF48"),
	      HL("EA024714AD5C4D84EA024714AD5C4D84"),
	      H("3E507730776B93FDEA661235E1DD99F0"));

  /* Test key padding. We use nettle_serpent256, which actually works
     also with key sizes smaller than 32 bytes. */
  test_cipher(&nettle_serpent256,
	      HL("00112233440100000000000000000000"
		 "00000000000000000000000000000000"),
	      HL("0000000001000000 0200000003000000"),
	      H("C1415AC653FD7C7F D917482EE8EBFE25"));

  /* Currrently, key sizes smaller than SERPENT_MIN_KEY_SIZE bytes
     (128 bits) are not supported. */
  test_cipher(&nettle_serpent256,
	      HL("0011223344"),
	      HL("0000000001000000 0200000003000000"),
	      H("C1415AC653FD7C7F D917482EE8EBFE25"));

  test_cipher(&nettle_serpent256,
	      HL("00112233445566778899aabbccddeeff"
		 "00010000000000000000000000000000"),
	      HL("0000000001000000 0200000003000000"),
	      H("8EB9C958EAFFDF42 009755D7B6458838"));

  test_cipher(&nettle_serpent256,
	      HL("00112233445566778899aabbccddeeff"
		 "00"),
	      HL("0000000001000000 0200000003000000"),
	      H("8EB9C958EAFFDF42 009755D7B6458838"));

  test_cipher(&nettle_serpent256,
	      HL("00112233445566778899aabbccddeeff"
		 "00112201000000000000000000000000"),
	      HL("0000000001000000 0200000003000000"),
	      H("C8A078D8212AC96D 9060E30EC5CBB5C7"));

  test_cipher(&nettle_serpent256,
	      HL("00112233445566778899aabbccddeeff"
		 "001122"),
	      HL("0000000001000000 0200000003000000"),
	      H("C8A078D8212AC96D 9060E30EC5CBB5C7"));

  /* Test with multiple blocks. */
  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"));

  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"));

  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"
		 "83c92a921b5b2028 d9cb313a5f07ab09"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"
		"8e44c2d463df4531 165461699edbad03"));

  test_cipher(&nettle_serpent128,
	      HL("91c8e949e12f0e38 7b2473238a3df1b6"),
	      HL("00000000 00000001 00000002 00000003"
		 "00000004 00000005 00000006 00000007"
		 "00000008 00000009 0000000a 0000000b"
		 "0000000c 0000000d 0000000e 0000000f"),
	      H("2db9f0a39d4f31a4 b1a83cd1032fe1bd"
		"3606caa84a220b1b f6f43ff80a831203"
		"8c6c8d2793dc10b3 904d30e194f086a6"
		"b2f3e932b9b3f8d1 d4d074f7bd1ff7a3"));
	      
  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"
		 "83c92a921b5b2028 d9cb313a5f07ab09"
		 "672eadf1624a2ed0 c42d1b08b076f75a"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"
		"8e44c2d463df4531 165461699edbad03"
		"30ac8c52697102ae 3b725dba79ceb250"));

  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"
		 "83c92a921b5b2028 d9cb313a5f07ab09"
		 "672eadf1624a2ed0 c42d1b08b076f75a"
		 "7378272aa57ad7c8 803e326689541266"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"
		"8e44c2d463df4531 165461699edbad03"
		"30ac8c52697102ae 3b725dba79ceb250"
		"d308b83478e86dbb 629f18736cca042f"));

  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"
		 "83c92a921b5b2028 d9cb313a5f07ab09"
		 "672eadf1624a2ed0 c42d1b08b076f75a"
		 "7378272aa57ad7c8 803e326689541266"
		 "b7a2efda5721776f 4113d63a702ac3ae"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"
		"8e44c2d463df4531 165461699edbad03"
		"30ac8c52697102ae 3b725dba79ceb250"
		"d308b83478e86dbb 629f18736cca042f"
		"006b89e494469adf 0ee78c60684dff86"));
    
  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"
		 "83c92a921b5b2028 d9cb313a5f07ab09"
		 "672eadf1624a2ed0 c42d1b08b076f75a"
		 "7378272aa57ad7c8 803e326689541266"
		 "b7a2efda5721776f 4113d63a702ac3ae"
		 "cd1be7bbfad74819 644617f8656e9e5b"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"
		"8e44c2d463df4531 165461699edbad03"
		"30ac8c52697102ae 3b725dba79ceb250"
		"d308b83478e86dbb 629f18736cca042f"
		"006b89e494469adf 0ee78c60684dff86"
		"5f2c99908ee77ffe aea3d30cb78a1ce1"));

  test_cipher(&nettle_serpent128,
	      HL("e87450aa0fd87293fd0371483a459bd2"),
	      HL("a78a7a8d392f629d bd13674c8dce6fa2"
		 "930c74dec02a11d8 c80d90b5e5c887a7"
		 "83c92a921b5b2028 d9cb313a5f07ab09"
		 "672eadf1624a2ed0 c42d1b08b076f75a"
		 "7378272aa57ad7c8 803e326689541266"
		 "b7a2efda5721776f 4113d63a702ac3ae"
		 "cd1be7bbfad74819 644617f8656e9e5b"
		 "34d449409c1f850a 4cb6700d6ef3405f"),
	      H("b3d488986c80dea7 c5ebdab4907871c9"
		"a4b92b13b79afb37 5518b01bfd706a37"
		"8e44c2d463df4531 165461699edbad03"
		"30ac8c52697102ae 3b725dba79ceb250"
		"d308b83478e86dbb 629f18736cca042f"
		"006b89e494469adf 0ee78c60684dff86"
		"5f2c99908ee77ffe aea3d30cb78a1ce1"
		"ebe855dd51532477 4d2d55969e032e6c"));

  SUCCESS();
}
