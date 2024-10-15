import string

def retLang(lang: str):
    english_text = """
He Him She Her They Them It I am

The world is a complex place, where countless topics and concerns interconnect, shaping societies, cultures, technologies, and even individual lives. Let's start with history, the story of humanity, a long timeline marked by civilization's rise and fall, significant discoveries, wars, and peace treaties. The early humans were hunters and gatherers, leading nomadic lifestyles and surviving with basic tools made of stone. The advent of agriculture around 10,000 BCE was a game-changer, leading to the development of the first permanent settlements in regions like Mesopotamia and the Nile Valley.

As civilizations advanced, so did their technologies. The invention of the wheel, the plow, and later on, written language, allowed societies to flourish. Ancient Egypt's pyramids, Greek democracy, and Roman law were significant milestones that shaped the cultural and structural development of future societies. Fast forward to the Renaissance, a period of cultural rebirth in Europe, where art, science, and exploration began to thrive. Think of da Vinci's paintings or Galileo’s scientific observations, which paved the way for the Enlightenment, a time when reason and individualism gained prominence, leading eventually to modern democracy and contemporary social norms.

As societies evolved, so did their economic systems. From barter and trade to the emergence of money as a medium of exchange, economies became more complex. The Industrial Revolution marked a major turning point, as mechanization and factory production transformed economies from agrarian-based to industrial-based. The invention of steam engines, the telegraph, and railways facilitated global trade and communication, accelerating the pace of change. Today, we see globalization, characterized by interconnected economies, international trade agreements, and multinational corporations that influence markets worldwide.

Technological advancements brought about by the digital revolution have drastically changed the way we live, work, and communicate. The emergence of the internet in the late 20th century revolutionized information sharing, while recent developments in artificial intelligence (AI), machine learning, and big data are transforming industries and even daily life. AI, in particular, raises ethical concerns about job displacement, privacy, and the decision-making capabilities of algorithms. However, it also offers remarkable potential in fields such as medicine, where it can help in diagnosing diseases or designing new drugs.

Speaking of medicine, healthcare is a fundamental concern for any society. Advances in medical science, from the discovery of penicillin to the development of vaccines, have significantly improved the quality of life. Modern healthcare focuses not only on curing diseases but also on preventive care, with an emphasis on diet, exercise, and mental health. However, disparities in healthcare access remain, especially in developing nations, where infrastructure and resources are often limited. Additionally, global health concerns, such as pandemics or antibiotic-resistant bacteria, pose challenges that require coordinated international responses.

Turning to politics, the way societies govern themselves varies widely. Democracies, where citizens have a voice in decision-making through elections, contrast with authoritarian regimes, where power is concentrated in the hands of a few. Political ideologies, such as liberalism, conservatism, socialism, and nationalism, influence policies and the balance of power within countries. Internationally, organizations like the United Nations (UN) work to foster cooperation and peace, although geopolitical tensions often complicate matters. Conflicts over resources, territory, and ideology continue to shape global politics, as seen in disputes in regions such as the Middle East or the South China Sea.

Climate change is one of the most pressing global challenges today. Human activities, particularly the burning of fossil fuels for energy, have increased levels of greenhouse gases in the atmosphere, leading to global warming. The effects include melting ice caps, rising sea levels, and extreme weather events such as hurricanes, droughts, and wildfires. Addressing this issue requires a transition to renewable energy sources like solar, wind, and hydroelectric power, as well as policies promoting sustainability and carbon neutrality. Individual actions, such as reducing waste, conserving energy, and supporting eco-friendly companies, can also contribute to tackling this global problem.

Another matter closely tied to our environment is biodiversity. The loss of species and natural habitats due to human expansion, pollution, and climate change is a growing concern. Conservation efforts aim to protect endangered species, restore habitats, and promote sustainable practices that minimize harm to ecosystems. This is crucial not only for preserving the planet's natural beauty but also for maintaining the balance of life-supporting systems that provide food, clean water, and air.

In modern life, education plays a vital role in shaping future generations. The importance of quality education, accessible to all, cannot be overstated. It enables individuals to acquire the skills needed for personal development, economic productivity, and civic engagement. The methods of teaching and learning are evolving, with online courses, digital resources, and AI-powered educational tools becoming commonplace. STEM education (Science, Technology, Engineering, and Mathematics) is particularly emphasized due to its relevance to future technological and scientific advancements.

Culture and the arts remain essential for expressing human experiences and fostering creativity. Throughout history, art has taken on many forms, from cave paintings to digital media. Music, literature, visual arts, and performing arts continue to evolve, reflecting societal changes and influencing people’s perspectives. Pop culture, driven by the entertainment industry, shapes trends, language, and even politics. While some criticize the rise of celebrity culture, others argue that it serves as a form of social connection and community.

Another critical issue in today's world is social justice. The fight for equal rights, regardless of race, gender, religion, or sexual orientation, has made significant progress, yet challenges persist. Movements such as Black Lives Matter, feminism, and LGBTQ+ rights continue to advocate for equality and fair treatment. The concept of intersectionality—which recognizes how various forms of discrimination can overlap—has gained traction, highlighting the importance of understanding and addressing complex social dynamics.

Philosophy delves into the deeper questions of existence, ethics, and the nature of reality. From ancient thinkers like Socrates, Plato, and Aristotle, to modern philosophers like Nietzsche, Kant, and Sartre, philosophical ideas have shaped the foundations of our beliefs and moral frameworks. The exploration of free will, consciousness, and the meaning of life continues to challenge our understanding of what it means to be human.

In the realm of sports, the focus is on physical fitness, competition, and entertainment. Major sporting events like the Olympics, the FIFA World Cup, and Super Bowl draw millions of viewers, showcasing the talents and dedication of athletes. Sports also play a role in cultural identity, community building, and even diplomacy. The rise of eSports, or competitive video gaming, reflects the increasing integration of technology into our recreational activities.

Finally, there is space exploration, a testament to humanity's curiosity and drive to explore the unknown. From the Apollo Moon landings to the current endeavors by NASA, ESA, and private companies like SpaceX, the goal is to understand more about our universe. Mars missions, exoplanet discoveries, and advancements in astronomy could pave the way for future human colonization of other planets or uncover signs of extraterrestrial life.
""".lower()
    german_text = """
Hier ist ein umfassender Text auf Deutsch, der viele Themen abdeckt:

---

Die Welt ist ein komplexer Ort, an dem unzählige Themen und Anliegen miteinander verbunden sind und Gesellschaften, Kulturen, Technologien und sogar das individuelle Leben prägen. Beginnen wir mit der **Geschichte**, der Geschichte der Menschheit, einer langen Zeitlinie, die von Aufstieg und Fall der Zivilisationen, bedeutenden Entdeckungen, Kriegen und Friedensverträgen geprägt ist. Die frühen Menschen waren Jäger und Sammler, führten ein nomadisches Leben und überlebten mit einfachen Werkzeugen aus Stein. Die Entstehung der Landwirtschaft um 10.000 v. Chr. war ein Wendepunkt, der zur Entwicklung der ersten dauerhaften Siedlungen in Regionen wie Mesopotamien und dem Niltal führte.

Mit dem Fortschritt der Zivilisationen entwickelten sich auch ihre **Technologien** weiter. Die Erfindung des Rades, des Pflugs und später der Schrift ermöglichte es den Gesellschaften, zu gedeihen. Die Pyramiden des alten Ägypten, die griechische Demokratie und das römische Recht waren bedeutende Meilensteine, die die kulturelle und strukturelle Entwicklung zukünftiger Gesellschaften prägten. Wenn wir zum **Renaissance-Zeitalter** vorspulen, erleben wir eine Zeit der kulturellen Wiedergeburt in Europa, in der Kunst, Wissenschaft und Entdeckungen aufblühten. Denken Sie an da Vincis Gemälde oder Galileos wissenschaftliche Beobachtungen, die den Weg für das **Zeitalter der Aufklärung** ebneten, eine Zeit, in der Vernunft und Individualismus an Bedeutung gewannen und schließlich zur modernen Demokratie und zu zeitgenössischen sozialen Normen führten.

Während sich Gesellschaften entwickelten, wurden auch ihre **Wirtschaftssysteme** komplexer. Vom Tauschhandel und Handel bis hin zum Aufkommen des **Geldes** als Tauschmittel wurden die Volkswirtschaften immer vielschichtiger. Die **industrielle Revolution** war ein Wendepunkt, als Mechanisierung und Massenproduktion die Volkswirtschaften von agrarwirtschaftlichen zu industriellen Strukturen wandelten. Die Erfindung von Dampfmaschinen, Telegrafen und Eisenbahnen erleichterte den globalen Handel und die Kommunikation und beschleunigte den Wandel. Heute erleben wir die **Globalisierung**, die sich durch miteinander verbundene Volkswirtschaften, internationale Handelsabkommen und multinationale Konzerne auszeichnet, die weltweit die Märkte beeinflussen.

Technologische Fortschritte, die durch die **digitale Revolution** ermöglicht wurden, haben drastisch verändert, wie wir leben, arbeiten und kommunizieren. Das Aufkommen des **Internets** Ende des 20. Jahrhunderts revolutionierte den Informationsaustausch, während aktuelle Entwicklungen in den Bereichen **künstliche Intelligenz (KI)**, maschinelles Lernen und **Big Data** Industrien und sogar den Alltag verändern. Insbesondere KI wirft ethische Fragen hinsichtlich des Arbeitsplatzverlusts, des Datenschutzes und der Entscheidungsfähigkeit von Algorithmen auf. Sie bietet jedoch auch bemerkenswerte Möglichkeiten in Bereichen wie der **Medizin**, wo sie bei der Diagnose von Krankheiten oder der Entwicklung neuer Medikamente helfen kann.

Apropos Medizin: **Gesundheitsversorgung** ist ein grundlegendes Anliegen jeder Gesellschaft. Fortschritte in der medizinischen Wissenschaft, von der Entdeckung des Penicillins bis zur Entwicklung von Impfstoffen, haben die Lebensqualität erheblich verbessert. Die moderne Gesundheitsversorgung konzentriert sich nicht nur auf die Heilung von Krankheiten, sondern auch auf die **Prävention**, wobei der Schwerpunkt auf Ernährung, Bewegung und psychischer Gesundheit liegt. Dennoch gibt es Unterschiede im Zugang zur Gesundheitsversorgung, insbesondere in Entwicklungsländern, wo die Infrastruktur und Ressourcen oft begrenzt sind. Hinzu kommen globale Gesundheitsprobleme wie **Pandemien** oder antibiotikaresistente Bakterien, die koordinierte internationale Reaktionen erfordern.

In der **Politik** unterscheidet sich die Art und Weise, wie sich Gesellschaften regieren, stark. **Demokratien**, in denen die Bürger durch Wahlen eine Stimme in der Entscheidungsfindung haben, stehen im Gegensatz zu **autoritären Regimen**, in denen die Macht in den Händen weniger konzentriert ist. Politische Ideologien wie **Liberalismus**, **Konservatismus**, **Sozialismus** und **Nationalismus** beeinflussen die Politik und das Machtgefüge innerhalb der Länder. Auf internationaler Ebene arbeiten Organisationen wie die **Vereinten Nationen (UN)** daran, Zusammenarbeit und Frieden zu fördern, obwohl geopolitische Spannungen die Dinge oft erschweren. Konflikte um Ressourcen, Territorien und Ideologien prägen weiterhin die globale Politik, wie man an Streitigkeiten in Regionen wie dem Nahen Osten oder dem Südchinesischen Meer sieht.

Der **Klimawandel** ist eine der dringendsten globalen Herausforderungen unserer Zeit. Menschliche Aktivitäten, insbesondere die Verbrennung fossiler Brennstoffe zur Energiegewinnung, haben die Treibhausgaskonzentration in der Atmosphäre erhöht und zur globalen Erwärmung geführt. Zu den Auswirkungen zählen das Schmelzen der Eiskappen, der Anstieg des Meeresspiegels und extreme Wetterereignisse wie Hurrikane, Dürren und Waldbrände. Um dieses Problem anzugehen, ist der Übergang zu erneuerbaren Energiequellen wie **Solarenergie**, **Windkraft** und **Wasserkraft** sowie politische Maßnahmen zur Förderung von **Nachhaltigkeit** und **Klimaneutralität** erforderlich. Auch individuelle Maßnahmen wie die Reduzierung von Abfall, das Energiesparen und die Unterstützung umweltfreundlicher Unternehmen können zur Bewältigung dieses globalen Problems beitragen.

Ein weiteres eng mit unserer Umwelt verbundenes Thema ist die **Biodiversität**. Der Verlust von Arten und natürlichen Lebensräumen durch menschliche Expansion, Umweltverschmutzung und den Klimawandel ist ein wachsendes Problem. **Naturschutzbemühungen** zielen darauf ab, gefährdete Arten zu schützen, Lebensräume wiederherzustellen und nachhaltige Praktiken zu fördern, die den Schaden für Ökosysteme minimieren. Dies ist nicht nur wichtig, um die natürliche Schönheit des Planeten zu bewahren, sondern auch, um das Gleichgewicht der lebenswichtigen Systeme zu erhalten, die Nahrung, sauberes Wasser und Luft liefern.

Im modernen Leben spielt die **Bildung** eine entscheidende Rolle bei der Prägung zukünftiger Generationen. Die Bedeutung einer qualitativ hochwertigen Bildung, die für alle zugänglich ist, kann nicht hoch genug eingeschätzt werden. Sie befähigt Einzelpersonen, die Fähigkeiten zu erwerben, die für die persönliche Entwicklung, wirtschaftliche Produktivität und gesellschaftliches Engagement notwendig sind. Die Methoden des Lehrens und Lernens entwickeln sich weiter, wobei Online-Kurse, digitale Ressourcen und KI-gestützte Bildungsinstrumente alltäglich werden. Besonders **MINT-Bildung** (Mathematik, Informatik, Naturwissenschaften und Technik) wird wegen ihrer Relevanz für zukünftige technologische und wissenschaftliche Fortschritte betont.

**Kultur und Kunst** bleiben essenziell für die Ausdrucksweise menschlicher Erfahrungen und die Förderung von Kreativität. Im Laufe der Geschichte hat die Kunst viele Formen angenommen, von **Höhlenmalereien** bis hin zu **digitalen Medien**. Musik, Literatur, bildende Kunst und darstellende Kunst entwickeln sich weiter und spiegeln gesellschaftliche Veränderungen wider und beeinflussen die Perspektiven der Menschen. **Popkultur**, angetrieben durch die Unterhaltungsindustrie, prägt Trends, Sprache und sogar die Politik. Während einige die Zunahme der **Promi-Kultur** kritisieren, argumentieren andere, dass sie eine Form der sozialen Verbindung und Gemeinschaft darstellt.

Ein weiteres kritisches Thema in der heutigen Welt ist die **soziale Gerechtigkeit**. Der Kampf für gleiche Rechte, unabhängig von Rasse, Geschlecht, Religion oder sexueller Orientierung, hat bedeutende Fortschritte gemacht, dennoch bestehen Herausforderungen weiter. Bewegungen wie **Black Lives Matter**, **Feminismus** und **LGBTQ+-Rechte** setzen sich weiterhin für Gleichberechtigung und faire Behandlung ein. Das Konzept der **Intersektionalität** – das anerkennt, wie verschiedene Formen von Diskriminierung sich überschneiden können – hat an Bedeutung gewonnen und verdeutlicht die Notwendigkeit, komplexe soziale Dynamiken zu verstehen und anzugehen.

Die **Philosophie** beschäftigt sich mit den tieferen Fragen der Existenz, Ethik und der Natur der Wirklichkeit. Von alten Denkern wie **Sokrates**, **Platon** und **Aristoteles** bis hin zu modernen Philosophen wie **Nietzsche**, **Kant** und **Sartre** haben philosophische Ideen die Grundlagen unserer Überzeugungen und moralischen Rahmenbedingungen geformt. Die Erforschung von freiem Willen, Bewusstsein und dem Sinn des Lebens stellt weiterhin unser Verständnis darüber, was es bedeutet, ein Mensch zu sein, auf die Probe.

Im Bereich des **Sports** liegt der Fokus auf körperlicher Fitness, Wettbewerb und Unterhaltung. Große Sportereignisse wie die **Olympischen Spiele**, die **FIFA-Weltmeisterschaft** und der **Super Bowl** ziehen Millionen von Zuschauern an und zeigen das Talent und die Hingabe von Athleten. Sport spielt auch eine Rolle in der kulturellen Identität, beim Gemeinschaftsaufbau und sogar in der Diplomatie. Der Aufstieg des **eSports**, also des wettbewerbsorientierten Videospielens, spiegelt die zunehmende Integration von Technologie in unsere Freizeitaktivitäten wider.

Abschließend gibt es die **Weltraumforschung**, ein Zeugnis für die Neugier und den Drang der Menschheit, das Un
    """.lower()
    italian_text = """
Il mondo è un luogo complesso, in cui innumerevoli argomenti e questioni si intrecciano, plasmando società, culture, tecnologie e persino la vita individuale. Cominciamo con la storia, la storia dell'umanità, una lunga cronologia segnata dall'ascesa e dalla caduta delle civiltà, scoperte significative, guerre e trattati di pace. I primi esseri umani erano cacciatori e raccoglitori, conducevano una vita nomade e sopravvivevano con strumenti di base fatti di pietra. L'avvento dell'agricoltura intorno al 10.000 a.C. ha rappresentato una svolta, portando allo sviluppo dei primi insediamenti permanenti in regioni come la Mesopotamia e la valle del Nilo.

Man mano che le civiltà avanzavano, anche le loro tecnologie si evolvevano. L'invenzione della ruota, dell'aratro e, successivamente, della scrittura ha permesso alle società di prosperare. Le piramidi dell'antico Egitto, la democrazia greca e il diritto romano furono pietre miliari significative che plasmarono lo sviluppo culturale e strutturale delle società future. Passando al Rinascimento, un periodo di rinascita culturale in Europa, l'arte, la scienza e l'esplorazione iniziarono a fiorire. Pensiamo ai dipinti di da Vinci o alle osservazioni scientifiche di Galileo, che aprirono la strada all'Illuminismo, un'epoca in cui la ragione e l'individualismo divennero importanti, portando infine alla democrazia moderna e alle norme sociali contemporanee.

Con l'evoluzione delle società, anche i loro sistemi economici divennero più complessi. Dal baratto e commercio all'emergere del denaro come mezzo di scambio, le economie divennero più intricate. La Rivoluzione Industriale segnò un punto di svolta, poiché la meccanizzazione e la produzione in fabbrica trasformarono le economie da agricole a industriali. L'invenzione delle macchine a vapore, del telegrafo e delle ferrovie facilitò il commercio globale e la comunicazione, accelerando il ritmo del cambiamento. Oggi vediamo la globalizzazione, caratterizzata da economie interconnesse, accordi commerciali internazionali e multinazionali che influenzano i mercati mondiali.

I progressi tecnologici portati dalla rivoluzione digitale hanno cambiato drasticamente il nostro modo di vivere, lavorare e comunicare. L'emergere di internet alla fine del XX secolo ha rivoluzionato la condivisione delle informazioni, mentre i recenti sviluppi nell'intelligenza artificiale (IA), nell'apprendimento automatico e nel big data stanno trasformando le industrie e persino la vita quotidiana. L'IA, in particolare, solleva preoccupazioni etiche riguardo alla perdita di posti di lavoro, alla privacy e alle capacità decisionali degli algoritmi. Tuttavia, offre anche straordinarie potenzialità in campi come la medicina, dove può aiutare nella diagnosi di malattie o nella progettazione di nuovi farmaci.

A proposito di medicina, l'assistenza sanitaria è una preoccupazione fondamentale per ogni società. I progressi nella scienza medica, dalla scoperta della penicillina allo sviluppo dei vaccini, hanno migliorato notevolmente la qualità della vita. L'assistenza sanitaria moderna non si concentra solo sulla cura delle malattie, ma anche sulla prevenzione, con un'enfasi su dieta, esercizio fisico e salute mentale. Tuttavia, esistono disparità nell'accesso all'assistenza sanitaria, soprattutto nei paesi in via di sviluppo, dove infrastrutture e risorse sono spesso limitate. Inoltre, preoccupazioni sanitarie globali come le pandemie o i batteri resistenti agli antibiotici pongono sfide che richiedono risposte internazionali coordinate.

In tema di politica, il modo in cui le società si governano varia notevolmente. Le democrazie, dove i cittadini hanno voce in capitolo nelle decisioni tramite le elezioni, contrastano con i regimi autoritari, dove il potere è concentrato nelle mani di pochi. Le ideologie politiche, come il liberalismo, il conservatorismo, il socialismo e il nazionalismo, influenzano le politiche e l'equilibrio del potere all'interno dei paesi. A livello internazionale, organizzazioni come le Nazioni Unite (ONU) lavorano per promuovere la cooperazione e la pace, anche se le tensioni geopolitiche spesso complicano le cose. I conflitti per le risorse, il territorio e l'ideologia continuano a plasmare la politica globale, come si vede nelle dispute in regioni come il Medio Oriente o il Mar Cinese Meridionale.

Il cambiamento climatico è una delle sfide globali più urgenti. Le attività umane, in particolare la combustione di combustibili fossili per produrre energia, hanno aumentato i livelli di gas serra nell'atmosfera, portando al riscaldamento globale. Gli effetti includono lo scioglimento delle calotte polari, l'innalzamento del livello del mare e eventi meteorologici estremi come uragani, siccità e incendi boschivi. Affrontare questa questione richiede una transizione verso fonti di energia rinnovabile come l'energia solare, l'energia eolica e l'idroelettrica, nonché politiche che promuovano la sostenibilità e la neutralità del carbonio. Anche le azioni individuali, come la riduzione dei rifiuti, il risparmio energetico e il sostegno a imprese eco-compatibili, possono contribuire a risolvere questo problema globale.

Un altro argomento strettamente legato al nostro ambiente è la biodiversità. La perdita di specie e habitat naturali dovuta all'espansione umana, all'inquinamento e ai cambiamenti climatici è una preoccupazione crescente. Gli sforzi di conservazione mirano a proteggere le specie in pericolo, ripristinare gli habitat e promuovere pratiche sostenibili che riducano al minimo i danni agli ecosistemi. Questo è cruciale non solo per preservare la bellezza naturale del pianeta, ma anche per mantenere l'equilibrio dei sistemi vitali che forniscono cibo, acqua pulita e aria.

Nella vita moderna, l'istruzione svolge un ruolo fondamentale nella formazione delle future generazioni. L'importanza di un'istruzione di qualità, accessibile a tutti, non può essere sottovalutata. Consente agli individui di acquisire le competenze necessarie per lo sviluppo personale, la produttività economica e l'impegno civico. I metodi di insegnamento e apprendimento stanno evolvendo, con corsi online, risorse digitali e strumenti educativi basati sull'IA che diventano sempre più comuni. L'istruzione STEM (Scienza, Tecnologia, Ingegneria e Matematica) è particolarmente enfatizzata per la sua rilevanza nei futuri progressi tecnologici e scientifici.

La cultura e le arti restano essenziali per esprimere le esperienze umane e favorire la creatività. Nel corso della storia, l'arte ha assunto molte forme, dai dipinti rupestri ai media digitali. La musica, la letteratura, le arti visive e le arti performative continuano a evolversi, riflettendo i cambiamenti sociali e influenzando le prospettive delle persone. La cultura pop, guidata dall'industria dell'intrattenimento, modella le tendenze, il linguaggio e persino la politica. Sebbene alcuni critichino l'ascesa della cultura delle celebrità, altri sostengono che rappresenti una forma di connessione sociale e comunità.

Un altro tema critico nella società odierna è la giustizia sociale. La lotta per i diritti uguali, indipendentemente da razza, genere, religione o orientamento sessuale, ha fatto significativi progressi, ma le sfide persistono. Movimenti come il Black Lives Matter, il femminismo e i diritti LGBTQ+ continuano a lottare per l'uguaglianza e il trattamento equo. Il concetto di intersezionalità – che riconosce come diverse forme di discriminazione possano sovrapporsi – ha guadagnato terreno, sottolineando l'importanza di comprendere e affrontare dinamiche sociali complesse.

La filosofia esplora le domande più profonde sull'esistenza, l'etica e la natura della realtà. Dai pensatori antichi come Socrate, Platone e Aristotele, ai filosofi moderni come Nietzsche, Kant e Sartre, le idee filosofiche hanno plasmato le basi della scienza, della politica e della cultura occidentale.
    """.lower()
    espaniol_text = """
El mundo es un lugar complejo, donde innumerables temas y cuestiones se entrelazan, moldeando sociedades, culturas, tecnologías e incluso la vida individual. Comencemos con la historia, la historia de la humanidad, una larga cronología marcada por el ascenso y caída de civilizaciones, descubrimientos significativos, guerras y tratados de paz. Los primeros seres humanos eran cazadores y recolectores, llevaban una vida nómada y sobrevivían con herramientas básicas hechas de piedra. La llegada de la agricultura alrededor del 10.000 a.C. marcó un punto de inflexión, llevando al desarrollo de los primeros asentamientos permanentes en regiones como Mesopotamia y el valle del Nilo.

A medida que las civilizaciones avanzaban, también lo hacían sus tecnologías. La invención de la rueda, el arado y, posteriormente, la escritura, permitió a las sociedades prosperar. Las pirámides del antiguo Egipto, la democracia griega y el derecho romano fueron hitos significativos que dieron forma al desarrollo cultural y estructural de las futuras sociedades. Pasando al Renacimiento, un período de renacimiento cultural en Europa, el arte, la ciencia y la exploración comenzaron a florecer. Pensemos en las pinturas de Da Vinci o las observaciones científicas de Galileo, que allanaron el camino para la Ilustración, una era en la que la razón y el individualismo cobraron importancia, llevando finalmente a la democracia moderna y a las normas sociales contemporáneas.

Con la evolución de las sociedades, también sus sistemas económicos se volvieron más complejos. Desde el trueque y el comercio hasta la aparición del dinero como medio de intercambio, las economías se hicieron más intrincadas. La Revolución Industrial marcó un punto de inflexión, ya que la mecanización y la producción en fábricas transformaron las economías de agrícolas a industriales. La invención de las máquinas de vapor, el telégrafo y los ferrocarriles facilitó el comercio global y la comunicación, acelerando el ritmo del cambio. Hoy en día, vemos la globalización, caracterizada por economías interconectadas, acuerdos comerciales internacionales y multinacionales que influyen en los mercados globales.

Los avances tecnológicos impulsados por la revolución digital han cambiado drásticamente nuestra forma de vivir, trabajar y comunicarnos. El surgimiento de Internet a finales del siglo XX revolucionó la compartición de información, mientras que los desarrollos recientes en inteligencia artificial (IA), el aprendizaje automático y el big data están transformando industrias e incluso la vida cotidiana. La IA, en particular, plantea preocupaciones éticas sobre la pérdida de empleos, la privacidad y la toma de decisiones por parte de algoritmos. Sin embargo, también ofrece extraordinarias posibilidades en campos como la medicina, donde puede ayudar en el diagnóstico de enfermedades o en el diseño de nuevos fármacos.

Hablando de medicina, la atención sanitaria es una preocupación fundamental para cualquier sociedad. Los avances en la ciencia médica, desde el descubrimiento de la penicilina hasta el desarrollo de vacunas, han mejorado considerablemente la calidad de vida. La atención sanitaria moderna no se centra solo en curar enfermedades, sino también en la prevención, con énfasis en la dieta, el ejercicio y la salud mental. Sin embargo, existen disparidades en el acceso a la atención sanitaria, especialmente en los países en desarrollo, donde la infraestructura y los recursos son a menudo limitados. Además, preocupaciones sanitarias globales como las pandemias o las bacterias resistentes a los antibióticos plantean desafíos que requieren respuestas internacionales coordinadas.

En cuanto a la política, la forma en que las sociedades se gobiernan varía enormemente. Las democracias, donde los ciudadanos tienen voz en la toma de decisiones a través de elecciones, contrastan con los regímenes autoritarios, donde el poder está concentrado en manos de unos pocos. Las ideologías políticas, como el liberalismo, el conservadurismo, el socialismo y el nacionalismo, influyen en las políticas y el equilibrio de poder dentro de los países. A nivel internacional, organizaciones como las Naciones Unidas (ONU) trabajan para promover la cooperación y la paz, aunque las tensiones geopolíticas a menudo complican las cosas. Los conflictos por los recursos, el territorio y la ideología continúan dando forma a la política global, como se ve en disputas en regiones como el Medio Oriente o el Mar de China Meridional.

El cambio climático es uno de los desafíos globales más urgentes. Las actividades humanas, en particular la quema de combustibles fósiles para producir energía, han aumentado los niveles de gases de efecto invernadero en la atmósfera, llevando al calentamiento global. Los efectos incluyen el derretimiento de las capas polares, la elevación del nivel del mar y fenómenos meteorológicos extremos como huracanes, sequías e incendios forestales. Abordar este problema requiere una transición hacia fuentes de energía renovables como la energía solar, la energía eólica y la hidroeléctrica, así como políticas que promuevan la sostenibilidad y la neutralidad del carbono. También las acciones individuales, como la reducción de residuos, el ahorro energético y el apoyo a empresas ecológicas, pueden contribuir a resolver este problema global.

Otro tema estrechamente relacionado con nuestro entorno es la biodiversidad. La pérdida de especies y hábitats naturales debido a la expansión humana, la contaminación y el cambio climático es una preocupación creciente. Los esfuerzos de conservación buscan proteger a las especies en peligro, restaurar los hábitats y promover prácticas sostenibles que minimicen el daño a los ecosistemas. Esto es crucial no solo para preservar la belleza natural del planeta, sino también para mantener el equilibrio de los sistemas que proporcionan alimentos, agua limpia y aire.

En la vida moderna, la educación juega un papel fundamental en la formación de las futuras generaciones. La importancia de una educación de calidad, accesible para todos, no puede ser subestimada. Permite a las personas adquirir las habilidades necesarias para el desarrollo personal, la productividad económica y el compromiso cívico. Los métodos de enseñanza y aprendizaje están evolucionando, con cursos en línea, recursos digitales y herramientas educativas basadas en la IA que se vuelven cada vez más comunes. La educación STEM (Ciencia, Tecnología, Ingeniería y Matemáticas) se enfatiza particularmente por su relevancia en futuros avances tecnológicos y científicos.

La cultura y las artes siguen siendo esenciales para expresar experiencias humanas y fomentar la creatividad. A lo largo de la historia, el arte ha adoptado muchas formas, desde las pinturas rupestres hasta los medios digitales. La música, la literatura, las artes visuales y las artes escénicas continúan evolucionando, reflejando los cambios sociales e influyendo en las perspectivas de las personas. La cultura pop, impulsada por la industria del entretenimiento, moldea las tendencias, el lenguaje e incluso la política. Aunque algunos critican el ascenso de la cultura de las celebridades, otros argumentan que representa una forma de conexión social y comunidad.

Otro tema crítico en la sociedad actual es la justicia social. La lucha por la igualdad de derechos, independientemente de la raza, el género, la religión o la orientación sexual, ha logrado progresos significativos, pero los desafíos persisten. Movimientos como Black Lives Matter, el feminismo y los derechos LGBTQ+ siguen luchando por la igualdad y el trato justo. El concepto de interseccionalidad, que reconoce cómo diversas formas de discriminación pueden superponerse, ha ganado terreno, subrayando la importancia de comprender y abordar dinámicas sociales complejas.

La filosofía explora las preguntas más profundas sobre la existencia, la ética y la naturaleza de la realidad. Desde los antiguos pensadores como Sócrates, Platón y Aristóteles, hasta los filósofos modernos como Nietzsche, Kant y Sartre, las ideas filosóficas han moldeado los cimientos de la ciencia, la política y la cultura occidental.
    """
    if lang == "es":
        return espaniol_text
    if lang == "de":
        return german_text
    elif lang == "en":
        return english_text
    elif lang == "it":
        return italian_text

