from Ciphers.CrittersCipher import CrittersCipher


def Test1():
    critters = CrittersCipher()

    s1 = "testencrypt"
    s1again = "testencrypt"
    res1 = critters.convertToBitsThenBlocks(s1)
    res2 = critters.convertToBitsThenBlocks(s1again)
    print("bitversion", res1)
    print("bitversion", res2)
    res1encrypted = critters.runOneEncryptionCycle(res1)
    res2encrypted = critters.runOneEncryptionCycle(res2)
    res1 = critters.isolateResult(res1encrypted)
    res2 = critters.isolateResult(res2encrypted)
    print("After one cycle - Res1:", res1, "Res2:", res2)

    res1encrypted = critters.runOneEncryptionCycle(res1encrypted)
    res2encrypted = critters.runOneEncryptionCycle(res2encrypted)
    res1 = critters.isolateResult(res1encrypted)
    res2 = critters.isolateResult(res2encrypted)
    print("After two cycles - Res1:", res1, "Res2:", res2)

    res1encrypted = critters.runOneEncryptionCycle(res1encrypted)
    res2encrypted = critters.runOneEncryptionCycle(res2encrypted)
    res1 = critters.isolateResult(res1encrypted)
    res2 = critters.isolateResult(res2encrypted)
    print("After three cycles - Res1:", res1, "Res2:", res2)

    res1encrypted = critters.runOneEncryptionCycle(res1encrypted)
    res2encrypted = critters.runOneEncryptionCycle(res2encrypted)
    res1 = critters.isolateResult(res1encrypted)
    res2 = critters.isolateResult(res2encrypted)
    print("After four cycles - Res1:", res1, "Res2:", res2)


def Test2():
    critters = CrittersCipher()
    # testing that CA algorithm works
    testCase1 = [[[0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                  [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
                  [0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
                  [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
                  [0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                  [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
                  [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                  [0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]]
    res1 = critters.runOneEncryptionCycle(testCase1)
    expectedRes = [[[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 0, 0, 1, 0, 1, 1]]]
    if res1 == expectedRes:
        print(True)
    else:
        print(False)
        print(res1)
        print(expectedRes)

def Test3():
    critters = CrittersCipher()

    s1 = "testencrypt"
    s1again = "testencrypt"
    publickey = 3
    secretkey = 1
    encrypted1 = critters.encrypt(s1, publickey)
    encrypted1again = critters.encrypt(s1again, publickey)
    print("encrypted - s1:", encrypted1, "s2:", encrypted1again)
    decrypted1 = critters.decrypt(encrypted1, secretkey)
    decryptedagain1 = critters.decrypt(encrypted1again, secretkey)
    print("decrypted - s1:", decrypted1, "s2:", decryptedagain1)
# E©ÌG©r¨F¿Bÿ

def Test4():
    testStr = 'testStringStayTheSame'
    critters = CrittersCipher()
    for i in range(10):
        res = critters.convertToBitsThenBlocks(testStr)
        encrypted = critters.runOneEncryptionCycle(res)
        testStr = critters.isolateResult(encrypted)
        print(testStr)

#µ¾Î¶¾qh¶ò{pO
#µ¾Î¶¾qh¶ò{pO

Test1()
Test2()
Test3()
Test4()