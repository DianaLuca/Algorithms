"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


import time


class Solution(object):
    def ispal(self, s):
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True

    def validPalindrome(self, s):
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return self.ispal(s[i: n-i-1]) or self.ispal(s[i+1: n-i])
        return True

    # ------------ TLE solution ------------
    def validPalindromeTLE(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        res = False
        t = ""
        if s[n // 2:][::-1] == s[:n // 2] or s[n // 2 + 1:][::-1] == s[:n // 2]:
            return True

        for i in range(n):
            if i == 0:
                t = s[1:]
            elif i == n - 1:
                t = s[:i]
            else:
                t = s[:i] + s[i + 1:]
            m = n - 1
            res = res or (t[m // 2:][::-1] == t[:m // 2]) or (t[m // 2 + 1:][::-1] == t[:m // 2])
            if res:
                return True
        return res


# test case
s = Solution()
# str - is 50000 #chars long and is not a palindrome - simulating Worst Case Scenario
str = "ipjiabbborwutgpnvarhbhjflnfztggysbomzpesulanxwtmahpitzxrscmyjyatyflapdkcsjmmvuvpkrevsxlcrkbqnrqcmwl\
        tqjbewlmmslzcgrusgfthllruivocaaoiuyqduwyqkcsoohanzxryudthnblqidmvnqlqnurqdliebsezgdlzskhxzzvenxwmj\
        okyunloqagyoklswajycvdijniolcpvslvemumzzzdgzwzfskkztjxmfyltznajikmdebspxvxcxvigpzvwipajgtxdkztaitg\
        ukitljtwjsuhdjbtkqmtvpguqoxxndvwuzyjhntlopuwbnbpxymbfnpnurgfgwnhlplzpnnpqdbpygrhswpqyaffwazvkuxlvh\
        tuaaxgcshnmsexjmofonbzbmeshcjjzwtemequcjcmtswahgzkktgnvlsyrxoqwsenclwckwkmtrkmxgkfdgvimyejtitcugyn\
        hymonndswxgjlcimyrnlpzxpdbmzqfjhjyikrejjlwnxvksoiucyvjtuzptxwvxdssudxxmwmrgbocdhqbdssbbanwmnflqedg\
        tzjqobgofvxeiwbggadbgudvsdatarbzjxtccraqxemsxfzqlwqislkbuneoymhqhrzhczhteqauvcaacmynrxfmrndgdudjcw\
        dcirujjutsiunfjumgxfjgbpegellqwcwbraekfaxvrpveswjrhuinqgmujnorstfvptoceghvafewlhaujmonvvtmthibbotz\
        cuqhfladmdrtbfsrnrjkilqxqoyjziwijuozdklzbrijkdvxkgcshbylqkbeqrwrigiyyvfeiaqwavqxyvhzbescjqpqjaqaqy\
        pwhztukkbdwgojdqiqlvygxvioubygirwmlfrqgylohfuodcvfpaqruiwzcglvrqmtwebxorngbscaxdfxguxhfzkikumxscrh\
        lsbczsfptsatmdlxjziosjvxmlnrysfgsyouzrsxddseoncqpmwerajhkzxvxucxlltllrplhbehpmjxpkoghqxwcfdvwuwogi\
        dkedwpilwpaqetypuzarvnrupqtxxrzjscdvkawcgezftvusddqhwszadragxqpgwhhugvykxytgmtsivuxfyjuslgqkbnpvtg\
        pqyiimpzfwfkcdssskbmfehigeqxdzprylbnnjlawjwpaxnfanufzhpcuzotfayrnheqppddirlsdjxrgujtoobmiwdylfbfzd\
        cqygjpsupepqmcmvyuohyqywaszwiiabfdjngklkcwiwtdhkvwlpdmilrjvzemfxpvfzavejxgultgulvigqmxfsecojlpzghm\
        ookwxwytsxuadbpkdfjuzicharfhnytysuriecrwvdnguhzapktlzxcfhuacclgdcbkdrorfylzeybsdmqiymwjvpsxxegeegc\
        fkrnlvmhgvenoxnprsswshskjwazrocohpliayyagaygmdlrxaomgvarzdavayurbrktoxblvntzscehdyyzcdbjhlrqjlyteq\
        cfuqoihdwvegobzpqxdwcuoezglbrtlofjnedqfjnoraglzxfghbxaieavytzirsdscilscsbocfdthbdsflsflqibkmtapvau\
        koqbmodlgewcrqmjdzecllqmgpnfindnaevogrpbzzyrbdrvqlpgtlnrmrwhfkrqrayrlbqcfojjpydogiryxmxjkljbyrxsfi\
        kmkfvxyyaoygzxiswgaodxlebnncwuywsqphrxqcioxdfjmkzpfjytroajttdlaegdsvnwfemagxcysnqdjoeagfvgdvuwonxy\
        naahdqegykcwgevzrfiwgvizmadhodejgppegcjwrwxvoszfbfmpigqwyedebsylpicvvvjvqnkwtfdycslvjhoxqhmvfzwdgn\
        fksaoaanhackimdjxjyyxpuyierdlwcgxxzxqnfexqjwuxbbgbzndrcgvzrdocoahclawkhvxitexpyybrsxaulpvumygggyxo\
        llkadoaucnqnmygsyqjxjagdtqjrmgfsgofocxgijekwovcyecqpghtezymqidgrmlzzkozxpgnxfoczemsfqltmpgqbmsokwd\
        sqbhifdojrvkraoysmaxsnetkiqiduvnqkhmxlnvjwchiolixwzyiziunzudacfyfbovnxhfkzedkfmwpuxgaqhortuooducau\
        jqhgoqnhiptxvayizefjivkphqbsngwaijczssrftvilmcbnotvibznbjzojgaopljdfcmpuaeaasnpduilohcgfocjljijwqa\
        llfcftebxssxtkcgcltvjhzsgfczillatgyzeoydazmagbrupzajkuhfgcetgwqenajijtoxnffkyxqruyuxywehdtyrtivbrg\
        nmvasfwtpzfhzsnoclknqkhwklepciijaoykvivmidchplymzbeyyltmsnddymvieoydsqzypnmsdyzgcuujzqqtgxybhslise\
        lfamhnemjmkiufsnqevdtjgggakeygnpypbbjvdayqppajprhsfbehdjtahrwlxkqvqsimbvcbwuyrjksbnkteaoqhdzkaimkt\
        eoxitalzvzjrdeenrtbtrbppjjajqnzuizvdgmlgxsbyjwzxfsqagutkfbzkzezdfnjlgxrlvpymbpdgzbneglootnpnclrgnk\
        cmtsaivetdnkfkkowgmsbvvrrfdscxmzybygaphvzpocjpbkouydoszcingtkreqgmjudvjgjhaylurngmemamzumzvhxnoqzv\
        mmdipocgzacelrdodpbfpupzwffbqzjwcmieydvdkvgiashklljmnijdlchtxmofuhvzkihzlroveuqparrbmlgazfzonvmvoj\
        ffuzhlzthmbzzsqetkbwfeyphmsetjeoaktjrmmyuexrlyezvsxmxgmntnlwtqsqfiacwkdjmltmgrkxoijawdypkegrulxpbp\
        iknovpswibodsuqavszcttkchdsobwvfngqxzpidqwvlwzafswiattvwnniboldikuxwzvmfmqlpnydfjyvipmudkqmbrlmthy\
        ddnbkyazqrydxmbtvvooluumrrfbtkqqhunitsmndoikcvtijzurhfprdjlclnnfvwkovbbbzyrcbszlgrjswhvuqwevhlrsps\
        oypxdocxjigwaotioazvsnpaebvantycbpntvtzfzyjxupumdxnzqxxeavdloumekxqzxlabdkdqhydtzbpjcszkppjvaaotjt\
        yhnffibvdzdugupuqcqcjudporpyqykbllbjgtunewqoeuqdufwjbpgiroqsgotrkqxwayrucfzetmzbzazwdfmebnrelkxyfw\
        bifzajgxodbwryzyxacgtmsmvdqmvghyrtbpohysqpmzoxnldneajwrkzzbemrttgqslyqloonosogakddsopvrneksguqnzkx\
        wcmtbncninwczyuqexhfcpvqhogrbaaoanpabknwfdjfttuphlpeqmqghmtwhillyhxeckxleyfvjvwhalffdgdhjqqtonbvlx\
        qywcmxeolaaxxgmkdixrkyrhiltsdpzqddkirshtmcvdifizzgnyxfckxegiowtawgstkljnjxbtgdisekpkaotioditojivku\
        piipomnrkytnoiirvszjbdcovbmfpymagauofnrqltszswiykkokrixfenqznfbrdxsipvqxyqpnhlwtusnvbbyizqzlwthzkm\
        clnkndlcgeqjohzfrtuxxfkdjdeyawiresqkbkhwqsyajiphhnvqjromrvetbdhqbrojdnoqcachzmnnozmjvrglpbqedxwcvw\
        fnupnvmgnkylkuuyrvkhfwrylwbvutekovgqsnhqzveqjtgfpnmytkmwfjcjncrcazmbkegmzesfexozjrjirmfszfciraxsil\
        nxydjbemkdapxzagzbqeufubzcikcvrrqjgtsiqtvczgegwlugfjljjqnobcyyysdfpsdgplirugwobatiwstojbtsmhdxlljp\
        gbbawerlxpzsupgzybyffjrlxogahvtyhigtpcmexvgbxryymmpwmmkndxzuuirxuuduvqpbaywnqqjqhxeoxaltncwswgeidm\
        dfcxrfrycwfqklfjaucuuazmddgaggeeeacscupeqvuiaeembweabwfvkumfpebchagzlqvgzzwgbeztxvvicoquffsiuhbfup\
        neikkekmklgxrrweyaahzzukuauctcevrsxvxpxaswwrkespnhfqoqtxxlicppldbtilqzhsvgzwqhogggeogovlaclygljdwx\
        oalmebnacmyxxwhytnvydlhaqgelhvblomycggcttfsgpcwiihpnpskocxoqhqddnqttsdqredayysxsxhntxlnaolfnklpjgt\
        txssmekttsktqhqbkpyhmmribrvamxmhvensenhorpktppydgvlvzkhysvtbylyfjvioqydtanyidhqyasfxvvhribyzcmndlc\
        dlwaktnlzkzlfhcnvhhfnoqivdcasvgnxorequzonywuhrvzwlwdpvgafgbwyhwqtogjgnupmrgxeokkpxuddsbdtjymcycnos\
        mwoqonlzsbwzwmlqyrwzcneuywvwiaoclzrzyvacngjuuzkmsxubkcjunyanmwegplprwtrgqkfgwjuflzywglyewunsudzjbj\
        cuonevldylbaibrbfbhctdconoohpmvwmeozbgcjqzmsqdltgovzuhyxnvrhbldabjooigfzealnrutqikeisljdozhjzmnrwd\
        qqdldpsltgtcjmlhuirzinefgvyvtyldclwuwrqsngtwjzuvsjitjovqsxgmwwcaetefbxowgultdlgxccbtrzmtqkpyvqipcr\
        rkuukrrcpiqvypkqtmzrtbccxgldtlugwoxbfeteacwwmgxsqvojtijsvuzjwtgnsqrwuwlcdlytvyvgfenizriuhlmjctgtls\
        pdldqqdwrnmzjhzodjlsiekiqturnlaezfgioojbadlbhrvnxyhuzvogtldqsmzqjcgbzoemwvmphoonocdtchbfbrbiablydl\
        venoucjbjzdusnuweylgwyzlfujwgfkqgrtwrplpgewmnaynujckbuxsmkzuujgncavyzrzlcoaiwvwyuenczwryqlmwzwbszl\
        noqowmsoncycmyjtdbsdduxpkkoexgrmpungjgotqwhywbgfagvpdwlwzvrhuwynozuqeroxngvsacdviqonfhhvnchflzkzln\
        tkawldcldnmczybirhvvxfsayqhdiynatdyqoivjfylybtvsyhkzvlvgdypptkprohnesnevhmxmavrbirmmhypkbqhqtksttk\
        emssxttgjplknfloanlxtnhxsxsyyaderqdsttqnddqhqoxcokspnphiiwcpgsfttcggcymolbvhlegqahldyvntyhwxxymcan\
        belaoxwdjlgylcalvogoegggohqwzgvshzqlitbdlppcilxxtqoqfhnpsekrwwsaxpxvxsrvectcuukuzzhaayewrrxglkmkek\
        kienpufbhuisffuqocivvxtzebgwzzgvqlzgahcbepfmukvfwbaewbmeeaiuvqepucscaeeeggagddmzauucuajflkqfwcyrfr\
        xcfdmdiegwswcntlaxoexhqjqqnwyabpqvuduuxriuuzxdnkmmwpmmyyrxbgvxemcptgihytvhagoxlrjffybyzgpuszpxlrew\
        abbgpjllxdhmstbjotswitabowgurilpgdspfdsyyycbonqjjljfgulwgegzcvtqistgjqrrvckiczbufueqbzgazxpadkmebj\
        dyxnlisxaricfzsfmrijrjzoxefsezmgekbmzacrcnjcjfwmktymnpfgtjqevzqhnsqgvoketuvbwlyrwfhkvryuuklykngmvn\
        punfwvcwxdeqbplgrvjmzonnmzhcacqondjorbqhdbtevrmorjqvnhhpijaysqwhkbkqseriwayedjdkfxxutrfzhojqegcldnknlcmkzhtwlzqziybbvnsutwlhnpqyxqvpisxdrbfnzqnefxirkokkyiwszstlqrnfouagamypfmbvocdbjzsvriiontykrnmopiipukvijotidoitoakpkesidgtbxjnjlktsgwatwoigexkcfxyngzzifidvcmthsrikddqzpdstlihrykrxidkmgxxaaloexmcwyqxlvbnotqqjhdgdfflahwvjvfyelxkcexhyllihwtmhgqmqeplhputtfjdfwnkbapnaoaabrgohqvpcfhxequyzcwnincnbtmcwxkznqugskenrvposddkagosonoolqylsqgttrmebzzkrwjaendlnxozmpqsyhopbtryhgvmqdvmsmtgcaxyzyrwbdoxgjazfibwfyxklernbemfdwzazbzmtezfcuryawxqkrtogsqorigpbjwfudqueoqwenutgjbllbkyqypropdujcqcqupugudzdvbiffnhytjtoaavjppkzscjpbztdyhqdkdbalxzqxkemuoldvaexxqznxdmupuxjyzfztvtnpbcytnavbeapnsvzaoitoawgijxcodxpyospsrlhvewquvhwsjrglzsbcryzbbbvokwvfnnlcljdrpfhruzjitvckiodnmstinuhqqktbfrrmuuloovvtbmxdyrqzaykbnddyhtmlrbmqkdumpivyjfdynplqmfmvzwxukidlobinnwvttaiwsfazwlvwqdipzxqgnfvwbosdhckttczsvaqusdobiwspvonkipbpxlurgekpydwajioxkrgmtlmjdkwcaifqsqtwlntnmgxmxsvzeylrxeuymmrjtkaoejtesmhpyefwbkteqszzbmhtzlhzuffjovmvnozfzaglmbrrapquevorlzhikzvhufomxthcldjinmjllkhsaigvkdvdyeimcwjzqbffwzpupfbpdodrlecazgcopidmmvzqonxhvzmuzmamemgnrulyahjgjvdujmgqerktgniczsodyuokbpjcopzvhpagybyzmxcsdfrrvvbsmgwokkfkndteviastmckngrlcnpntoolgenbzgdpbmypvlrxgljnfdzezkzbfktugaqsfxzwjybsxglmgdvziuznqjajjppbrtbtrneedrjzvzlatixoetkmiakzdhqoaetknbskjryuwbcvbmisqvqkxlwrhatjdhebfshrpjappqyadvjbbpypngyekagggjtdveqnsfuikmjmenhmaflesilshbyxgtqqzjuucgzydsmnpyzqsdyoeivmyddnsmtlyyebzmylphcdimvivkyoajiicpelkwhkqnklconszhfzptwfsavmngrbvitrytdhewyxuyurqxykffnxotjijaneqwgtecgfhukjazpurbgamzadyoezygtallizcfgszhjvtlcgcktxssxbetfcfllaqwjijljcofgcholiudpnsaaeaupmcfdjlpoagjozjbnzbivtonbcmlivtfrsszcjiawgnsbqhpkvijfeziyavxtpihnqoghqjuacudooutrohqagxupwmfkdezkfhxnvobfyfcaduznuiziyzwxiloihcwjvnlxmhkqnvudiqiktensxamsyoarkvrjodfihbqsdwkosmbqgpmtlqfsmezcofxngpxzokzzlmrgdiqmyzethgpqceycvowkejigxcofogsfgmrjqtdgajxjqysgymnqncuaodaklloxygggymuvpluaxsrbyypxetixvhkwalchaocodrzvgcrdnzbgbbxuwjqxefnqxzxxgcwldreiyupxyyjxjdmikcahnaaoaskfngdwzfvmhqxohjvlscydftwknqvjvvvciplysbedeywqgipmfbfzsovxwrwjcgeppgjedohdamzivgwifrzvegwckygeqdhaanyxnowuvdgvfgaeojdqnsycxgamefwnvsdgealdttjaortyjfpzkmjfdxoicqxrhpqswyuwcnnbelxdoagwsixzgyoayyxvfkmkifsxrybjlkjxmxyrigodypjjofcqblryarqrkfhwrmrnltgplqvrdbryzzbprgoveandnifnpgmqllcezdjmqrcwegldombqokuavpatmkbiqlfslfsdbhtdfcobscslicsdsriztyvaeiaxbhgfxzlgaronjfqdenjfoltrblgzeoucwdxqpzbogevwdhioqufcqetyljqrlhjbdczyydhecsztnvlbxotkrbruyavadzravgmoaxrldmgyagayyailphocorzawjkshswssrpnxonevghmvlnrkfcgeegexxspvjwmyiqmdsbyezlyfrordkbcdglccauhfcxzltkpazhugndvwrceirusytynhfrahcizujfdkpbdauxstywxwkoomhgzpljocesfxmqgivlugtlugxjevazfvpxfmezvjrlimdplwvkhdtwiwcklkgnjdfbaiiwzsawyqyhouyvmcmqpepuspjgyqcdzfbflydwimbootjugrxjdslriddppqehnryaftozucphzfunafnxapwjwaljnnblyrpzdxqegihefmbksssdckfwfzpmiiyqpgtvpnbkqglsujyfxuvistmgtyxkyvguhhwgpqxgardazswhqddsuvtfzegcwakvdcsjzrxxtqpurnvrazupyteqapwlipwdekdigowuwvdfcwxqhgokpxjmphebhlprlltllxcuxvxzkhjarewmpqcnoesddxsrzuoysgfsyrnlmxvjsoizjxldmtastpfszcbslhrcsxmukikzfhxugxfdxacsbgnroxbewtmqrvlgczwiurqapfvcdoufholygqrflmwrigybuoivxgyvlqiqdjogwdbkkutzhwpyqaqajqpqjcsebzhvyxqvawqaiefvyyigirwrqebkqlybhscgkxvdkjirbzlkdzoujiwizjyoqxqlikjrnrsfbtrdmdalfhqucztobbihtmtvvnomjuahlwefavhgecotpvftsronjumgqniuhrjwsevprvxafkearbwcwqllegepbgjfxgmujfnuistujjuricdwcjdudgdnrmfxrnymcaacvuaqethzchzrhqhmyoenubklsiqwlqzfxsmexqarcctxjzbratadsvdugbdaggbwiexvfogboqjztgdeqlfnmwnabbssdbqhdcobgrmwmxxdussdxvwxtpzutjvycuioskvxnwljjerkiyjhjfqzmbdpxzplnrymicljgxwsdnnomyhnyguctitjeymivgdfkgxmkrtmkwkcwlcneswqoxryslvngtkkzghawstmcjcuqemetwzjjchsembzbnofomjxesmnhscgxaauthvlxukvzawffayqpwshrgypbdqpnnpzlplhnwgfgrunpnfbmyxpbnbwupoltnhjyzuwvdnxxoqugpvtmqktbjdhusjwtjltikugtiatzkdxtgjapiwvzpgivxcxvxpsbedmkijanztlyfmxjtzkksfzwzgdzzzmumevlsvpcloinjidvcyjawslkoygaqolnuykojmwxnevzzxhkszldgzesbeildqrunqlqnvmdiqlbnhtduyrxznahoosckqywudqyuioaacoviurllhtfgsurgczlsmmlwebjqtlwmcqrnqbkrclxsverkpvuvmmjsckdpalfytayjymcsrxztiphamtwxnalusepzmobsyggtzfnlfjhbhravnpgtuwrobbbaijpi"

t2 = time.clock()
print(s.validPalindrome(str))
print("Fast Solution", (time.clock()-t2) * 1000)

t1 = time.clock()
print(s.validPalindromeTLE(str))
print("Valid Palindrome TLE: ", (time.clock()-t1) * 1000)