def split_and_clean(prompt):
    prompt = prompt.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_prompt = prompt.translate(translator)
    
    # Split into a list of words
    word_list = cleaned_prompt.split()
    
    return word_list

def whatLanguage(prompt: str) -> list:
    languages = ["it", "en", "de", "es"]
    listed_words_prompt = split_and_clean(prompt=prompt)
    scores = {"en": 0, "de": 0, "it": 0, "es": 0}
    for lang in languages:

        for word in  listed_words_prompt:


            if word in split_and_clean(retLang(lang)):
                scores[lang] += 1
    total_score = sum(scores.values())
    if total_score == 0:
        return {"Error": "Not enough data passed"}
    else:
        en_score = round((scores["en"] / total_score) * 100, 2)
        de_score = round((scores["de"] / total_score) * 100, 2)
        it_score = round((scores["it"] / total_score) * 100, 2)
        es_score = round((scores["es"] / total_score) * 100, 2)
        best_lang = max(scores, key=scores.get)
        return {"en": en_score, "de": de_score, "it": it_score, "es": es_score,"best_score":  max(en_score, de_score, it_score, es_score), "best_lang": best_lang}




        
prompt = "Voraussetzungen für die 6 Denkhüte"
scores = whatLanguage(prompt=prompt)
print(scores)
# Output : {'en': 0.0, 'de': 100.0, 'it': 0.0, 'es': 0.0, 'best_score': 100.0, 'best_lang': 'de'}

# change the languages or above data, i used data generated by chatgpt and translated it into those languages


